# views.py - модуль представления контроллеров

from django.shortcuts import render
from django.http import HttpResponse

def example_view(request):
    """Контроллер выполняет базовую задачу в веб-разработке — отображает HTML-страницу по указанному адресу"""
    return render(request, 'app/example.html')

def show_data(request):
    """Контроллер (представление) отвечает за обычный показ (отображение) HTML-страницы пользователю."""
    if request.method == 'GET':
        return render(request, 'app/show_data.html')

def submit_data(request):
    """Контроллер (в Django он называется view или представление) обрабатывает отправку данных на сервер"""
    if request.method == 'POST':
        return HttpResponse("Данные отправлены")

def show_item(request, item_id):
    """контроллер с параметром из маршрута"""
    return render(request, 'app/item.html', {'item_id': item_id})


# - - - - - - контроллер обрабатывает шаблон - - - - - - - - - - - - - - - - - - - - - - - - -
from django.shortcuts import render

def about(request):
    """Контроллер отвечает за отображение статической страницы «О нас» для приложения students"""
    return render(request, 'students/about.html')



from django.http import HttpResponse

def contact(request):
    """Контроллер показывать посетителю форму для отправки сообщения и обрабатывать данные, которые пользователь в эту форму вводит"""
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, 'students/contact.html')

