import random

BOARD = [
    {"name": "GO", "type": "go"},
    {"name": "Mediterranean Ave", "type": "property", "price": 60, "rent": [2,10,30,90,160,250], "color": "brown", "house_cost": 50},
    {"name": "Community Chest", "type": "community_chest"},
    {"name": "Baltic Ave", "type": "property", "price": 60, "rent": [4,20,60,180,320,450], "color": "brown", "house_cost": 50},
    {"name": "Income Tax", "type": "tax", "amount": 200},
    {"name": "Reading Railroad", "type": "railroad", "price": 200},
    {"name": "Oriental Ave", "type": "property", "price": 100, "rent": [6,30,90,270,400,550], "color": "light_blue", "house_cost": 50},
    {"name": "Chance", "type": "chance"},
    {"name": "Vermont Ave", "type": "property", "price": 100, "rent": [6,30,90,270,400,550], "color": "light_blue", "house_cost": 50},
    {"name": "Connecticut Ave", "type": "property", "price": 120, "rent": [8,40,100,300,450,600], "color": "light_blue", "house_cost": 50},
    {"name": "Jail / Just Visiting", "type": "jail"},
    {"name": "St. Charles Place", "type": "property", "price": 140, "rent": [10,50,150,450,625,750], "color": "pink", "house_cost": 100},
    {"name": "Electric Company", "type": "utility", "price": 150},
    {"name": "States Ave", "type": "property", "price": 140, "rent": [10,50,150,450,625,750], "color": "pink", "house_cost": 100},
    {"name": "Virginia Ave", "type": "property", "price": 160, "rent": [12,60,180,500,700,900], "color": "pink", "house_cost": 100},
    {"name": "Pennsylvania Railroad", "type": "railroad", "price": 200},
    {"name": "St. James Place", "type": "property", "price": 180, "rent": [14,70,200,550,750,950], "color": "orange", "house_cost": 100},
    {"name": "Community Chest", "type": "community_chest"},
    {"name": "Tennessee Ave", "type": "property", "price": 180, "rent": [14,70,200,550,750,950], "color": "orange", "house_cost": 100},
    {"name": "New York Ave", "type": "property", "price": 200, "rent": [16,80,220,600,800,1000], "color": "orange", "house_cost": 100},
    {"name": "Free Parking", "type": "free_parking"},
    {"name": "Kentucky Ave", "type": "property", "price": 220, "rent": [18,90,250,700,875,1050], "color": "red", "house_cost": 150},
    {"name": "Chance", "type": "chance"},
    {"name": "Indiana Ave", "type": "property", "price": 220, "rent": [18,90,250,700,875,1050], "color": "red", "house_cost": 150},
    {"name": "Illinois Ave", "type": "property", "price": 240, "rent": [20,100,300,750,925,1100], "color": "red", "house_cost": 150},
    {"name": "B&O Railroad", "type": "railroad", "price": 200},
    {"name": "Atlantic Ave", "type": "property", "price": 260, "rent": [22,110,330,800,975,1150], "color": "yellow", "house_cost": 150},
    {"name": "Ventnor Ave", "type": "property", "price": 260, "rent": [22,110,330,800,975,1150], "color": "yellow", "house_cost": 150},
    {"name": "Water Works", "type": "utility", "price": 150},
    {"name": "Marvin Gardens", "type": "property", "price": 280, "rent": [24,120,360,850,1025,1200], "color": "yellow", "house_cost": 150},
    {"name": "Go To Jail", "type": "go_to_jail"},
    {"name": "Pacific Ave", "type": "property", "price": 300, "rent": [26,130,390,900,1100,1275], "color": "green", "house_cost": 200},
    {"name": "North Carolina Ave", "type": "property", "price": 300, "rent": [26,130,390,900,1100,1275], "color": "green", "house_cost": 200},
    {"name": "Community Chest", "type": "community_chest"},
    {"name": "Pennsylvania Ave", "type": "property", "price": 320, "rent": [28,150,450,1000,1200,1400], "color": "green", "house_cost": 200},
    {"name": "Short Line Railroad", "type": "railroad", "price": 200},
    {"name": "Chance", "type": "chance"},
    {"name": "Park Place", "type": "property", "price": 350, "rent": [35,175,500,1100,1300,1500], "color": "dark_blue", "house_cost": 200},
    {"name": "Luxury Tax", "type": "tax", "amount": 100},
    {"name": "Boardwalk", "type": "property", "price": 400, "rent": [50,200,600,1400,1700,2000], "color": "dark_blue", "house_cost": 200},
]

