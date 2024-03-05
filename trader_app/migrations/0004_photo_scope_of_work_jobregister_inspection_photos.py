# Generated by Django 4.1.4 on 2024-03-05 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trader_app', '0003_windingdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
            ],
            options={
                'verbose_name_plural': 'photos',
            },
        ),
        migrations.CreateModel(
            name='scope_of_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_no', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('to', models.TextField(default='<name of the officer>\n<designation>\n<address_line>\n')),
                ('sub', models.TextField()),
                ('ref', models.TextField()),
                ('scope_of_work', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader_app.jobregister')),
            ],
            options={
                'verbose_name_plural': 'Scope of Works',
            },
        ),
        migrations.AddField(
            model_name='jobregister',
            name='inspection_photos',
            field=models.ManyToManyField(help_text='Select multiple photos', to='trader_app.photo'),
        ),
    ]