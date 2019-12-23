from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


from .models import Vacancie



def index(request):
    vacancies = Vacancie.objects.all()
    template_name = 'vacancies/index.html'
    context = {
        'vacancies': vacancies
    }
    return render(request, template_name, context)

def details(request, slug):
    vacancie = get_object_or_404(Vacancie, slug=slug)
    context = {
        'vacancie': vacancie
    }
    template_name = 'vacancie/details.html'
    return render(request, template_name, context)