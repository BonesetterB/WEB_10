from django.urls import path
from . import views

app_name='Quotes'

urlpatterns = [
    path('Quotes/',views.index, name='Home'),
    path('author/<str:author_name>/', views.authores, name='author'),
    path('Author/create/', views.CreateAuthorView.as_view(), name='create_author'),
    path('Quote/create/', views.CreateQuoteView.as_view(), name='create_Quote'),

    
]