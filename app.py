from flask import Flask, render_template, request, jsonify
from logic import is_safe_state, detect_deadlock, draw_resource_graph
import os

app = Flask(__name__)

# Create static directory if it doesn't exist
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check-safe', methods=['POST'])
def check_safe():
    try:
        data = request.json
        allocation = data['allocation']
        max_need = data['max']
        available = data['available']

        safe, sequence = is_safe_state(allocation, max_need, available)
        return jsonify({'safe': safe, 'sequence': sequence})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/detect-deadlock', methods=['POST'])
def detect():
    try:
        data = request.json
        allocation = data['allocation']
        request_matrix = data['request']
        deadlocked = detect_deadlock(allocation, request_matrix)
        return jsonify({'deadlocked': deadlocked})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/draw-graph', methods=['POST'])
def draw_graph():
    try:
        data = request.json
        allocation = data['allocation']
        max_need = data['max']
        available = data['available']
        
        img_path = draw_resource_graph(allocation, max_need, available)
        return jsonify({"status": "success", "path": img_path})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)