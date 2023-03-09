from django.db import models
import uuid
# Create your models here.

# Définition de notre classe BasicClass, précisement un model
class BasicClass(models.Model): 
    """Model définissant les propriétés que toutes les classes modèles partagent qui sont:
    - l'identifiant (attribut: id (UUIDField))
    - le slug (attribut: slug (SlugField))
    - la date de création (attribut: created_at  (DateTimeField))
    - la date de la derniere mise à jour (attribut: update_at  (DateTimeField))"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Date de dernière modification")

    class Meta:
        abstract = True
        ordering = ['created_at']
