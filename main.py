import requests
import mysql.connector
from bs4 import BeautifulSoup
import datetime

# establish mySQL connection 
def conntectMySQl(): 
        connection = mysql.connector.connect(
            host='localhost',
            user = 'aaroncfrancis',
            password = 'samplepassword',
            database = 'news'
        )
        if connection.is_connected():
            print('Successful connection')
        return connection

def createNewsTable(connection):
      cursor = connection.cursor()
      cursor.execute()
      connection.commit()
      print('news table created')

# Add news data into the table
def insertNewsData(connection, headline, summary, url, publication_date, citation): 
      cursor = connection.cursor()
      query = "Insert into news (headline, summary, url, publication_date, citation)"
      data = (headline, summary, url, publication_date, citation)
      cursor.execute(query, data)
      connection.commit()
      print('data successfully inserted into the table')

# Scraper
def scrapeAndStore():
      url = 'https://www.bbc.com/news'
      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')
      
      headlines =  [headline.text for headline in soup.find_all('h2')]
      summaries = [summary.text for summary in soup.find_all('p')]
      urls = [url["href"] for url in soup.find_all]
      publication_dates = [date.text for date in soup.find_all('span', class_='date')]
      citations = [citation.text for citation in soup.find_all('span', class_='citation')]
      
      connection = create_connection()
      create_news_table(connection)
      today = datetime.date.today()

if __name__ == '__main__':
      scrapeAndStore()

connection.close()


    

        
