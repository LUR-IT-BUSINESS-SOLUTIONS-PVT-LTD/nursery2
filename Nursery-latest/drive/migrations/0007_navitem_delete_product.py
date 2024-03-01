# Generated by Django 4.2.5 on 2024-01-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0006_remove_productimage_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
