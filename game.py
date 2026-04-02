"""
Main game logic for Rock-Paper-Scissors
"""
from utils import *
from ai_player import AIPlayer

class RockPaperScissorsGame:
    def __init__(self):
        self.player_score = 0
        self.ai_score = 0
        self.rounds_played = 0
        self.game_history = []
        
    def get_player_choice(self):
        """Get valid choice from player"""
        valid_choices = ['rock', 'paper', 'scissors', '1', '2', '3']
        choice_map = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        
        while True:
            print("\nMake your choice:")
            print("1. 🪨 Rock")
            print("2. 📄 Paper") 
            print("3. ✂️  Scissors")
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
    
    def update_scores(self, result):
        """Update game scores"""
        if result == "player":
            self.player_score += 1
        elif result == "ai":
            self.ai_score += 1
        self.rounds_played += 1
    
    def display_result(self, result):
        """Display round result"""
        if result == "tie":
            print("🤝 It's a TIE!")
        elif result == "player":
            print("🎉 YOU WIN this round!")
        else:
            print("🤖 AI WINS this round!")
    
    def display_score(self):
        """Display current score"""
        print(f"\n📊 SCORE BOARD:")
        print(f"You: {self.player_score} | AI: {self.ai_score}")
        print(f"Rounds played: {self.rounds_played}")
    
    def play_round(self, ai_player):
        """Play a single round"""
        player_choice = self.get_player_choice()
        if player_choice is None:
            return False  # Player wants to quit
        
        print("\nGet ready...")
        animate_countdown()
        
        ai_choice = ai_player.make_choice()
        
        # Display choices
        display_choices(player_choice, ai_choice)
        
        # Determine winner
        result = self.determine_winner(player_choice, ai_choice)
        self.display_result(result)
        self.update_scores(result)
        
        # Let AI learn from this move
        ai_player.learn_from_move(player_choice)
        
        # Record game history
        self.game_history.append({
            'round': self.rounds_played,
            'player': player_choice,
            'ai': ai_choice,
            'result': result
        })
        
        return True
    
    def display_final_stats(self, ai_player):
        """Display final game statistics"""
        clear_screen()
        print("🏁 GAME OVER - FINAL STATS")
        print("=" * 40)
        
        # Overall winner
        if self.player_score > self.ai_score:
            print("🏆 CONGRATULATIONS! YOU WON THE GAME!")
        elif self.ai_score > self.player_score:
            print("🤖 AI WINS THE GAME! Better luck next time!")
        else:
            print("🤝 IT'S A TIE GAME!")
        
        # Detailed stats
        print(f"\nFinal Score: You {self.player_score} - {self.ai_score} AI")
        print(f"Total rounds: {self.rounds_played}")
        
        if self.rounds_played > 0:
            win_rate = (self.player_score / self.rounds_played) * 100
            print(f"Your win rate: {win_rate:.1f}%")
        
        # AI stats
        ai_stats = ai_player.get_stats()
        print(f"\nAI Difficulty: {ai_stats['difficulty'].upper()}")
        if ai_stats['difficulty'] == 'smart':
            print(f"Patterns learned: {ai_stats['patterns_learned']}")
