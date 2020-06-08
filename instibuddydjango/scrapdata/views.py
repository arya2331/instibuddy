from django.shortcuts import render
import webbrowser, sys, requests, time,csv
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Scrapcode
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ScrapcodeSerializer

# class ScrapcodeViewSet(viewsets.ModelViewSet):
    # queryset=Scrapcode.objects.all()
    # serializer_class= ScrapcodeSerializer

@api_view(['POST',])
def api_detail_scrapcode_view(request):
    try:
        scrapcode= Scrapcode.objects.filter(department=request.data["dept"])
        # scrapcode= request.data["department"]
    except Scrapcode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method== 'POST':
        serializer=ScrapcodeSerializer(scrapcode, many=True)
        return Response(serializer.data)

def get_Recipe_cese(request):
    # outfile = open("scrape.csv", 'w', newline='')
    # writer = csv.writer(outfile)
    URL = 'http://www.cese.iitb.ac.in/faculty-directory'
    # df = pd.DataFrame(columns=['Name', 'Post', 'Contact', 'Email-ID'])
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
        if (title_elem is not None) and (PhoneNo_elem is not None) and (Email_elem is not None):
            scrapcode=Scrapcode(prof_Name=title_elem.text,email=Email_elem.text,phone_number=PhoneNo_elem.text,department='Environmental Science & Engineering')
            scrapcode.save()
        else:
            continue
    return HttpResponse(status=201)


def get_Recipe_chem(request):
    URL1='https://www.che.iitb.ac.in/faculty-directory'
    page1=requests.get(URL1)

    soup1=BeautifulSoup(page1.content,'html.parser')
    results1=soup1.find(id='datatable')
    con_elems=results1.find_all('tr')
    for con_elem in con_elems:
        name_elem= con_elem.find('td',class_='views-field views-field-title')
        phone_elem= con_elem.find('td',class_='views-field views-field-field-phone-no-new')
        email_elem=con_elem.find('td',class_='views-field views-field-field-email-new')
        if (name_elem is not None) and (phone_elem is not None) and (email_elem is not None):
            scrapcode1=Scrapcode(prof_Name=name_elem.text,email=email_elem.text,phone_number=phone_elem.text,department='Chemical Engineering')
            scrapcode1.save()
        else:
            continue
    return HttpResponse(status=201)

def get_Recipe_mech(request):
    URL = 'https://www.me.iitb.ac.in/?q=full-time-faculty'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', class_='views-table cols-5')
    fac_elems = table.find_all('tr')
    for fac_elem in fac_elems:

        fac_name = fac_elem.find('h4', class_='bluecolor')
        fac_tele = fac_elem.find_all('td')
        fac_email = fac_elem.find('td', class_='views-field views-field-field-display-email bluecolor')
        fac_interests = fac_elem.find_all('p')
        if (fac_name is not None) and (fac_tele is not None) and (fac_email is not None) and (fac_interests is not None):
            scrapcode2=Scrapcode(prof_Name=fac_name.text,email=fac_email.text,phone_number=fac_tele[2].text,expertise=fac_interests[1].text,department='Mechanical Engineering')
            scrapcode2.save()
        else:
            continue
    return HttpResponse(status=201)

def get_Recipe_elec(request):
    URL = 'https://www.ee.iitb.ac.in/web/people/faculty'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='wrapper')

    job_elems = results.find_all('div', class_='auxunder')
    #print(job_elems[0])

    list_elems=job_elems[0].find_all('ul', class_='facultyview')
    #print(list_elems[0].text) //bgf details

    detail_elems=list_elems[1].find_all('li')
    list_name=[]
    list_phone_number=[]
    list_email=[]
    list_area=[]
    # so we have 1,3,5... as area of interest. so we have detail_elems[2n+1] as area
    #name_elem=detail_elems.find_all('div', class_='faculty_name')
    for detail_elem in detail_elems:
        name_elem=detail_elem.find('div', class_='faculty_name')
        if name_elem is None:
            continue
        else:
            list_name.append(name_elem.text)
        contact_elem=detail_elem.find('div', class_='ppe')
        #print(contact_elem.text)
        phone_and_email=contact_elem.find_all("span")
        #print(phone_and_email[0])
        for contact_number in phone_and_email[0]:
            list_phone_number.append(contact_number)
        for email_detail in phone_and_email[1]:
            list_email.append(email_detail)
        area_elem=detail_elem.find('div', class_='row faculty_box')
        if area_elem is None:
            continue
        else:
            list_area.append(area_elem.text)
    list_name = list(map(lambda s: s.strip(), list_name) )
    list_phone_number = list(map(lambda s: s.strip(), list_phone_number) )    
    list_email = list(map(lambda s: s.strip(), list_email) )
    list_area = list(map(lambda s: s.strip(), list_area) )
    i=0
    for i in range(len(list_name)):
        scrapcode3=Scrapcode(prof_Name=list_name[i],email=list_email[i],phone_number=list_phone_number[i],expertise=list_area[i],department='Electrical Engineering')
        scrapcode3.save()
    return HttpResponse(status=201)
        
