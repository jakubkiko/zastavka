import requests
from bs4 import BeautifulSoup
import codecs
import unidecode
import re

url = "http://www.imhd.sk/ba/online-zastavkova-tabula?st="

i = 0

#pridali nove zastavky > 4000
while i < 5000:

    link = url + str(i)

    page = requests.get(link)

    soup = BeautifulSoup(page.text, 'html.parser')

    name = soup.select("div#stop-name")

    text = str(name)

    if text == '[]':

        print('')

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

        li = '<li><a href="https://nullreferer.com?' + link + '"><strong class="name">' + lowercase + '</strong>' + title \
             + '</a></li>'

        print(li)
