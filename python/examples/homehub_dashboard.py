#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import json
import psutil
import subprocess
import logging
import time
import traceback
import re

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd4in2
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime
from gpiozero import CPUTemperature


logging.basicConfig(level=logging.DEBUG)

json_file = "weather_data.json"
with open(json_file, "r") as data_file:
    weather_data = json.load(data_file)

aqi = ["---","Low","Low","Low","Moderate","Moderate","Moderate","High","High","High","Very High"]

try:
    epd = epd4in2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    
#    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
#    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
#    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
#    
#    # Drawing on the Horizontal image
#    logging.info("1.Drawing on the Horizontal image...")
#    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
#    draw = ImageDraw.Draw(Himage)
#    draw.text((10, 0), 'HOMEHUB', font = font35, fill = 0)
#    draw.text((10, 20), '4.2inch e-Paper Computer More words bla', font = font18, fill = 0)
#    draw.line((20, 50, 70, 100), fill = 0)
#    draw.line((70, 50, 20, 100), fill = 0)
#    draw.rectangle((20, 50, 70, 100), outline = 0)
#    draw.line((165, 50, 165, 100), fill = 0)
#    draw.line((140, 75, 190, 75), fill = 0)
#    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
#    draw.rectangle((80, 50, 130, 100), fill = 0)
#    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
#    epd.display(epd.getbuffer(Himage))
#    time.sleep(2)
#
#    font24 = ImageFont.truetype(os.path.join(picdir, 'NeueHaasDisplay.ttf'), 24)
#    font18 = ImageFont.truetype(os.path.join(picdir, 'NeueHaasDisplay.ttf'), 18)
#    font35 = ImageFont.truetype(os.path.join(picdir, 'NeueHaasDisplay.ttf'), 35)
#    
#    # Drawing on the Horizontal image
#    logging.info("1.Drawing on the Horizontal image...")
#    Himage1 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
#    draw = ImageDraw.Draw(Himage1)
#    draw.text((10, 0), 'HOMEHUB', font = font35, fill = 0)
#    draw.text((10, 20), '4.2inch e-Paper Computer More words bla', font = font18, fill = 0)
#    draw.line((20, 50, 70, 100), fill = 0)
#    draw.line((70, 50, 20, 100), fill = 0)
#    draw.rectangle((20, 50, 70, 100), outline = 0)
#    draw.line((165, 50, 165, 100), fill = 0)
#    draw.line((140, 75, 190, 75), fill = 0)
#    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
#    draw.rectangle((80, 50, 130, 100), fill = 0)
#    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
#    epd.display(epd.getbuffer(Himage1))
#    time.sleep(2)
#    
#    font24 = ImageFont.truetype(os.path.join(picdir, 'CircularStd.ttf'), 24)
#    font18 = ImageFont.truetype(os.path.join(picdir, 'CircularStd.ttf'), 18)
#    font35 = ImageFont.truetype(os.path.join(picdir, 'CircularStd.ttf'), 35)
#    
#    # Drawing on the Horizontal image
#    logging.info("1.Drawing on the Horizontal image...")
#    Himage2 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
#    draw = ImageDraw.Draw(Himage2)
#    draw.text((10, 0), 'HOMEHUB', font = font35, fill = 0)
#    draw.text((10, 20), '4.2inch e-Paper Computer More words bla', font = font18, fill = 0)
#    draw.line((20, 50, 70, 100), fill = 0)
#    draw.line((70, 50, 20, 100), fill = 0)
#    draw.rectangle((20, 50, 70, 100), outline = 0)
#    draw.line((165, 50, 165, 100), fill = 0)
#    draw.line((140, 75, 190, 75), fill = 0)
#    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
#    draw.rectangle((80, 50, 130, 100), fill = 0)
#    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
#    epd.display(epd.getbuffer(Himage2))
#    time.sleep(2)
#
#    font24 = ImageFont.truetype(os.path.join(picdir, 'HelveticaNeue.ttc'), 24)
#    font18 = ImageFont.truetype(os.path.join(picdir, 'HelveticaNeue.ttc'), 18)
#    font35 = ImageFont.truetype(os.path.join(picdir, 'HelveticaNeue.ttc'), 35)
#    
#    # Drawing on the Horizontal image
#    logging.info("1.Drawing on the Horizontal image...")
#    Himage3 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
#    draw = ImageDraw.Draw(Himage3)
#    draw.text((10, 0), 'HOMEHUB', font = font35, fill = 0)
#    draw.text((10, 20), '4.2inch e-Paper Computer More words bla', font = font18, fill = 0)
#    draw.line((20, 50, 70, 100), fill = 0)
#    draw.line((70, 50, 20, 100), fill = 0)
#    draw.rectangle((20, 50, 70, 100), outline = 0)
#    draw.line((165, 50, 165, 100), fill = 0)
#    draw.line((140, 75, 190, 75), fill = 0)
#    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
#    draw.rectangle((80, 50, 130, 100), fill = 0)
#    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
#    epd.display(epd.getbuffer(Himage3))
#    time.sleep(2)
#
#    font24 = ImageFont.truetype(os.path.join(picdir, 'AirbnbCerealLight.ttf'), 24)
#    font18 = ImageFont.truetype(os.path.join(picdir, 'AirbnbCerealLight.ttf'), 18)
#    font35 = ImageFont.truetype(os.path.join(picdir, 'AirbnbCerealLight.ttf'), 35)
#    
#    # Drawing on the Horizontal image
#    logging.info("1.Drawing on the Horizontal image...")
#    Himage4 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
#    draw = ImageDraw.Draw(Himage4)
#    draw.text((10, 0), 'HOMEHUB', font = font35, fill = 0)
#    draw.text((10, 20), '4.2inch e-Paper Computer More words bla', font = font18, fill = 0)
#    draw.line((20, 50, 70, 100), fill = 0)
#    draw.line((70, 50, 20, 100), fill = 0)
#    draw.rectangle((20, 50, 70, 100), outline = 0)
#    draw.line((165, 50, 165, 100), fill = 0)
#    draw.line((140, 75, 190, 75), fill = 0)
#    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
#    draw.rectangle((80, 50, 130, 100), fill = 0)
#    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
#    epd.display(epd.getbuffer(Himage4))
#    time.sleep(2)
#
    font24 = ImageFont.truetype(os.path.join(picdir, 'SourceSansPro.ttf'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'SourceSansPro.ttf'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'SourceSansPro.ttf'), 35)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage5 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage5)
    draw.text((10, 0), 'HOMEHUB', font = font35, fill = 0)
    draw.text((10, 20), '4.2inch e-Paper Computer More words bla', font = font18, fill = 0)
    draw.line((20, 50, 70, 100), fill = 0)
    draw.line((70, 50, 20, 100), fill = 0)
    draw.rectangle((20, 50, 70, 100), outline = 0)
    draw.line((165, 50, 165, 100), fill = 0)
    draw.line((140, 75, 190, 75), fill = 0)
    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw.rectangle((80, 50, 130, 100), fill = 0)
    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Himage5))
    time.sleep(2)

    font12 = ImageFont.truetype(os.path.join(picdir, 'SourceSansPro.ttf'), 12)
    powerFont = ImageFont.truetype(os.path.join(picdir, 'ArialBold.ttf'), 15)
    cpuTemp = 'CPU: ' + str(round(CPUTemperature().temperature,1)) + '°'
    cpuActivity = 'CPU: ' + str(psutil.cpu_percent()) + '%'
    ramActivity = 'MEM:' + str(round(psutil.virtual_memory().available / 1024.0/1024.0/1024.0,2)) + 'GB'
    today = datetime.now()
    weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    currentDate = weekday[today.weekday()].upper() + ", " + today.strftime("%b").upper() + " " + str(today.day)
    currentTime = today.strftime("%H:%M")
    ipAddress = subprocess.getoutput('hostname -I').split(' ')[0]

    logging.info("Dashboard")
    Dashboard = Image.new('1', (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(Dashboard)
    # draw.text((, ), '', font = font, fill = 0)
    draw.text((0, 0), currentTime, font = font18, fill = 0)
    draw.text((140, 0), 'HOMEHUB', font = font24, fill = 0)
    draw.text((303, 0), currentDate, font = font18, fill = 0)
    draw.line((0, 30, 400, 30), fill = 0)

    draw.text((0,35), 'Weather >', font = font18, fill = 0)
    draw.line((0,55, 61, 55), fill = 0)
    bmp = Image.open(os.path.join(picdir, 'cloud.bmp'))
    Dashboard.paste(bmp, (80,38))
    Dashboard.paste(bmp, (165,38))
    Dashboard.paste(bmp, (225,38))
    Dashboard.paste(bmp, (295,38))
    draw.text((110, 35), str(weather_data["weather_data"]["weather"]), font = font18, fill = 0)
    draw.text((195, 35), str(weather_data["weather_data"]["temperature"]) + '°', font = font18, fill = 0)
    draw.text((255, 35), str(weather_data["weather_data"]["precipitation"]) + '%', font = font18, fill = 0)
    draw.text((325, 35), aqi[weather_data["weather_data"]["air_quality"]], font = font18, fill = 0)
    draw.line((0, 62, 400, 62), fill = 0)

    draw.text((0,65), 'Devices >', font = font18, fill = 0)
    draw.line((0, 85, 57, 85), fill = 0)
#    draw.arc((16, 382, 87, 152), 0, 360, fill = 0)
    draw.text((75,77), 'ON', font = powerFont, fill = 1)

    draw.line((0,240,400,240), fill = 0)
    draw.text((0,245), 'RasPi >', font = font18, fill = 0)   
    draw.line((0, 265, 46, 265), fill = 0)
    draw.text((90, 245), cpuActivity, font = font18, fill = 0)
    draw.text((205, 245), cpuTemp, font = font18, fill = 0)
    draw.text((315, 245), ramActivity, font = font18, fill = 0)
    

    draw.line((0, 272, 400, 272), fill = 0) 

    draw.text((0, 280), 'PI-HOLE: ACTIVE', font = font18, fill = 0)
    draw.text((147, 280), ipAddress, font = font18, fill = 0)
    draw.text((272, 280), 'AIRPORT: ACTIVE', font = font18, fill = 0)

#    draw.line((100, 0, 100, 300), fill = 0)
#    draw.line((200, 0, 200, 300), fill = 0)
#    draw.line((300, 0, 300, 300), fill = 0)

    epd.display(epd.getbuffer(Dashboard))
    time.sleep(2)

#    epd.Clear()
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in2.epdconfig.module_exit()
    exit()
