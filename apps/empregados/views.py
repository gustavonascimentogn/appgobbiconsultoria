from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .form import EmpregadoForm
from .models import Empregado

## Classe para listagem dos registros
from ..empresas.models import Empresa


class EmpregadosList(LoginRequiredMixin,ListView):
    model = Empregado
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        return Empregado.objects.filter(empresa=empresa_logada).order_by('nome')


## Classe para edição dos registros
class EmpregadoEdit(LoginRequiredMixin,UpdateView):
    model = Empregado
    form_class = EmpregadoForm

    def form_valid(self, form):
        empregado = form.save(commit=False)
        empresa_logada = self.request.user.empregado.empresa

        ## Empregado sendo alterado é da empresa que o usuario está logado?
        if Empregado.objects.filter(pk=empregado.pk,empresa=empresa_logada):
            ## Empregado sendo alterado possui o e-mail informado no formulario?
            if User.objects.filter(username=self.request.POST.get("email"),pk=empregado.user.pk):
                ## Se encontrou, então e-mail do usuario NÃO foi alterado (existe o email para aquele empregado)
                empregado.user.username = self.request.POST.get("email")
                empregado.user.email = self.request.POST.get("email")
                empregado.user.password = self.request.POST.get("senha")
                empregado.user.save()
                empregado.save()
                mensagem = 'Alteração de funcionário realizado com sucesso'
            else:
                ## Se entrou, então e-mail do usuario foi alterado (não existe o email para aquele empregado)
                ## Verifica se existe o e-mail cadastrado para qualquer outro usuario
                if not User.objects.filter(username=self.request.POST.get("email")):
                    ## se não existe, então e-mail liberado para cadastro
                    empregado.user.username = self.request.POST.get("email")
                    empregado.user.email = self.request.POST.get("email")
                    empregado.user.password = self.request.POST.get("senha")
                    empregado.user.save()
                    empregado.save()
                    mensagem = 'Alteração de funcionário realizado com sucesso'
                else:
                    mensagem = 'Cadastro de funcionário não alterado (e-mail já cadastrado para outro usuário)'
        else:
            mensagem = 'Você não tem permissão para alterar este funcionário'

        from django.shortcuts import redirect
        return redirect('list_empregados',mensagem)


class EmpregadoDelete(LoginRequiredMixin,DeleteView):
    model = Empregado
    success_url = reverse_lazy('list_empregados')

class EmpregadoNovo(LoginRequiredMixin,CreateView):
    model = Empregado
    form_class = EmpregadoForm

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        empregado = form.save(commit=False)
        empregado.empresa = self.request.user.empregado.empresa

        ## Incluindo USER no auth
        usr = User.objects.filter(username=self.request.POST.get("email"))
        if not usr:
            user = User.objects.create_user(username=self.request.POST.get("email"),
                                 email=self.request.POST.get("email"),
                                 password=self.request.POST.get("senha"))
            empregado.user = user
            my_group = Group.objects.get(name='Gerente')
            user.groups.add(my_group)
            mensagem = 'Cadastro de funcionário realizado com sucesso'
            empregado.save()
        else:
            mensagem = 'Cadastro não realizado (e-mail já cadastrado na base de dados)'

        from django.shortcuts import redirect
        return redirect('list_empregados', mensagem)
