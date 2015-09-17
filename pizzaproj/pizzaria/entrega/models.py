from django.db import models


class Cliente(models.Model):
    fone = models.CharField(max_length=16, db_index=True)
    ramal = models.CharField(max_length=4, blank=True, db_index=True)
    contato = models.CharField(max_length=64, db_index=True)
    outros_contatos = models.TextField(blank=True)
    logradouro = models.CharField(max_length=32)
    numero = models.PositiveIntegerField('número')
    complemento = models.CharField(max_length=32, blank=True)
    obs = models.TextField(blank=True)

    def __str__(self):
        return '{} ({})'.format(self.contato, self.fone)


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente)
    entrada = models.DateTimeField(auto_now_add=True)
    partida = models.TimeField(null=True, blank=True)
    entregador = models.ForeignKey('Entregador', null=True, blank=True)
    obs = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return '{} - {:%m-%d %H:%M}'.format(self.cliente, self.entrada)


class Entregador(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Entregadores'

    def __str__(self):
        return self.nome


SABORES_PIZZA = [
    ('', '(escolha o sabor)'),
    ('mozzarella', 'Muçarela'),
    ('calabresa', 'Calabresa'),
    ('portuguesa', 'Portuguesa'),
    ('4queijos', '4 Queijos'),
]


class Pizza(models.Model):
    pedido = models.ForeignKey(Pedido)
    sabor = models.CharField(max_length=32, choices=SABORES_PIZZA)
    sabor2 = models.CharField(max_length=32, choices=SABORES_PIZZA, blank=True)
    obs = models.CharField(max_length=256, blank=True)

    def __str__(self):
        if self.sabor2:
            return '½ {}, ½ {}'.format(self.sabor, self.sabor2)
        else:
            return self.sabor
