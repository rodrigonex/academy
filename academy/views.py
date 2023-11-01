from django.shortcuts import render, redirect

from academy.form import PersonalTrainerForm
from academy.models import PersonalTrainer

# Create your views here.


def home(request):
    return render(request, 'academy/home.html')


def registerPersonalTrainer(request):
    data = {}
    form = PersonalTrainerForm(request.POST or None)

    if (form.is_valid()):
        form.save()
        return redirect('list_personal')

    data['form'] = form

    return render(request, 'academy/personal_trainer_form.html', data)


def listPersonalTrainer(request):
    result = {}
    result['personal_trainers'] = PersonalTrainer.objects.all()

    return render(request, 'academy/list_personal_trainer.html', result)
