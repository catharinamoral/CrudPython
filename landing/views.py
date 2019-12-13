from django.shortcuts import render, redirect
from .models import Aluno, Usuario

# Create your views here.

def index(request):
    if request.method == 'POST':
        data_usuario = Usuario()
        data_usuario.email = request.POST['email']
        data_usuario.senha = request.POST['senha']
        data_usuario.save()
        
        data_aluno = Aluno()
        data_aluno.nome = request.POST['nome']
        data_aluno.frase = request.POST['frase']
        data_aluno.save()
        
    return render(request, 'index.html')

def login(request):
    if(request.method == 'POST'):
        usuario = Usuario()
        if (usuario.email == request.POST['email']):
            return

    return render(request, 'login.html')

def listar(request):
    listar_frases = Aluno.objects.filter(ativo = True).all()
    args = {
        'listar_frase' : listar_frases
    }
    return render(request, 'lista.html', args)

def deletar(request):
    item = Aluno.objects.get(id = id)
    if item is not None:
        item.ativo = False
        item.save()
        return redirect('aluno/listar')
    return redirect('/')

def home(request):
    return render(request, 'home.html')

