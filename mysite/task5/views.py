from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

def index(request):
    if request.method == 'Post':
        login = request.Post.get('login')
        password1 = request.Post.get('password1')
        password2 = request.Post.get('password2')
        age = request.Post.get('age')

        print(login)
        print(password1)
        print(password2)
        print(age)


        return HttpResponse(f"Приветствуем, {login}")
    return render(request, 'fifth_task/registration_page.html')
