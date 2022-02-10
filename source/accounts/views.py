from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.user.is_authenticated:
        return redirect('To_Do_list:index')
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('To_Do_list:index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


