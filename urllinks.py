import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
import ssl
import pandas as pd

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=5&RegionName=Nashik'
#url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

fh = open("arguments.txt", "a")

add = []
attr = []
tags = soup('a')
for tag in tags:
    add.append(tag.get('href', None))

for i in add:
    if i == None:
        continue
    else:
        attr.append(i)

for i in attr:
    if i.startswith("frmInstituteSummary"):
        fh.write(i + "\n")
    else:
        continue