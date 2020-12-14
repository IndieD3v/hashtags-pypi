from bs4 import BeautifulSoup
import requests

def best_hashtags(category):

    URL = f"http://best-hashtags.com/hashtag/{category}/"
    page = requests.get(URL)

    soup =  BeautifulSoup(page.content,"html.parser")

    hashtag = soup.find("p1").get_text()
    
    print("\n",hashtag,"\n")
    
    
def top_hashtags():

    URL = "https://top-hashtags.com/instagram/"
    page = requests.get(URL)

    soup =  BeautifulSoup(page.content,"html.parser")

    for i in range(30):
        hashtag = soup.find_all(class_='i-tag')

        print(hashtag[i].get_text())

def hashtag_by_location(country,category):

    URL = f"https://www.tagsfinder.com/en-{country}/related/{category}/"
    page = requests.get(URL)

    soup =  BeautifulSoup(page.content,"html.parser")

    hashtag = soup.find(id='hashtagy').get_text()

    print("\n",hashtag,"\n")
    

