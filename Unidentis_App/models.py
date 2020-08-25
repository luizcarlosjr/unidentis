from django.db import models

# Create your models here.

class Funcionario(models.Model):
    SETOR_CHOICES = (
         ("ti", "Tecnico de Informatica"),
         ("autorização", "Autorização"),
         ("cobranca", "Cobrança"),
         ("recepção","Recepção"),
         ("Call center", "Call Center"),
         ("DP","Departamento Pessoal"),
         ("CC", "Creditos e Contas")

    )
    nome = models.CharField(max_length=50, null=False)
    setor = models.CharField(max_length=20, null=False, choices=SETOR_CHOICES)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    CORES_CHOICES = (
            ("preto", "Preto"),
            ("azul", "Azul"),
            ("amarelo", "Amarelo"),
            ("branco", "Branco"),
            ("prata", "Prata"),
            ("vermelho", "Vermelho"),
        )
        
    modelo = models.CharField(max_length=50, null=False)
    marca = models.CharField(max_length=20, null=False)
    cor = models.CharField(max_length=20, null=True, choices=CORES_CHOICES)
    preco = models.FloatField(null=False)
    Data = models.DateTimeField(null=False)
    Funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)


    def publish(self):
        self.Data = timezone.now()
        self.save()

    def __str__(self):
          return self.modelo

 