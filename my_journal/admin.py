from django.contrib import admin
from .models import Journal, Thought

# Register your models here.
admin.site.register(Journal)
admin.site.register(Thought)