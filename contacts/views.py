from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm


def mainpage(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts_page.html', {'contacts': contacts})


def testpage(request):
    return HttpResponse('This is a test page!')


def createContact(request):
    form = ContactForm()
    if request.method == 'POST':
        #print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contacts')


    context = {'form':form}
    return render(request, 'contacts_form.html', context)


def updateContact(request, id):

    contact = Contact.objects.get(id=id)
    form = ContactForm(instance=contact)


    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/contacts')


    context = {'form': form}
    return render(request, 'contacts_form.html', context)