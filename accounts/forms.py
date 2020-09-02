from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Contact
from string import digits


class RegistrationForm(UserCreationForm):
    mobile = forms.CharField(max_length=13, label='',
                             widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))

    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'First Name'}))

    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(label='',
                            widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    password1 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'mobile', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def clean(self):
        username = self.cleaned_data['username']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        mobile = self.cleaned_data['mobile']
        if '+' not in mobile or len(mobile) <= 0:
            raise forms.ValidationError('Please, fill your mobile number correctly.')
        return self.cleaned_data


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))

    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    text = forms.CharField(label='',
                           widget=forms.Textarea(attrs={'placeholder': 'Give us more details...'}))
    phone = forms.CharField(max_length=13, label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Your Phone'}))
    email = forms.CharField(label='',
                            widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'text']

    def save(self, commit=True):
        user = super(ContactForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.text = self.cleaned_data['text']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user

    def clean(self):
        phone = self.cleaned_data['phone']
        if '+' not in phone or len(phone) <= 0:
            raise forms.ValidationError('Please, fill your mobile number correctly.')
        return self.cleaned_data
