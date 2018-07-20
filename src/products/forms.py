from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Введіть назву допису"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 15, "cols": 75, "placeholder": "Введіть текст допису"}))
	price = forms.DecimalField(initial=199.99)
	summary = forms.CharField()
	class Meta:
		model = Product
		fields = ['title', 'description', 'price', 'summary']

class RawProductForm(forms.Form):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Введіть назву допису"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 15, "cols": 75, "placeholder": "Введіть текст допису"}))
	price = forms.DecimalField(initial=199.99)
	summary = forms.CharField()