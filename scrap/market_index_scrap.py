import requests
import pandas as pd
from bs4 import BeautifulSoup as BS
import lxml
from selenium import webdriver
import time
import sys
from sqlalchemy import create_engine
import pymysql
import os
import date
try:
    cwd=str(os.path.abspath(os.getcwd()))
    upath=cwd+'\\chromedriver.exe'
    driver=webdriver.Chrome(executable_path=cwd+'\\chromedriver.exe')
    url='http://index.krx.co.kr/contents/IDX/0101/IDX0101.jsp'
    driver.get(url)
    time.sleep(2)
    html=driver.page_source
    soup=BS(html,'lxml')
    table=soup.select('table')
    table_=table[-1]
    df=pd.read_html(str(table_))
    df=df[0]
    df.set_index('지수명')
    dialect='mysql'
    db_driver='pymysql'
    username='admin'
    password='pnudb960726!'
    host='personaldb.cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com'
    port='3306'
    database='scrap_data'
    db_url=f"{dialect}+{db_driver}://{username}:{password}@{host}:{port}/{database}"
    print(db_url)
    engine=create_engine(db_url)
    conn=engine.connect()
    df.to_sql('market_index',conn,if_exists='replace',index=False)
except Exception as e:
    with open('./krx_index_scrap_error_log.txt','w') as log:
        log.write(e)
        log.write(datetime())
    print(e)
finally:
    driver.close()
    driver.quit()
    sys.exit()