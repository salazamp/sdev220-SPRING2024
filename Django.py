from django.db import models

class book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  genre = models.CharField(max_length=50)
  puplication_date = models.DateField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  def __str__(self):
    return self.title