from subprocess import *
from time import sleep
from os import system
from colorama import init,Fore,Back,Style

init(autoreset=True)                
fg = Fore.GREEN;fw = Fore.WHITE;fr = Fore.RED;fy = Fore.YELLOW
sn = Style.BRIGHT

G = fg + sn
W = fw + sn
R = fr + sn
Y = fy + sn

def banner():

                system("mode 100,30")

		print('''

    d8b      888                     888
    Y8P      888                     888
             888                     888
    888      88888b.  8888b.  .d8888b888  888 .d88b. 888d888
    888      888 "88b    "88bd88P"   888 .88Pd8P  Y8b888P"
    888888888888  888.d888888888     888888K 88888888888
    888      888  888888  888Y88b.   888 "88bY8b.    888
    888      888  888"Y888888 "Y8888P888  888 "Y8888 888


	Interceping Hacker With (ip)

	programmer: Abolfazl Hajizade
	
	NickName: Zero_d4y

	gmail: zeroday1010@gmail.com

	=======================================

	press Enter for Start ...

			''')
		raw_input("\n")
		system("cls")

def pattern_intercep(data):

			protocol = data [0:5].replace(" ","")
			
			new_data= data [9:]
			
			src_ip= new_data [ 0 : new_data.find(" ") ].replace(" ","")
			
			dst_ip= new_data [ new_data.find(" ")+1 : ].replace("ESTABLISHED","").replace(" ","")
			
			port_src= src_ip [ src_ip.find(":") : ].replace(":","")
			
			port_dst= dst_ip [ dst_ip.find(":") : ].replace(":","")#
			
			src_ip= new_data [ 0 : new_data.find(":") ].replace(" ","")#
			
			dst_ip= new_data [ new_data.find(" ")+1 : ].replace("ESTABLISHED","").replace(" ","")
			
			dst_ip= dst_ip [ 0 : dst_ip.find(":") ]
							
			print src_ip+"    "+G+str(port_src)+W+"        "+dst_ip+"    "+G+str(port_dst)+W
			print Y+"-----------------------------------------------------\n"+W

def intercept():

		while True:
                    
			intercepting = check_output("netstat -an > data.zeroday",shell=True)
			
			check_task = check_output("tasklist",shell=True)

			check_firefox = "firefox.exe".encode('utf-8') in check_task
			
			check_opera = "opera.exe".encode("utf-8") in check_task
			
			check_Edge = "MicrosoftEdge.exe".encode("utf-8") in check_task
			
			check_chrome = "chrome.exe".encode("utf-8") in check_task
			
			f = open("data.zeroday","r")

			print Y+"\n----ip---------port----------------ip--------port----\n"+W

			for data in f.readlines():
			
					data = data.strip("\n")
					
					if check_chrome or check_Edge or check_firefox or check_opera:
                                            
							if "ESTABLISHED" in data and not "127.0.0.1" in data and not ":443" in data and not ":80" in data:

									pattern_intercep(data)
					else:

							if "ESTABLISHED" in data and not "127.0.0.1" in data:

									pattern_intercep(data)
				
			sleep(6)
			system("cls")					
							
			f.close()

if "__main__" == __name__:	

			banner()
			
			system("mode 55,35")
			
			intercept()
			
					
					
			
	
