from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import todo_items


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'you@example.com'})
    )

    class Meta:
        model = UserCreationForm.Meta.model
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'input-field', 'placeholder': 'Choose a username', 'autofocus': True
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'input-field', 'placeholder': 'Create a password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'input-field', 'placeholder': 'Confirm password'
        })


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'input-field', 'placeholder': 'Username', 'autofocus': True
        })
        self.fields['password'].widget.attrs.update({
            'class': 'input-field', 'placeholder': 'Password'
        })


class Create_todo(forms.ModelForm):
    class Meta:
        model = todo_items
        fields = ["title", "desc", "time", "urgency"]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Title'}),
            "desc": forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Description', 'rows': 3}),
            "time": forms.DateInput(attrs={'class': 'input-field', 'type': 'date'}),
            "urgency": forms.NumberInput(attrs={'class': 'input-field', 'min': 1, 'max': 5}),
        }
