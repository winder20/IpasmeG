from django.conf.urls import url
from django.contrib import admin
from ..authentication import views
from .views import *



urlpatterns = [

	url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^add/$',views.UsersCreateView.as_view(), name='add'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),


	url(r'^$', views.UserUpdateView.as_view(), name='list'),
    url(r'^(?P<pk>[-\ \w]+)/delete/$',views.UserDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>[-\ \w]+)/update/$',views.UserUpdateView.as_view(), name='update'),
    #url(r'^accounts/login/$', ErrorView.as_view(), name='error'),

 	url(r'^principal/$', principal, name='principal'),
] 


