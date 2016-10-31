#!/usr/bin/python3

import sys
import urllib3
import json

baseUrl = "http://api.urbandictionary.com/v0/"

def generateTable(ID, item, name, file):
	#read from file
	f = open(file,'r').read()
	#replace $ID, $name, and $item
	f = f.replace("$ID",ID).replace("$name", name).replace("$item", item)
	return f

def httpRequest(url):
	#returns string contents of http get request to url
	return urllib3.PoolManager().request('GET', url).data.decode('utf-8')

def autocomplete(term):
	#returns json from urbandictionary autocomplete
	return json.loads(httpRequest(baseUrl + "autocomplete?term=" + term.replace(" ","+")))

def search(term):
	#returns the tags, names, and corresponding definitions from urbandictionary search
	data = json.loads(httpRequest(baseUrl + "define?term=" + term.replace(" ","+")))
	tags = data['tags']
	definitions = []
	names = []
	for i in range(len(data['list'])):
		definitions.append(data['list'][i]['definition'])
		names.append(data['list'][i]['word'])
	return tags, names, definitions

def main():
	#use argument to search urbandictionary for tags and definitions
	
	#determine term from commandline argument; replace spaces with '+'
	term = ""
	if len(sys.argv) > 1:
		term = sys.argv[1].replace(" ", "+")

	#get autocomplete, tags, names, and definitions for term
	autoList = autocomplete(term)
	tagList, nameList, defList = search(term)

	#print definitions in table
	print("<h2 class='heading2'>Definitions</h2>\n<table>")
	for i in range(len(defList)):
		print(generateTable(str(i+1), defList[i], nameList[i], "template_define.html"))
	#print tags
	print("</table>\n<h2 class='heading2'>Related Words</h2>\n<table class='related_words'>")
	for i in range(len(tagList)):
		print(generateTable(str(i+1), tagList[i], "", "template_relate.html"))
	#print suggestions
	print("</table>\n<h2 class='heading2'>Suggested Words</h2>\n<table class='suggested_words'>")
	for i in range(len(autoList)):
		print(generateTable(str(i+1), autoList[i], "", "template_suggest.html"))

main()
