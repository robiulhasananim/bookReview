from django.urls import path
from book import views
urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('book/new/', views.book_create, name='book-create'),
    
]