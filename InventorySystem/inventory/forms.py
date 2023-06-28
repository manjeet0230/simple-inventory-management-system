from django import forms
from .models import Product

class productdetailform(forms.ModelForm):
    Description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}))
    class Meta:
        model=Product
        fields=['Name','Description','Quantity','Price']

        widgets={
            'Name':forms.TextInput(attrs={'class':'form control','placeholder':'Enter the product name'}),
            'Quantity':forms.NumberInput(attrs={'class':'form control','placeholder':'Enter quantity'}),
            'Price':forms.NumberInput(attrs={'class':'form control','placeholder':'Enter price'})
        }
