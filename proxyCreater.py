#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
global proxyIp
def proxyGenerator():
	ipv4Address1Part = random.randint(0, 255)
	ipv4Address2Part = random.randint(0, 255)
	ipv4Address3Part = random.randint(0, 255)
	ipv4Address4Part = random.randint(0, 255)
	ipv4Port = random.randint(1, 65535)
	if str(ipv4Address1Part) == "127":
		print("Прокси не найден")
	elif str(ipv4Address1Part) == "169" and str(ipv4Address2Part) == "254" and str(ipv4Address3Part) >= "1" or str(ipv4Address3Part) <= "254":
		print("Прокси не найден")
	else:
		print("Прокси найден")
		proxyIp = str(ipv4Address1Part) + str(ipv4Address2Part) + str(ipv4Address3Part) + str(ipv4Address4Part) + str(ipv4Port)
		os.environ["HTTPS_PROXY"] = "https://%s/" % proxyIp
		