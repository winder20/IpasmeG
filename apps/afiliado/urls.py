
from django.conf.urls import url, include
from .views import * 
from ..afiliado import views 




# Estan son mis Urls de mi app  #

urlpatterns = [
    url(r'^afiliado/', Afiliado , name='Afiliado'),

]
