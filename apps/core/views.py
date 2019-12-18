from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.empregados.models import Empregado

@login_required
def home(request):
    data = {} #dicionario
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)
