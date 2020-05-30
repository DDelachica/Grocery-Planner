# Generated by Django 2.2 on 2020-05-30 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_planner_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='creator',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='grocery_planner_app.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='grocery_planner_app.Ingredient'),
        ),
    ]
