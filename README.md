## Hourly Weather Data API
### Objective
The primary objective of this project is to develop an intuitive RESTful API that enables users to programmatically access real-time weather data. This API will accept parameters such as station number, date, and time, allowing users to retrieve tailored weather information in JSON format.

### Preprocessing
- The Hourly Weather Data API Project aims to provide users with seamless access to real-time weather information across various locations worldwide. This comprehensive project involves preprocessing a vast dataset consisting of nearly 15,000 CSV files, each containing weather station data from 1972 to 2022.
- The preprocessing phase is crucial for consolidating and refining the dataset to extract pertinent information about each weather station. By aggregating data into a unified dataset, subsequent data retrieval and manipulation processes are streamlined.

## Code Break Down
### PART 1: Importing Necessary Libraries
```python
import json,datetime,pymysql
import os
import csv
from datetime import datetime
```
This section imports all the necessary libraries and modules required.

### PART 2: Creating a table CSV_station and storing all the 13474 station data
```python

conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='gonuguc',
                       passwd='********', db='gonuguc_Weather', autocommit=True)
cur = conn.cursor(pymysql.cursors.DictCursor)

sql = '''DROP TABLE IF EXISTS CSV_station
'''

cur.execute(sql)

#creating a table CSV_station and storing all the 13474 station data.
sql = """
CREATE TABLE CSV_station (
    Station_id int NOT NULL AUTO_INCREMENT,
    STATION VARCHAR(255),
    SOURCE VARCHAR(255),
    LATITUDE VARCHAR(255),
    LONGITUDE VARCHAR(255),
    ELEVATION VARCHAR(255),
    NAME VARCHAR(255),
    REPORT_TYPE VARCHAR(255),
    CALL_SIGN VARCHAR(255),
    PRIMARY KEY(Station_ID)
    )ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1 COLLATE=utf8mb4_0900_ai_ci;
"""

cur.execute(sql)

sql = '''INSERT INTO CSV_station(STATION,SOURCE,LATITUDE,LONGITUDE,ELEVATION, NAME,REPORT_TYPE,CALL_SIGN) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''
folder_path = '2022'

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as f:
            csv_reader = csv.reader(f)     
            n = 0
            for row in csv_reader:
                n += 1
                    
                if n == 2:
                    station = row[0]
                    source = row[2]
                    lat = row[3]
                    long = row[4]
                    elevate = row[5]
                    name = row[6]
                    report = row[7]
                    call = row[8]
                    tokens =[station,source,lat,long,elevate,name,report,call]
                    cur.execute(sql,tokens)
                    break
```
### Explanation:
This Python script establishes a connection to a MySQL database and creates a table named `CSV_station` to store weather station information. It then iterates through CSV files in a specified folder, extracts station data, and inserts it into the database table. The script ensures data integrity and security by using parameterized SQL queries and commits the changes to the database.
### STATION DATA:
<img width="1440" alt="CSV_Station" src="https://github.com/CHANDRAKANTHGONUGUNTLA/Hourly-Weather-API-Accessing-Real-time-Weather-Data-by-Station-Date-and-Time/assets/97879005/e74b96ef-300a-4520-8c5e-977c8bd4ed70">

## COLUMNS DETAILS:
This dataset contains weather station information with the following attributes:

- **Station_id:** Unique identifier for each weather station.
- **STATION:** Station code or identifier.
- **SOURCE:** Source of the weather data.
- **LATITUDE:** Latitude of the weather station.
- **LONGITUDE:** Longitude of the weather station.
- **ELEVATION:** Elevation of the weather station.
- **NAME:** Name of the weather station.
- **REPORT_TYPE:** Type of weather report.
- **CALL_SIGN:** Call sign associated with the weather station.

