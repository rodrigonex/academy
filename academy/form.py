from django.forms import ModelForm

from academy.models import PersonalTrainer


class PersonalTrainerForm(ModelForm):
    class Meta:
        model = PersonalTrainer
        fields = ['name', 'specialization',
                  'experience', 'registration_number']
