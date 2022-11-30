from django import forms
from django.db.models import fields
from .models import Catatan

class CatatanForm(forms.ModelForm):
    class Meta:
        model = Catatan
        fields = ['uploader_id', 'title']
        exclude = ('uploader_id',)

    title = forms.CharField(label="Title", required=True, max_length = 100, widget=forms.Textarea(attrs = {'placeholder': 'Title'}))