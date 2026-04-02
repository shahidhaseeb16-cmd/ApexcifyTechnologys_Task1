"""
Main game logic for Rock-Paper-Scissors
"""

import random
import time
import os

#  AI PLAYER 
class AIPlayer:
    def __init__(self, difficulty='easy'):
        self.difficulty = difficulty
        self.patterns_learned = 0
        self.player_history = []

    def make_choice(self):
        """AI chooses move"""
        if self.difficulty == 'easy' or not self.player_history:
            return random.choice(['rock', 'paper', 'scissors'])
        else:
            predicted_player = self.player_history[-1]
            counter = {'rock':'paper', 'paper':'scissors', 'scissors':'rock'}
            return counter[predicted_player]

    def learn_from_move(self, player_choice):
        """AI learns from player's move"""
        self.player_history.append(player_choice)
        if self.difficulty == 'smart':
            self.patterns_learned = len(set(self.player_history))

    def get_stats(self):
        return {
            'difficulty': self.difficulty,
            'patterns_learned': self.patterns_learned
        }

#  GAME CLASS 
class RockPaperScissorsGame:
    def __init__(self, difficulty='easy'):
        self.player_score = 0
        self.ai_score = 0
        self.rounds_played = 0
        self.game_history = []
        self.ai_player = AIPlayer(difficulty)

    #  PLAYER INPUT 
    def get_player_choice(self):
        """Get valid choice from player"""
        choice_map = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        while True:
            print("\nMake your choice:")
            print("1. 🪨 Rock")
            print("2. 📄 Paper")
            print("3. ✂️ Scissors")
            print("Type 'quit' to exit")

            choice = input("\nEnter your choice (1-3 or rock/paper/scissors): ").lower().strip()

            if choice == 'quit':
                return None
            if choice in choice_map:
                return choice_map[choice]
            elif choice in ['rock', 'paper', 'scissors']:
                return choice
            else:
                print("❌ Invalid choice! Please try again.")

    #  DETERMINE WINNER 
    def determine_winner(self, player_choice, ai_choice):
        """Determine round winner"""
        if player_choice == ai_choice:
            return "tie"
        winning_combinations = {
            ('rock', 'scissors'),
            ('paper', 'rock'),
            ('scissors', 'paper')
        }
        if (player_choice, ai_choice) in winning_combinations:
            return "player"
        else:
            return "ai"

    #  UPDATE SCORES 
    def update_scores(self, result):
        """Update the score based on result"""
        if result == "player":
            self.player_score += 1
        elif result == "ai":
            self.ai_score += 1
        self.rounds_played += 1

    #  DISPLAY FUNCTIONS 
    def display_result(self, result):
        """Show result of the round"""
        if result == "tie":
            print("🤝 It's a TIE!")
        elif result == "player":
            print("🎉 YOU WIN this round!")
        else:
            print("🤖 AI WINS this round!")

    def display_score(self):
        """Show current scoreboard"""
        print(f"\n📊 SCORE BOARD:")
        print(f"You: {self.player_score} | AI: {self.ai_score}")
        print(f"Rounds played: {self.rounds_played}")

    def display_choices(self, player_choice, ai_choice):
        """Show what player and AI chose"""
        choice_emoji = {'rock':'🪨', 'paper':'📄', 'scissors':'✂️'}
        print(f"You chose: {player_choice} {choice_emoji[player_choice]}")
        print(f"AI chose: {ai_choice} {choice_emoji[ai_choice]}")

    def animate_countdown(self):
        """Simple 3-2-1 Go countdown"""
        for i in range(3, 0, -1):
            print(f"{i}...")
            time.sleep(0.5)
        print("Go!\n")

    def clear_screen(self):
        """Clear console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    #  PLAY ROUND 
    def play_round(self):
        """Play one round of the game"""
        player_choice = self.get_player_choice()
        if player_choice is None:
            return False  # Player wants to quit

        print("\nGet ready...")
        self.animate_countdown()

        ai_choice = self.ai_player.make_choice()

        self.display_choices(player_choice, ai_choice)

        result = self.determine_winner(player_choice, ai_choice)
        self.display_result(result)
        self.update_scores(result)

        # Let AI learn
        self.ai_player.learn_from_move(player_choice)

        # Record game history
        self.game_history.append({
            'round': self.rounds_played,
            'player': player_choice,
            'ai': ai_choice,
            'result': result
        })

        return True

    #  FINAL STATS 
    def display_final_stats(self):
        """Show final game statistics"""
        self.clear_screen()
        print("🏁 GAME OVER - FINAL STATS")
        print("="*40)

        if self.player_score > self.ai_score:
            print("🏆 CONGRATULATIONS! YOU WON THE GAME!")
        elif self.ai_score > self.player_score:
            print("🤖 AI WINS THE GAME! Better luck next time!")
        else:
            print("🤝 IT'S A TIE GAME!")

        print(f"\nFinal Score: You {self.player_score} - {self.ai_score} AI")
        print(f"Total rounds: {self.rounds_played}")
        if self.rounds_played > 0:
            win_rate = (self.player_score / self.rounds_played) * 100
            print(f"Your win rate: {win_rate:.1f}%")

        ai_stats = self.ai_player.get_stats()
        print(f"\nAI Difficulty: {ai_stats['difficulty'].upper()}")
        if ai_stats['difficulty'] == 'smart':
            print(f"Patterns learned: {ai_stats['patterns_learned']}")

#  RUN GAME 
if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.clear_screen()
    print("🎮 Welcome to Rock-Paper-Scissors Game!")

    difficulty = input("Choose AI difficulty (easy/smart): ").lower().strip()
    if difficulty not in ['easy', 'smart']:
        difficulty = 'easy'
    game.ai_player = AIPlayer(difficulty)

    while True:
        continue_game = game.play_round()
        if not continue_game:
            break
        game.display_score()

    game.display_final_stats()
