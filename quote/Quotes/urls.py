from django.urls import path
from . import views

app_name='Quotes'

urlpatterns = [
    path('',views.index, name='Home'),
    path('quote/',views.quote, name='quote'),
    path('Authors/',views.Authors, name='Authors'),
    path('Author/',views.Author, name='Author'),
]