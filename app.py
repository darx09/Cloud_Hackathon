from flask import Flask, render_template, request, jsonify
import sqlite3  # For SQLite database

# Initialize the Flask app
app = Flask(__name__)

# Function to initialize the database
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, info TEXT)')
        conn.commit()

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API to save data to the database
@app.route('/save', methods=['POST'])
def save_data():
    try:
        # Get data from the frontend
        data = request.json.get('data')
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Save data to the database
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO data (info) VALUES (?)', (data,))
            conn.commit()
            return jsonify({'message': 'Data saved successfully!'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API to retrieve all data from the database
@app.route('/data', methods=['GET'])
def get_data():
    try:
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM data')
            rows = cur.fetchall()
            return jsonify(rows)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Run the app in debug mode
