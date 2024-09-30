
## Real-Time Chat Application in Python

This project is a basic *real-time chat application* built using Python's socket and threading modules. It allows multiple clients to connect to a server and exchange messages that are broadcast to all connected clients in real time.

### Key Features:
- *Real-time message broadcasting* between clients.
- Supports *multiple client connections* to the server.
- *Unique nicknames* for each client.
- Messages are shared with all connected clients.
- *Simple and easy-to-understand code* for educational purposes.

### How It Works:
1. The server listens for incoming connections and manages all clients.
2. Each client is assigned a unique nickname upon connecting.
3. Clients send messages to the server, which broadcasts them to all other connected clients.
4. Clients can send and receive messages simultaneously in real time.

### Requirements:
- *Python 3.x* installed.
- No additional external libraries required.

### How to Run:
1. *Run the Server:*
   - Open a terminal and navigate to the project directory.
   - Start the server by running:
     bash
     python server.py
     
   - The server listens for incoming connections on localhost:55555.

2. *Run the Client(s):*
   - Open a new terminal (repeat this to simulate multiple clients).
   - Start a client by running:
     bash
     python client.py
     
   - Enter a unique nickname to join the chat.

3. *Example Workflow:*
   - Start the server: 
     bash
     python server.py
     
   - Run multiple clients:
     bash
     python client.py
     
   - Messages sent by one client will be received by all other clients in real time.

### Project Structure:

├── server.py   # Server code
├── client.py   # Client code
└── README.md   # Documentation


### Future Enhancements:
- *Private Messaging*: Add functionality for clients to send private messages.
- *Encryption*: Implement message encryption for secure communication.
- *Graphical User Interface (GUI)*: Use frameworks like Tkinter or PyQt to enhance the user experience.
- *Persistent Chat History*: Save chat messages to a file or database for future reference.