def get_Recipe_aero(request):
    URL='https://www.aero.iitb.ac.in/home/people/faculty'
    page=requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    containers=soup.find(id="block-views-faculty-block-1")
    containers3=soup.find(id="block-views-adjunct-faculty-block-1")
    adjunct_faculty=containers3.find('table')
    body3=adjunct_faculty.find("tbody")
    rows3=body3.find_all("tr")
    containers4=soup.find(id="block-views-visiting-faculty-block-1")
    visiting_faculty=containers4.find('table')
    body4=visiting_faculty.find("tbody")
    rows4=body4.find_all("tr")


    faculty_table=containers.find('table') 
    body=faculty_table.find("tbody")
    rows=body.find_all("tr")
    containers2=soup.find(id="block-views-emeritus-faculty-block-1")
    emeritus_faculty=containers2.find('table')
    body2=emeritus_faculty.find("tbody")
    rows2 = body2.find_all("tr")
        

    for row in rows:
        name=row.find("td",class_="views-field views-field-title").text.strip()
        area_expertise=row.find("td",class_="views-field views-field-field-specialization").text.strip()
        phone_number=row.find("td",class_="views-field views-field-field-phone-number").text.strip()
        email_=row.find("td",class_="views-field views-field-field-email").text.strip()
        scrapcode4=Scrapcode(prof_Name=name,email=email_,phone_number=phone_number,expertise=area_expertise,department='Aerospace Engineering')
        scrapcode4.save()
        
        

    for row2 in rows2:
        name=row2.find("td",class_="views-field views-field-title").text.strip()
        area_expertise=row2.find("td",class_="views-field views-field-field-specialization").text.strip()
        phone_number=row2.find("td",class_="views-field views-field-field-phone-number").text.strip()
        email_=row2.find("td",class_="views-field views-field-field-email").text.strip()
        scrapcode5=Scrapcode(prof_Name=name,email=email_,phone_number=phone_number,expertise=area_expertise,department='Aerospace Engineering')
        scrapcode5.save()

        

    for row3 in rows3:
        name=row3.find("td",class_="views-field views-field-title").text.strip()
        area_expertise=row3.find("td",class_="views-field views-field-field-specialization").text.strip()
        phone_number=row3.find("td",class_="views-field views-field-field-phone-number").text.strip()
        email_=row3.find("td",class_="views-field views-field-field-email").text.strip()
        scrapcode6=Scrapcode(prof_Name=name,email=email_,phone_number=phone_number,expertise=area_expertise,department='Aerospace Engineering')
        scrapcode6.save()

    for row4 in rows4:
        name=row4.find("td",class_="views-field views-field-title").text.strip()
        area_expertise=row4.find("td",class_="views-field views-field-field-specialization").text.strip()
        phone_number=row4.find("td",class_="views-field views-field-field-phone-number").text.strip()
        email_=row4.find("td",class_="views-field views-field-field-email").text.strip()
        scrapcode7=Scrapcode(prof_Name=name,email=email_,phone_number=phone_number,expertise=area_expertise,department='Aerospace Engineering')
        scrapcode7.save()
    return HttpResponse(status=201)

def get_Recipe_ctara(request):
    URL = 'http://www.ctara.iitb.ac.in/en/faculty-details'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find('div', class_='view-content')
    fac_elems = results.find_all('div', class_='group-right')


    for fac_elem in fac_elems:

        fac_name = fac_elem.find('div', class_='field field-name-title field-type-ds field-label-hidden')
        fac_tele = fac_elem.find('div', class_='field field-name-field-emp-phone field-type-text field-label-inline clearfix')
        fac_email = fac_elem.find('div', class_='field field-name-field-emp-email field-type-email field-label-inline clearfix')
        fac_interests = fac_elem.find('div', class_='field field-name-field-emp-role field-type-text-long field-label-inline clearfix')
        if (fac_name is not None) and (fac_tele is not None) and (fac_email is not None) and (fac_interests is not None):
            scrapcode2=Scrapcode(prof_Name=fac_name.text.strip(),email=fac_email.text[7:].strip(),phone_number=fac_tele.text[13:].strip(),expertise=fac_interests.text[20:].strip(),department='C.T.A.R.A.')
            scrapcode2.save()
        else:
            continue
    return HttpResponse(status=201)

