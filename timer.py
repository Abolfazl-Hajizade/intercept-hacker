import time
import os 
import pyttsx
from dtectcolors import Style,Fore,Back,init

init() # for colors

global W    ;    W  =   Style.BRIGHT+Fore.WHITE
global C    ;    C  =   Fore.GREEN
global R    ;   R   =   Fore.RED 
global B    ;   B   =   Fore.BLUE
global Y    ;   Y   =   Fore.YELLOW


os.system('mode 30,10')
os.system('cls')

h = 0
m = 0
s = 0

while True:
	try:
		h = input(C+'\nHours'+ R +' : '+W)
		m = input(C+'minute'+ R + ' : '+W)
		break	
	except:
		print R+'\njust number !\n'+W
		continue

s = 60
os.system('cls')

if h == 0:
	i_h = 0
	for i_m in range(m):
		for i_s in range(s):
			print '\n\n\n\t'+C+'[ '+W+str(str(i_h)+R+':'+W+str(i_m)+R+':'+W+str(i_s))+C+' ]\n'
			time.sleep(1)
			os.system('cls')

elif m == 0:
	i_h = 0
	i_m = 0
	for i_s in range(s):
		print '\n\n\n\t'+C+'[ '+W+str(str(i_h)+R+':'+W+str(i_m)+R+':'+W+str(i_s))+C+' ]\n'
		time.sleep(1)
		os.system('cls')
else:
	for i_h in range(h):
		for i_m in range(m):
			for i_s in range(s):
				print '\n\n\n\t'+C+'[ '+W+str(str(i_h)+R+':'+W+str(i_m)+R+':'+W+str(i_s))+C+' ]\n'
				time.sleep(1)
				os.system('cls')

for i in range(0,5):
	os.system('color c0')
	time.sleep(0.8)
	os.system('color b0')
	e = pyttsx.init()
	e.setProperty('rate', 110)
	e.say("Time Out")
	e.runAndWait()


	
			
