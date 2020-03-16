from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Andamento
from .form import AndamentoForm
from django.shortcuts import redirect
from apps.pedidos.models import Pedido

from django.core.mail import send_mail
from django.conf import settings



class AndamentosList(ListView):
    model = Andamento
    paginate_by = 20

## Classe para edição dos registros
class AndamentoEdit(UpdateView):
    model = Andamento
    form_class = AndamentoForm

    def form_valid(self, form):
        andamento = form.save(commit=False)
        andamento.save()

        ## ESSE CODIGO SE REPETE NO EDIT E NO CREATE
        if andamento.disponivelCliente:
            ## enviando e-mail para o cliente, caso campo esteja marcado como True
            nomeFantasia = self.request.user.empregado.empresa.nomeFantasia ## da empresa que enviara o email
            subject = '['+ nomeFantasia + '] Novidade referente ao seu atendimento'
            ##if (str(self.kwargs['origem']) == 'pedido'):
            if andamento.pedido:
                emailContato = andamento.pedido.cliente.emailContato ## para quem vai a mensagem
                message = 'Referente ao serviço ' + andamento.pedido.servico.nome + ' | Status atual: ' + andamento.status.nome + ' | Informação adicionada: ' + andamento.comentario
                html_message= 'Este e-mail refere-se ao serviço <b>' + andamento.pedido.servico.nome + '</b><br>Status atual: <b>' + andamento.status.nome + '</b><br>Informação adicionada: <b>' + andamento.comentario + '</b>'
            else: #elif (self.kwargs['origem'] is 'solicitacao'):
                emailContato = andamento.solicitacao.cliente.emailContato ## para quem vai a mensagem
                message = 'Referente a solicitação ' + andamento.solicitacao.solicitacao + ' | Status atual: ' + andamento.status.nome + ' | Informação adicionada: ' + andamento.comentario
                html_message= 'Este e-mail refere-se a solicitação <b>' + andamento.solicitacao.solicitacao + '</b><br>Status atual: <b>' + andamento.status.nome + '</b><br>Informação adicionada: <b>' + andamento.comentario + '</b>'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [emailContato, email_from,]
            send_mail( subject, message, email_from, recipient_list,html_message=html_message )

        return redirect('list_andamentos')


    ## Methodo para filtrar o campo "cliente", trazendo somente os clientes da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(AndamentoEdit, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs


class AndamentoDelete(DeleteView):
    model = Andamento
    success_url = reverse_lazy('list_pedidos')


class AndamentoNovo(CreateView):
    model = Andamento
    form_class = AndamentoForm

    def form_valid(self, form):
        andamento = form.save(commit=False)
        andamento.save()

        ## ESSE CODIGO SE REPETE NO EDIT E NO CREATE
        if andamento.disponivelCliente:
            ## enviando e-mail para o cliente, caso campo esteja marcado como True
            nomeFantasia = self.request.user.empregado.empresa.nomeFantasia ## da empresa que enviara o email
            subject = '['+ nomeFantasia + '] Novidade referente ao seu atendimento'
            if andamento.pedido:
                emailContato = andamento.pedido.cliente.emailContato ## para quem vai a mensagem
                message = 'Referente ao serviço ' + andamento.pedido.servico.nome + ' | Atualização de status: ' + andamento.status.nome + ' | Informação adicionada: ' + andamento.comentario
                html_message= 'Este e-mail refere-se ao serviço <b>' + andamento.pedido.servico.nome + '</b><br>Atualização de status: <b>' + andamento.status.nome + '</b><br>Informação adicionada: <b>' + andamento.comentario + '</b>'
            else: #elif (self.kwargs['origem'] is 'solicitacao'):
                emailContato = andamento.solicitacao.cliente.emailContato ## para quem vai a mensagem
                message = 'Referente a solicitação ' + andamento.solicitacao.solicitacao + ' | Atualização de status: ' + andamento.status.nome + ' | Informação adicionada: ' + andamento.comentario
                html_message= 'Este e-mail refere-se a solicitação <b>' + andamento.solicitacao.solicitacao + '</b><br>Atualização de status: <b>' + andamento.status.nome + '</b><br>Informação adicionada: <b>' + andamento.comentario + '</b>'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [emailContato, email_from,]
            send_mail( subject, message, email_from, recipient_list,html_message=html_message)


        if (str(self.kwargs['origem']) == 'pedido'):
            return redirect('list_pedidos')
        else: #elif (self.kwargs['origem'] is 'solicitacao'):
            return redirect('list_solicitacoes')


    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if (self.kwargs['origem'] == 'pedido'):
            form.instance.pedido_id = self.kwargs['pk']
        else: #elif (self.kwargs['origem'] is 'solicitacao'):
            form.instance.solicitacao_id = self.kwargs['pk']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    ## Methodo para filtrar o campo "status", trazendo somente os status da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(AndamentoNovo, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs

        return kwargs

