#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests as req
import os
import time
"""
a = domain
b = site
"""

print("""1. Проверка одного сайта, ручной ввод, Пример: 'https://youtube.com' или 'youtube.com'""")
print("""2. Проверка множества сайтов, нужен файл, который должен находиться в том же каталоге где скрипт, ссылки должны быть разделены пробелом, не использовать для DDOS'а.""")
method = str(input())
siteHttps = "https://"

firstSplit = []

def domainName(b, c):
	global domain	
	c = b.split("/")
	domain = c[2]
	return domain

def siteCheckOne(a):
	global siteRequest
	r = req.get("%s" % a)
	if r.status_code == 200:
		siteRequest = "Correct"
		return siteRequest
	elif r.status_code != 200:
		siteRequest = "Error"
		return siteRequest
	else:
		siteRequest = "Incorrect link"
		return siteRequest

def siteLinksInFile(a):
	global fileRead
	global fileLinkList
	fileLinkList = []
	fileOpen = open("%s" % a, "r")
	fileRead = fileOpen.read()
	fileLinkList = fileRead.split(" ")
	fileLinkList = [line.rstrip("\n") for line in fileLinkList]
	fileOpen.close()
	print("fix 1 func " + str(fileLinkList))
	return fileLinkList

if __name__ == '__main__':
	if method == "1":
		siteLink = input("URL-address ")

		if siteHttps not in siteLink:
			site = str(siteHttps + siteLink)
		else:
			site = str(siteLink)

		domainName(site, firstSplit)
		siteCheckOne(site)
		print(domain + " Connect: " + siteRequest)
	elif method == "2":
		global fileName
		fileName = input("File Name: ")
		siteLinksInFile(fileName)
		for n in range(0, len(fileLinkList)):
			domainName(fileLinkList[n], firstSplit)
			siteCheckOne(fileLinkList[n])
			print(domain + " Connect: " + siteRequest)
			time.sleep(3)
	else: 
		pass
else:
	pass