# urls.py - модуль маршрутизации при создании не реализован (создан самосточтельно прописываем маршруты)
# from django.urls import path
# from . import views
#
# # указываем пространство имён
# app_name = 'students'
#
# urlpatterns = [
#     path('show_data/', views.show_data, name='show_data'),
#     path('submit_data/', views.submit_data, name='submit_data'),
#     path('item/<int:item_id>/', views.show_item, name='show_item')
#
# ]

# - - - - - связывает определенный веб-адрес с контроллером (функцией), который отвечает за показ страницы - - - - - -
from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
