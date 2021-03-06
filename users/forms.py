from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import SideChallenge, Statement_1, Statement_2, Statement_3

class UserRegisterForm(UserCreationForm):
    # Write down all the additional inputs we want for the form
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    email = forms.EmailField()  # default: required = True

    class Meta:
        model = User    # The model that would be affected is the User model
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']    # The fields that we want in the form and in what order

class MasterForm(forms.Form):
    # (value, label) pair
    CHOICES = [
    ('1', 'Challenge Statement 1'),
    ('2', 'Challenge Statement 2'),
    ('3', 'Challenge Statement 3'),
    ('4', 'Side Challenge'),
    ]

    statement = forms.CharField(label='Which Challenge Statement do You Want to Submit', widget=forms.RadioSelect(choices=CHOICES))
        


class Form1(forms.ModelForm):
    class Meta:
        model = Statement_1
        fields = ['img', 'raw']

class Form2(forms.ModelForm):
    class Meta:
        model = Statement_2
        fields = ['img', 'raw']

class Form3(forms.ModelForm):
    class Meta:
        model = Statement_3
        fields = ['img', 'raw']

class Form4(forms.ModelForm):
    class Meta:
        model = SideChallenge
        fields = ['img', 'raw']