import time
import os
import requests
from ping3 import ping, verbose_ping
from bs4 import BeautifulSoup
from pokebase import cache
from lxml import html

html_doc = "<html></html>"
soup = BeautifulSoup(html_doc, 'html.parser')
cache.API_CACHE

dokurl = 'https://pokedoku.com/'

def sleep(slumtime):
    time.sleep(slumtime)

# testing /w/ just a lil' memeing
hubping = verbose_ping("pornhub.com")
# it gets annoying after a while.
# print(hubping)
try:
    with open('pingck.txt', 'r') as f:
        pingck_content = f.read()
except FileNotFoundError:
    pingck_content = None

if hubping is None:
    print("hubping returned None")
elif pingck_content is None:
    print("pingck_content is None")
elif hubping == pingck_content:
    print("hub is down")
else:
    print("hub is up")

# get html
response = requests.get(dokurl)

if response.status_code == 200:
    byte_data = response.content
    source_code = html.fromstring(byte_data)
    tree = source_code.xpath('//body')
    if tree:
        print(tree[0].text_content())
    else:
        print("no content found in the tree")
    
    # html to file
    with open("output.html", "wb") as file:
        file.write(byte_data)
else:
    print(f"fail 2 get: {response.status_code}")

# Parsing /w/ bs4
try:
    with open("output.html") as f:
        soup = BeautifulSoup(f, 'html.parser')
        print(soup.get_text())
except FileNotFoundError:
    print("html file not found.")

# dev
print("end")