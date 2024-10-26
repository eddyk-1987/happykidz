# Generated by Django 5.1.2 on 2024-10-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_cart_quantity_alter_orderplaced_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('JHR', 'Johor'), ('KDH', 'Kedah'), ('KTN', 'Kelantan'), ('MLK', 'Malacca'), ('NSN', 'Negeri Sembilan'), ('PHG', 'Pahang'), ('PNG', 'Penang'), ('PRK', 'Perak'), ('PLS', 'Perlis'), ('SBH', 'Sabah'), ('SWK', 'Sarawak'), ('SGR', 'Selangor'), ('TRG', 'Terengganu'), ('KUL', 'Kuala Lumpur'), ('LBN', 'Labuan'), ('PJY', 'Putrajaya')], max_length=54),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Painting'), ('L', 'Handcraft'), ('TW', 'Subscription'), ('BW', 'Bottom Wear')], max_length=2),
        ),
    ]