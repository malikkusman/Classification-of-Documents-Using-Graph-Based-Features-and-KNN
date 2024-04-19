import requests
from bs4 import BeautifulSoup
import csv

url = "https://tijmenr.medium.com/two-types-of-entrepreneurship-the-freelancer-and-the-entrepreneur-d584df320ff0"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

title_element = soup.find("h1", id="55c5")
title = title_element.text.strip() if title_element else "Title not found"
content = soup.get_text()

print("Title: ", title)
print("Content: ", content)

file_path = "E:\\Semester 6\\GT\\article_data.csv"

with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)    
    if csvfile.tell() == 0:
        csv_writer.writerow(['Title', 'Content'])
    csv_writer.writerow([title, content])

print("Data appended to article_data.csv at", file_path)
