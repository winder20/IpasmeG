from django.conf.urls import url
from django.contrib import admin
from ..activista import views

urlpatterns = [
	url(r'^login/$', views.LoginView.as_view(), name='login'),
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
	url(r'^add/$', views.ActivistaCreateView.as_view(), name='add'),
    url(r'^$', views.ActivistaListView.as_view(), name='list'),
    url(r'^(?P<pk>[-\ \w]+)/delete/$',views.ActivistaDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>[-\ \w]+)/update/$',views.ActivistaUpdateView.as_view(), name='update'),
]
