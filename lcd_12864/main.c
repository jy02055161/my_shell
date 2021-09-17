#include <reg51.h>
#include <intrins.h>

#define uchar unsigned char
#define uint  unsigned int
#define LCD_data  P0             //���ݿ�
#define delayNOP(); {_nop_();_nop_();_nop_();_nop_();};

sbit LCD_RS  =  P1^3;            //�Ĵ���ѡ������ 
sbit LCD_RW  =  P1^4;            //Һ����/д����
sbit LCD_EN  =  P1^5;            //Һ��ʹ�ܿ���
sbit LCD_PSB =  P1^0;            //��/����ʽ����
sbit wx      =  P2^7;
sbit dx      =  P2^6;

unsigned char code zhu[]=		//ͼƬ����
{
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,

};

/*
* ��  �ܣ�11.0592M �� ��ʱ1����
* ��  ����Ҫ��ʱ�ĺ�����
* ����ֵ����
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
* ��  �ܣ����LCD12864�Ƿ�æ
* ��  ������
* ����ֵ������1��LCD����æ״̬
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
* ��  �ܣ�дָ�LCD
* ��  ����Ҫд���ָ��
* ����ֵ����
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
* ��  �ܣ�LCDд����
* ��  ����Ҫд�������
* ����ֵ����
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
* ��  �ܣ�LCD��ʼ��
* ��  ������
* ����ֵ����
*/
void lcd_init(void)
{ 

	LCD_PSB = 1;         //���ڷ�ʽ
	
	lcd_wcmd(0x34);      //����ָ�����     0b  00110100
	delay(5);
	lcd_wcmd(0x30);      //����ָ�����     0b  00110000
	delay(5);
	lcd_wcmd(0x0C);      //��ʾ�����ع��   0b  00001100
	delay(5);
	lcd_wcmd(0x01);      //���LCD����ʾ���� 0b 00000001 
	delay(5);
}

/*
* ��  �ܣ�������Һ����Ļ�ϻ�ͼ
* ��  ����ͼƬ�ĵ�������
* ����ֵ����
*/
void Draw_PM(const unsigned  char *ptr)
{
	uchar i, j, k;
	
	wx = 0;
	dx = 0; 
	lcd_wcmd(0x34);        //����չָ�
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
	lcd_wcmd(0x36);        //�򿪻�ͼ��ʾ
	lcd_wcmd(0x30);        //�ص�����ָ�
}

void main(void)
{
	wx = 0;
	dx = 0; 
	lcd_init();                //��ʼ��LCD    
	Draw_PM(zhu);                       //��ʾ�ɰ����ͼƬ
	while(1);	
}
