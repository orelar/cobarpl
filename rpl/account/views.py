from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import response
from .forms import CreateUserForm

def registerPage(request):
	if request.user.is_authenticated:
		return hello(request)
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + username)
				return redirect('login')


		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return hello(request)
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return hello(request)
			else:
				messages.info(request, 'Incorrect Username or Password')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='/auth/login/')
def hello(request):
	msg = "Hello, " + request.user.username + "!"
	html = f'''
    <html>
        <body>
            <h1>{ msg }</h1>
			<h1>id: { request.user.id }</h1>
        </body>
    </html>
    '''
	return HttpResponse(html)