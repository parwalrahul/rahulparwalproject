#! /usr/bin/python2

import os
import time

def a():
	os.system("dialog --infobox '	   The Vulnerability Scanner  ' 10 40") 
	time.sleep(1)
	def vul():
		os.system("dialog --title 'Vulnerability Scanning' --menu 'Select Your Choice : ' 20 100 8 1 'Detect WAF (Web Application Firewall) on a Website ' 2 'Detect Load Balancing on a Website. (DNS & HTTP) ' 3 'Change your IP address. ' 4 'Change Your MAC address ' 5 'Know Hosts MAC Address ' 6 'Know the Speed of your Lan Card.' 7 'Know your DNS Address' 8 'Back' 2> /root/Desktop/Project/choice.txt")
		f=open('/root/Desktop/Project/choice.txt','r')
		c=f.read()
		if c=='1':
			os.system("dialog --title 'WAF Detection' --inputbox 'Enter URL of Website (Ex: www.google.com) ' 10 50 2> /root/Desktop/dump/hello.txt")
			f=open('/root/Desktop/dump/hello.txt','r')
			x=f.read()
			os.system("dialog --infobox 'Please wait till the processing is being done...\nWe are fetching the results for you.' 10 50")
			os.system("wafw00f "+x+" > /root/Desktop/dump/result")
			os.system("grep -A100 Checking /root/Desktop/dump/result > /root/Desktop/dump/result1")
			os.system("dialog --textbox /root/Desktop/dump/result1 20 100")
			vul()

		if c=='2':
			os.system("dialog --title 'Load Balancing Detection' --inputbox 'Enter URL of Website (Ex: www.google.com)' 10 50 2> /root/Desktop/dump/hello")
			f=open('/root/Desktop/dump/hello','r')
			x=f.read()
			os.system("dialog --infobox 'Please wait till the processing is being done...\nWe are fetching the results for you.\nThis may take some minutes.' 10 50")
			os.system("lbd "+x+" > /root/Desktop/dump/result")
			os.system("grep -A100 Checking /root/Desktop/dump/result > /root/Desktop/dump/result1")
			os.system("dialog --textbox /root/Desktop/dump/result1 20 100")
			vul()



	vul()

a()