CHANCE_CARDS = [
    {"text": "Advance to GO. Collect $200.", "action": "advance_to", "target": 0},
    {"text": "Advance to Illinois Ave.", "action": "advance_to", "target": 24},
    {"text": "Advance to St. Charles Place.", "action": "advance_to", "target": 11},
    {"text": "Advance to nearest Railroad.", "action": "nearest_railroad"},
    {"text": "Bank pays you dividend of $50.", "action": "collect", "amount": 50},
    {"text": "Get out of Jail Free.", "action": "jail_free"},
    {"text": "Go Back 3 Spaces.", "action": "move", "amount": -3},
    {"text": "Go to Jail.", "action": "go_to_jail"},
    {"text": "Make general repairs: $25/house, $100/hotel.", "action": "repairs", "house": 25, "hotel": 100},
    {"text": "Pay poor tax of $15.", "action": "pay", "amount": 15},
    {"text": "Take a trip to Reading Railroad.", "action": "advance_to", "target": 5},
    {"text": "Advance to Boardwalk.", "action": "advance_to", "target": 39},
    {"text": "Pay each player $50.", "action": "pay_each", "amount": 50},
    {"text": "Collect $150.", "action": "collect", "amount": 150},
    {"text": "Collect $100.", "action": "collect", "amount": 100},
]

COMMUNITY_CHEST_CARDS = [
    {"text": "Advance to GO. Collect $200.", "action": "advance_to", "target": 0},
    {"text": "Bank error in your favor. Collect $200.", "action": "collect", "amount": 200},
    {"text": "Doctor's fee. Pay $50.", "action": "pay", "amount": 50},
    {"text": "From sale of stock you get $50.", "action": "collect", "amount": 50},
    {"text": "Get out of Jail Free.", "action": "jail_free"},
    {"text": "Go to Jail.", "action": "go_to_jail"},
    {"text": "Holiday fund matures. Collect $100.", "action": "collect", "amount": 100},
    {"text": "Income tax refund. Collect $20.", "action": "collect", "amount": 20},
    {"text": "It's your birthday! Collect $10 from each player.", "action": "collect_each", "amount": 10},
    {"text": "Life insurance matures. Collect $100.", "action": "collect", "amount": 100},
    {"text": "Pay hospital fees of $100.", "action": "pay", "amount": 100},
    {"text": "Pay school fees of $150.", "action": "pay", "amount": 150},
    {"text": "Receive $25 consultancy fee.", "action": "collect", "amount": 25},
    {"text": "You are assessed for street repairs: $40/house, $115/hotel.", "action": "repairs", "house": 40, "hotel": 115},
    {"text": "You have won second prize in a beauty contest. Collect $10.", "action": "collect", "amount": 10},
    {"text": "You inherit $100.", "action": "collect", "amount": 100},
]

COLORS = {
    "brown": ["Mediterranean Ave", "Baltic Ave"],
    "light_blue": ["Oriental Ave", "Vermont Ave", "Connecticut Ave"],
    "pink": ["St. Charles Place", "States Ave", "Virginia Ave"],
    "orange": ["St. James Place", "Tennessee Ave", "New York Ave"],
    "red": ["Kentucky Ave", "Indiana Ave", "Illinois Ave"],
    "yellow": ["Atlantic Ave", "Ventnor Ave", "Marvin Gardens"],
    "green": ["Pacific Ave", "North Carolina Ave", "Pennsylvania Ave"],
    "dark_blue": ["Park Place", "Boardwalk"],
}

RAILROAD_POSITIONS = [5, 15, 25, 35]


class Player:
    def __init__(self, pid, name):
        self.id = pid
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0
        self.jail_free_cards = 0
        self.bankrupt = False

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "money": self.money,
            "position": self.position,
            "properties": self.properties,
            "in_jail": self.in_jail,
            "jail_free_cards": self.jail_free_cards,
            "bankrupt": self.bankrupt,
        }


