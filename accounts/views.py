from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

""""
1. if its POST, retrieves forms data and validates it.
  a. if its valid it saves it in DB
  b. if its not valid, renders signup.html with same form data
2. if its GET renders signup.html with a new form
"""


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.get_user())
            return redirect('tasks:list')  # redirects to the url named 'list' inside 'tasks' namespace
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        # sends the data to the DB in order to retrieve data matched with request data
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # retrieves the user from the valid form
            login(request, user)  # uses imported django built in login to log the user
            if 'next' in request.POST:  # if next value exists un the request method, redirect to that value.
                return redirect(request.POST.get('next'))
            else:
                return redirect('tasks:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('tasks:list')
