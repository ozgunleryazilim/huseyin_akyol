# Generated by Django 3.2 on 2022-07-06 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='surgery',
            options={'verbose_name': 'Obezite ve Metabolik Cerrahi Bloku', 'verbose_name_plural': 'Obezite ve Metabolik Cerrahi Blokları'},
        ),
        migrations.AlterModelOptions(
            name='surgerytranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Obezite ve Metabolik Cerrahi Bloku Translation'},
        ),
        migrations.AlterField(
            model_name='treatmentplanitemtranslation',
            name='info',
            field=models.CharField(max_length=100, verbose_name='Plan Maddesi'),
        ),
        migrations.AlterField(
            model_name='treatmentplantranslation',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Plan Adı'),
        ),
    ]