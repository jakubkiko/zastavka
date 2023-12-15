import requests
from bs4 import BeautifulSoup
import codecs
import unidecode
import re

url = "http://www.imhd.sk/ba/online-zastavkova-tabula?st="

i = 0

file1 = open("index_new.html", "w") 

#pridali nove zastavky > 4000
while i < 5000:

    link = url + str(i)

    page = requests.get(link)

    soup = BeautifulSoup(page.text, 'html.parser')

    name = soup.select("div#stop-name")

    text = str(name)

    if text == '[]':

        file1.write('')

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

file1.close()
