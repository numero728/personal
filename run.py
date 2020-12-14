from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app=Flask(__name__)
app.secret_key='personal'

@app.route('/')
def home():
  return render_template('index.html')

if __name__=='__main__':
  app.run(debug=True)