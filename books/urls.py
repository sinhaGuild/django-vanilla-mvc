from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('authors/<int:author_id>/', views.authors, name='authors'),
    path('publishers/<int:publisher_id>/', views.publishers, name='publishers'),
]
