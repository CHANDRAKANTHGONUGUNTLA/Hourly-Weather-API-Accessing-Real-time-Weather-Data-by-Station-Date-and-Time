
import json,requests,time,pymysql
from queue import Empty
from flask import Flask
from flask import request,redirect
import time
import pymysql,csv

app = Flask(__name__)

#When 'Station number & 'datetime' is entered, the API below returns the weather data at the particular time.
#http://127.0.0.1:5000/hourly_weather?station_number=A0001823162&date=2022-01-01&time=06:55:00
@app.route("/hourly_weather", methods =['GET','POST'])
def hourly_time():
    results = {}
    results['request'] = '/hourly_weather'
    Station_number = request.args.get('station_number')
    date = request.args.get('date') 
    time = request.args.get('time')
    results['Date'] = date
    results['Time'] = time

    conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='gonuguc',passwd='******', db='gonuguc_Weather', autocommit=True) #setup our credentials
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = f'''SELECT STATION,NAME,LATITUDE,LONGITUDE,ELEVATION
            FROM CSV_station
            WHERE STATION ='{Station_number}' '''

    cur.execute(sql)
    items=[]
    for row in cur:
        items.append(row)
    results['Result']=items
    
    conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='gonuguc',passwd='Chandu@1604', db='gonuguc_Weather', autocommit=True)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    
  
    sql = f'''SELECT DATE, TIME, QUALITY, WIND, CEILING, VISIBILITY, TEMPERATURE, DEW_POINT, SEA_LEVEL_PRESSURE 
         FROM `Observation_data` 
         WHERE Station_id = '{Station_number}' and DATE = '{date}' 
         ORDER BY ABS(TIME_TO_SEC(TIMEDIFF(TIMESTAMP(`DATE`, `TIME`), TIMESTAMP('{date}', '{time}')))) 
         LIMIT 1'''



    cur.execute(sql)
    data=[]
    for row in cur:
        data.append(row)
    if len(data)==0:
        results['Weather_details']='Enter the nearest time possible within the range bound of one hour'
    else:results['Weather_details']=data
    
    return json.dumps(results,indent=4,sort_keys=True, default=str)



if __name__ =='__main__':
    app.run()

