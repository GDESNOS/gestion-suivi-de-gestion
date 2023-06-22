from django import forms
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#from django.core.mail import send_mail
from django.contrib import messages
from .models import CategorieProjet, Project, Membership, Taches
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required



def accueil(request):
    return render(request, 'pages/navbar.html')

def connexion(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')

         try:
              user = User.objects.get(username=username)
         except User.DoesNotExist:
              user= None
         if user is not None:
              authenticated_user = authenticate(request, username=username, password=password)
              if authenticated_user is not None:
                   login(request, authenticated_user)
                   return redirect(accueil)
              else :
                   messages.error(request, "L'identifiant incorrect")
    else :
         return render(request, 'memoire/connexion.html')
    return render(request, 'memoire/connexion.html')
                          
def logoutview(request):
     logout(request) 
     return redirect(accueil)         


@login_required
def createproject(request):
    categories = CategorieProjet.objects.all()
    utilisateurs =User.objects.all()

    if request.method == 'POST':
        nom_projet = request.POST.get('nom_projet')
        description = request.POST.get('description')
        categorie_id = request.POST.get('categorie')

        # Créer le projet et l'associer au chef de projet (utilisateur connecté)
        chef_projet = request.user
        projet = Project.objects.create(
            nom=nom_projet,
            description=description,
            categorieProjet_id=categorie_id,
            chef_projet=chef_projet
        )
    
        # Ajouter le chef de projet comme membre avec le statut estChefProjet=True
        Membership.objects.create(user=chef_projet, project=projet, estChefProjet=True)

        # Récupérer la liste des adresses e-mail des membres soumises dans le formulaire
        membres = request.POST.getlist('membres')

        # Ajouter les membres au projet et envoyer un email d'invitation
        for email in membres:
            # Vérifier si l'utilisateur avec cette adresse e-mail existe déjà
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # Gérer le cas où l'utilisateur n'existe pas
                # Par exemple, afficher un message d'erreur ou ignorer l'adresse e-mail
                continue

            # Ajouter l'utilisateur comme membre du projet
            Membership.objects.create(user=user, project=projet)

            # Envoyer un email d'invitation pour rejoindre le projet
            """ send_mail(
                'Invitation à rejoindre le projet',
                f'Vous êtes invité à rejoindre le projet "{projet.nom}".',
                'noreply@example.com',
                [email],
                fail_silently=False,
            )
 """
        return redirect('dashboad')

    return render(request, 'pages/create_team.html', {'categories': categories, 'utilisateurs': utilisateurs})

def creertachesview(request, projet_id):
    if request == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        date_debut=request.POST.get('dateDebut')
        date_fin=request.POST.get('dateFin')
        


        tache = Taches.objects.create(
               nom = nom,
               description = description,
               date_debut = date_debut,
               date_fin = date_fin,
               projet_id = projet_id
        )

        print(tache.description)  

        return render(request, 'memoire/dashboard.html')
def dashboad(request):
    projets = Project.objects.all()
    return render(request, 'memoire/dashboard.html', {'projets': projets})

# La definition de la methode qui permet de creer un projet
def contenu_projet(request, id):
     projet = Project.objects.get(id =id)
     return render(request, 'memoire/affichageprojet.html', {'projet': projet })
     
def messagerie(request):
        return render(request, 'memoire/messagerie.html')


def notifications(request):
        return render(request, 'memoire/notifications.html')

# La methode qui permet l'affichage de fichiers soumis par un membre 

def photo_upload(request):
    form = forms.MyForm()
    if request.method == 'POST':
        form = forms.MyForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('create-du-project')
    return render(request, 'pages/create_team.html', {'form': form})

