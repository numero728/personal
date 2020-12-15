from flask import Flask, render_template, session, make_response, url_for, redirect, request, jsonify
from flask_socketio import SocketIO, emit
import re
import time
from DB.db_query import *

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

if True:
  @app.route('/')
  def home():
      return render_template('home.html', name='사용자명')

  @app.route('/news')
  def news():
      # pageNo이 있는 경우;
      # 주어진 pageNo으로 쿼리 수행한 다음
      # 결과 반환
      print(request.args.get('pageNo'))
      if 'pageNo' in request.args:
        pageNo=request.args.get('pageNo')
        data=news_query(pageNo)
        res={
          'pageNo':pageNo,
          'result':data
          }
        return jsonify(res)
      else:
        pageNo=1
        data=news_query(pageNo)
        return render_template('news.html', result=data, pageNo=pageNo)

  @app.route('/exchange')
  def exchange():
      data=exch_query()
      return render_template('exchange.html', result=data)

  @app.route('/index')
  def index():
      data=index_query()
      return render_template('index.html', result=data)

  @app.route('/youtube')
  def youtube():
      data=youtube_query()
      return render_template('youtube.html', result=data)


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



