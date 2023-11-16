from django.db import models

class Pessoa(models.Model):
    codPessoa = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=65)
    Email = models.CharField(max_length=60)
    Celular = models.CharField(max_length=18, null=True)

class Fisica(models.Model):
    codPF = models.AutoField(primary_key=True)
    CPF = models.PositiveIntegerField()
    DataNASC = models.DateField()
    saldoCash = models.CharField(max_length=45, null=True)
    codPessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, related_name='fisica')
    usuario = models.CharField(max_length=45, null=True)

class Juridica(models.Model):
    codPJ = models.AutoField(primary_key=True)
    CNPJ = models.PositiveIntegerField()
    codPessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, related_name='juridica')
    usuario = models.CharField(max_length=45, null=True)

class Item(models.Model):
    codItem = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=200)

class Produtos(models.Model):
    codItem = models.ForeignKey(Item, on_delete=models.CASCADE)
    codPJ = models.ForeignKey(Juridica, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valCashback = models.DecimalField(max_digits=10, decimal_places=2)
    perPendentec = models.CharField(max_length=45)
    descricao = models.CharField(max_length=100, null=True)

class Carrinho(models.Model):
    codCarrinho = models.AutoField(primary_key=True)
    codPF = models.ForeignKey(Fisica, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Em aberto', choices=[('Em aberto', 'Em aberto'), ('Concluido', 'Concluido')])
    
class Compra(models.Model):
    codCompra = models.CharField(primary_key=True, max_length=45)
    codCarrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    data = models.DateField()
    formaPag = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pendente', choices=[('Pendente', 'Pendente'), ('Enviado', 'Enviado'), ('Cancelado', 'Cancelado')])

class Transacao(models.Model):
    codTransac = models.AutoField(primary_key=True)
    codPJ = models.ForeignKey(Juridica, on_delete=models.CASCADE)
    codCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)

class Itens(models.Model):
    codCarrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    codItem = models.ForeignKey(Produtos, on_delete=models.CASCADE)



