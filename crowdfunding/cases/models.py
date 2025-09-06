from django.db import models
from django.contrib.auth import get_user_model


class Case(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   image = models.URLField()
   is_open = models.BooleanField()
   date_created = models.DateTimeField(auto_now_add=True)
   owner = models.ForeignKey(
      get_user_model(),
      related_name='owned_cases',
      on_delete=models.CASCADE    
   )

class Judgement(models.Model):
   verdict = models.BooleanField()
   comment = models.CharField(max_length=200)
   anonymous = models.BooleanField()
   case = models.ForeignKey(
      'Case',
      related_name='judgements',
      on_delete=models.CASCADE
   )
   supporter = models.ForeignKey(
      get_user_model(),
      related_name='judgements',
      on_delete=models.CASCADE         
   )
