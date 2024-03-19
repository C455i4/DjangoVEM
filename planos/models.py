from django.db import models

class PlanosModel(models.Model):
    nome = models.CharField(max_length = 100)
    preco = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


    def get_display_price(self):
        return "{0:.2f}".format(self.preco / 100)
