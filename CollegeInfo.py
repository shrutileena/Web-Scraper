import urllib.request, urllib.parse, urllib.error
import requests
import ssl
from bs4 import BeautifulSoup
import pandas as pd

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("D://Live Project/Project/arguments.txt", "r")
lines = fh.readlines()


rows = []

for i in range(len(lines)):
    print("Processing Link ", i+1, " ...")
    html = urllib.request.urlopen('http://dtemaharashtra.gov.in/' + lines[i], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    instName = soup.find('span', id="ctl00_ContentPlaceHolder1_lblInstituteNameEnglish").text
    address = soup.find('span', id="ctl00_ContentPlaceHolder1_lblAddressEnglish").text
    dte_region = soup.find('span', id="ctl00_ContentPlaceHolder1_lblRegion").text
    pincode = soup.find('span', id="ctl00_ContentPlaceHolder1_lblPincode").text
    website = soup.find('span', id="ctl00_ContentPlaceHolder1_lblWebAddress").text
    email = soup.find('span', id="ctl00_ContentPlaceHolder1_lblEMailAddress").text
    principal = soup.find('span', id="ctl00_ContentPlaceHolder1_lblPrincipalNameEnglish").text
    registrar = soup.find('span', id="ctl00_ContentPlaceHolder1_lblRegistrarNameEnglish").text
    office = soup.find('span', id="ctl00_ContentPlaceHolder1_lblOfficePhoneNo").text
    personal = soup.find('span', id="ctl00_ContentPlaceHolder1_lblPersonalPhoneNo").text
    
    rows.append([instName, address, dte_region, pincode, email, website, principal, office, personal, registrar])

df = pd.DataFrame(rows, columns=['Institute_Name', 'Address', 'DTE_Region', 'Pincode', 'Email_Address', 'Website_Link', 'Principal_Name', 'Office_Number', 'Personal_Number', 'Registrar_Name'])
#print(df.head)
df.to_csv('College_Data.csv')