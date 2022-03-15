from bs4 import BeautifulSoup as bs
import urllib3

def GetArticleText(art_url):    
    http = urllib3.PoolManager()
    requested = http.request('GET', art_url)
    B = BeautifulSoup(requested.data.decode('utf-8'), 'lxml')
    Btmp = B.find('div', {'id': 'storytext'})
    T = Btmp.get_text().replace("\n", "")
    return T
 
def ScrapeNPR():
    http = urllib3.PoolManager()
    npr_url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
    requested = http.request('GET', npr_url)
    B = BeautifulSoup(requested.data.decode('utf-8'), 'lmxl')
    Articles = B.find_all('h2', attrs = {'class':'title'})
    for meta_art in Articles:
        title = meta_art.find('a').string
        art_url = meta_art.find('a')['href']
        article = GetArticleText(art_url)
        print(title)
        print(art_url)
        SentimentAnalysis(article)
        Summary(article)
        print("-------------------------")



def main():
    ScrapeNPR()
main()