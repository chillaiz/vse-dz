from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    name = models.CharField(max_length=199,
                            verbose_name='Название')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    title = models.CharField(max_length=199, verbose_name= 'название')
    description = models.TextField(null=True, verbose_name='описание')
    price = models.IntegerField(default=0, null=True, verbose_name='цена')
    categorys = models.ForeignKey(Category, null=True,
                                  on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return self.title

class Review(models.Model):
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    text = models.TextField(null=True, verbose_name='текст')
    products = models.ForeignKey(Product, null=True,
                                 on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return self.text