### PART 3: CSV Weather Data Parsing and Database Insertion Script
```python
conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='gonuguc',
                       passwd='******', db='gonuguc_Weather', autocommit=True)
cur = conn.cursor(pymysql.cursors.DictCursor)

sql = '''DROP TABLE IF EXISTS Observation_data
'''

cur.execute(sql)

#creating a new table
sql = """
CREATE TABLE Observation_data (
    Weather_id int NOT NULL AUTO_INCREMENT,
    Station_id VARCHAR(255),
    DATE TIMESTAMP,
    TIME VARCHAR(255),
    QUALITY VARCHAR(255),
    WIND VARCHAR(255),
    CEILING  VARCHAR(255),
    VISIBILITY  VARCHAR(255),
    TEMPERATURE  VARCHAR(255),
    DEW_POINT  VARCHAR(255),
    SEA_LEVEL_PRESSURE  VARCHAR(255),
    PRIMARY KEY(Weather_id)
    )ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1 COLLATE=utf8mb4_0900_ai_ci;
"""
cur.execute(sql)
n=0
#function to iterate files in folder
def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
        return files
    except Exception as e:
        print(f"Error listing files: {e}")
        return []
folder_path = "/Users/avinashkalamati/Desktop/IA626/project/2022/"#folder location 
files_in_folder = list_files_in_folder(folder_path)
if files_in_folder:
    print(f"Files in folder '{folder_path}':")
    for file in files_in_folder:
        n+=1
        print(n)
        if n>500:
            # exit after 500 stations
            break
        else:
            with open (file) as f:
                data = [{k: str(v) for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)]
                conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='gonuguc',
                                passwd='Chandu@1604', db='gonuguc_Weather', autocommit=True)
                cur = conn.cursor(pymysql.cursors.DictCursor)
                    
                try:
                    sql = '''INSERT INTO Observation_data (Station_id,DATE,TIME,QUALITY,WIND,CEILING,VISIBILITY,TEMPERATURE,DEW_POINT,SEA_LEVEL_PRESSURE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
                    blocksize = 10000
                    tokens = []
                    for row in data:
                        #date
                        date = datetime.strptime(row['DATE'],'%Y-%m-%dT%H:%M:%S').strftime("%Y-%m-%d")
                        #time
                        time = datetime.strptime(row['DATE'],'%Y-%m-%dT%H:%M:%S').strftime("%H:%M:%S")
                        #wind
                        string = row['WND']
                        if string.split(',')[0][-3:] == '999':
                            wind=None
                        else:
                            wind=str(string.split(',')[0])+str(string.split(',')[2])                        
                            #ceiling
                            string = row['CIG']
                            if string.split(',')[0][-3:] == '999':
                                ceil = None
                            else:
                                ceil = int(string.split(',')[0])
                                
                            #visibility
                            string = row['VIS']
                            if string.split(',')[0][-3:] == '999':
                                visi = None
                            else:
                                visi = int(string.split(',')[0])
                                
                            #Temperature
                            string = row['TMP']
                            if string.split(',')[0][-3:] == '999':
                                temp=None
                            else:
                                temp=int(string.split(',')[0])/10

                            #DEW point
                            string = row['DEW']
                            if string.split(',')[0][-3:] == '999':
                                dew_point=None
                            else:
                                dew_point=int(string.split(',')[0])/10
                                
                            #SEA LEVEL PRESSURE
                            string = row['SLP']
                            if string.split(',')[0][-3:] == '999':
                                sea=None
                            else:
                                sea = int(string.split(',')[0])/10
                            tokens.append([row['STATION'],date,time,row['QUALITY_CONTROL'],wind,ceil,visi,temp,dew_point,sea])
                    if len(tokens) >= blocksize:
                        cur.executemany(sql, tokens)#sending data as blocks of size 10000
                        conn.commit()
                except Exception as e:
                    print(e)        
cur.close()
conn.close()
```
### Explanation:
This Python script interacts with CSV files containing weather observation data, parsing each file and extracting relevant information. It establishes a connection to a MySQL database, creates a table named `Observation_data`, and inserts the parsed data into the table, ensuring data integrity. The script commits changes in blocks to optimize performance and handles exceptions gracefully.
### OBSERVATION DATA
<img width="1440" alt="Observation" src="https://github.com/CHANDRAKANTHGONUGUNTLA/Hourly-Weather-API-Accessing-Real-time-Weather-Data-by-Station-Date-and-Time/assets/97879005/ae825d30-d105-42c6-89d1-d45d81d93540">

