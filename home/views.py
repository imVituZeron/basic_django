from django.shortcuts import render

def index(req) :
    print('home')

    context:dict = {
        'text': "haha agora sim posso ver algo!",
        'title': "Home"
    }

    # it fetch into the app's template folder 
    return render(
        req,
        'home/index.html',
        context
    )