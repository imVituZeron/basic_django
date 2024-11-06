from django.shortcuts import render

def index(req):
    # it fetch into the app's template folder 
    return render(
        req,
        'blog/index.html'
    )

def example(req):
    return render(
        req,
        'blog/example.html'
    )

