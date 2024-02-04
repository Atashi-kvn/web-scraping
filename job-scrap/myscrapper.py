import sys
import requests
from bs4 import BeautifulSoup
import csv 


job_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=').text
scrap = BeautifulSoup(job_text, 'lxml')
jobs = scrap.find_all('li', class_ ='clearfix job-bx wht-shd-bx')

for job in jobs:
    onsite_time = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in onsite_time:
        job_title = job.find('header', class_ = "clearfix").text.replace(' ', '')
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')



        print(f'''
        Company Name: {company_name}
        Job Title: {job_title}
        Skills: {skills}
        On site time: {onsite_time}
              ''')

        # with open('jobs.csv', 'a') as file:
        #     writer = csv.writer(file)
        #     writer.writerow([company_name, job_title, skills, onsite_time])


