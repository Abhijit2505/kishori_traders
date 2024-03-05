# Generated by Django 4.1.4 on 2024-03-05 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trader_app', '0006_quotation'),
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_no', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('to', models.TextField(default='<name of the officer>\n<designation>\n<address_line>\n')),
                ('sub', models.TextField()),
                ('image_captions', models.TextField(blank=True, help_text='Enter captions separated by comma', null=True)),
                ('inspection_actual_report', models.TextField()),
                ('comments', models.TextField(blank=True, help_text='comments if any', null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader_app.jobregister')),
            ],
            options={
                'verbose_name_plural': 'Inspection Reports',
            },
        ),
    ]