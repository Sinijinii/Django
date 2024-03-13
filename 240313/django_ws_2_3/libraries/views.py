from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = 'ttbthdckddyd1231146001'
    params = {
        'ttbkey': API_KEY,
        'Version': '20131101',
        'MaxResults': 50,
        'start': 1,
        'output': 'js',
        'SearchTarget': 'Book',
        'QueryType': 'ItemNewSpecial'
    }
    response = requests.get(API_URL, params=params).json()
    data = response['item']
    aladin = []
    for i in range(50):
        aladin.append({"국제 표준 도서 번호": data[i]['isbn'],
                    "저자": data[i]['author'],
                    "제목": data[i]['title'],
                    '출간일': data[i]['pubDate']
                    })
    context = {
        'result' : aladin
    }
    return render(request,'recommend.html',context)