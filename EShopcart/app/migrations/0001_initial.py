# Generated by Django 4.2.2 on 2023-06-23 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("locality", models.CharField(max_length=256)),
                ("city", models.CharField(max_length=54)),
                ("zipcode", models.PositiveIntegerField(null=True)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("AN", "Andaman and Nicobar Islands"),
                            ("AP", "Andhra Pradesh"),
                            ("AR", "Arunachal Pradesh"),
                            ("AS", "Assam"),
                            ("BR", "Bihar"),
                            ("CH", "Chandigarh"),
                            ("CT", "Chhattisgarh"),
                            ("DN", "Dadra and Nagar Haveli and Daman and Diu"),
                            ("DL", "Delhi"),
                            ("GA", "Goa"),
                            ("GJ", "Gujarat"),
                            ("HR", "Haryana"),
                            ("HP", "Himachal Pradesh"),
                            ("JK", "Jammu and Kashmir"),
                            ("JH", "Jharkhand"),
                            ("KA", "Karnataka"),
                            ("KL", "Kerala"),
                            ("LA", "Ladakh"),
                            ("LD", "Lakshadweep"),
                            ("MP", "Madhya Pradesh"),
                            ("MH", "Maharashtra"),
                            ("MN", "Manipur"),
                            ("ML", "Meghalaya"),
                            ("MZ", "Mizoram"),
                            ("NL", "Nagaland"),
                            ("OD", "Odisha"),
                            ("PY", "Puducherry"),
                            ("PB", "Punjab"),
                            ("RJ", "Rajasthan"),
                            ("SK", "Sikkim"),
                            ("TN", "Tamil Nadu"),
                            ("TS", "Telangana"),
                            ("TR", "Tripura"),
                            ("UP", "Uttar Pradesh"),
                            ("UK", "Uttarakhand"),
                            ("WB", "West Bengal"),
                        ],
                        max_length=54,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                ("selling_price", models.FloatField()),
                ("discounted_price", models.FloatField()),
                ("description", models.CharField(max_length=150)),
                ("brand", models.CharField(max_length=50)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("M", "Painting"),
                            ("L", "HAndc"),
                            ("TW", "Top Wear"),
                            ("BW", "Bottom Wear"),
                        ],
                        max_length=2,
                    ),
                ),
                ("product_image", models.ImageField(upload_to="productsimg")),
            ],
        ),
        migrations.CreateModel(
            name="OrderPlaced",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                ("ordered_date", models.DateField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Accepted", "Accepted"),
                            ("Packed", "Packed"),
                            ("On the way", "On the way"),
                            ("Delivered", "Delivered"),
                            ("Cancel", "Cancel"),
                        ],
                        default="Pending",
                        max_length=54,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.customer"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
