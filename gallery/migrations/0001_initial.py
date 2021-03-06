# Generated by Django 4.0.4 on 2022-05-28 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='Wepukhulu', upload_to='uuploads/')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
