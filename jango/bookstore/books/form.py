from logging import PlaceHolder
from django import forms

class ReviewForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={'cars':'border rounded p-2 w-full',
                                                        'placeholder':'write your review here'}))
    image = forms.ImageField(required=False)