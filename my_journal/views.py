from django.shortcuts import render
from django.http import HttpResponse
from .models import Journal

# Create your views here.
def home(request):
    return render(request, 'home.html')

def journal_index(request):
    journal_entries = Journal.objects.all()
    return render(request, 'journal/index.html', { 'journal_entries': journal_entries })

def journal_detail(request):
    return HttpResponse('<h1>And here is the specific journal entry you clicked on</h1>')