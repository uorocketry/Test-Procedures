import threading
import time
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, escape, request


app = Flask(__name__)
socketio = SocketIO(app)

page1 = {"avionics": ["task 1", "task 2"], "prop": ["task1", "task2", "task3"]}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print("connected")
    createNewPage("first title", "this is a short description")

def thread_function(name):
    print(name)
    i = 0
    
    while True:
        print(f"ok{i}")
        i += 1
        if(i == 5):
            createNewPage("other title", "this is a short description 2")
        time.sleep(1)

def createNewPage(title, description):
    socketio.emit('load page',  {'title':title, 'description':description, "content":page1})


def startThread():
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    x.start()

if __name__ == "__main__":
    startThread()
    socketio.run(app)
    