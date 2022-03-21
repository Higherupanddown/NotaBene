from django.db import models
from operator import mod
# Create your models here.



class Users(models.Model):
    userName=models.CharField(max_length=45)
    mail=models.EmailField(max_length=254)
    

    def __str__(self):
        return self.userName

    
class Docs(models.Model):
    idOwner=models.IntegerField()
    docName=models.CharField(max_length=45)
    state=models.BooleanField(default=True)
    content=models.FileField(upload_to='files/')    


class Docs_Users(models.Model):
    Docs_id=models.IntegerField()
    Users_id=models.CharField(max_length=45)
    state=models.BooleanField(default=True)
    content=models.FileField(upload_to='files/')    