# Generated by Django 5.0.6 on 2024-07-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_ingredients_recipes_recipe_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('cr', 'created'), ('im', 'in_progress'), ('dn', 'done'), ('cn', 'canceled'), ('ex', 'expired')], max_length=2, verbose_name='Статус')),
                ('deadline', models.DateField(verbose_name='Срок выполнения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', to='app.ingredients'),
        ),
    ]
