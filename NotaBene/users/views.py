from django.shortcuts import render
from django.http import HttpResponse


def doIndex(request):
    return HttpResponse('Hello World')

def doTest(request):
    return HttpResponse('<p>Тестовая страница</p>')