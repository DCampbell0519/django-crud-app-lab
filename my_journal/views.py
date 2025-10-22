from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Journal, Thought
from .forms import ThoughtForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def home(request):
#     return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('journal-index')
        else:
            error_message = 'Invalid sign up - Please try again.'
    form = CustomUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class Home(LoginView):
    template_name = 'home.html'

@login_required
def journal_index(request):
    journal_entries = Journal.objects.filter(user=request.user)
    return render(request, 'my_journal/index.html', { 'journal_entries': journal_entries })

@login_required
def journal_detail(request, journal_id):
    journal_entry = Journal.objects.get(id=journal_id)
    thought_form = ThoughtForm()
    return render(request, 'my_journal/detail.html', { 'journal_entry': journal_entry, 'thought_form': thought_form })

@login_required
def add_thought(request, journal_id):
    form = ThoughtForm(request.POST)
    if form.is_valid():
        new_thought = form.save(commit=False)
        new_thought.journal_id = journal_id
        new_thought.save()
    return redirect('journal-detail', journal_id=journal_id)

class ThoughtUpdate(LoginRequiredMixin, UpdateView):
    model = Thought
    fields = ['thought']
    # success_url = '/journal/'
    def get_success_url(self):
        journal = self.object.journal
        return reverse('journal-detail', kwargs={'journal_id': journal.id})

class ThoughtDelete(LoginRequiredMixin, DeleteView):
    model = Thought
    # success_url = '/journal/'
    def get_success_url(self):
        journal = self.object.journal
        return reverse('journal-detail', kwargs={'journal_id': journal.id})

class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    fields = ['title', 'entry']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JournalUpdate(LoginRequiredMixin, UpdateView):
    model = Journal
    fields = ['title', 'entry']

class JournalDelete(LoginRequiredMixin, DeleteView):
    model = Journal
    success_url = '/journal/'