def get_Recipe_edtech(request):
    
    URL = 'http://www.et.iitb.ac.in/Faculty.html'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(class_='col-lg-12 Core-faculty')
    fac_elems = results.find_all(class_='col-lg-9 col-md-9 col-sm-9 faculty-brief')

    for fac_elem in fac_elems:
            
        fac_use = fac_elem.find_all('p')
        if None in(fac_use):
            continue

        # thewriter.writerow([fac_use[0].text.strip(), fac_use[2].text[11:].strip(), fac_use[1].text[9:].strip(), fac_use[-1].text[20:].strip()])   

        scrapcode2=Scrapcode(prof_Name=fac_use[0].text.strip(),email=fac_use[1].text[9:].strip(),phone_number=fac_use[2].text[11:].strip(),expertise= fac_use[-1].text[20:].strip(),department='Educational Technology')
        scrapcode2.save()
        # thewriter.writerow([fac_use[0].text.strip(), fac_use[2].text[11:].strip(), fac_use[1].text[9:].strip(), fac_use[-1].text[20:].strip()])   


    return HttpResponse(status=201)   

def get_Recipe_maths(request):
    URL = 'http://www.math.iitb.ac.in/People/faculty.php'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(class_='tab-content')
    fac_elems = results.find_all('div', class_='col-md-8 col-sm-8 col-xs-12')

    for fac_elem in fac_elems: 

        fac_use = fac_elem.find_all('h4')
        fac_link = fac_elem.find_all('a')
        
        if(fac_use[5].text[0:4] == "Home"):
            scrapcode2=Scrapcode(prof_Name=fac_link[0].text.strip(),email=fac_use[2].text[5:].strip(),phone_number=fac_use[6].text[10:].strip(),expertise= fac_link[1].text.strip(),department='Maths')
            scrapcode2.save()
            # thewriter.writerow([fac_link[0].text.strip(), fac_use[6].text[10:].strip(), fac_use[2].text[5:].strip(), fac_link[1].text.strip()])  

        else:
            scrapcode2=Scrapcode(prof_Name=fac_link[0].text.strip(),email=fac_use[2].text[5:].strip(),phone_number=fac_use[5].text[10:].strip(),expertise= fac_link[1].text.strip(),department='Maths')
            scrapcode2.save()
            # thewriter.writerow([fac_link[0].text.strip(), fac_use[5].text[10:].strip(), fac_use[2].text[5:].strip(), fac_link[1].text.strip()])  

    return HttpResponse(status=201) 
        

def get_Recipe_chemistry(request):
    URL = 'https://www.chem.iitb.ac.in/people'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find('div', class_='view-content')
    fac_elems = results.find_all('div', class_='col-xs-12 col-sm-6 col-md-4 col-lg-3')
    for fac_elem in fac_elems:

        fac_name = fac_elem.find('p')

        site = fac_elem.find('a')
        link = site.get('href')

        page2 = requests.get("https://www.chem.iitb.ac.in" + link)
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        output = soup2.find('div', class_='panel-display panel-2col clearfix')
        
        fac_tele = output.find('div', class_='views-field views-field-field-contact-number')
        fac_email = output.find('div', class_='views-field views-field-mail')
        
        if (fac_name is not None) and (fac_tele is not None) and (fac_email is not None):
            scrapcode2=Scrapcode(prof_Name=fac_name.text.strip(),email=fac_email.text.strip(),phone_number=fac_tele[2].text.strip(),department='Chemistry')
            scrapcode2.save()
        else:
            continue
    return HttpResponse(status=201)
        # thewriter.writerow([fac_name.text.strip(), fac_tele.text.strip(), fac_email.text.strip()])

def get_Recipe_cse(request):
    URL = 'https://www.cse.iitb.ac.in/page14'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='main')
    contact_table=results.find('div', class_='mpart')
    contact_elem_1=contact_table.find_all('tr', class_='row1')
    contact_elem_2=contact_table.find_all('tr', class_='row2')
    #print(len(contact_elem_2))
    #print(len(contact_elem_2))

    #print(contact_elem_2[0])
    #contact_elem_1 and contact_elem_2 are two arrays containing details of the faculties.


    for x in contact_elem_2:
        elems=x.find_all('tr')
        name_email=elems[1].find_all('td')
        name=name_email[0]
        email=name_email[1]
        area=elems[2].find('td')
        try:
            office_address=elems[3].find('td')
            phone=elems[4].find('td')
        except IndexError:
            break
        if None in (name, email, area, office_address, phone):
            continue
        scrapcode2=Scrapcode(prof_Name=name.text.strip(),email= email.text.strip(),phone_number= phone.text.strip(),expertise=area.text.strip(),department='Computer Science & Engineering')
        scrapcode2.save()
        
        # writerow([name.text.strip(), phone.text.strip(), email.text.strip(), office_address.text.strip(),area.text.strip()])
    for x in contact_elem_1:
        elems=x.find_all('tr')
        name_email=elems[1].find_all('td')
        name=name_email[0]
        email=name_email[1]
        area=elems[2].find('td')
        try:
            office_address=elems[3].find('td')
            phone=elems[4].find('td')
        except IndexError:
            break
        if None in (name, email, area, office_address, phone):
            continue
        scrapcode3=Scrapcode(prof_Name=name.text.strip(),email= email.text.strip(),phone_number= phone.text.strip(),expertise=area.text.strip(),department='Computer Science & Engineering')
        scrapcode3.save()
        # thewriter.writerow([name.text.strip(), phone.text.strip(), email.text.strip(), office_address.text.strip(),area.text.strip()])
    return HttpResponse(status=201)    

