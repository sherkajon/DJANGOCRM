from django.http import HttpResponse
from django.shortcuts import render


def mainpage(request):
    return HttpResponse('Hello World')


def testpage(request):
    return HttpResponse('This is a test page!')




