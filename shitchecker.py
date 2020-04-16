
import pycard
import os
import time
# Create a card
os.system("clear")
print(""" 
    


       ███████╗██╗  ██╗██╗████████╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
       ██╔════╝██║  ██║██║╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
       ███████╗███████║██║   ██║   ██║     ███████║█████╗  ██║     █████╔╝ 
       ╚════██║██╔══██║██║   ██║   ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
       ███████║██║  ██║██║   ██║   ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
       ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
                                                                       


   
	""")
cardsfile=input(' \033[2;37;40m Enter the Cards file : ')
print('\033[0;35m')
cardsfile=open(cardsfile,'r')
for card in cardsfile:
	sp= card.split()
	number= str(sp[0])
	month= int(sp[1])
	year= int(sp[2])
	cvc= int(sp[3])
	
	#print(number,month,year,cvc)
	cards = pycard.Card(number,month,year,cvc)
	time.sleep(1)
	if cards.is_valid == True:
	   print("  ")
	   print("\033[0;32m [+] Card is valid ==> ",card,card,cards.friendly_brand,cards.is_expired)
	   
	else:
		print(" ")
		print("\033[0;31;40m [!] Card is not valid ==> \033[0;33m",card,cards.friendly_brand)