def get_Recipe_hss(request):
    URL = 'http://www.hss.iitb.ac.in/en/faculty_details'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('table', class_='views-table cols-5')
    contact_table=results.find_all('tr')
    #print(contact_table[1].text)

    size=len(contact_table)
    #print(size)
    for x in range (1, size):
        elems=contact_table[x].find_all('td')
        name=elems[0]
        phone=elems[3]
        email=elems[2]
        discipline=elems[4]
        scrapcode3=Scrapcode(prof_Name=name.text.strip(),email= email.text.strip(),phone_number= phone.text.strip(),expertise=discipline.text.strip(),department='Humanities & Social Sciences')
        scrapcode3.save()        
        # thewriter.writerow([name.text.strip(), phone.text.strip(), email.text.strip(), discipline.text.strip()])
    return HttpResponse(status=201)    

def get_Recipe_monash(request):
    
    URL = 'http://www.iitbmonash.org/iitb/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('div', class_='vc_tta-panels-container')
    #print(results)
    contact_table=results.find_all('div', class_='vc_tta-panel')
    #contact_table2=results.find_all('div', class_='vc_tta-panel')
    #print(contact_table2[2].text)
    #print(contact_table[0].text)
    #print(contact_table[2].text)

    for x in contact_table:
        #print(x.text)
        y1=x.find_all('tr', class_='odd')
        y2=x.find_all('tr', class_='even')
        for z in y1:
            elem=z.find_all('td')
            name=elem[0]
            email=elem[1]
            speciality=elem[2]
            # thewriter.writerow([name.text.strip(), email.text.strip(), speciality.text.strip()])
            scrapcode3=Scrapcode(prof_Name=name.text.strip(),email= email.text.strip(),phone_number= '',expertise=speciality.text.strip(),department='Monash Research Academy')
            scrapcode3.save() 
        for z in y2:
            elem=z.find_all('td')
            name=elem[0]
            email=elem[1]
            speciality=elem[2]
            # thewriter.writerow([name.text.strip(), email.text.strip(), speciality.text.strip()])
            scrapcode4=Scrapcode(prof_Name=name.text.strip(),email= email.text.strip(),phone_number='',expertise=speciality.text.strip(),department='Monash Research Academy')
            scrapcode4.save()  
    
    return HttpResponse(status=201)

def get_Recipe_physics(request):
    
    URL = 'http://www.phy.iitb.ac.in/en/faculty'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('div', class_='view-content')
    contact_table=results.find_all('tr')

    for x in contact_table:
        elems=x.find_all('td')
        for y in elems:
            name=y.find('div', class_='views-field views-field-title')
            phone=y.find('div', class_='views-field views-field-field-emp-phone')
            email=y.find('div', class_='views-field views-field-field-emp-email')
            #address=y.find('div' , class_='views-field views-field-field-address')
            if (name is not None) and (phone is not None) and (email is not None):
                scrapcode4=Scrapcode(prof_Name=name.text.strip(),email= email.text.strip(),phone_number=phone.text.strip(),department='Physics')
                scrapcode4.save()
    return HttpResponse(status=201)
            #print(email.text)
            # thewriter.writerow([name.text.strip(), phone.text.strip(), email.text.strip(), address.text.strip()])
    
def get_Recipe_syscon(request):
    
    URL = 'https://www.sc.iitb.ac.in/coreFaculty.html'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('div', class_='content')
    #print(results.text)
    contact_table=results.find_all('tr')
    size=len(contact_table)
    for x in range (1, size):
        elems=contact_table[x].find_all('td')
        name=elems[1].find('a')
        area=elems[1].find('span' , class_='researchArea')
        contact=elems[1].find('span', class_='profContact')
        if None in (name,area,contact):
            continue
        scrapcode4=Scrapcode(prof_Name=name.text.strip(),email= contact.text.strip(),expertise=area.text.strip(),department='Systems & Controls Engineering')
        scrapcode4.save()
    return HttpResponse(status=201)
        # thewriter.writerow([name.text.strip(), contact.text.strip(), area.text.strip()])

