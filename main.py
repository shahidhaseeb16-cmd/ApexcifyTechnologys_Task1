"""
Main entry point
"""
from utils import *
from game import RockPaperScissorsGame
from ai_player import AIPlayer
from pattern_analyzer import PatternAnalyzer

def select_difficulty():
    """Let player select AI difficulty"""
    print("\n🎚️  Select AI Difficulty:")
    print("1. Random AI (Easy)")
    print("2. Smart AI (Hard - Learns your patterns)")
    
    while True:
        choice = input("\nSelect difficulty (1 or 2): ").strip()
        if choice == '1':
            return "random"
        elif choice == '2':
            return "smart"
        else:
            print("❌ Please enter 1 or 2")

def main_menu():
    """Display main menu"""
    clear_screen()
    display_banner()
    
    print("\n🎮 Welcome to Rock-Paper-Scissors AI!")
    print("\nHow to play:")
    print("• Choose Rock, Paper, or Scissors")
    print("• Rock beats Scissors")
    print("• Scissors beats Paper") 
    print("• Paper beats Rock")
    print("• First to score more wins!")
    
    difficulty = select_difficulty()
    return difficulty

def play_game():
    """Main game loop"""
    difficulty = main_menu()
    
    # Initialize game components
    game = RockPaperScissorsGame()
    ai_player = AIPlayer(difficulty=difficulty)
    
    print(f"\n🤖 AI set to {difficulty.upper()} mode")
    input("\nPress Enter to start the game...")
    
    # Main game loop
    while True:
        clear_screen()
        display_banner()
        game.display_score()
        
        # Play a round
        continue_game = game.play_round(ai_player)
        
        if not continue_game:
            break
        
        # Ask if player wants to continue
        print("\n" + "="*30)
        choice = input("Continue playing? (y/n): ").lower().strip()
        if choice in ['n', 'no', 'quit']:
            break
    
    # Display final statistics
    game.display_final_stats(ai_player)
    
    # Pattern analysis for smart AI
    if difficulty == "smart" and game.rounds_played > 0:
        show_analysis = input("\nWould you like to see pattern analysis? (y/n): ").lower().strip()
        if show_analysis in ['y', 'yes']:
            analyzer = PatternAnalyzer(game.game_history)
            analyzer.display_analysis()

def main():
    """Main function"""
    try:
        while True:
            play_game()
            
            play_again = input("\nWould you like to play another game? (y/n): ").lower().strip()
            if play_again not in ['y', 'yes']:
                break
        
        print("\n🎮 Thanks for playing Rock-Paper-Scissors AI!")
        print("👋 See you next time!")
        
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
