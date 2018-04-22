import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def send_message(t,w,n,c,f):
	driver = webdriver.Chrome(c)
	driver.get('http://web.whatsapp.com')
	name = n 
	wait = WebDriverWait(driver = driver, timeout = w)
	lists = []
	with open(f,"r") as f: # set the path acc to ur system
		lines = f.readlines()
		for line in lines:
			line = line.replace("\n","")
			lists.append(line)

	input('Press any key after scanning QR code')
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	input_path = '//div[@class="_2S1VP copyable-text selectable-text"][@data-tab="1"]'
	
	msg_box = wait.until(EC.presence_of_element_located((By.XPATH,input_path)))
	for k in lists:
		msg = k
		msg_box.send_keys(msg + Keys.ENTER)
		time.sleep(t)
if __name__ == "__main__":
	import sys
	import argparse
	parser = argparse.ArgumentParser(description='automatically sends messages to whatsapp contacts')
	parser.add_argument('-t', '--time_out', default=2.0, type=float, help='time out time in seconds after each message')
	parser.add_argument('-w', '--wait', default=90.0,type=float,help='specify the waiting time until the textbar of whatsapp is located')
	parser.add_argument('-n', '--name', default=None, type=str, help='specify the name of the recipient')
	parser.add_argument('-c', '--chrome', default=None, type=str, help='specify the path of chrome driver')
	parser.add_argument('-f', '--file', default=None, type=str, help='specify the path of the text file containing the messages')
	args = parser.parse_args()
	if args.name:
		send_message(args.time_out,args.wait,args.name,args.chrome,args.file)
	#elif args.wait:
	#	send_message(args.time_out,args.wait,args.name)
	#elif args.name:
	#	send_message(args.time_out,args.wait,args.name,args.divclass)
	#elif args.divclass:
	#	send_message(args.time_out,args.wait,args.name,args.divclass)

	else:
		parser.print_help()


