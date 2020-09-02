from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, ContactForm


def main(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:main')
        else:
            raise ValidationError('Form is not valid.')
    else:
        form = RegistrationForm()

    context = {'registration_form': form}
    return render(request, 'main/index.html', context)


def teachers(request):
    return render(request, 'main/teachers.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:main')
        else:
            raise ValidationError('Form is not valid.')
    else:
        form = ContactForm()

    context = {'contact_form': form}
    return render(request, 'main/contact.html', context)


def about(request):
    return render(request, 'main/about.html')
