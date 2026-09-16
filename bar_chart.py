from flask import Flask, request, jsonify
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)

@app.route('/generate-bar-chart', methods=['POST'])
def generate_bar_chart():
    # 1. Catch the true data sent by Make.com
    data = request.json
    
    # Expecting Make.com to send: {"scores": [3344, 1258, ...]}
    # If it fails, it defaults to zeros to prevent crashes
    actual_scores = data.get('scores', [0, 0, 0, 0, 0, 0])
    
    labels = ['Physical\nWellness', 'Mental\nWellness', 'Pranic\nWellness', 
              'Psychic\nWellness', 'Behavioural\nWellness', 'Lifestyle\nWellness']
    max_scores = [4050, 1640, 2070, 1200, 3390, 1250]
    
    x = np.arange(len(labels))
    width = 0.32  
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    rects1 = ax.bar(x - width/2, max_scores, width, label='Max Score', color='#BC764A')
    rects2 = ax.bar(x + width/2, actual_scores, width, label='Score', color='#3F5265')
    
    ax.bar_label(rects1, padding=4, fontsize=10, fontweight='bold', color='#333333')
    ax.bar_label(rects2, padding=4, fontsize=10, fontweight='bold', color='#333333')
    
    ax.set_ylim(0, 4700) 
    ax.set_yticks(np.arange(0, 5000, 500))
    ax.tick_params(axis='y', colors='#555555')
    
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11, fontweight='bold', color='#444444')
    ax.tick_params(axis='x', bottom=False) 
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#DDDDDD')
    ax.spines['bottom'].set_color('#DDDDDD')
    
    ax.legend(
        loc='upper center', 
        bbox_to_anchor=(0.5, -0.15), 
        ncol=2, 
        frameon=False, 
        fontsize=11,
        handletextpad=0.5
    )
    
    plt.tight_layout()
    
    # 2. Convert image to Base64 text string instead of saving a file
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300, bbox_inches='tight', transparent=True)
    buf.seek(0)
    plt.close(fig)
    
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    
    # 3. Send the encoded image back to Make.com
    return jsonify({
        "status": "success",
        "chart_base64": image_base64
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)