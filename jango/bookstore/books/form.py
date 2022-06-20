from django import forms
from models import Review

class ReviewForm(forms.ModelForm):
    
    body = forms.CharField(widget=forms.Textarea(attrs={'cars':'border rounded p-2 w-full',
                                                        'placeholder':'write your review here'}))
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Review
        fields = ['body', ['image']]
        # widgets = {'body' :forms.Textarea(
        #     attrs={'cars':'border rounded p-2 w-full', 'placeholder':'write your review here'} 
        #     )}
    