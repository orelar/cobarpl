from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import response
from .forms import CourseForm, BabForm
from .models import Course, Bab
# from .filters import *
from django.contrib.auth.models import User

from django.urls import reverse

def index(request, courid):
    courses = Course.objects.filter(course_id=courid)
    context = {'courses': courses}
    return render(request, 'list_course.html', context)


def search_all_course(request):
    course_name = request.GET.get('course_name')

    if course_name is not None:
        nama_course_dicari = Course.objects.filter(course_name__startswith=course_name)
        if not nama_course_dicari and course_name.isnumeric():
            nama_course_dicari = Course.objects.filter(course_id=course_name)
    else:
        nama_course_dicari = Course.objects.all()

    context = {'nama_course_dicari': nama_course_dicari}
    return render(request, 'search_course.html', context)


def search_all_bab(request, course_id):
    # form = SearchCourseForm(request.POST)
    nama_course_dicari = Bab.objects.filter(course_id=course_id)
    context = {'nama_bab_dicari': nama_course_dicari}
    return render(request, 'search_bab.html', context)


@login_required(login_url='/auth/login/')
def create_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            user_id = User.objects.get(id=request.user.id)
            course.user_id = user_id
            course.save()
            return HttpResponseRedirect(reverse('search-all-course'))

    context = {'form':form}
    return render(request, 'create_course.html', context)


@login_required(login_url='/auth/login/')
def create_bab(request, course_id):
    form = BabForm()
    if request.method == 'POST':
        form = BabForm(request.POST)
        if form.is_valid():
            bab = form.save(commit=False)
            bab.course_id = course_id
            bab.save()
            return HttpResponseRedirect(reverse('search-all-bab', args=(bab.course_id,)))

    context = {'form':form}
    return render(request, 'create_bab.html', context)

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
