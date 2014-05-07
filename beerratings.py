__author__ = 'Janet'

# http://www.beerpal.com/vault/topbeer.asp?state=&country=USA&bwb=17475&sa=1&rank=1
# bwb=1 to 17475

import urllib
from bs4 import BeautifulSoup
import csv

template_url = 'http://www.beerpal.com/vault/topbeer.asp?state=&country=USA&bwb=%d&sa=1&rank=1'
csv_filename = 'beer_ratings.csv'
fields = ['Beer', 'Origin', 'Style', 'ABV', 'Ratings']

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def csv_writer_field(field_list, filename=csv_filename):
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(field_list)

def csv_writer(data_list, filename=csv_filename):
    with open(filename, 'ab') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data_list)

def get_beer_table():
    for i in my_range(1, 17476, 25):
        print "Retrieving", i, "to", i+25, "..."
        url = template_url % i
        page = urllib.urlopen(url)

        soup = BeautifulSoup(page)

        for j in range(0, 25):
            table = soup.find_all("table", attrs={"class":"dat"})[1].find_all("td", attrs={"class":"dat"})
            beer = list(table[j*5].descendants)[1]
            origin = list(table[j*5+1].descendants)[0].split(',')[0]
            style = list(table[j*5+2].descendants)[0]
            abv = list(table[j*5+3].descendants)[0]
            rating = list(table[j*5+4].descendants)[2]
            csv_writer([str(beer.encode("utf-8")), str(origin.encode("utf-8")), str(style.encode("utf-8")),
                        str(abv.encode("utf-8")), str(rating.encode("utf-8"))])

csv_writer_field(fields)
get_beer_table()