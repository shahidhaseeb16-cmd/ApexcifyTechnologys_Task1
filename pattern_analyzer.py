"""
Pattern analyzer for advanced AI behavior
"""
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None
from collections import Counter

class PatternAnalyzer:
    def __init__(self, game_history):
        self.game_history = game_history
    
    def analyze_player_patterns(self):
        """Analyze player choice patterns"""
        if not self.game_history:
            return None
        
        player_choices = [round_data['player'] for round_data in self.game_history]
        choice_counts = Counter(player_choices)
        
        analysis = {
            'total_rounds': len(player_choices),
            'choice_distribution': dict(choice_counts),
            'most_frequent': choice_counts.most_common(1)[0] if choice_counts else None,
            'patterns': self._find_sequences(player_choices)
        }
        
        return analysis
    
    def _find_sequences(self, choices):
        """Find repeating sequences in choices"""
        sequences = {}
        
        # Look for 2-move and 3-move patterns
        for seq_len in [2, 3]:
            if len(choices) >= seq_len:
                for i in range(len(choices) - seq_len + 1):
                    sequence = tuple(choices[i:i + seq_len])
                    sequences[sequence] = sequences.get(sequence, 0) + 1
        
        # Filter out sequences that appear only once
        return {seq: count for seq, count in sequences.items() if count > 1}
    
    def display_analysis(self):
        """Display pattern analysis"""
        analysis = self.analyze_player_patterns()
        if not analysis:
            print("No data to analyze yet.")
            return
        
        print("\n📈 PATTERN ANALYSIS")
        print("=" * 30)
        print(f"Total rounds analyzed: {analysis['total_rounds']}")
        
        print("\n🎯 Choice Distribution:")
        for choice, count in analysis['choice_distribution'].items():
            percentage = (count / analysis['total_rounds']) * 100
            print(f"  {choice.capitalize()}: {count} times ({percentage:.1f}%)")
        
        if analysis['most_frequent']:
            choice, count = analysis['most_frequent']
            print(f"\n⭐ Most frequent choice: {choice.capitalize()} ({count} times)")
        
        if analysis['patterns']:
            print(f"\n🔍 Repeating Patterns Found:")
            for pattern, count in analysis['patterns'].items():
                pattern_str = " → ".join(pattern)
                print(f"  {pattern_str}: {count} times")
    
    def create_visualization(self):
        """Create visual charts of player patterns"""
        try:
            analysis = self.analyze_player_patterns()
            if not analysis:
                return
            
            # Create pie chart of choice distribution
            choices = list(analysis['choice_distribution'].keys())
            counts = list(analysis['choice_distribution'].values())
            
            plt.figure(figsize=(10, 5))
            
            # Pie chart
            plt.subplot(1, 2, 1)
            plt.pie(counts, labels=choices, autopct='%1.1f%%', startangle=90)
            plt.title('Choice Distribution')
            
            # Bar chart
            plt.subplot(1, 2, 2)
            plt.bar(choices, counts, color=['red', 'blue', 'green'])
            plt.title('Choice Frequency')
            plt.ylabel('Count')
            
            plt.tight_layout()
            plt.show()
        
        except ImportError:
            print("Matplotlib not installed. Install with: pip install matplotlib")
