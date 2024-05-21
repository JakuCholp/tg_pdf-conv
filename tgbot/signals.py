from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import User_field, User_doc, Field

def get_all_finished_fields(user_doc):
    all_finsihed_fields = User_field.objects.filter(userdoc = user_doc)
    user_fields_dict = {}
    for uf in all_finsihed_fields:
        user_fields_dict[uf.field.name] = uf.value

    return user_fields_dict




@receiver(post_save, sender=User_field)
def add_first(sender, instance, **kwargs):
    user_document = instance.userdoc
    document = user_document.document
    all_field = Field.objects.filter(document=document)
    user_field = User_field.objects.filter(userdoc = instance.userdoc)
    if len(all_field) == len(user_field):
        userdoc = instance.userdoc
        value = get_all_finished_fields(userdoc)
        userdoc.result = value
        userdoc.save()

    