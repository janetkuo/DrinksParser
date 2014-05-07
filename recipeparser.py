__author__ = 'Janet'

import csv
import re
import os

txt_filename = 'mixes.txt'
csv_filename = 'mixes.csv'
fields = ['Recipe', 'Glass', 'Ingredients', 'Steps']

def generateCSV(filename):
    f = open(filename, 'rU')
    lines = f.readlines()
    output(lines)

def csv_writer_field(field_list, filename=csv_filename):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(field_list)

def csv_writer(data_list, filename=csv_filename):
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data_list)

def output(lines):
    csv_writer_field(fields)
    for line in lines:
        #match = re.findall(r'\[["\'](.+?)["\'],\s*["\'](.+?)["\'],\s*\[(.+?)\],\s*\'(.+?)\'', line)
        match = re.findall(r'\[(.+?),\s*(.+?),\s*\[(.+?)\],\s*(.+?)\]', line)
        data_list = []
        if match:
            for item in match[0]:
                data_list.append(item)
        csv_writer(data_list)

def main():
    generateCSV(txt_filename)

if __name__ == '__main__':
    main()
