from django.shortcuts import render

def index(req) :
    print('home')

    return render(
        req,
        'home/index.html'
    )