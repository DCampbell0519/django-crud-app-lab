from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to Jazzy Journal!</h1>')

def journal_index(request):
    return HttpResponse('<h1>And here lies all of your Journal Entries</h1>')