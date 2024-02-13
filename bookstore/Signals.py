from django.db.models.signals import post_save
from django.contrib.auth.models import User ,Group
from .models import Costumer

def costumer_create_profile(sender,instance,created,**kwargs):
    if created:
        group = Group.objects.get(name="costumer")
        instance.groups.add(group)

        Costumer.objects.create(
            user = instance,
            name=instance.username
        )
        print("Customer profile created !")
post_save.connect(costumer_create_profile,sender=User)

