from django import forms
from django.db.models import fields
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'list_bab']
        exclude = ('list_bab', 'course_id')

    course_name = forms.CharField(label="Course", required=True, widget=forms.Textarea(attrs = {'placeholder': 'Course'}))

class SearchCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'list_bab']
        exclude = ('list_bab', 'course_id')
    course_name = forms.CharField(label="Course", required=True, widget=forms.Textarea(attrs = {'placeholder': 'Course'}))