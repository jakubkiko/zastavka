import requests
from bs4 import BeautifulSoup
import codecs
import unidecode
import re

index_html = "<!DOCTYPE html><html><head><meta http-equiv='content-type' content='text/html; charset=UTF-8'><title>Zastavka</title><link rel='stylesheet' href='style.css'><script src='search.js' type='text/javascript'/></head><body><div id='header'><div class='input'><input placeholder='Hľadaj zastávku...' type='text' id='input'/><div id='searchclear' onmousedown='input.value=&quot;&quot;'><b>x</b></div></div></div><ul><!-- odkazy na zastavky -->"
url = "http://www.imhd.sk/ba/online-zastavkova-tabula?st="

file1 = open("index_new.html", "w", encoding="utf-8")

i = 0

while i < 5000:

    link = url + str(i)

    page = requests.get(link)

    soup = BeautifulSoup(page.text, 'html.parser')

    name = soup.select("div#stop-name")

    text = str(name)

    if text == '[]':

        i = i + 1

    else:

        text = text.replace('[<div class="float-left" id="stop-name">', '')

        text = text.replace(' </div>]', '')

        #na linuxe netreba kodovat
        #title = codecs.decode(text, "unicode_escape")

        if text == '':
            title = 'Najbližšia zastávka'
        else:
            title = text

        accentless = unidecode.unidecode(title)

        lowercase = accentless.lower()

        lowercase = re.sub('[^A-Za-z0-9 ]+', '', lowercase)

        li = '<li><a href="https://www.nullreferer.com/?https://' + link + '"><strong class="name">' + lowercase + '</strong>' + title \
             + '</a></li>'

        index_html += li
        print(li)

        i = i + 1

index_html += "</ul></body></html>"

soup2 = BeautifulSoup(index_html, 'html.parser')

file1.write(str(soup2.prettify()))
file1.close()
