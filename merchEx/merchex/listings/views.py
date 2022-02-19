from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def hello(request):
    template = get_template("index.html")
    page = template.render({"exemple": "coucou ! depuis views.py"})
    return HttpResponse(page)
    # return HttpResponse('<h1>Hello Django!<h1!>')

# fonction; injecter = {{}}; 

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons échanger !</p>')

def listing(request):
    return HttpResponse('vue pour lister les offres')

def contact(request):
    return HttpResponse('vue où placer le formulaire de contact')