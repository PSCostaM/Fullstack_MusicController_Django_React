from django.shortcuts import render
from django.http import HttpResponse

# create the endpoints

def main(request):
    return HttpResponse("<h1>Music Controller</h1>")
    