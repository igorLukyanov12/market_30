from django.shortcuts import render

from .PerForms import PersonForm
from .models import Person


def index(request):
    form = PersonForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {
                'form': form
            }
            return render(request, 'index2.html', context)
    return render(request, 'index2.html', context)

def new_person_form(request):
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, 'index2.html', context)
