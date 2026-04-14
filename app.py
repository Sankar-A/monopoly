from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, emit
from game import Game
import uuid

app = Flask(__name__)
app.config["SECRET_KEY"] = "monopoly-secret-key"
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

rooms = {}  # room_id -> Game


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("create_room")
def on_create_room(data):
    name = data.get("name", "Player")
    room_id = str(uuid.uuid4())[:6].upper()
    game = Game(room_id)
    rooms[room_id] = game
    pid = request.sid
    game.add_player(pid, name)
    join_room(room_id)
    emit("room_created", {"room_id": room_id, "player_id": pid})
    emit("game_state", game.state(), to=room_id)


@socketio.on("join_room_game")
def on_join_room(data):
    room_id = data.get("room_id", "").upper()
    name = data.get("name", "Player")
    pid = request.sid
    if room_id not in rooms:
        emit("error", {"msg": "Room not found"})
        return
    game = rooms[room_id]
    if game.started:
        emit("error", {"msg": "Game already started"})
        return
    if not game.add_player(pid, name):
        emit("error", {"msg": "Room is full"})
        return
    join_room(room_id)
    emit("room_joined", {"room_id": room_id, "player_id": pid})
    emit("game_state", game.state(), to=room_id)
    emit("player_joined", {"name": name}, to=room_id, include_self=False)


@socketio.on("start_game")
def on_start_game(data):
    room_id = data.get("room_id")
    game = rooms.get(room_id)
    if not game:
        return
    ok, msg = game.start()
    if ok:
        emit("game_state", game.state(), to=room_id)
    else:
        emit("error", {"msg": msg})


@socketio.on("roll_dice")
def on_roll_dice(data):
    room_id = data.get("room_id")
    game = rooms.get(room_id)
    if not game:
        return
    state, result = game.roll_dice(request.sid)
    if state:
        emit("game_state", state, to=room_id)
        emit("action_result", {"result": result}, to=room_id)


@socketio.on("buy_property")
def on_buy_property(data):
    room_id = data.get("room_id")
    game = rooms.get(room_id)
    if not game:
        return
    state, result = game.buy_property(request.sid)
    if state:
        emit("game_state", state, to=room_id)


@socketio.on("decline_buy")
def on_decline_buy(data):
    room_id = data.get("room_id")
    game = rooms.get(room_id)
    if not game:
        return
    state, result = game.decline_buy(request.sid)
    if state:
        emit("game_state", state, to=room_id)


@socketio.on("buy_house")
def on_buy_house(data):
    room_id = data.get("room_id")
    pos = data.get("pos")
    game = rooms.get(room_id)
    if not game:
        return
    state, result = game.buy_house(request.sid, int(pos))
    if state:
        emit("game_state", state, to=room_id)
    else:
        emit("error", {"msg": result})


@socketio.on("use_jail_free")
def on_use_jail_free(data):
    room_id = data.get("room_id")
    game = rooms.get(room_id)
    if not game:
        return
    state, result = game.use_jail_free(request.sid)
    if state:
        emit("game_state", state, to=room_id)
    else:
        emit("error", {"msg": result})


@socketio.on("disconnect")
def on_disconnect():
    pid = request.sid
    for room_id, game in list(rooms.items()):
        if pid in game.players:
            game.remove_player(pid)
            emit("game_state", game.state(), to=room_id)
            if not game.players:
                del rooms[room_id]
            break


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)
