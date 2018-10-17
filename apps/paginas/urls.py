
from django.conf.urls import url, include
from  .views import *

# Estan son mis Urls de mi app  #

urlpatterns = [
	url(r'$^', inicio ),
    url(r'^sobre_nosotros/', sobre_nosotros ,name='sobre_nosotros'),
    url(r'^galeria/', galeria ,name='galeria'),
    url(r'^blog/', blog ,name='blog'),
    url(r'^contacto/', contacto ,name='contacto'),
]
