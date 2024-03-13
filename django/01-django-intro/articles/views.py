from django.shortcuts import render
from random import random
# Create your views here.
# 메인 페이지를 만드는 index라는 이름의 함수를 작성
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
