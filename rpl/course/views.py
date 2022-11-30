from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import response
from .forms import CourseForm, SearchCourseForm
from .models import Course
# from .filters import *

from django.urls import reverse

def index(request, courid):
    courses = Course.objects.filter(course_id=courid)

    # searchCourse = SearchCourseName(request.GET, queryset=courses)
    # searchCourse = SearchCourseName(request.GET, queryset=courses)
    # course = searchCourse.qs
    # context = {'courses': courses, 'search_course':searchCourse}
    context = {'courses': courses}
    return render(request, 'list_course.html', context)

def search_course(request, namacourse):
    form = SearchCourseForm(request.POST)
    nama_course_dicari = Course.objects.filter(namacourse__startswith=namacourse)
    context = {'nama_course_dicari': nama_course_dicari}
    return render(request, 'search_course.html', context)


@login_required(login_url='/auth/login/')
def create_course(request, courid):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            # course.user_id = request.user.id
            course.course_id = courid
            course.save()
            return HttpResponseRedirect(reverse('courses', args=(courid,)))

    context = {'form':form}
    return render(request, 'create_course.html', context)

# @login_required(login_url='/auth/login/')
# def create_bab(request, course_id):
#     form = CourseForm()
#     if request.method == 'POST':
#         form = CourseForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.reviewer_id = request.user.id
#             review.catatan_id = course_id
#             review.save()
#             return HttpResponseRedirect(reverse('course', args=(course_id,)))

#     context = {'form':form}
#     return render(request, 'create_course.html', context)
