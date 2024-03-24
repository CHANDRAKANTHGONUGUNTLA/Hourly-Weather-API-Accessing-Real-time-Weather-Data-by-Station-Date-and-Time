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