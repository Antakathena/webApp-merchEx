from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    context ={
        "bands": bands
    }
    print(bands[0].name)
    return render(request, "hello.html", context)

    return HttpResponse(f"""
    <h1> Hello Django!</h1>
    <p>Mes groupes sont :</p>
    <ul>
        <li>{bands[0].name}</li>

    </ul>
    """)
    template = get_template("hello.html")
    page = template.render({"exemple": "coucou ! depuis views.py", "bands": bands})

    return HttpResponse(page)


def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons échanger !</p>')

def listing(request):
    return HttpResponse('vue pour lister les offres')

def contact(request):
    date = datetime.today()
    return render(request, "contact.html",  )
    # return HttpResponse('vue où placer le formulaire de contact')