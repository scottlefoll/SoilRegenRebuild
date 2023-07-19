from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from .models import Farm
import requests
import pandas as pd


class AddFarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm_name', 'street_address', 'town', 'state', 'zip']
        labels = {
            'Farm name': 'Name',
            'Street address': 'Street Address',
            'Town': 'Town',
            'State': 'State',
            'Zip': 'Zip'
        }
        widgets = {
            'farm_name': forms.TextInput(attrs={'required': True}),
            'street_address': forms.TextInput(attrs={'required': True}),
            'town': forms.TextInput(attrs={'required': True}),
            'state': forms.TextInput(attrs={'required': True}),
            'zip': forms.TextInput(attrs={'required': True})
        }


class DeleteFarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = []
        widgets = {'id': forms.HiddenInput()}
