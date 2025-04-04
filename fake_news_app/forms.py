from django import forms
from .models import ContactMessage
class NewsForm(forms.Form):
    news_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter news text here...', 'rows': 5}))



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]