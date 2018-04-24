# automated_whatsapp_message_sender

DESCRIPTION:
------------
This is a simple tool to automate the process of sending WhatsApp messages to uses registered to WhatsApp. The unique feature of this tool is tht instead of the users having to type one message at a time, it can read a text file which contains stored messages and send them one by one to the mentioned recipients.

OUTPUT FORMAT:
--------------
After executing the code, the WhatsApp web page opens and the users is required to do the QR based login. After the successful login, tthere will be a prompt in the terminal asking the user to press any key to start sending the messages. The messages will be sent only when a key is pressed on the keyboard. 

USAGE:
------
$ python3 ./send_msg.py -p ./sample/testing.pcap -t 1.00    
OR    
$ python3 ./send_msg.py -pcap ./sample/testing.pcap -t 1.00

if you need help, the following command would be useful:

$ python3 ./send_msg.py -h

PS: timeout is in seconds and default value is 90.00 

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
