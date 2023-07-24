import os
import django

from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE","quote.settings")
django.setup()

from Quotes.models import author, Quote, Tag

client=MongoClient(f"mongodb+srv://CityNine:60604@croaker.hbarqcq.mongodb.net/?retryWrites=true&w=majority")

db=client.HMW_09

authors=db.author.find()

for auto in authors:
    author.objects.get_or_create(
        fullname=auto['fullname'],
        born_date=auto['born_date'],
        born_location=auto['born_location'],
        description=auto['description']
    )

quots=db.quotes.find()

for quot in quots:
    tags=[]
    for tag in quot['tags']:
        t,*_=Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote=bool(len(Quote.objects.filter(quote=quot['quote'])))

    if not exist_quote:
        auth=db.author.find_one({'_id':quot['author'][0]})
        a=author.objects.get(fullname=auth['fullname'])
        q=Quote.objects.create(
            quote=quot['quote'],
            author=a
        )
        for tag in tags:
            q.tags.add(tag)

    

