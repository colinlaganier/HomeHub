#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd4in2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd4in2 Demo")
    
    epd = epd4in2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
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
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)

    font24 = ImageFont.truetype(os.path.join(picdir, 'NeueHaasDisplay.ttf'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'NeueHaasDisplay.ttf'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'NeueHaasDisplay.ttf'), 35)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage1 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage1)
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
    epd.display(epd.getbuffer(Himage1))
    time.sleep(2)
    
    font24 = ImageFont.truetype(os.path.join(picdir, 'CircularStd.ttf'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'CircularStd.ttf'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'CircularStd.ttf'), 35)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage2 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage2)
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
    epd.display(epd.getbuffer(Himage2))
    time.sleep(2)

    font24 = ImageFont.truetype(os.path.join(picdir, 'HelveticaNeue.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'HelveticaNeue.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'HelveticaNeue.ttc'), 35)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage3 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage3)
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
    epd.display(epd.getbuffer(Himage3))
    time.sleep(2)

    font24 = ImageFont.truetype(os.path.join(picdir, 'AirbnbCerealLight.ttf'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'AirbnbCerealLight.ttf'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'AirbnbCerealLight.ttf'), 35)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage4 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage4)
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
    epd.display(epd.getbuffer(Himage4))
    time.sleep(2)

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


    logging.info("Dashboard")
    Dashboard = Image.new('1', (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(Dashboard)
    # draw.text((, ), '', font = font, fill = 0)
    draw.text((0, 0), '14:25', font = font18, fill = 0)
    draw.text((160, 0), 'HOMEHUB', font = font24, fill = 0)
    draw.text((310, 0), 'SUN, MAY 7', font = font18, fill = 0)
    draw.line((0, 29, 400, 25), fill = 0)

    draw.text((0,35) 'Weather >', font18, fill = 0)
    mp = Image.open(os.path.join(picdir, 'cloud.bmp'))
    Dashboard.paste(bmp, (18,300))
    draw.text((55, 35), 'Cloudy', font = font18, fill = 0)
    draw.text((154, 35), '22°', font = font18, fill = 0)
    draw.text((250, 35), '45%', font = font18, fill = 0)
    draw.text((330, 35), 'Moderate', font = font18, fill = 0)
    draw.line((0, 55, 400, 51), fill = 0)

    draw.text((0,59), 'Devices >', font = font18, fill = 0)
    draw.line((0, 66, 51, 66), fill = 0)
    draw.arc((16, 82, 87, 152), 0, 360, fill = 0)
    draw.text((75,77), 'ON', font = powerFont, fill = 1)

    draw.line((0,244,400,244), fill = 0)
    draw.text((0,251), 'RasPi >', font = font18, fill = 0)   
    draw.line((0, 264, 48, 264), fill = 0)
    draw.text((115,251), 'CPU: 27%', font = font18, fill = 0)
    draw.text((223,251), 'CPU: 43°', font = font18, fill = 0)
    draw.text((318, 251), '1.82GB', font = font18, fill = 0)
    

    draw.line((0, 272, 400, 272), fill = 0)    

    draw.text((18, 280), 'PI-HOLE: ACTIVE', font = font18, fill = 0)
    draw.text((170, 280), '192.168.0.136', font = font18, fill = 0)
    draw.text((282, 280), 'AIRPORT: ACTIVE', font = font18, fill = 0)




    epd.display(epd.getbuffer(Dashboard))
    time.sleep(2)

    epd.Clear()
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in2.epdconfig.module_exit()
    exit()

#     Paint_DrawString_EN(0, 0, "14:25", &Font16, WHITE, BLACK);
# Paint_DrawString_EN(160, 0, "HOMEHUB", &Font20, WHITE, BLACK);
# // GUI_ReadBmp("./pic/homehub.bmp", 160, 0);
# // Paint_DrawBitMap(gImage_Homehub);
# Paint_DrawString_EN(325, 0, "SUN, MAY 7", &Font16, WHITE, BLACK);
# Paint_DrawLine(0, 25, 400, 25, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);

# GUI_ReadBmp("./pic/cloud.bmp", 18, 26);
# Paint_DrawString_EN(55,32,"Cloudy", &Font12, WHITE, BLACK);
# Paint_DrawString_EN(154,32,"22°", &Font12, WHITE, BLACK);
# Paint_DrawString_EN(250,32,"45%", &Font12, WHITE, BLACK);
# Paint_DrawString_EN(330,32,"Moderate", &Font12, WHITE, BLACK);
# Paint_DrawLine(0, 51, 400, 51, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);

# Paint_DrawString_EN(0, 55, "Devices >", &Font12, WHITE, BLACK);
# Paint_DrawLine(0, 65, 50, 65, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);
# Paint_DrawCircle(45, 105, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
# Paint_DrawCircle(150, 105, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
# Paint_DrawCircle(150, 105, 35, GRAY2, DOT_PIXEL_1X1, DRAW_FILL_FULL);
# Paint_DrawCircle(249, 105, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
# Paint_DrawCircle(249, 105, 35, GRAY3, DOT_PIXEL_1X1, DRAW_FILL_FULL);
# Paint_DrawCircle(347, 105, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
# Paint_DrawCircle(347, 105, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_FULL);
# Paint_DrawString_EN(30,146,"Computer", &Font12, WHITE, BLACK);
# Paint_DrawString_EN(127,146,"Computer", &Font12, WHITE, BLACK);
# Paint_DrawString_EN(225,146,"Computer", &Font12, WHITE, BLACK);
# Paint_DrawString_EN(323,146,"Computer", &Font12, WHITE, BLACK);

# Paint_DrawLine(0, 161, 400, 161, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);

# Paint_DrawString_EN(0, 165, "RasPi >", &Font12, WHITE, BLACK);
# Paint_DrawLine(0, 175, 50, 175, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);
# Paint_DrawLine(0, 65, 50, 65, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);
# Paint_DrawCircle(45, 220, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
# Paint_DrawCircle(150, 220, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
# Paint_DrawCircle(150, 220, 35, GRAY2, DOT_PIXEL_1X1, DRAW_FILL_FULL);
# Paint_DrawCircle(249, 220, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
# Paint_DrawCircle(249, 220, 35, GRAY3, DOT_PIXEL_1X1, DRAW_FILL_FULL);
# Paint_DrawCircle(347, 220, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
# Paint_DrawCircle(347, 220, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_FULL);
# Paint_DrawLine(0, 272, 400, 272, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);

# Paint_DrawString_EN(18, 280, "PI-HOLE: ACTIVE", &Font12, WHITE, BLACK);
# Paint_DrawString_EN(170, 280, "192.168.0.136", &Font12, WHITE, BLACK);
# Paint_DrawString_EN(282, 280, "AIRPORT: ACTIVE", &Font12, WHITE, BLACK);
