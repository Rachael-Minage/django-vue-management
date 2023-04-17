# from django.conf.urls import url
from . import views
from .views import departmentApi, employeeApi, saveFile
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
                  path('department', departmentApi, name='department'),
                  path('view_employees/', views.view_employees, name='view_employees'),
                  path('department/<int:id>/', departmentApi, name='deleteDepartment'),
                  path('employee', employeeApi, name='employee'),
                  path('employee/<int:id>/', employeeApi, name='deleteEmployee'),
                  path('employee/file', saveFile, name='savedfile'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
