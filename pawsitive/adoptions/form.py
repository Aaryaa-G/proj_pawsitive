from django import forms
from .models import Donation, Adoption, Volunteer

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = '__all__'

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
