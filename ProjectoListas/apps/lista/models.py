from django.db import models

# estos son los clases y funciones principales

class Lista(models.Model):
	usuario = models.ForeignKey( ,on_delete=models.CASCADE)
	idLista = models.AutoField(primary_key=True)
	nombreLista = models.CharField(max_length=30)
	linea = models.AutoField()
	contenido = models.CharField(max_length=30)

def __str__(self):
	return self.nombreLista







class Empresa(models.Model):
	idEmpresa = models.AutoField(primary_key=True)
	nombreEmpresa = models.CharField(max_length=50)


