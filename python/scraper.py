from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests 

#also need a way to get the name of the novel here
class Scraper: 
    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.namenum = None
        self.nametext = None

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
            if (text != None):
                i += 1
                #and the base url
                baseurl = "https://www.wuxiaworld.co"
                print(baseurl + text)
                chapterlist[i]= baseurl + text
                
        return chapterlist

    # METHOD NAME:
    # DESCRIPTION
    #PARAMETERS
    # RETURN TYPE
    def getChapterText(self, url):

        r = requests.get(url)
        page_source = r.text

        #get the div with the text
        soup = BeautifulSoup(page_source, 'html.parser')
        data = soup.find("div",'chapter-entity')
        
        #replace all <br> tags in the div with '\n'
        replacement = '\n'
        cleanText = BeautifulSoup(str(data).replace("<br/>", replacement),features="lxml")
        
        #return the string of the clean version
        return cleanText.get_text()
    
    #this function should create two dictionaries 
    def createDictionaries(self):
        #name-url dic 
        numurl = self.getChapterUrls()
        
        for num in numurl:
            print(num,":", numurl[num])
        #name-num dic
        namenum = {}
        
        #name-text dic
        nametext = {}

        for num in numurl:
            print(num,":", numurl[num])
            #stuff for name-num
            name = self.getName(numurl[num])
            namenum[name] = num
            #stuff for name-text
            text = self.getChapterText(numurl[num])
            nametext[name] = text

        #update global dictionaries 
        self.nametext = nametext
        self.namenum = namenum

    def getName(self, url):
        r = requests.get(url)
        page_source = r.text

        #get the div with the text
        soup = BeautifulSoup(page_source, 'html.parser')
        data = soup.find("h1", "chapter-title")
        chaptername = data.get_text()
        
        #split the number from the name -- also we will use our own internal documentation of chapter numbers to avoid inconsistency
        i = 0
        for char in chaptername:
            if char.isalpha():
                break
            i += 1
        chaptername = chaptername[i:]
        #return with whitespace stripped
        return chaptername.strip()
    
    def getNameNum(self):
        return self.namenum

    def getNameText(self):
        return self.nametext

#TESTING

#testing getChapterURLS

s = Scraper("https://www.wuxiaworld.co/Mark-of-London/", "Mark of London")
# dic = s.getChapterUrls()
# for line in dic:
#     print(line,":",dic[line])

#testing getChapterText 
# url = " https://www.wuxiaworld.co/Reincarnation-Of-The-Strongest-Sword-God/1239956.html"
# print(s.getChapterText(url))

#testing dictionary creation
# url = " https://www.wuxiaworld.co/Reincarnation-Of-The-Strongest-Sword-God/1239956.html"
s.createDictionaries()
d = s.getNameText()
x = s.getNameNum()
for t in d:
    print(t,":",d[t])
for t in x:
    print(t,":",x[t])
