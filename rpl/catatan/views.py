from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import response
from .forms import CatatanForm
from .models import Catatan


def index(request):
    catatan = Catatan.objects.all()
    context = {'catatan': catatan}
    return render(request, 'list_catatan.html', context)

@login_required(login_url='/auth/login/')
def buatCatatan(request):
    form = CatatanForm()
    if request.method == 'POST':
        form = CatatanForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploader_id = request.user.id
            note.save()
            return redirect('notes')


    context = {'form':form}
    return render(request, 'buat_catatan.html', context)