# Generated by Django 5.1.1 on 2024-10-09 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_todo_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=300, verbose_name='Description')),
            ],
        ),
    ]
