from django.urls import path

from .import views

urlpatterns=[
    path('home/', views.accueil, name='accueil'),
    path('connexion/', views.connexion, name='connexion'),
    path('dashboad/', views.dashboad, name='dashboad'),
    #path('viewProject/',views.viewToutProjet, name='viewToutProjet'),
    #path('createtacheview/<int:id>/', views.viewCreactionTache, name='CreateProject'),
    path('messagerie/', views.messagerie, name='messagerie'),
    path('contenu/<int:id>', views.contenu_projet, name='contenu'),

    path('notifications/', views.notifications, name='notifications'),
    path('create-du-project/', views.createproject, name='create_team'),
    #path('affichageProjetAttente/', views.affichageProjetAttente, name='affichageProjetAttente'),
    path('logoutview/', views.logoutview, name='logoutview'),

]