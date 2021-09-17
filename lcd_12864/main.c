#include <reg51.h>
#include <intrins.h>

#define uchar unsigned char
#define uint  unsigned int
#define LCD_data  P0             //数据口
#define delayNOP(); {_nop_();_nop_();_nop_();_nop_();};

sbit LCD_RS  =  P1^3;            //寄存器选择输入 
sbit LCD_RW  =  P1^4;            //液晶读/写控制
sbit LCD_EN  =  P1^5;            //液晶使能控制
sbit LCD_PSB =  P1^0;            //串/并方式控制
sbit wx      =  P2^7;
sbit dx      =  P2^6;

unsigned char code zhu[]=		//图片代码
{
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,

};

/*
* 功  能：11.0592M 下 延时1毫秒
* 参  数：要延时的毫秒数
* 返回值：无
*/
void delay(unsigned  int ms)
{
	while(ms--)
	{
		unsigned  char i;
		for(i=0; i<250; i++)  
		{
			_nop_();			   
			_nop_();
			_nop_();
			_nop_();
		}
	}
}		


/*
* 功  能：检查LCD12864是否忙
* 参  数：无
* 返回值：返回1：LCD出于忙状态
*/
bit lcd_busy()
{                          
	bit result;

	LCD_RS = 0;
	LCD_RW = 1;
	LCD_EN = 1;
	delayNOP();
	result = (bit)(P0&0x80);
	LCD_EN = 0;

	return(result); 
}

/*
* 功  能：写指令到LCD
* 参  数：要写入的指令
* 返回值：无
*/
void lcd_wcmd(uchar cmd)
{                          
	while(lcd_busy());

	LCD_RS = 0;
	LCD_RW = 0;
	LCD_EN = 0;
	_nop_();
	_nop_(); 
	P0 = cmd;
	delayNOP();
	LCD_EN = 1;
	delayNOP();
	LCD_EN = 0;  
}

/*
* 功  能：LCD写数据
* 参  数：要写入的数据
* 返回值：无
*/
void lcd_wdat(uchar dat)
{                          
	while(lcd_busy());

	LCD_RS = 1;
	LCD_RW = 0;
	LCD_EN = 0;
	P0 = dat;
	delayNOP();
	LCD_EN = 1;
	delayNOP();
	LCD_EN = 0; 
}

/*
* 功  能：LCD初始化
* 参  数：无
* 返回值：无
*/
void lcd_init(void)
{ 

	LCD_PSB = 1;         //并口方式
	
	lcd_wcmd(0x34);      //扩充指令操作     0b  00110100
	delay(5);
	lcd_wcmd(0x30);      //基本指令操作     0b  00110000
	delay(5);
	lcd_wcmd(0x0C);      //显示开，关光标   0b  00001100
	delay(5);
	lcd_wcmd(0x01);      //清除LCD的显示内容 0b 00000001 
	delay(5);
}

/*
* 功  能：在整个液晶屏幕上画图
* 参  数：图片的点阵数据
* 返回值：无
*/
void Draw_PM(const unsigned  char *ptr)
{
	uchar i, j, k;
	
	wx = 0;
	dx = 0; 
	lcd_wcmd(0x34);        //打开扩展指令集
	i = 0x80;
	            
	for(j=0; j<32; j++)
	{
		lcd_wcmd(i++);
		lcd_wcmd(0x80);
		for(k=0; k<16; k++)
		{
			lcd_wdat(*ptr++);
		}
	}
	i = 0x80;
	for(j=0; j<32; j++)
	{
		lcd_wcmd(i++);
		lcd_wcmd(0x88);	   
		for(k=0; k<16; k++)
		{
			lcd_wdat(*ptr++);
		} 
	}  
	lcd_wcmd(0x36);        //打开绘图显示
	lcd_wcmd(0x30);        //回到基本指令集
}

void main(void)
{
	wx = 0;
	dx = 0; 
	lcd_init();                //初始化LCD    
	Draw_PM(zhu);                       //显示可爱猪的图片
	while(1);	
}
