from django.shortcuts import render
from .utils import get_base
# Create your views here.
def index(request):
    db=get_base()
    quotes=db.quotes.find()
    return render(request,'Quotes/quotes.html', context={'quotes':quotes})

def quote(request):
    return render(request,'Quotes/quote.html')

def Authors(request):
    return render(request,'Quotes/Authors.html')

def Author(request):
    return render(request,'Quotes/Author.html')
