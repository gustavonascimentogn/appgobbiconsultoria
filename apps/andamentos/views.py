from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Andamento
from .form import AndamentoForm
from django.shortcuts import redirect

from django.core.mail import send_mail
from django.conf import settings
import requests
import json

from ..pedidos.models import Pedido
from ..servicos.models import Servico
from ..solicitacoes.models import Solicitacao


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
                player_id_onesignal = andamento.pedido.cliente.playerId_onesignal
                message = 'Referente ao Contrato/Serviço "' + str(andamento.servico.nome) + '" | Status atual: ' + andamento.status.nome + ' | Informação adicionada: ' + andamento.comentario
                html_message= 'Este e-mail refere-se ao Contrato/Serviço <b>ID: "' + str(andamento.servico.nome) + '"</b><br>Status atual: <b>' + andamento.status.nome + '</b><br>Informação adicionada: <b>' + andamento.comentario + '</b>'
                message_onesignal = 'Atualização referente ao Contrato/Serviço "' + str(andamento.servico.nome) + '" disponível no App. Acesse e confira o andamento mais recente.'
            else: #elif (self.kwargs['origem'] is 'solicitacao'):
                emailContato = andamento.solicitacao.cliente.emailContato ## para quem vai a mensagem
                player_id_onesignal = andamento.solicitacao.cliente.playerId_onesignal
                message = 'Referente a Solicitação "' + andamento.solicitacao.solicitacao + '" | Status atual: ' + andamento.status.nome + ' | Informação adicionada: ' + andamento.comentario
                html_message= 'Este e-mail refere-se a Solicitação <b> "' + andamento.solicitacao.solicitacao + '"</b><br>Status atual: <b>' + andamento.status.nome + '</b><br>Informação adicionada: <b>' + andamento.comentario + '</b>'
                message_onesignal = 'Atualização referente a Solicitação "' + andamento.solicitacao.solicitacao + '" disponível no App. Acesse e confira o andamento mais recente.'
            email_from = self.request.user.empregado.email #settings.EMAIL_HOST_USER
            recipient_list = [emailContato, email_from,]
            send_mail( subject, message, email_from, recipient_list,html_message=html_message,auth_user=settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD)

            ##ENVIANDO PUSH NOTIFICATION
            header = {"Content-Type": "application/json; charset=utf-8"}
            payload = {"app_id": self.request.user.empregado.empresa.appid_onesignal,
                       "include_player_ids": [player_id_onesignal],
                       "contents": {"en": message_onesignal}}
            req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
            ## print(req.status_code, req.reason)

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
        origem = self.kwargs['origem']
        if origem == 'pedido' or origem == 'cliente':
            andamento.pedido = Pedido.objects.get(pk=self.kwargs['pk'])
            andamento.servico = Servico.objects.get(pk=self.kwargs['servico'])
        else:
            andamento.solicitacao = Solicitacao.objects.get(pk=self.kwargs['pk'])
        andamento.save()

        ## ESSE CODIGO SE REPETE NO EDIT E NO CREATE
        if andamento.disponivelCliente:
            ## enviando e-mail para o cliente, caso campo esteja marcado como True
            nomeFantasia = self.request.user.empregado.empresa.nomeFantasia ## da empresa que enviara o email
            subject = '['+ nomeFantasia + '] Novidade referente ao seu atendimento'
            if origem == 'pedido' or origem == 'cliente':
                emailContato = andamento.pedido.cliente.emailContato ## para quem vai a mensagem
                player_id_onesignal = andamento.pedido.cliente.playerId_onesignal
                message = 'Referente ao Contrato/Serviço "' + str(andamento.servico.nome) + '" | Status atual: ' + andamento.status.nome + ' | Informação adicionada: ' + andamento.comentario
                html_message= 'Este e-mail refere-se ao Contrato/Serviço <b>"' + str(andamento.servico.nome) + '"</b><br>Status atual: <b>' + andamento.status.nome + '</b><br>Informação adicionada: <b>' + andamento.comentario + '</b>'
                message_onesignal = 'Atualização referente ao Contrato/Serviço "' + str(andamento.servico.nome) + '" disponível no App. Acesse e confira o andamento mais recente.'
            else: #elif (self.kwargs['origem'] == 'solicitacao'):
                emailContato = andamento.solicitacao.cliente.emailContato ## para quem vai a mensagem
                player_id_onesignal = andamento.solicitacao.cliente.playerId_onesignal
                message = 'Referente a Solicitação "' + andamento.solicitacao.solicitacao + '" | Status atual: ' + andamento.status.nome + ' | Informação adicionada: ' + andamento.comentario
                html_message= 'Este e-mail refere-se a Solicitação <b>"' + andamento.solicitacao.solicitacao + '"<br>Status atual: <b>' + andamento.status.nome + '</b><br>Informação adicionada: <b>' + andamento.comentario + '</b>'
                message_onesignal = 'Atualização referente a Solicitação "' + andamento.solicitacao.solicitacao + '" disponível no App. Acesse e confira o andamento mais recente.'
            email_from = self.request.user.empregado.email #settings.EMAIL_HOST_USER
            recipient_list = [emailContato, email_from,]
            ## EXEMPLO COMPLETO: send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
            send_mail( subject, message, email_from, recipient_list,html_message=html_message,auth_user=settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD)

            ##ENVIANDO PUSH NOTIFICATION
            header = {"Content-Type": "application/json; charset=utf-8"}
            payload = {"app_id": self.request.user.empregado.empresa.appid_onesignal,
                       "include_player_ids": [player_id_onesignal],
                       "contents": {"en": message_onesignal}}
            req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
            ## print(req.status_code, req.reason)

        if (str(self.kwargs['origem']) == 'pedido'):
            return redirect('list_pedidos')
        elif (str(self.kwargs['origem']) == 'cliente'):
            return redirect('list_clientes')
        else: #elif (self.kwargs['origem'] == 'solicitacao'):
            return redirect('list_solicitacoes')


    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if (self.kwargs['origem'] == 'pedido'):
            form.instance.pedido_id = self.kwargs['pk']
            form.instance.servico_id = self.kwargs['servico']
        else: #elif (self.kwargs['origem'] == 'solicitacao'):
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

