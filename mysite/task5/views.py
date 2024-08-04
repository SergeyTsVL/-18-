from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

def index(request):
    info = {}
    if request.method == 'Post':
        login = request.Post.get('login')
        password1 = request.Post.get('password1')
        password2 = request.Post.get('password2')
        age = request.Post.get('age')

        if password1 == password2 and int(age) >= 18:
            return HttpResponse(f"Приветствуем, {login}")
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            # return render(request, 'fifth_task/registration_page.html')

    return render(request, 'fifth_task/registration_page.html', context=info)