### COLUMN DETAILS:
This dataset provides weather-related information collected from various weather stations. The dataset includes the following columns:

- **Weather_id**: Unique identifier for each weather record.
- **Station_id**: Identifier for the weather station.
- **DATE**: Date of the weather record.
- **TIME**: Time of the weather record.
- **QUALITY**: Quality indicator for the data.
- **WIND**: Wind information, including direction and speed.
- **CEILING**: Ceiling height information.
- **VISIBILITY**: Visibility information.
- **TEMPERATURE**: Temperature at the time of the record.
- **DEW_POINT**: Dew point temperature.
- **SEA_LEVEL_PRESSURE**: Sea level pressure.

### Main API
```python
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

    conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='gonuguc',passwd='Chandu@1604', db='gonuguc_Weather', autocommit=True) #setup our credentials
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = f'''SELECT STATION,NAME,LATITUDE,LONGITUDE,ELEVATION
            FROM CSV_station
            WHERE STATION ='{Station_number}' '''

    cur.execute(sql)
    items=[]
    for row in cur:
        items.append(row)
    results['Result']=items
    
    conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='gonuguc',passwd='******', db='gonuguc_Weather', autocommit=True)
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
```
### Explanation: 
This Python script defines a Flask API endpoint `/hourly_weather` that retrieves weather data based on station number, date, and time parameters. It connects to a MySQL database to fetch station information and observation data. The API returns JSON-formatted weather details including station metadata and observation data for the specified time.
### Main file
<img width="1049" alt="main_file" src="https://github.com/CHANDRAKANTHGONUGUNTLA/Hourly-Weather-API-Accessing-Real-time-Weather-Data-by-Station-Date-and-Time/assets/97879005/694e6f24-d63c-46ae-a775-0b3b53bcff45">

### CLIENT API
```python
import json
import requests
import datetime
import pymysql
from flask import Flask, redirect, request

def weather_data(station_number, date, time):
    url = f'http://127.0.0.1:5000/hourly_weather?station_number={station_number}&date={date}&time={time}'
    r = requests.get(url)
    data = json.loads(r.text)
    return data



print(weather_data('94683099999', '2022-12-12', '09:41:00'))
print(weather_data('71912099999', '2022-12-26', '07:29:00'))
print(weather_data('71912099999', '2022-12-26', '07:30:00'))
print(weather_data('71912099999', '2022-12-26', '07:31:00'))
print(weather_data('72405663805', '2022-08-27', '16:15:00'))
print(weather_data('72210103039', '2022-01-01', '18:30:00'))
print(weather_data('02869099999', '2022-01-01 ', '05:20:00'))
```
### Explanation:
This Python script demonstrates how to retrieve weather data using the weather_data function. It makes HTTP requests to a Flask API endpoint /hourly_weather with station number, date, and time parameters, and prints the JSON response.
### Client File
<img width="1436" alt="Client_file" src="https://github.com/CHANDRAKANTHGONUGUNTLA/Hourly-Weather-API-Accessing-Real-time-Weather-Data-by-Station-Date-and-Time/assets/97879005/80dda6e9-5c60-4196-bed2-d7cadddfb81a">


### Hourly Weather Data API
The Hourly Weather Data API provides programmatic access to real-time weather data. By accepting parameters such as station number, date, and time, the API delivers tailored weather information in JSON format, ensuring flexibility and compatibility across diverse applications.

### Usage
To utilize the Hourly Weather Data API, users simply make HTTP requests to the designated endpoint, supplying the necessary parameters in the query string. The API promptly responds with weather data curated to meet the user's specifications.


