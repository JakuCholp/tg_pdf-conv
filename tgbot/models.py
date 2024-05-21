from django.db import models

class User_tg(models.Model):
    name = models.CharField(max_length=100)
    chat_id = models.CharField(max_length=100)

class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    fields_count = models.IntegerField()
    file = models.FileField(upload_to='documents/')


class Field(models.Model):
    name = models.CharField(max_length=244)
    description = models.TextField()
    document = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    order = models.IntegerField()

class User_doc(models.Model):
    user = models.ForeignKey(User_tg, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    document = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    result = models.CharField(max_length=255)

class User_field(models.Model):
    userdoc = models.ForeignKey(User_doc, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)


class UserFieldsChange(models.Model):
    user = models.ForeignKey(User_tg, on_delete=models.CASCADE)
    user_field = models.ForeignKey(User_field, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)






