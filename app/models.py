from django.db import models

class Ingredients(models.Model):
    title= models.CharField(max_length=255, verbose_name='Название')


    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name='Ингредиент'
        verbose_name_plural='Ингредиенты'



class Recipe(models.Model):
    title= models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    ingredients = models.ManyToManyField(Ingredients, related_name='recipes')    

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name='Рецепт'
        verbose_name_plural='Рецепты'


class Todo(models.Model):
    class Status(models.TextChoices):
        CREATED = 'cr', 'created'
        IN_PROGRESS = 'im', 'in_progress'
        DONE = 'dn', 'done'
        CANCELED = 'cn', 'canceled'
        EXPIRED = 'ex', 'expired'


    title= models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    status=models.CharField(max_length=2, choices=Status.choices ,verbose_name='Статус')
    deadline= models.DateField(verbose_name='Срок выполнения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return f'{self.title} ({self.get_status_display()} - {self.deadline})'
    
    class Meta:
        verbose_name='Задача'
        verbose_name_plural='Задачи'
