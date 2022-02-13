# Generated by Django 3.2.9 on 2022-02-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('oil', 'oil'), ('grains', 'grains'), ('cosmetics', 'cosmetics')], default='oil', max_length=100)),
                ('quantity', models.IntegerField()),
                ('rate_per_unit', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
