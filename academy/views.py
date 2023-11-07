from django.shortcuts import get_object_or_404, render, redirect

from academy.form import PersonalTrainerForm
from academy.models import PersonalTrainer
from academy.form import CustomerForm
from academy.models import Customer

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
    result['personal_trainer_length'] = len(result['personal_trainers'])
    return render(request, 'academy/list_personal_trainer.html', result)


def updatePersonalTrainer(request, pk):
    data = {}
    personalTrainer = PersonalTrainer.objects.get(pk=pk)
    form = PersonalTrainerForm(request.POST or None, instance=personalTrainer)

    if (form.is_valid()):
        form.save()
        return redirect('list_personal')

    data['form'] = form

    return render(request, 'academy/personal_trainer_form.html', data)


def deletePersonalTreiner(request, pk):
    result = {}
    personal_trainer = get_object_or_404(PersonalTrainer, pk=pk)
    personal_trainer.delete()
    result['personal_trainers'] = PersonalTrainer.objects.all()
    result['personal_trainer_length'] = len(result['personal_trainers'])

    return redirect('list_personal')

def registerCustomer(request):
    data = {}
    form = CustomerForm(request.POST or None)

    if (form.is_valid()):
        form.save()
        return redirect('list_customer')

    data['form'] = form

    return render(request, 'academy/customer_form.html', data)

def listCustomer(request):
    result = {}
    result['customers'] = Customer.objects.all()
    result['customer_length'] = len(result['customers'])
    return render(request, 'academy/list_customer.html', result)

def updateCustomer(request, pk):
    data = {}
    customer = Customer.objects.get(pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)

    if (form.is_valid()):
        form.save()
        return redirect('list_customer')

    data['form'] = form

    return render(request, 'academy/customer_form.html', data)

def deleteCustomer(request, pk):
    result = {}
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    result['customers'] = Customer.objects.all()
    result['customer_length'] = len(result['customers'])

    return redirect('list_customer')