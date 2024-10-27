from django.shortcuts import render, redirect
from .models import Donation, Adoption, Volunteer
from .form import DonationForm, AdoptionForm, VolunteerForm

def donate_form_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = DonationForm()
    return render(request, 'adoptions/donation_form.html', {'form': form})

def adopt_form_view(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AdoptionForm()
    return render(request, 'adoptions/adopt_form.html', {'form': form})

def volunteer_form_view(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VolunteerForm()
    return render(request, 'adoptions/volunteer_form.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def home_view(request):
    return render(request, 'adoptions/home.html')

def about_view(request):
    return render(request, 'adoptions/about-us.html')

def donate_view(request):
    return render(request, 'adoptions/donate.html')

def volunteer_view(request):
    return render(request, 'adoptions/volunteer.html')

def adopt_view(request):
    return render(request, 'adoptions/adopt.html')
