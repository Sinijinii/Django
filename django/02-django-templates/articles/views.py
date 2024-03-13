# import random
from django.shortcuts import render
import random

def index(request):
    # 왜요??
    # render 함수가 그렇게 만들어져 있습니다.
    # render(요청객체, 템플릿경로)
    context= {
        'name':'SINIJINI'
    }
    return render(request,'articles/index.html',context)

def dinner(request):
    foods = [
        '김밥',
        '국수',
        '고기',
        '회',
        '마라탕',
        '육회'
    ]
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked
    }
    return render(request,'articles/dinner.html',context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # throw 페이지에서 데이터를 받고 그 안에서 사용자 입력 데이터를 추출
    # 템플릿에 그대로 출력
    print(request) #<WSGIRequest: GET '/catch/'>
    print(type(request)) # <class 'django.core.handlers.wsgi.WSGIRequest'>
    print(dir(request)) # ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__',....]
    print(request.GET) # <QueryDict: {}>
    print(request.GET.get('message')) # <QueryDict: {'message': ['신희진']} > <input type="text" name='message'>
    message = request.GET.get('message')
    context={"message":message}
    return render(request, 'articles/catch.html',context)

def greeting(request,name):
    context = {
        'name': name
    }
    return render(request, 'articles/greeting.html',context)