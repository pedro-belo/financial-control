# Generated by Django 4.1.3 on 2022-11-30 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_recordentry"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="recordentry",
            options={
                "ordering": ("parent", "name"),
                "verbose_name": "Record Entry",
                "verbose_name_plural": "Records Entries",
            },
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="april",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="august",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="december",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="february",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="january",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="july",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="june",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="march",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="may",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="november",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="octuber",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="recordentry",
            name="september",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]