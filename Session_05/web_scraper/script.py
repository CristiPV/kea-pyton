import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get( URL )

file = open( "page.txt", "w" )

soup = BeautifulSoup( page.content, "html.parser" )

print( page )

results = soup.find( id="ResultsContainer" )

job_elements = results.find_all( "section", class_="card-content" )
for job in job_elements:
    title_elem = job.find('h2', class_='title')
    company_elem = job.find('div', class_='company')
    location_elem = job.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    file.write( f"\nTitle: \n {title_elem.text.strip()}" )
    file.write( f"\nCompany: \n {company_elem.text.strip()}" )
    file.write( f"\nLocation: \n {location_elem.text.strip()}" )
    file.write( "\n"*2 )

