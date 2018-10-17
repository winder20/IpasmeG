# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.views.generic import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.context import RequestContext
from ..utils.mixins import AdminRequiredMixin, UsuarioRequiredMixin
from ..authentication.forms import UsersModelForm,UsersUpdateModelForm
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, View
# import mixins
from django.template.context import RequestContext
from django.conf import settings
from .models import Users
from .forms import UsersModelForm, UsersUpdateModelForm
# mixins
from django.contrib.auth.mixins import LoginRequiredMixin

# import class based views
from django.views.generic import View







# Create your views here.



class LoginView(View):
    form_class = AuthenticationForm
    template_name = "login/login.html"
    mensaje = ""

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form, 'message': ''})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('/'))
            else:
                return HttpResponse('no esta activo')
        else:
            mensaje ="Por favor, ingrese la cedula y la clave correctos."
            return render(request, self.template_name, {'form': self.form_class, 'message': mensaje})


class UsersCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model=Users
    form_class=UsersModelForm


    def get_success_url(self):
        return reverse_lazy('usuarios:add')



class UserListView(LoginRequiredMixin,AdminRequiredMixin, ListView):
    model = Users
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super(ActivistaListView, self).get_context_data(**kwargs)
        if self.request.GET.get('cedula'):
            result_list = self.model.objects.filter(cedula=int(self.request.GET['cedula'])).order_by('id')
        else:
            result_list = self.model.objects.all().order_by('cedula')

        paginator = Paginator(result_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        context['object_list'] = object_list
        return context



class UserDeleteView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
    model = Users
    

    def get_success_url(self):
        return reverse_lazy('usuarios:list')


class UserUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Users
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse_lazy('usuarios:list')


# logout
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')


def principal(request):
    return render(request ,"base2/index.html")

