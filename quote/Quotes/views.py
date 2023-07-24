from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Quotes/quotes.html')

def quote(request):
    return render(request,'Quotes/quote.html')

def Authors(request):
    return render(request,'Quotes/Authors.html')

def Author(request):
    return render(request,'Quotes/Author.html')
