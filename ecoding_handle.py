# -*- coding: utf-8 -*-
import os
import chardet
import shutil
import re
import uniout
import csv, itertools

def main():
	for root, dirs, files in os.walk("../csv/"):
	    for f in files:
	        file_name = os.path.join(root, f)
	       	if file_name.split('.')[-1]=="csv":
	       		# print file_name
	       		f = open(file_name,'r')

	       		content = f.read()

	       		file_encoding = chardet.detect(content)
	       		if len(content.splitlines())>6:
	       			if len(content.splitlines()[3].split(","))==len(content.splitlines()[4].split(",")):
	       				print "len is the same!"

			       		if file_encoding['encoding']=="utf-8" or file_encoding['encoding']=="UTF-8-SIG" :\
			       		
			       			path = "../UTF-8/" + file_name.split("/")[-2]
			       			info_path = "../csv/" + file_name.split("/")[-2] + "/info.json"
			
			       			if os.path.exists(path) == False :
			       				os.makedirs(path)
			       			shutil.copy(file_name,path)
			       			if os.path.isfile(path + "/info.json") == False :
			       				shutil.copy(info_path,path)

			       		elif file_encoding['encoding']=="Big5":
			
			       			path = "../Big5/" + file_name.split("/")[-2]
			       			info_path = "../csv/" + file_name.split("/")[-2] + "/info.json"

			       			if os.path.exists(path) == False :
			       				os.makedirs(path)
			       			shutil.copy(file_name,path)

			       			if os.path.isfile(path + "/info.json") == False :
			       				shutil.copy(info_path,path)


if __name__ == "__main__":
	main()