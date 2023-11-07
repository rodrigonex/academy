from django.forms import ModelForm

from academy.models import PersonalTrainer
from academy.models import Customer



class PersonalTrainerForm(ModelForm):
    class Meta:
        model = PersonalTrainer
        fields = ['name', 'specialization',
                  'experience', 'registration_number']
        
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'age',
                  'sex', 'address' ,'phone_number']


