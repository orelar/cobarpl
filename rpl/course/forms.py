from django import forms
from django.db.models import fields
from .models import Course, Bab


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']
        exclude = ()

    course_name = forms.CharField(label="Course", required=True, widget=forms.Textarea(attrs = {'placeholder': 'Course'}))


class BabForm(forms.ModelForm):
    class Meta:
        model = Bab
        fields = ['bab_name']
        exclude = ('bab_id',)

    bab_name = forms.CharField(label="Bab", required=True, widget=forms.Textarea(attrs = {'placeholder': 'Bab'}))
