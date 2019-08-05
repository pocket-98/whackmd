#!/usr/bin/python3

import sys
from urllib.request import urlopen
import json

baseUrl = "http://api.urbandictionary.com/v0/"

def generateTable(ID, item, name, file):
    #read from search_template.html and replace $ID and $item
    f = open(file,'r')
    return f.read().replace("$ID",ID).replace("$name", name).replace("$item", item)

def httpRequest(url):
    return urlopen(url).read().decode('utf-8')

def autocomplete(term):
    return json.loads(httpRequest(baseUrl + "autocomplete?term=" + term.replace(" ","+")))

def search(term):
    data = json.loads(httpRequest(baseUrl + "define?term=" + term.replace(" ","+")))
    tags = []
    definitions = []
    names = []
    if 'tags' in data:
        tags = data['tags']
    for i in range(len(data['list'])):
        definitions.append(data['list'][i]['definition'])
        names.append(data['list'][i]['word'])
    return tags, names, definitions

def main():
    #use argument to search urbandictionary for autocomplete, tags, and definition
    term = ""
    if len(sys.argv) > 1:
        term = sys.argv[1].replace(" ", "+")
    autoList = autocomplete(term)
    tagList, nameList, defList = search(term)

    #print definitions
    print("<h2 class='heading2'>Definitions</h2><table>")
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
