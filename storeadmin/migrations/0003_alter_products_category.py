# Generated by Django 4.1.1 on 2022-09-26 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storeadmin', '0002_alter_categories_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='storeadmin.categories'),
        ),
    ]
