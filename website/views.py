from django.shortcuts import render , redirect 
from website.models import Pessoa , Ideia

# Create your views here.

def index(request):
    #vai cadastrar uma pessoa 
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        contexto = {'msg': 'Parabéns :)'}

    return render(request, 'index.html', contexto)


def sobre(request):
    #essa pag listara as ideias e seus criadores!
    ideias = Ideia.objects.filter(ativo=True).all()
    contexto = {
        'ideias':ideias
    }
    return render(request, 'sobre.html', contexto)

def login(request):
    #conferir a existencia de um usuario cadastro, se sim retornará para pagina sobre se não retornará p/ casdatro
    #com uma mensagem cadastre-se para criar uma ideia
    #peguei o email 
    if request.method == 'POST':
        email_form = request.POST.get('email') 
        pessoa = Pessoa.objects.filter(email=email_form) .first()

        

        if pessoa is None:
            #mandar para pagina de cadastro 
            contexto = {'msg' : 'Cadastre-se para criar sua ideia!'}
            return render(request, 'index.html' , contexto)
        else:
            contexto = {'pessoa' : pessoa}
            return render(request, 'ideias.html' contexto)


    return render(request, 'login.html' ,{})

def casdastar_ideia(request) :
    if request.method == 'POST' :
        email_pessoa = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_pessoa).first(
        if pessoa is not None:
            ideia = ideia()
            ideia.pessoa = Pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categoria_outros = request.POST.get('categoria_outros')
            ideia.save()
            print('Uhuu')

            return
            return render(request,'sobre.html',{})

        )
     return render(request, 'ideias.html' {})