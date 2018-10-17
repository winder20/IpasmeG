from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
# django paginator
from django.http import HttpResponse, HttpResponseRedirect

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# class based views.
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView,View
# models
from ..activista.models import Account
from ..activista.forms import AccountModelForm,AccountUpdateModelForm
# import login required
from django.contrib.auth.mixins import LoginRequiredMixin
from ..utils.mixins import AdminRequiredMixin, voceroRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate


# Create your views here.


class LoginView(View):
    form_class = AuthenticationForm
    template_name = "login/login.html"

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


class ActivistaCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model=Account
    form_class=AccountModelForm


    def get_success_url(self):
        return reverse_lazy('usuarios:add')


class ActivistaListView(LoginRequiredMixin, ListView):
    model = Account
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

class ActivistaDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Account
    

    def get_success_url(self):
        return reverse_lazy('usuarios:list')

class ActivistaUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Account
    form_class = AccountUpdateModelForm

    def get_success_url(self):
        return reverse_lazy('usuarios:list')

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')