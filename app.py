import threading
import time
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, escape, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

i = 0

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print("connected")
    #emit('after connect',  {'data':'Lets dance'})

def thread_function(name):
    print(name)
    global i
    
    while True:
        print(f"ok{i}")
        i += 1
        socketio.emit('after connect',  {'data':f'{i}'})
        time.sleep(0.01)


def startThread():
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    x.start()

if __name__ == "__main__":
    startThread()
    socketio.run(app)
    