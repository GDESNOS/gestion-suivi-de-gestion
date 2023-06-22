from django.db import models
from django.contrib.auth.models import User



class CategorieProjet(models.Model):
    nom_categorie= models.CharField(max_length=250)
    def __str__(self) -> str:
        return f'{self.nom_categorie}'
    

class Project(models.Model):    
    nom= models.CharField(max_length=50)
    description=models.TextField()
    dateDebut = models.DateField(auto_now=True)
    categorieProjet = models.ForeignKey(CategorieProjet, on_delete=models.CASCADE)
    chef_projet = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    estChefProjet = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.project.nom}"
    

class MyModel(models.Model):
    my_file = models.FileField(upload_to='files/')


class Taches(models.Model):
    nom = models.CharField(max_length=120)
    description = models.TextField()
    dateDebut=models.DateField()
    dateFin=models.DateField()
    projet = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return self.description
    

class Notifications(models.Model):
    pass
    