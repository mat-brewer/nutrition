# Generated by Django 3.1.5 on 2021-01-07 00:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('serving_size_g', models.DecimalField(decimal_places=1, default=100, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('total_fats', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('saturated_fats', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('mono_unsaturated_fats', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('poly_unsaturated_fats', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('total_carbohydrates', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('energy', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('sugars', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('fiber', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('calcium', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('iron', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('magnesium', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('potassium', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('sodium', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('vitamin_c', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'user', 'protein', 'total_fats', 'total_carbohydrates', 'energy', 'sugars', 'fiber', 'calcium', 'iron', 'magnesium', 'potassium', 'sodium', 'vitamin_c', 'saturated_fats', 'mono_unsaturated_fats', 'poly_unsaturated_fats')},
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('foods', models.ManyToManyField(to='MainApp.Food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('notes', models.CharField(blank=True, max_length=140, null=True)),
                ('meals', models.ManyToManyField(to='MainApp.Meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('date', 'user')},
            },
        ),
    ]