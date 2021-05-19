from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    return HttpResponse("hello, this is main page")
# Create your views here.
