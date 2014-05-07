__author__ = 'Janet'

import urllib

# http://api.brewerydb.com/v2/beers?key=13ef64215cc26735e0a4c0964e854659&p=1

template_url = "http://api.brewerydb.com/v2/%s?key=13ef64215cc26735e0a4c0964e854659"
beers_url = template_url % "beers"
max_page = 554

def getbeers(url):
    file = open("beers_first100.json", "a")
    for i in range(1, 101):
        print "fetching page", i, "..."
        file.write(urllib.urlopen(url+"&p=%d" % i).read())

getbeers(beers_url)