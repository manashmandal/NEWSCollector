# _*_ coding:utf-8 _*_
from DhakaTribune.dhaka_tribune import DhakaTribune

news_link = 'http://www.dhakatribune.com/tags/Garments'


if __name__ == '__main__':
    dt = DhakaTribune()
    dt.news_request('Garments')
