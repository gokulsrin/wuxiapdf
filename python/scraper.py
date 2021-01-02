from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests 

#also need a way to get the name of the novel here
class Scraper: 
    def __init__(self, url, name):
        self.url = url
        self.name = name

   # METHOD NAME:
   # DESCRIPTION
   #PARAMETERS
   # RETURN TYPE
    def getChapterUrls(self):
        #get the page source 
        r = requests.get(self.url)
        page_source = r.text

        #construct soup object
        soup = BeautifulSoup(page_source, 'html.parser')

        # here is our query related info 

    
        chapterlist = {}
        # find all of the links associated with the chapters 
        data = soup.findAll('a','chapter-item')
        i = 0
        for link in data:
            text = link.get('href')
            #redundant check but better to be safe 
            if (text != None) and (".html" and self.name in text and ".jpg" not in text):
                i += 1
                #and the base url
                baseurl = self.url[0:len(self.url)-1]
                chapterlist[i]= baseurl + text
                
        return chapterlist

    # METHOD NAME:
    # DESCRIPTION
    #PARAMETERS
    # RETURN TYPE
    def getChapterText(self, url):

        r = requests.get(url)
        page_source = r.text

        soup = BeautifulSoup(page_source, 'html.parser')
        data = soup.find("div",'chapter-entity')
        # print(str(data))
        replacement = '\n'
        cleanText = BeautifulSoup(str(data).replace("<br/>", replacement),features="lxml")
        
        return cleanText.get_text()
      

#TESTING

#testing getChapterURLS

s = Scraper("https://www.wuxiaworld.co/Reincarnation-Of-The-Strongest-Sword-God/", "Reincarnation")
# dic = s.getChapterUrls()
# for line in dic:
#     print(line,":",dic[line])

#testing getChapterText 
url = " https://www.wuxiaworld.co/Reincarnation-Of-The-Strongest-Sword-God/1239956.html"
print(s.getChapterText(url))