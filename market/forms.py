from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django import forms
from .models import Product


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        return user


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name'
        ]