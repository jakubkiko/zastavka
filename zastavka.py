import requests
from bs4 import BeautifulSoup
import codecs
import unidecode
import re

index_file_start = "<!DOCTYPE html><html><head><meta http-equiv='content-type' content='text/html; charset=UTF-8'><title>Zastavka</title><link rel='stylesheet' href='style.css'><script src='search.js' type='text/javascript'/></head><body><div id='header'><div class='input'><input placeholder='Hľadaj zastávku...' type='text' id='input'/><div id='searchclear' onmousedown='input.value='';'><b>x</b></div></div></div><ul><li><a href='https://imhd.sk/ba/online-zastavkova-tabula?theme=darkblue&st=%3B%3B%3B'><strong class='name'/>4 Najbližšie zastávky</a></li><!-- odkazy na zastavky -->"
index_file_end = "</body></html>"

url = "http://www.imhd.sk/ba/online-zastavkova-tabula?st="

file1 = open("index_new.html", "w", encoding="utf-8")
file1.write(index_file_start)

i = 0

while i < 594:

    link = url + str(i)

    page = requests.get(link)

    soup = BeautifulSoup(page.text, 'html.parser')

    name = soup.select("div#stop-name")

    text = str(name)

    if text == '[]':

        i = i + 1

    else:

        i = i + 1

        text = text.replace('[<div class="float-left" id="stop-name">', '')

        text = text.replace(' </div>]', '')

        #na linuxe netreba kodovat
        #title = codecs.decode(text, "unicode_escape")

        title = text

        accentless = unidecode.unidecode(title)

        lowercase = accentless.lower()

        lowercase = re.sub('[^A-Za-z0-9 ]+', '', lowercase)

        li = '<li><a href="' + link + '"><strong class="name">' + lowercase + '</strong>' + title \
             + '</a></li>'

        file1.write(li)
        print(li)

file1.write(index_file_end)
file1.close()
