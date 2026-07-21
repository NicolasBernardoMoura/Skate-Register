from django.db import models

class Skatista(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    cidade = models.CharField(max_length=100)


    MODALIDADES = [
        ('Street', 'Street'),
        ('Park', 'Park'),
        ('Vert', 'Vert'),
        ('Bowl', 'Bowl'),
    ]


    modalidade = models.CharField(max_length=20, choices=MODALIDADES)


    NIVEIS = [
        ('Iniciante' , 'Iniciante'),
        ('Intermediário' , 'Intermediário'),
        ('Avançado' , 'Avançado'),
    ]


    nivel = models.CharField(max_length=20, choices=NIVEIS)


    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)


    def __str__(self):
        return self.nome