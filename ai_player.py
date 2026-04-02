from collections import deque, defaultdict
import random

class AIPlayer:
    def __init__(self, difficulty="smart"):
        self.difficulty = difficulty
        self.choices = ["rock", "paper", "scissors"]
        self.player_history = deque(maxlen=5)  # track last 5 moves
        self.pattern_memory = defaultdict(lambda: defaultdict(int))
        self.games_played = 0

    def make_choice(self):
        if self.difficulty == "random" or self.games_played < 3:
            return random.choice(self.choices)
        else:
            return self._smart_choice()

    def _smart_choice(self):
        if len(self.player_history) < 2:
            return random.choice(self.choices)

        # Predict player's next move
        last_pattern = tuple(list(self.player_history)[-2:])
        predicted = self._predict_player_move(last_pattern)

        # Counter the predicted move
        counters = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        # 70% chance to counter, 30% random
        return counters.get(predicted, random.choice(self.choices)) if random.random() < 0.7 else random.choice(self.choices)

    def _predict_player_move(self, pattern):
        counts = self.pattern_memory.get(pattern, None)
        if counts:
            return max(counts, key=counts.get)  # most probable next move
        else:
            return random.choice(self.choices)

    def learn_from_move(self, move):
        if len(self.player_history) >= 2:
            pattern = tuple(list(self.player_history)[-2:])
            self.pattern_memory[pattern][move] += 1
        self.player_history.append(move)
        self.games_played += 1