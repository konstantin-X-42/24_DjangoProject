# модуль urls.py определяет маршрутизацию для проекта связывая url адреса с конкретными контроллерами

# подключен маршрут к административной панели
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls', namespace='students'))
]

# проверяем что включен режим DEBUG (метод будет работать только во время доработки)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)      # добавляем в urlpatterns
