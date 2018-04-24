# automated_whatsapp_message_sender

DESCRIPTION:
------------
This is a simple tool to automate the process of sending WhatsApp messages to uses registered to WhatsApp. The unique feature of this tool is tht instead of the users having to type one message at a time, it can read a text file which contains stored messages and send them one by one to the mentioned recipients.

OUTPUT FORMAT:
--------------
After executing the code, the WhatsApp web page opens and the users is required to do the QR based login. After the successful login, tthere will be a prompt in the terminal asking the user to press any key to start sending the messages. The messages will be sent only when a key is pressed on the keyboard.

CHANGES TO BE MADE BEFORE USAGE:
--------------------------------
In line 24, 2S1VP copyable-text selectable-text needs to be changed in input_path = '//div[@class="2S1VP copyable-text selectable-text"][@data-tab="1"]'. The user needs to replace it with his/her div class id value. This div class value can be found by pointing at the WhatsApp web text bar running in Google Chrome and then inspecting element. 

![alt text](https://github.com/nishantuzir/automated_whatsapp_message_sender/blob/master/inspect.png)

The div class id value that is displayed, needs to be used in place of the value that has been provided in the code. 

![alt text](https://github.com/nishantuzir/automated_whatsapp_message_sender/blob/master/divclass.png)

USAGE:
------
$ python3 ./send_msg.py -t 1.00 -w 100.00 -n 'John Doe' -c /home/user/chromedriver -f /home/user/msg.txt

OR    

$ python3 ./send_msg.py --time_out 1.00 --wait 100.00 --name 'John Doe' --chrome /home/user/chromedriver --file /home/user/msg.txt

if you need help, the following command would be useful:

$ python3 ./send_msg.py -h

PS: time_out and wait are in seconds and default values are 2.00 and 90.00 respectively. Even though chromedrive is an executable file, it is not required to add the '.exe' in 'chromedriver' in case of Linux and Mac

ARGUMENT MEANINGS:
------------------
--time_out is used to set the time delay that is desired between the events of sending each message

--wait is the waiting time until the textbar of whatsapp is located by selenium

--name is the WhatsApp user recipient name

--chrome is the path specifier of the chromedrive executable file

--file is the path spacifier of the text file that contains the collection of messages that are needed to be sent 

DEPENDENCY:
-----------
python3.x

Google Chrome v65.x.x.x.x

Chromedriver.exe

PACKAGES:
---------
The package required for running the flowmeter, are provided in the 'requirements.txt' file.

The following python packages will be already be installed with the python3.x distibutions, if not, kindly install them:

1.os

2.pathlib

3.sys

4.argparse

5.time
