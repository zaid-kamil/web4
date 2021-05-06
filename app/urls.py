from django.urls import path
from .views import contactview # a function in views]
from .views import add_publisher_view, show_publishers,homeview,search_publishers

urlpatterns = [
    path('',homeview,name='home'),
    path('contact/',contactview,name='contact'),
    path('addpublisher/',add_publisher_view,name='addpub'),
    path('viewpublisher/',show_publishers,name='viewpub'),
    path('searchpublisher/',search_publishers,name='searchpub'),
]