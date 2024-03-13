from django.shortcuts import render

# Create your views here.
def introduce(request,username):
    context = {
        'name':username
    }
    return render(request, 'articles/introduce.html',context)