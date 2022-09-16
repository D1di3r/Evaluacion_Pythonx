from distutils.command.upload import upload
from pyexpat import model
from unicodedata import name
from django.db import models
from django.utils.html import format_html

class GamePosition (models.Model):
    name=models.CharField(max_length=30,verbose_name="Nombre de la Posición")
    description=models.CharField(max_length=50,verbose_name="Descripcion de la Posición")

    def __str__(self):
        return self.name


    class Meta :
     verbose_name='Posicion de Juego'
     verbose_name_plural="Posiciones de Juego"
     db_table='posicion'
     ordering= ['id']

class team (models.Model):
    name=models.CharField(max_length=30,verbose_name="Nombre del Equipo")
    flagteam=models.ImageField(upload_to='media',null=False, blank=False)
    shieldteam=models.ImageField(upload_to='media',null=False, blank=False)

    def __str__(self):
        return self.name

    def Bandera(self):
        return format_html('<img src={} width="100" /> ', self.flagteam.url)

    def Escudo(self):
        return format_html('<img src={} width="100" /> ', self.shieldteam.url)

    class Meta :
     verbose_name='Equipo'
     verbose_name_plural="Equipos"
     db_table='equipo'
     ordering= ['id']

class instructor (models.Model):
    name=models.CharField(max_length=30,verbose_name="Nombre del Técnico")
    lastname= models.CharField(max_length=30, verbose_name="Apellido del Técnico")
    birthdate=models.DateField(verbose_name="Fecha de Nacimiento")
    nationality=models.CharField(max_length=35, verbose_name="Nacionalidad")
    rol=models.CharField(max_length=30, verbose_name="Rol")

    def __str__(self):
        return self.name


    class Meta :
     verbose_name='Técnico'
     verbose_name_plural="Instructor"
     db_table='técnico'
     ordering= ['id']

class player (models.Model):
    name=models.CharField(max_length=30,verbose_name="Nombre del Jugador")
    lastname= models.CharField(max_length=30, verbose_name="Apellido del Jugador")
    photoplayer=models.ImageField(upload_to='media',null=False, blank=False)
    birthdate=models.DateField(verbose_name="Fecha de Nacimiento")
    position=models.ForeignKey(GamePosition,on_delete=models.CASCADE)
    numTshirt=models.IntegerField(verbose_name="Número de Camiseta")
    titled=models.CharField(max_length=35, verbose_name="¿Es Titulado?")
    teamp=models.ForeignKey(team,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def Foto(self):
        return format_html('<img src={} width="100" /> ', self.photoplayer.url)

    class Meta :
     verbose_name='Jugador'
     verbose_name_plural="Jugadores"
     db_table='jugador'
     ordering= ['id']


