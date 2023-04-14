from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '' #'<span class="form-text text-muted small">Required. 150 charectors or fewer. Letters, digits and @/./+/-/_ only. </span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '' #'<ul class="form-text text-muted small"><li>Your Password can`t be too similer to other information. </li><li>your password must contain at least 8 charactors.</li><li>Your password can`t be a commonly used password.</li><li>Your password can`t be entirely numeric.</li> </ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '' #'<span class="form-text text-muted small">Enter the same password as before, for verification.</span>' 


class AddRecordForm(forms.ModelForm):
        first_name = forms.CharField(label='', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
        last_name = forms.CharField(label='', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
        email = forms.CharField(label='', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email ID'}))
        phone = forms.CharField(label='', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}))
        address = forms.CharField(label='', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))
        city = forms.CharField(label='', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}))
        state = forms.CharField(label='', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}))
        zipcode = forms.CharField(label='', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}))

        class Meta:
             model = Record
             exclude = ("user",)


