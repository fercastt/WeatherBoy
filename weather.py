#!/usr/bin/python3

from rpi_lcd import LCD
from time import sleep
import json
import urllib.request

lcd = LCD()
str_pad = " " * 16
API = '8bQB5anlSsmouSMmlUCjedjtMdbxhtzZ'

countryCode = input('Enter two letter country code: ')
cityOrCode = input('City or ZipCode: ')

if ' ' in cityOrCode:
    cityOrCode = cityOrCode.replace(' ', '%20')

def location(CountryCode, cityOrCode):
    search_address = 'http://dataservice.accuweather.com/locations/v1/cities/'+CountryCode+'/search?apikey='+API+'&q='+cityOrCode+'&details=true'
    search_address = urllib.request.urlopen(search_address)
    data = json.loads(search_address.read().decode())
    location_key = data[0]['Key']
    return location_key 

def current(location_key):
    currentWeather = 'http://dataservice.accuweather.com/currentconditions/v1/'+location_key+'?apikey='+API+'&details=true'
    currentWeather = urllib.request.urlopen(currentWeather)
    data = json.loads(currentWeather.read().decode())
    for i in data:
        tempF = str(i['Temperature']['Imperial']['Value'])
        tempC = str(i['Temperature']['Metric']['Value'])
        unitF = str(i['Temperature']['Imperial']['Unit'])
        unitC = str(i['Temperature']['Metric']['Unit'])
        relHumidity = str(i['RelativeHumidity'])
        windSpeed = str(i['Wind']['Speed']['Imperial']['Value'])
        windSpeedUnit = str(i['Wind']['Speed']['Imperial']['Unit'])
        uv = str(i['UVIndex'])
        precip = str(i['PrecipitationSummary']['Past12Hours']['Imperial']['Value'])
        precipUnit = str(i['PrecipitationSummary']['Past12Hours']['Imperial']['Unit'])
        localDateTime = str(i['LocalObservationDateTime'])
        visibility = str(i['Visibility']['Imperial']['Value'])
        visibilityUnit = str(i['Visibility']['Imperial']['Unit'])
        weatherText =str(i['WeatherText'])
        pressure = str(i['Pressure']['Metric']['Value'])
        pressureUnit = str(i['Pressure']['Metric']['Unit'])

    while True:
        # Infinity mode:
        lcd.text('Time & Date:', 1)
        lcd.text(localDateTime, 2)
        sleep(3)
        for i in range(0, len(localDateTime)):
            ldt = localDateTime[i:i+16]
            lcd.text(ldt, 2)
            sleep(.2)
        lcd.clear()

        lcd.text(cityOrCode.replace('%20', ' ')+', '+countryCode+':', 1)
        lcd.text(weatherText+'.', 2)
        sleep(2)
        for i in range(0, len(weatherText)):
            wt = weatherText[i:i+16]
            lcd.text(wt+'.', 2)
            sleep(.3)
        lcd.clear()

        lcd.text('Temperature:', 1)
        lcd.text(tempF+chr(223)+unitF+' / '+tempC+chr(223)+unitC, 2)
        sleep(5)
        lcd.clear()

        lcd.text('Precipitation in', 1)
        lcd.text('12 hrs: '+precip+precipUnit, 2)
        sleep(5)
        lcd.clear()

        lcd.text('Wind speed:', 1)
        lcd.text(windSpeed+windSpeedUnit, 2)
        sleep(5)
        lcd.clear()

        lcd.text('Humidity: '+relHumidity+'%', 1)
        lcd.text('UV Index: '+uv, 2)
        sleep(5)
        lcd.clear()

        lcd.text('Pressure: ', 1)
        lcd.text(pressure+pressureUnit, 2)
        sleep(5)
        lcd.clear()

        lcd.text('Visibility:', 1)
        lcd.text(visibility+visibilityUnit, 2)
        sleep(5)
        lcd.clear()

key = location(countryCode, cityOrCode)

try:
    current(key)

except KeyboardInterrupt:
    lcd.clear()
    pass
