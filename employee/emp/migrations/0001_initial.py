# Generated by Django 3.2.4 on 2022-02-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emploee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=30)),
                ('eaddress', models.CharField(max_length=30)),
                ('ejoin_dt', models.DateField()),
                ('edept', models.CharField(max_length=30)),
            ],
        ),
    ]