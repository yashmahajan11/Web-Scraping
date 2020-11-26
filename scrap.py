import csv
import pytesseract
from bs4 import BeautifulSoup
import requests


url = " https://main.sci.gov.in/case-status "

r=requests.get(url)
htmlContent = r.content

bsobj = BeautifulSoup(htmlContent, "lxml")

table = bsobj.findAll("table",{"class":"z-content-inner"})
rows = table.findAll("tr")
csvFile = open("scrapData.csv",'wt',newline='')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()