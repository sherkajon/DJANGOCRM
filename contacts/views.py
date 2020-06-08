from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact


def mainpage(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts_page.html', {'contacts': contacts})


def testpage(request):
    return HttpResponse('This is a test page!')




