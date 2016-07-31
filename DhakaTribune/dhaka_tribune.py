from bs4 import BeautifulSoup
import urllib2

# Constants
base_url = 'http://www.dhakatribune.com/'

# Scrapper credentials
header = 'User-agent'
browser = 'Mozilla/5.0'

# Fix unicode error
def decode(input):
    return input.encode('ascii', 'ignore')

class DhakaTribune:
    def __init__(self):
        self.request = None
        self.response = None
        self.dhakatribune_soup = None
        self.tag = ''
        self.request_url = ''

    def news_request(self, tag):
        self.tag = tag
        self.news_url = self.make_taglink()
        print self.news_url
        self.request = urllib2.Request(self.news_url)
        self.request.add_header(header, browser)
        self.response = urllib2.urlopen(self.request)
        self.dhakatribune_soup = BeautifulSoup(self.response, 'lxml')
        news_title = self.dhakatribune_soup.findAll('h2', {"class": "entry-title"})
        for title in news_title:
            s = BeautifulSoup(str(title), 'lxml')
            print decode(s.a.string)
            print decode(s.a['href'])

    def make_taglink(self):
        return 'http://www.dhakatribune.com/tags/' + self.tag

    # Fix unicode error
    def decode(self, input):
        return input.encode('ascii', 'ignore')
