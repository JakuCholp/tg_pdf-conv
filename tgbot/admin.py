from django.contrib import admin
from. models import User_tg,DocumentType, Field, User_doc, User_field, UserFieldsChange
# Register your models here.
admin.site.register(User_tg)
admin.site.register(User_field)
admin.site.register(DocumentType)
admin.site.register(Field)
admin.site.register(User_doc)