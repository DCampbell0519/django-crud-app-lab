from django.shortcuts import render
from django.http import HttpResponse
from .models import Journal

# Create your views here.
def home(request):
    return render(request, 'home.html')

def journal_index(request):
    journal_entries = Journal.objects.all()
    return render(request, 'journal/index.html', { 'journal_entries': journal_entries })

def journal_detail(request, journal_id):
    journal_entry = Journal.objects.get(id=journal_id)
    return render(request, 'journal/detail.html', { 'journal_entry': journal_entry })