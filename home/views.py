from django.shortcuts import render

def index(req) :
    print('home')

    # it fetch into the app's template folder 
    return render(
        req,
        'home/index.html'
    )