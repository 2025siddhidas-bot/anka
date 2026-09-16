import matplotlib.pyplot as plt
import numpy as np
import io
import base64

def generate_bar_chart(actual_scores):
    # Category labels with line breaks for clean X-axis formatting
    labels = ['Physical\nWellness', 'Mental\nWellness', 'Pranic\nWellness', 
              'Psychic\nWellness', 'Behavioural\nWellness', 'Lifestyle\nWellness']
    
    # Static maximum scores extracted from the reference table
    max_scores = [4050, 1640, 2070, 1200, 3390, 1250]
    
    x = np.arange(len(labels))
    width = 0.32  # Bar thickness
    
    # Initialize the figure with proper dimensions
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot the clustered bars with matched hex colors
    rects1 = ax.bar(x - width/2, max_scores, width, label='Max Score', color='#BC764A')
    rects2 = ax.bar(x + width/2, actual_scores, width, label='Score', color='#3F5265')
    
    # Attach data labels directly above the bars
    ax.bar_label(rects1, padding=4, fontsize=10, fontweight='bold', color='#333333')
    ax.bar_label(rects2, padding=4, fontsize=10, fontweight='bold', color='#333333')
    
    # Format the Y-axis to scale exactly from 0 to 4500
    ax.set_ylim(0, 4700) # Slightly above 4500 to leave breathing room for the labels
    ax.set_yticks(np.arange(0, 5000, 500))
    ax.tick_params(axis='y', colors='#555555')
    
    # Format the X-axis labels
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11, fontweight='bold', color='#444444')
    ax.tick_params(axis='x', bottom=False) # Hide bottom tick marks for a cleaner look
    
    # Remove top and right border spines to match the modern Canva aesthetic
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#DDDDDD')
    ax.spines['bottom'].set_color('#DDDDDD')
    
    # Position the legend horizontally at the bottom center
    ax.legend(
        loc='upper center', 
        bbox_to_anchor=(0.5, -0.15), 
        ncol=2, 
        frameon=False, 
        fontsize=11,
        handletextpad=0.5
    )
    
    plt.tight_layout()
    
    # ---------------------------------------------------------
    # LOCAL TESTING OUTPUT
    # This saves the chart as an image in your VS Code folder
    # ---------------------------------------------------------
    output_filename = 'test_bar_chart.png'
    plt.savefig(output_filename, format='png', dpi=300, bbox_inches='tight', transparent=False)
    print(f"Success! Open {output_filename} in VS Code to see the result.")
    
    # ---------------------------------------------------------
    # FUTURE RENDER.COM OUTPUT
    # When moving to the API, we will swap to this base64 return:
    # buf = io.BytesIO()
    # plt.savefig(buf, format='png', dpi=300, bbox_inches='tight', transparent=True)
    # buf.seek(0)
    # return base64.b64encode(buf.read()).decode('utf-8')
    # ---------------------------------------------------------
    
    plt.close(fig)

if __name__ == '__main__':
    # Test dataset matching the exact scores from your screenshot
    test_scores = [3344, 1258, 1754, 909, 2634, 1027]
    generate_bar_chart(test_scores)