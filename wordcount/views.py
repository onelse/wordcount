from django.shortcuts import render
from collections import Counter
from threading import Thread
from urllib.request import urlopen, Request
import urllib
import bs4
from bs4 import BeautifulSoup

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    loc = urllib.parse.quote(text + '+날씨')
    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ loc
    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html.parser')
    ondo = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
    dust = soup.find('div', class_='detail_box').find('span', class_='num').text
    return render(request, 'result.html', {'fulltext': text, 'ondo': ondo, 'dust' : dust })

# def result(request):
#         full_text = request.GET['fulltext']
    
#         word_list = full_text.split()
    
#         word_dictionary = {}
    
#         for word in word_list:
#             if word in word_dictionary:
#                 # Increase
#                 word_dictionary[word] += 1
#             else:
#                 # add to the dictionary
#                 word_dictionary[word] = 1
    
#         return render(request, 'result.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})