class Game:
    def __init__(self, room_id):
        self.room_id = room_id
        self.players = {}
        self.player_order = []
        self.current_turn_index = 0
        self.started = False
        self.ownership = {}   # position -> player_id
        self.houses = {}      # position -> house count (5 = hotel)
        self.chance_deck = CHANCE_CARDS[:]
        self.community_deck = COMMUNITY_CHEST_CARDS[:]
        random.shuffle(self.chance_deck)
        random.shuffle(self.community_deck)
        self.log = []
        self.dice = (0, 0)
        self.doubles_count = 0
        self.waiting_for_action = None  # 'buy' or None
        self.last_roll_position = None

    def add_player(self, pid, name):
        if self.started or len(self.players) >= 6:
            return False
        self.players[pid] = Player(pid, name)
        self.player_order.append(pid)
        return True

    def remove_player(self, pid):
        if pid in self.players:
            del self.players[pid]
        if pid in self.player_order:
            self.player_order.remove(pid)

    def start(self):
        if len(self.players) < 2:
            return False, "Need at least 2 players"
        self.started = True
        random.shuffle(self.player_order)
        self.log_msg(f"Game started! Turn order: {', '.join(self.players[p].name for p in self.player_order)}")
        return True, "Game started"

    def current_player_id(self):
        if not self.player_order:
            return None
        return self.player_order[self.current_turn_index % len(self.player_order)]

    def log_msg(self, msg):
        self.log.append(msg)
        if len(self.log) > 50:
            self.log = self.log[-50:]

    def roll_dice(self, pid):
        if pid != self.current_player_id():
            return None, "Not your turn"
        if self.waiting_for_action:
            return None, "Waiting for action"

        player = self.players[pid]
        d1, d2 = random.randint(1, 6), random.randint(1, 6)
        self.dice = (d1, d2)
        is_doubles = d1 == d2

        if player.in_jail:
            if is_doubles:
                player.in_jail = False
                player.jail_turns = 0
                self.log_msg(f"{player.name} rolled doubles and got out of jail!")
            else:
                player.jail_turns += 1
                if player.jail_turns >= 3:
                    player.money -= 50
                    player.in_jail = False
                    player.jail_turns = 0
                    self.log_msg(f"{player.name} paid $50 to get out of jail.")
                else:
                    self.log_msg(f"{player.name} is in jail. Rolled {d1}+{d2}. ({3 - player.jail_turns} turns left)")
                    self._next_turn()
                    return self.state(), "In jail"

        if is_doubles:
            self.doubles_count += 1
            if self.doubles_count >= 3:
                self.log_msg(f"{player.name} rolled 3 doubles! Go to jail.")
                self._send_to_jail(player)
                self._next_turn()
                return self.state(), "Three doubles - jail"
        else:
            self.doubles_count = 0

        steps = d1 + d2
        old_pos = player.position
        new_pos = (old_pos + steps) % 40

        if new_pos < old_pos and not player.in_jail:
            player.money += 200
            self.log_msg(f"{player.name} passed GO! Collected $200.")

        player.position = new_pos
        self.last_roll_position = new_pos
        self.log_msg(f"{player.name} rolled {d1}+{d2}={steps}, moved to {BOARD[new_pos]['name']}")

        result = self._land_on(player, new_pos)

        if not self.waiting_for_action:
            if is_doubles and not player.in_jail:
                self.log_msg(f"{player.name} rolled doubles! Roll again.")
            else:
                self._next_turn()

        return self.state(), result

    def _land_on(self, player, pos):
        tile = BOARD[pos]
        t = tile["type"]

        if t == "go":
            player.money += 200
            self.log_msg(f"{player.name} landed on GO! Collect $200.")
            return "go"

        elif t == "property":
            if pos not in self.ownership:
                self.waiting_for_action = "buy"
                return f"buy_option:{pos}"
            elif self.ownership[pos] != player.id:
                owner = self.players[self.ownership[pos]]
                rent = self._calc_rent(pos, owner)
                player.money -= rent
                owner.money += rent
                self.log_msg(f"{player.name} paid ${rent} rent to {owner.name} for {tile['name']}.")
                self._check_bankruptcy(player)
                return f"paid_rent:{rent}"
            else:
                return "own_property"

        elif t == "railroad":
            if pos not in self.ownership:
                self.waiting_for_action = "buy"
                return f"buy_option:{pos}"
            elif self.ownership[pos] != player.id:
                owner = self.players[self.ownership[pos]]
                owned = sum(1 for p in RAILROAD_POSITIONS if p in self.ownership and self.ownership[p] == owner.id)
                rent = 25 * (2 ** (owned - 1))
                player.money -= rent
                owner.money += rent
                self.log_msg(f"{player.name} paid ${rent} railroad rent to {owner.name}.")
                self._check_bankruptcy(player)
                return f"paid_rent:{rent}"
            return "own_railroad"

        elif t == "utility":
            if pos not in self.ownership:
                self.waiting_for_action = "buy"
                return f"buy_option:{pos}"
            elif self.ownership[pos] != player.id:
                owner = self.players[self.ownership[pos]]
                owned_utils = sum(1 for p in [12, 28] if p in self.ownership and self.ownership[p] == owner.id)
                mult = 10 if owned_utils == 2 else 4
                rent = mult * sum(self.dice)
                player.money -= rent
                owner.money += rent
                self.log_msg(f"{player.name} paid ${rent} utility rent to {owner.name}.")
                self._check_bankruptcy(player)
                return f"paid_rent:{rent}"
            return "own_utility"

        elif t == "tax":
            player.money -= tile["amount"]
            self.log_msg(f"{player.name} paid ${tile['amount']} tax.")
            self._check_bankruptcy(player)
            return "tax"

        elif t == "go_to_jail":
            self._send_to_jail(player)
            return "jail"

        elif t == "chance":
            card = self.chance_deck.pop(0)
            self.chance_deck.append(card)
            self.log_msg(f"{player.name} drew Chance: {card['text']}")
            self._apply_card(player, card)
            return f"chance:{card['text']}"

        elif t == "community_chest":
            card = self.community_deck.pop(0)
            self.community_deck.append(card)
            self.log_msg(f"{player.name} drew Community Chest: {card['text']}")
            self._apply_card(player, card)
            return f"community_chest:{card['text']}"

        elif t == "free_parking":
            self.log_msg(f"{player.name} landed on Free Parking.")
            return "free_parking"

        elif t == "jail":
            self.log_msg(f"{player.name} is just visiting jail.")
            return "visiting_jail"

        return "ok"

    def _apply_card(self, player, card):
        action = card["action"]
        if action == "advance_to":
            target = card["target"]
            if target < player.position:
                player.money += 200
                self.log_msg(f"{player.name} passed GO! Collected $200.")
            player.position = target
            self._land_on(player, target)
        elif action == "collect":
            player.money += card["amount"]
        elif action == "pay":
            player.money -= card["amount"]
            self._check_bankruptcy(player)
        elif action == "go_to_jail":
            self._send_to_jail(player)
        elif action == "jail_free":
            player.jail_free_cards += 1
        elif action == "move":
            player.position = (player.position + card["amount"]) % 40
            self._land_on(player, player.position)
        elif action == "nearest_railroad":
            pos = player.position
            nearest = min(RAILROAD_POSITIONS, key=lambda r: (r - pos) % 40)
            if nearest < pos:
                player.money += 200
            player.position = nearest
            self._land_on(player, nearest)
        elif action == "repairs":
            total = 0
            for p in player.properties:
                h = self.houses.get(p, 0)
                if h == 5:
                    total += card["hotel"]
                else:
                    total += h * card["house"]
            player.money -= total
            self.log_msg(f"{player.name} paid ${total} for repairs.")
            self._check_bankruptcy(player)
        elif action == "pay_each":
            for pid, other in self.players.items():
                if pid != player.id and not other.bankrupt:
                    other.money -= card["amount"]
                    player.money += card["amount"]
        elif action == "collect_each":
            for pid, other in self.players.items():
                if pid != player.id and not other.bankrupt:
                    other.money -= card["amount"]
                    player.money += card["amount"]

    def _calc_rent(self, pos, owner):
        tile = BOARD[pos]
        houses = self.houses.get(pos, 0)
        color = tile.get("color")
        color_props = COLORS.get(color, [])
        monopoly = all(
            any(BOARD[i]["name"] == name and i in self.ownership and self.ownership[i] == owner.id
                for i in range(40))
            for name in color_props
        )
        if houses == 0 and monopoly:
            return tile["rent"][0] * 2
        return tile["rent"][min(houses, 5)]

    def _send_to_jail(self, player):
        player.position = 10
        player.in_jail = True
        player.jail_turns = 0
        self.log_msg(f"{player.name} went to jail!")

    def _check_bankruptcy(self, player):
        if player.money < 0:
            player.bankrupt = True
            self.log_msg(f"{player.name} is bankrupt!")
            for p in player.properties:
                del self.ownership[p]
                if p in self.houses:
                    del self.houses[p]
            player.properties = []
            if player.id in self.player_order:
                self.player_order.remove(player.id)
            if self.current_turn_index >= len(self.player_order):
                self.current_turn_index = 0

    def buy_property(self, pid):
        if pid != self.current_player_id():
            return None, "Not your turn"
        if self.waiting_for_action != "buy":
            return None, "No property to buy"
        player = self.players[pid]
        pos = player.position
        tile = BOARD[pos]
        price = tile["price"]
        if player.money < price:
            self.waiting_for_action = None
            self._next_turn()
            return self.state(), "Not enough money"
        player.money -= price
        self.ownership[pos] = pid
        player.properties.append(pos)
        self.log_msg(f"{player.name} bought {tile['name']} for ${price}.")
        self.waiting_for_action = None
        self._next_turn()
        return self.state(), "bought"

    def decline_buy(self, pid):
        if pid != self.current_player_id():
            return None, "Not your turn"
        self.waiting_for_action = None
        self.log_msg(f"{self.players[pid].name} declined to buy {BOARD[self.players[pid].position]['name']}.")
        self._next_turn()
        return self.state(), "declined"

    def buy_house(self, pid, pos):
        player = self.players.get(pid)
        if not player:
            return None, "Player not found"
        if self.ownership.get(pos) != pid:
            return None, "You don't own this property"
        tile = BOARD[pos]
        if tile["type"] != "property":
            return None, "Not a property"
        color = tile["color"]
        color_props = COLORS.get(color, [])
        for name in color_props:
            prop_pos = next((i for i, t in enumerate(BOARD) if t["name"] == name), None)
            if prop_pos is None or self.ownership.get(prop_pos) != pid:
                return None, "You don't own the full color group"
        current = self.houses.get(pos, 0)
        if current >= 5:
            return None, "Already has a hotel"
        cost = tile["house_cost"]
        if player.money < cost:
            return None, "Not enough money"
        player.money -= cost
        self.houses[pos] = current + 1
        label = "hotel" if current + 1 == 5 else "house"
        self.log_msg(f"{player.name} built a {label} on {tile['name']}.")
        return self.state(), "built"

    def use_jail_free(self, pid):
        player = self.players.get(pid)
        if not player or not player.in_jail:
            return None, "Not in jail"
        if player.jail_free_cards < 1:
            return None, "No jail free card"
        player.jail_free_cards -= 1
        player.in_jail = False
        player.jail_turns = 0
        self.log_msg(f"{player.name} used a Get Out of Jail Free card.")
        return self.state(), "freed"

    def _next_turn(self):
        active = [p for p in self.player_order if not self.players[p].bankrupt]
        if len(active) <= 1:
            return
        self.current_turn_index = (self.current_turn_index + 1) % len(self.player_order)
        while self.players[self.player_order[self.current_turn_index]].bankrupt:
            self.current_turn_index = (self.current_turn_index + 1) % len(self.player_order)
        self.doubles_count = 0

    def winner(self):
        active = [p for p in self.player_order if not self.players[p].bankrupt]
        if len(active) == 1:
            return self.players[active[0]].name
        return None

    def state(self):
        return {
            "started": self.started,
            "players": {pid: p.to_dict() for pid, p in self.players.items()},
            "player_order": self.player_order,
            "current_player": self.current_player_id(),
            "ownership": {str(k): v for k, v in self.ownership.items()},
            "houses": {str(k): v for k, v in self.houses.items()},
            "log": self.log[-10:],
            "dice": self.dice,
            "waiting_for_action": self.waiting_for_action,
            "board": BOARD,
            "winner": self.winner(),
        }
