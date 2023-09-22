from app.models import *
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}



class ProfileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['address','profile_pic']