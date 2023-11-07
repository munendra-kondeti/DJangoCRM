from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
class SignupForm(forms.ModelForm):
    user_name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'User Name'}));
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email address'}));
    first_name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First name'}));
    last_name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last name'}));
    password = forms.CharField(label='',max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}));
    confirm_password = forms.CharField(label='',max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}));
    
    class Meta:
        model = User;
        fields = ('user_name','first_name','last_name','email');
        
    def __init_(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs);
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].label = ''
        self.fields['password'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# create the add form
class AddForm(forms.ModelForm):
    first_name = forms.CharField(label='', required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'First Name'}));
    last_name = forms.CharField(label='', required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}));
    email = forms.EmailField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Email'}));
    phone_number = forms.CharField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}));
    address = forms.CharField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'address'}));
    city = forms.CharField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'city'}));
    state = forms.CharField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'state'}));
    zip_code = forms.CharField(label='',required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'zip_code'}));
    
    class Meta:
        model = Record
        exclude = ('user',)