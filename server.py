from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(_name_)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
db = SQLAlchemy(app)
socketio = SocketIO(app)

# Model for storing chat messages
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(500), nullable=False)

# Route to the chatroom
@app.route('/')
def index():
    messages = Message.query.all()
    return render_template('chat.html', messages=messages)

# WebSocket event handling
@socketio.on('message')
def handle_message(msg):
    username = msg['username']
    message_content = msg['message']
    
    # Save message to the database
    new_message = Message(username=username, message=message_content)
    db.session.add(new_message)
    db.session.commit()

    # Broadcast the message to all connected clients
    send(msg, broadcast=True)

if _name_ == '_main_':
    # Create database if it doesn't exist
    if not os.path.exists('chat.db'):
        db.create_all()
    
    socketio.run(app, debug=True)