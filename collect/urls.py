from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register_student,name='register'),
    path('register_teacher', views.register_teacher,name='register_teacher'),
    path('creat_test',views.creat_test,name='creat_test'),
    path('login', views.login,name='login'),
    path('teacher_login',views.teacher_login,name='teacher_login'),
    path('test', views.test,name='test'),
    path('', views.home,name='home'),
    path('home', views.home,name='home'),
    path('check', views.check,name='check')
]
