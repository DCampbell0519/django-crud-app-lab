from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Journal

# Create your views here.
def home(request):
    return render(request, 'home.html')

def journal_index(request):
    journal_entries = Journal.objects.all()
    return render(request, 'my_journal/index.html', { 'journal_entries': journal_entries })

def journal_detail(request, journal_id):
    journal_entry = Journal.objects.get(id=journal_id)
    # thought_form = ThoughtForm()
    return render(request, 'my_journal/detail.html', { 'journal_entry': journal_entry })

class JournalCreate(CreateView):
    model = Journal
    fields = ['title', 'entry']
    # success_url = '/journal/'

class JournalUpdate(UpdateView):
    model = Journal
    fields = ['title', 'entry']

class JournalDelete(DeleteView):
    model = Journal
    success_url = '/journal/'