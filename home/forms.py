from django import forms
from home.models import Support


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
