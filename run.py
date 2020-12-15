from flask import Flask, render_template, session, make_response, url_for, redirect, request
from flask_socketio import SocketIO, emit
import re
import time
from db_query import news_query, sector_query

app=Flask(__name__)

socketio=SocketIO(app,cors_allowed_origins='*', pingInterval=600000,pingTimeout=600000,async_mode='threading', manage_session=False)
msg_pack=[]

if True:
  @socketio.on('connect')
  def connect():
    print('유저 접속')

  @socketio.on('client_send_name')
  def client_send_name_handler(data):
    print(dir(data))
    client_name=data['client_name']
    msg=f'{client_name}님이 입장하셨습니다.'
    emit('system_msg',{'user':'admin','msg':msg},broadcast=True)
    # if len(msg_pack)>100:
    #   msg_pack.pop(msg_pack[0])
    #   msg_pack.append({'user':'awedmin','msg':msg})
    # else:
    #   msg_pack.append({'user':'admin','msg':msg}) 
    
  @socketio.on('client_send_msg')
  def client_send_msg_handler(data):
    client_name=data['client_name']
    msg=data['client_msg']
    emit('server_send_msg',{'user':client_name,'msg':msg, 'stock_code':'Null'},broadcast=True)
    # if len(msg_pack)>100:
    #   msg_pack.pop(msg_pack[0])
    #   msg_pack.append({'user':client_name,'msg':msg})
    # else:
    #   msg_pack.append({'user':client_name,'msg':msg})

@app.route('/')
def home():
    return render_template('home.html', name='사용자명')

@app.route('/news')
def news():
    # if request.args.get('sector')=='None' or request.args.get('sector') is False:
    #   if request.args.get('pageNo'):
    #     pageNo=request.args.get('pageNo')
    #   else:
    #     pageNo='1'
    #   sector=request.args.get('sector')
    #   data=sector_query(sector,pageNo)
    #   print(data)
    #   return render_template('news.html', pageNo=int(pageNo),result=data, sector=sector )

    # else:
    if request.args.get('pageNo'):
      pageNo=request.args.get('pageNo')
    else:
      pageNo='1'
    data=news_query(pageNo)
    print(data)
    return render_template('news.html', pageNo=int(pageNo),result=data)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/chat')
def chat():
  if 'username' in session:
    print('''
    
    
    
    
    
    
    
    테스트
    
    
    
    
    
    
    
    
    
    ''')
    return render_template('chat.html', reconnect='True')
  else:
    return render_template('chat.html', reconnect='False')


if __name__=='__main__':
  socketio.run(app, debug=True)



