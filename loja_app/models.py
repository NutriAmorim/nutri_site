from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    arquivo = models.FileField(upload_to='pdf/', null=True, blank=True)  # <- Novo campo

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} unidades"


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    produtos = models.TextField()  # Aqui você pode mudar para um modelo mais adequado para os produtos
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.username}'
    

class Endereco(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.rua}, {self.bairro}, {self.cidade}'