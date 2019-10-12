"""为应用程序users添加URL模式"""
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    #登陆页面
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    #注销
    url(r'^logout/$',views.logout_view,name='logout'),
    #注册页面
    url(r'^register/$',views.register,name='register'),
    #解方程
    url(r'^counter/$',views.counter,name='counter'),
]