# Name
    - WeatherBoy (AccuWeather Python Raspberry Pi 4 API)
## Description
    - An international weather station in just two lines (of display)
    - A minimalistic weather station with Raspberry Pi 4b.
    - A Python and Accuweather API for current wheater conditions by city.
## Requirements
    - Python 3
    - Raspberry Pi 4b
    - LCD 1602A with I2C adapter
## Dependencies
    - I'm using rpi-lcd to interact with the LCD. https://pypi.org/project/rpi-lcd/
## Features
    - Date, and time around 10 minutes before request.
    - Short message describing current conditions in city (or zipcode).
    - Temperature, in Farenheit and Celsius.
    - Precipitation for the past 12 hours, in inches.
    - Wind Speed, in miles/hr.
    - Relative humidity.
    - Ultra Violet index.
    - Pressure, in milibars.
    - Visibility, in miles. 
## Raspberry Pi 4b setup:
    - I'm using the GPIO Extension Board connected directly to the breadboard. 
        If you don't have the Extension Board, connect directly to the GPIO pins in the Pi's board.
    - You need four female-to-male jumper wires.
    - Need the I2c adapter.
        In the I2c:
        Connect GND to a GND in the breadboard.
        Connect VCC to 5V0 on breadboard.
        In the I2C Connect SDA to SDA1 in breadboard.
        In the I2C, connect the SCL to the SCL1 in breadboard.
    Remember that if you have the GPIO Extension Board, that's how you'll know where to connect in the breadboard.
## Get the API key
    - Register and get an API key at accuweather. -> https://developer.accuweather.com/user/register
    - Create a new app and you'll have the API key.
## Use
    - Use your API key and run the code.
    - Input the two letter country code(alpha-2(ISO 3166)).
    - Input the city name or zipcode (if applies).
    - Enjoy the loop.
