from django import forms
from recipes.models import Author


class AddAuthorForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(
        max_length=30, widget=forms.PasswordInput)
    author_name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class StaffAddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)


class UserAddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
