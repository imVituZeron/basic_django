from django.shortcuts import render

def index(req):
    return render(
        req,
        'blog/index.html'
    )

def example(req):
    return render(
        req,
        'blog/example.html'
    )

