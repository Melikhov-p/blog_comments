from django import forms
from .models import Comment

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'class':'form-control'}))

class CommentForm(forms.Form):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control'}))