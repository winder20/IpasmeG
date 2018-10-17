


from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()



 			# Estan son mis Urls de mi app  ingresadas en mi Proyecto #

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.paginas.urls', namespace = 'paginas' )),
    url(r'^', include('apps.authentication.urls', namespace = 'authentication' )),
    url(r'^', include('apps.afiliado.urls', namespace = 'Afiliado' )),
    url(r'^', include('apps.beneficiario.urls', namespace = 'Beneficiario')),
    url(r'^', include('apps.institucion.urls', namespace = 'Institucion')),
    url(r'^', include('apps.reposo.urls', namespace = 'Reposo')),

]
