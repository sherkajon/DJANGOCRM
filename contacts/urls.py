from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainpage, name="home"),
    path('testpage', views.testpage),
    path('createcontact', views.createContact, name="createContact"),
    path('updatecontact/<int:id>', views.updateContact, name="updateContact")
]