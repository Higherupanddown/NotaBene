from django.db import models
from operator import mod
# Create your models here.



class Users(models.Model):
    userName=models.CharField(max_length=45)
    mail=models.EmailField(max_length=254)
    

    def __str__(self):
        return self.userName

    
class Docs(models.Model):
    idOwner=models.ForeignKey(Users, on_delete = models.CASCADE)
    docName=models.CharField(max_length=45)
    state=models.BooleanField(default=True)
    content=models.FileField(upload_to='files/')    


class DocsUsers(models.Model):
    idDocs = models.ForeignKey(Docs, on_delete = models.CASCADE, related_name = "doc")
    idUsers = models.ForeignKey(Users, on_delete = models.CASCADE, related_name = "users")