from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'title',
            'experience',
            'image_url',
            'relationship',
            'location',
            'stars',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter the title of the item',
                'class': 'form-control',
                'style': 'border-radius: 5px; padding: 10px;',
            }),
            'experience': forms.Textarea(attrs={
                'placeholder': 'Share your experience',
                'rows': 5,
                'class': 'form-control',
                'style': 'border-radius: 5px; padding: 10px;',
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Enter the image URL',
                'class': 'form-control',
                'style': 'border-radius: 5px; padding: 10px;',
            }),
            'relationship': forms.TextInput(attrs={
                'placeholder': 'Describe your association with the item',
                'class': 'form-control',
                'style': 'border-radius: 5px; padding: 10px;',
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Enter the location',
                'class': 'form-control',
                'style': 'border-radius: 5px; padding: 10px;',
            }),
            'stars': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'class': 'form-control',
                'style': 'border-radius: 5px; padding: 10px;',
            }),
        }
