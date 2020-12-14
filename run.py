from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app=Flask(__name__)
app.secret_key='personal'

@app.route('/')
def main():
  return render_template('main.html')

@app.route('/chat')
def chat():
  return render_template('chat.html')

if __name__=='__main__':
  app.run(debug=True)