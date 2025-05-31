from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

# Database initialization
def init_db():
    conn = sqlite3.connect('hostels.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hostels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_type TEXT NOT NULL,
            owner_name TEXT NOT NULL,
            location TEXT NOT NULL,
            rent INTEGER NOT NULL,
            contact TEXT NOT NULL,
            description TEXT NOT NULL,
            image_path TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database when app starts
init_db()

@app.route('/api/submit-listing', methods=['POST'])
def submit_listing():
    try:
        data = request.form
        
        # Handle file upload
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
            
        # Create uploads directory if it doesn't exist
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
            
        # Save the file
        filename = os.path.join('uploads', file.filename)
        file.save(filename)
        
        # Connect to database
        conn = sqlite3.connect('hostels.db')
        cursor = conn.cursor()
        
        # Insert data into database
        cursor.execute('''
            INSERT INTO hostels (room_type, owner_name, location, rent, contact, description, image_path)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['roomType'],
            data['ownerName'],
            data['location'],
            data['rent'],
            data['contact'],
            data['description'],
            filename
        ))
        
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Listing added successfully'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 