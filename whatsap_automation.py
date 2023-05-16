import argparse
import pywhatkit as w
from pynput.mouse import Controller as MouseController
import keyboard as k
import time

parser = argparse.ArgumentParser(description="Send a WhatsAPP message: "
                                             "python3 whatsap_automation.py -n <phone_number> -m <message> --hr <hour> --min <min>")
parser.add_argument('-n','--number',type=int,metavar='',required=True,help='Phone number')
parser.add_argument('-m','--message',type=str,metavar='',required=True,help='Message to be sent')
parser.add_argument('--hr',type=int,metavar='',required=True,help='Hour of sending')
parser.add_argument('--min',type=int,metavar='',required=True,help='min of sending')
group = parser.add_mutually_exclusive_group()
args = parser.parse_args()

if __name__ == '__main__':
    message = args.message
    phone_number = args.number
    hr = args.hour
    min = args.min
    mouse = MouseController
    w.sendwhatmsg(phone_number, message, hr, min)
    mouse.move(1453, 930)
    time.sleep(5)
    k.press_and_release('enter')
