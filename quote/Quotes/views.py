from django.shortcuts import render, get_object_or_404
from .models import Quote,author,Tag
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    quotes = Quote.objects.all()
    return render(request,'Quotes/quotes.html', context={'quotes':quotes})

def authores(request,author_name):
    author_instance = get_object_or_404(author, fullname=author_name)
    return render(request,'Quotes/Author.html',context={'author': author_instance})


class CreateAuthorView(LoginRequiredMixin, View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'Quotes/cret_athor.html')

    def post(self, request):
        fullname = request.POST.get('fullname')
        born_date = request.POST.get('born_date')
        born_location = request.POST.get('born_location')
        description = request.POST.get('description')

        authore = author.objects.create(
            fullname=fullname,
            born_date=born_date,
            born_location=born_location,
            description=description
        )

        return render(request, 'Quotes/cret_athor.html', context={'author': authore})
    


class CreateQuoteView(LoginRequiredMixin, View):
    @method_decorator(login_required)
    def get(self, request):
        authors = author.objects.all()

        tags = Tag.objects.all()
        return render(request, 'Quotes/cret_quote.html', context={'authors': authors, 'tags': tags})


    def post(self, request):
        quote = request.POST.get('quote')
        authosr = request.POST.get('author')
        tags = request.POST.getlist('tags')


        authore = author.objects.get(id=authosr)

        tags = Tag.objects.filter(id__in=tags)

        quote = Quote.objects.create(
            quote=quote,
            author=authore,
        )

        quote.tags.set(tags) 

        return render(request, 'Quotes/quotes.html', context={'quote': quote})
