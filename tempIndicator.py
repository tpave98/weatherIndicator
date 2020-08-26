import time
import dht11
import RPi.GPIO as GPIO
from bs4 import BeautifulSoup as bs
import requests

#define GPIO 14 as DHT11 data pin
Temp_sensor=4
def main():
# Main program block
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbers
	GPIO.setup(23,GPIO.OUT)
# Initialise display
#  lcd_init()
	
main()
instance = dht11.DHT11(pin = Temp_sensor)
while True:
	
	soup = bs(requests.get("https://darksky.net/forecast/41.4936,-71.3087/us12/en").content,features="lxml")

	out_feels_like_F = soup.find("span", attrs={'class': 'feels-like-text'}).text
	out_humid = soup.find("span", attrs={'class': 'num swip humidity__value'}).text
	

	Num_out_feels_like_F = out_feels_like_F[:-1]
	Num_out_feels_like_F = int(Num_out_feels_like_F,10)
	Num_out_humid = int(out_humid,10)


        #get DHT11 sensor value
	result = instance.read()
	in_temp_F = round(result.temperature*1.8+32,1)
	print("\nOutdoor Temp:", out_feels_like_F,"F","\nIndoor Temp:",in_temp_F,"F","\n\nOutdoor Humidity:",out_humid,"%","\nIndoor Humidity:",result.humidity,"%\n")
	
	if ((in_temp_F > Num_out_feels_like_F) and (result.humidity < 80)):
		GPIO.output(23,GPIO.HIGH)
		print("LED ON")
#	elif result.humidity == 0:
#		print("BAD READ")
	else:
		GPIO.output(23,GPIO.LOW)
		print("LED OFF")

	time.sleep(5)





if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
#  finally:
#    lcd_byte(0x01, LCD_CMD)

