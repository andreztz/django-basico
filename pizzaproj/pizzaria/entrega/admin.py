from django.contrib import admin

from entrega import models


class PizzaInline(admin.StackedInline):
    model = models.Pizza
    extra = 2


class PedidoAdmin(admin.ModelAdmin):
    inlines = [PizzaInline]
    list_display = ['entrada_fmt', 'cliente', 'entregador',
                    'partida', 'despachado']
    list_display_links = ['entrada_fmt', 'cliente']

    def entrada_fmt(self, pedido):
        return pedido.entrada.strftime('%H:%M')
    entrada_fmt.short_description = 'entrada'

    def despachado(self, pedido):
        return bool(pedido.entregador and pedido.partida)
    despachado.boolean = True


admin.site.register(models.Cliente)
admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.Entregador)
