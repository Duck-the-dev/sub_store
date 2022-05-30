from django import forms
from django.contrib import auth

from home.models import Support, Order


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['colors'].label = ""
        self.fields['first_name'].label = ""
        self.fields['last_name'].label = ""
        self.fields['email'].label = ""
        self.fields['address'].label = ""
        self.fields['address2'].label = ""
        self.fields['state'].label = ""
        self.fields['user'].label = ""

    class Meta:
        model = Order
        fields = ('colors', 'first_name', 'last_name', 'email', 'address', 'address2', 'state', 'user')

        widgets = {
            'colors': forms.Select(attrs={'class': 'form-control', }),
            'first_name': forms.TextInput(attrs={'class': 'form-control', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', }),
            'email': forms.TextInput(attrs={'class': 'form-control', }),
            'address': forms.TextInput(attrs={'class': 'form-control', }),
            'address2': forms.TextInput(attrs={'class': 'form-control', }),
            'state': forms.Select(attrs={'class': 'form-control', }),
            'user': forms.HiddenInput(),
        }


class SupportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SupportForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ""
        self.fields['email'].label = ""
        self.fields['body'].label = ""

    class Meta:
        model = Support
        fields = ('title', 'email', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', }),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your support ticket', }),
        }
