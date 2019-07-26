from django.db import models

# Create your models here.

class Pessoa(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )

    sobrenome = models.CharField(
        max_length=255,
        verbose_name='Sobrenome'
    )

    genero = models.CharField(
        max_length=255,
        verbose_name='Gênero',
        choices=GENEROS
    )

    email = models.EmailField(
        max_length=255,
        verbose_name='E-mail'
    )

    biografia = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

class Ideias(models.Model):
    CATEGORIAS = (
        ('TERRA_PLANA' , 'Terra plana'),
        ('CONTRA_GROGER' , 'Ideias para coach Groger') ,
        ('CONTRA_JOAO' ,'ideias  contra João'),
        ('PÚBLICAS' , 'Públicas'),
        ('OUTROS' , 'Outros'),
    )
    pessoa = models.ForeignKey(
        Pessoa, on_delete=None 
        #ao excluir a ideia não excluirei a pessoa 
    )
    titulo = models.CharField(
        max_length=255,
        verbose_name=' Nome da ideia ',
        unique=True)

    descricao = models.TextField(
        verbose_name='Descreva sua ideia'
    )

    categorias = models.CharField(
        verbose_name='categorias',
        choices=CATEGORIAS,
        max_length=255
    )
    
    categorias_outros = models.CharField(
        null=True,
        blank=True,
        max_length=225,
        verbose_name='caso outros, qual'
    )

    data_de_criacao = models.DateTimeField(auto_now_add=True)
    data_de_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)