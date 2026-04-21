# task_management_api
simple task management crud app with django

## Structure créée
Application Django 'tasks' : Créée avec python manage.py startapp tasks

Modèle Task : Défini dans tasks/models.py avec les champs title, description, 

completed, created_at, updated_at

Serializer : TaskSerializer dans tasks/serializers.py pour la sérialisation JSON

ViewSet : TaskViewSet dans tasks/views.py utilisant ModelViewSet de DRF

URLs : Configuration des routes dans tasks/urls.py et Task_management_api/urls.py

Migrations : Appliquées pour créer la table Task dans la base de données

Serveur : Lancé sur http://127.0.0.1:8000/

Endpoint disponible

POST /api/tasks/ : Pour créer une nouvelle tâche

GET /api/tasks/ : Lister toutes les tâches

GET /api/tasks/{id}/ : Détails d'une tâche

PUT /api/tasks/{id}/ : Modifier une tâche

DELETE /api/tasks/{id}/ : Supprimer une tâche