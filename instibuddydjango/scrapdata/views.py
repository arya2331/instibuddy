from django.shortcuts import render
import webbrowser, sys, requests, time,csv
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


def get_Recipe(request):
    outfile = open("scrape.csv", 'w', newline='')
    writer = csv.writer(outfile)
    URL = 'http://www.cese.iitb.ac.in/faculty-directory'
    df = pd.DataFrame(columns=['Name', 'Post', 'Contact', 'Email-ID'])
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='datatable')
    contact_elems = results.find_all('tr')
    for contact_elem in contact_elems:
        title_elem = contact_elem.find('td', class_='views-field views-field-title')
        post_elem = contact_elem.find('td', class_='views-field views-field-field-faculty-designation-1')
        appoint_elem = contact_elem.find('td', headers_='view-field-employment-category-table-column')
        roomno_elem = contact_elem.find('td', headers_='view-field-room-no-table-column')
        PhoneNo_elem = contact_elem.find('td', class_='views-field views-field-field-phone-no-new')
        Email_elem = contact_elem.find('td', class_='views-field views-field-field-email-new')
        if title_elem is None:
            continue
        else:
            Title = title_elem.text
            print(title_elem.text)
        if post_elem is None:
            continue
        else:
            Post = post_elem.text
            print(post_elem.text)
        if PhoneNo_elem is None:
            continue
        else:
            contact = PhoneNo_elem.text
            print(PhoneNo_elem.text)
        if Email_elem is None:
            print("none")
        else:
            Email = Email_elem.text
            print(Email)
        df2 = pd.DataFrame([[Title, Post, contact, Email]], columns=['Name', 'Post', 'Contact', 'Email-ID'])
        df = df.append(df2, ignore_index=True)
    response = HttpResponse(df, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=scrap.csv'
    # writer = csv.writer(response)
    df.to_csv(response, index=False)
    return response
