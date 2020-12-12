from selenium import webdriver
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import json
import os
path=os.path.abspath(os.getcwd())
url='https://www.naver.com/'
print(path)
driver=webdriver.Chrome(path+'/chromedriver')
driver.get(url)
got=driver.find_element_by_css_selector('#themecast [aria-selected="true"]')
got=str(got.text)
got=[got]
data=pd.DataFrame(got)
print(data)
DB_env=json.load(open(str(os.path.abspath(os.getcwd()))+'/database.json'))
DB_url=f"{DB_env['DIALECT']}+{DB_env['DB_DRIVER']}://{DB_env['DB_USERMAME']}:{DB_env['DB_PASSWORD']}@{DB_env['DB_HOST']}:{DB_env['DB_PORT']}/{DB_env['DB_DATABASE']}"
print(DB_url)
engine=create_engine(DB_url)
conn=engine.connect()
data.to_sql('cron_test',conn,if_exists='append',index=False)
driver.close()
driver.quit()