from django.db import models

class Operator(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class SimCard(models.Model):

    TAMAÑO = [
        ('PEQUEÑO','PEQUEÑO'),
        ('MEDIANO','MEDIANO'),
        ('GRANDE','GRANDE'),
        ('N/A','N/A'),
        ]
    
    ESTADO = [
        ('ACTIVA', 'ACTIVA'),
        ('INACTIVA', 'INACTIVA'),
    ]

    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    tamaño_sim = models.CharField(max_length=7, choices=TAMAÑO, default='N/A')
    estado = models.CharField(max_length=8, choices=ESTADO, default='ACTIVA')
