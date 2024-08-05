from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

def index(request):
    info = {}
    if request.method == 'POST':
        login = request.POST.get('login')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        age = request.POST.get('age')

        if password1 == password2 and int(age) >= 18:
            return HttpResponse(f"Приветствуем, {login}")
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password1 != password2:
            info['error'] = 'Пароли не совпадают'
            # return render(request, 'fifth_task/registration_page.html')

    return render(request, 'fifth_task/registration_page.html', context=info)