from django.db import models


# Create your models here.
class Product(models.Model):
    # name = # 여기에 코드를 작성하세요
    name = models.CharField(max_length=80)
    
    # price = # 여기에 코드를 작성하세요
    price = models.IntegerField()
    
    # img_path = # 여기에 코드를 작성하세요
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name
