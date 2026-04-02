"""
Utility functions for Rock-Paper-Scissors game
"""
import time
import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Display game banner"""
    print("=" * 50)
    print("🎮 ROCK-PAPER-SCISSORS AI GAME 🎮")
    print("=" * 50)

def get_choice_emoji(choice):
    """Return emoji for choice"""
    emojis = {
        'rock': '🪨',
        'paper': '📄',
        'scissors': '✂️'
    }
    return emojis.get(choice.lower(), '❓')

def animate_countdown():
    """Animated countdown"""
    for i in range(3, 0, -1):
        print(f"\n{i}...")
        time.sleep(0.8)
    print("SHOOT! 🎯\n")
    time.sleep(0.5)

def display_choices(player_choice, ai_choice):
    """Display both choices with emojis"""
    print(f"You chose: {get_choice_emoji(player_choice)} {player_choice.upper()}")
    print(f"AI chose:  {get_choice_emoji(ai_choice)} {ai_choice.upper()}")
    print("-" * 30)
