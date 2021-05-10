from django.urls import path
from .views import contactview # a function in views]
from .views import add_publisher_view, show_publishers,homeview,search_publishers,delete_publisher,edit_publisher

urlpatterns = [
    path('',homeview,name='home'),
    path('contact/',contactview,name='contact'),
    path('addpublisher/',add_publisher_view,name='addpub'),
    path('viewpublisher/',show_publishers,name='viewpub'),
    path('searchpublisher/',search_publishers,name='searchpub'),
    path('deletepublisher/<int:pk>',delete_publisher,name='deletepub'),
    path('editpublisher/<int:pk>',edit_publisher,name='editpub'),
]