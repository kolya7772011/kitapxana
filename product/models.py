from django.db import models

# Create your models here.
Country = (
    ('qaraqalpaqistan','Qaraqalpaqistan'),
    ('Uzbekistan','Uzbekistan'),
)

class AvtorModel(models.Model):
    full_name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='foto/'),
    birthday = models.DateField()
    country = models.CharField(max_length=100,choices=Country)
    create_ad = models.DateTimeField(auto_now_add=True)
class Meta:
    db_table = "AvtorModel"
    def __str__(self):
          return self.full_name
class BookModel(models.Model):
    name = models.CharField(max_length=100)
    page = models.IntegerField()
    foto = models.ImageField(upload_to='foto/'),
    price = models.PositiveIntegerField()
    year = models.IntegerField()
    avtor = models.ForeignKey(AvtorModel, on_delete=models.CASCADE)

class Meta:
    db_table = "BookModel"
    def __str__(self):
       return self.name