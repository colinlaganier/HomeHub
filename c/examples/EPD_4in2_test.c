/*****************************************************************************
* | File      	:   EPD_4in2_test.c
* | Author      :   Waveshare team
* | Function    :   4.2inch e-paper test demo
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2019-06-13
* | Info        :
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
******************************************************************************/
#include "EPD_Test.h"
#include "EPD_4in2.h"
#include <string.h>
#include <time.h> 

int EPD_4in2_test(void)
{
    printf("EPD_4IN2_test Demo\r\n");
    if(DEV_Module_Init()!=0){
        return -1;
    }

    printf("e-Paper Init and Clear...\r\n");
    EPD_4IN2_Init_Fast();

    struct timespec start={0,0}, finish={0,0}; 
    clock_gettime(CLOCK_REALTIME,&start);
    EPD_4IN2_Clear();
    DEV_Delay_ms(500);
    clock_gettime(CLOCK_REALTIME,&finish);
    Debug("%ld S\r\n",finish.tv_sec-start.tv_sec);	

    //Create a new image cache
    UBYTE *BlackImage;
    /* you have to edit the startup_stm32fxxx.s file and set a big enough heap size */
    UWORD Imagesize = ((EPD_4IN2_WIDTH % 8 == 0)? (EPD_4IN2_WIDTH / 8 ): (EPD_4IN2_WIDTH / 8 + 1)) * EPD_4IN2_HEIGHT;
    if((BlackImage = (UBYTE *)malloc(Imagesize)) == NULL) {
        printf("Failed to apply for black memory...\r\n");
        return -1;
    }
    printf("Paint_NewImage\r\n");
    Paint_NewImage(BlackImage, EPD_4IN2_WIDTH, EPD_4IN2_HEIGHT, 0, WHITE);
    

#if 1  // show bmp

    EPD_4IN2_Init_Fast();
    
    // printf("show window BMP-----------------\r\n");
    // Paint_SelectImage(BlackImage);
    // Paint_Clear(WHITE);
    // GUI_ReadBmp("./pic/100x100.bmp", 10, 10);
    // EPD_4IN2_Display(BlackImage);
    // DEV_Delay_ms(2000);

    printf("show bmp------------------------\r\n");
    Paint_SelectImage(BlackImage);
    GUI_ReadBmp("./pic/4in2.bmp", 0, 0);
    EPD_4IN2_Display(BlackImage);
    DEV_Delay_ms(2000);

#endif        

#if 1   // show image for array   
    printf("show image for array\r\n");
    Paint_SelectImage(BlackImage);
    Paint_Clear(WHITE);
    Paint_DrawBitMap(gImage_4in2);
    EPD_4IN2_Display(BlackImage);
    DEV_Delay_ms(500);
#endif
	
#if 0
    printf("Support for partial refresh, but the refresh effect is not good, but it is not recommended\r\n");
    EPD_4IN2_Init_Partial();
	printf("Partial refresh\r\n");
    PAINT_TIME sPaint_time;
    sPaint_time.Hour = 12;
    sPaint_time.Min = 34;
    sPaint_time.Sec = 56;
    UBYTE num = 20;
	for (;;) {
		sPaint_time.Sec = sPaint_time.Sec + 1;
		if (sPaint_time.Sec == 60) {
			sPaint_time.Min = sPaint_time.Min + 1;
			sPaint_time.Sec = 0;
			if (sPaint_time.Min == 60) {
				sPaint_time.Hour =  sPaint_time.Hour + 1;
				sPaint_time.Min = 0;
				if (sPaint_time.Hour == 24) {
					sPaint_time.Hour = 0;
					sPaint_time.Min = 0;
					sPaint_time.Sec = 0;
				}
			}
		}
		Paint_ClearWindows(150, 80, 150 + Font20.Width * 7, 80 + Font20.Height, WHITE);
		Paint_DrawTime(150, 80, &sPaint_time, &Font20, WHITE, BLACK);
		EPD_4IN2_PartialDisplay(150, 80, 150 + Font20.Width * 7, 80 + Font20.Height, BlackImage);
		DEV_Delay_ms(500);//Analog clock 1s
		num = num - 1;
		if(num == 0) {
			break;
		}
    }
#endif
#if 1
    EPD_4IN2_Init_Fast();
	EPD_4IN2_Clear();
	EPD_4IN2_Init_4Gray();
	printf("show Gray------------------------\r\n");
	free(BlackImage);
	BlackImage = NULL;
	Imagesize = ((EPD_4IN2_WIDTH % 8 == 0)? (EPD_4IN2_WIDTH / 4 ): (EPD_4IN2_WIDTH / 4 + 1)) * EPD_4IN2_HEIGHT;
    if((BlackImage = (UBYTE *)malloc(Imagesize)) == NULL) {
        printf("Failed to apply for black memory...\r\n");
        return -1;
    }
	Paint_NewImage(BlackImage, EPD_4IN2_WIDTH, EPD_4IN2_HEIGHT, 0, WHITE);
	Paint_SetScale(4);
	Paint_Clear(WHITE);

    printf("HOMEHUB demo\r\n");

    Paint_DrawString_EN(0, 0, "14:25", &Font15test, WHITE, BLACK);
    Paint_DrawString_EN(160, 0, "HOMEHUB", &Font15test, WHITE, BLACK);
    Paint_DrawString_EN(325, 0, "SUN, MAY 7", &Font15test, WHITE, BLACK);
    Paint_DrawLine(0, 25, 400, 25, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);

    Paint_DrawString_EN(55,32,"Cloudy", &Font10, WHITE, BLACK);
    Paint_DrawString_EN(154,32,"22°", &Font10, WHITE, BLACK);
    Paint_DrawString_EN(250,32,"45%", &Font10, WHITE, BLACK);
    Paint_DrawString_EN(330,32,"Moderate", &Font10, WHITE, BLACK);
    Paint_DrawLine(0, 51, 400, 51, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);

    Paint_DrawString_EN(0, 55, "Devices >", &Font10, WHITE, BLACK);
    Paint_DrawLine(0, 65, 50, 65, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);
    Paint_DrawCircle(45, 105, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
    Paint_DrawCircle(150, 105, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
    Paint_DrawCircle(150, 105, 35, GRAY2, DOT_PIXEL_1X1, DRAW_FILL_FULL);
    Paint_DrawCircle(249, 105, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
    Paint_DrawCircle(249, 105, 35, GRAY3, DOT_PIXEL_1X1, DRAW_FILL_FULL);
    Paint_DrawCircle(347, 105, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
    Paint_DrawCircle(347, 105, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_FULL);
    Paint_DrawString_EN(30,146,"Computer", &Font10, WHITE, BLACK);
    Paint_DrawString_EN(127,146,"Computer", &Font10, WHITE, BLACK);
    Paint_DrawString_EN(225,146,"Computer", &Font10, WHITE, BLACK);
    Paint_DrawString_EN(323,146,"Computer", &Font10, WHITE, BLACK);

    Paint_DrawLine(0, 161, 400, 161, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);

    Paint_DrawString_EN(0, 165, "RasPi >", &Font10, WHITE, BLACK);
    Paint_DrawLine(0, 175, 50, 175, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);
    Paint_DrawLine(0, 65, 50, 65, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);
    Paint_DrawCircle(45, 220, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
    Paint_DrawCircle(150, 220, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
    Paint_DrawCircle(150, 220, 35, GRAY2, DOT_PIXEL_1X1, DRAW_FILL_FULL);
    Paint_DrawCircle(249, 220, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
    Paint_DrawCircle(249, 220, 35, GRAY3, DOT_PIXEL_1X1, DRAW_FILL_FULL);
    Paint_DrawCircle(347, 220, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
    Paint_DrawCircle(347, 220, 35, BLACK, DOT_PIXEL_1X1, DRAW_FILL_FULL);
    Paint_DrawLine(0, 272, 400, 272, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);

    Paint_DrawString_EN(18, 280, "PI-HOLE: ACTIVE", &Font10, WHITE, BLACK);
    Paint_DrawString_EN(170, 280, "192.168.0.136", &Font10, WHITE, BLACK);
    Paint_DrawString_EN(282, 280, "AIRPORT: ACTIVE", &Font10, WHITE, BLACK);

	EPD_4IN2_4GrayDisplay(BlackImage);
	DEV_Delay_ms(20000);

	Paint_Clear(WHITE);
    EPD_4IN2_4GrayDisplay(gImage_4in2_4Gray1);
	DEV_Delay_ms(2000);

	GUI_ReadBmp_4Gray("./pic/4in2_Scale.bmp",0 , 0);
	EPD_4IN2_4GrayDisplay(BlackImage);
	DEV_Delay_ms(2000);
	
	Paint_Clear(WHITE);
    GUI_ReadBmp("./pic/100x100.bmp", 20, 20);
    EPD_4IN2_4GrayDisplay(BlackImage);
	DEV_Delay_ms(2000);
#endif	
    EPD_4IN2_Init_Fast();
    EPD_4IN2_Clear();
    printf("Goto Sleep...\r\n");
    EPD_4IN2_Sleep();
    free(BlackImage);
    BlackImage = NULL;
    DEV_Delay_ms(2000);//important, at least 2s
    // close 5V
    printf("close 5V, Module enters 0 power consumption ...\r\n");
    DEV_Module_Exit();
    
    return 0;
}

