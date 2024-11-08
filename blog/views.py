from django.shortcuts import render

def index(req):
    context:dict = {
        'text': "hi blog",
        'title': "Blog"
    }
    # it fetch into the app's template folder 
    return render(
        req,
        'blog/index.html',
        context
    )

def example(req):
    context:dict = {
        'text': "hi example",
        'title': "Example"
    }

    return render(
        req,
        'blog/example.html',
        context
    )

