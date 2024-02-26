import csv
import re
from datetime import datetime
import pandas as pd

with open("Capitec_Bank_dataset.csv",encoding='utf-8') as file:
    readers = csv.DictReader(file, delimiter=';')
    reviews = []
    for reader in readers:
        print(reader)

i = 0
header = reviews[0].keys()

file_path = "C:/Users/Pheta/OneDrive/Documents/Data Analytics/Scrape Data using API/clean_data.csv"
for review in reviews:

    clean = review['response']


    match = re.search(r"'body': '([^']*)'", clean)
    if match:
        desired_text = match.group(1)

    # Extract the 'created_at' value
    match = re.search(r"'created_at': '([^']*)'", clean)
    if match:
        created_at = match.group(1)
    desired_text = re.sub(r"\s^<div>(<br>)(&nbsp)(:-\))?(</div>)"," ",desired_text)

    desired_text = re.sub(r'<[^>]*>', '', desired_text)
    # Remove special characters and extra spaces

    desired_text = re.sub(r'[^A-Za-z0-9\s\'":.!?,]', '', desired_text)
    # Replace multiple spaces with a single space

    desired_text = re.sub(r'\s+', ' ', desired_text)

    desired_text = re.sub("nbspKind\sregardsnbspCapitec\sBank", "", desired_text)
    desired_text = re.sub("nbsp", " ", desired_text)
    desired_text = re.sub(r'\s+', ' ', desired_text)
    desired_text = re.sub(r'\sWhy do businesses and reviewers write private replies\?', '', desired_text)
    desired_text = desired_text.strip()
    review['response'] = desired_text
    review["responseTime"] = created_at
   # print(review['responseTime'])
    i+=1
    print(i)
##########################END OF DATA TRANSFORMATION FOR THE MESSAGES(RESPONSE) FIELD#########################



with open(file_path, "w", newline="",encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    writer.writerows(reviews)