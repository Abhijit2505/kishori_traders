# Generated by Django 4.1.4 on 2024-03-04 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trader_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobregister',
            options={'verbose_name_plural': 'Jobs'},
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=500)),
                ('kw', models.CharField(max_length=100)),
                ('voltage_R', models.CharField(max_length=100)),
                ('voltage_Y', models.CharField(max_length=100)),
                ('voltage_B', models.CharField(max_length=100)),
                ('no_load_amps_R', models.CharField(max_length=100)),
                ('no_load_amps_Y', models.CharField(max_length=100)),
                ('no_load_amps_B', models.CharField(max_length=100)),
                ('inductance_in_H_R', models.CharField(max_length=100)),
                ('inductance_in_H_Y', models.CharField(max_length=100)),
                ('inductance_in_H_B', models.CharField(max_length=100)),
                ('resistance_in_ohms_R', models.CharField(max_length=100)),
                ('resistance_in_ohms_Y', models.CharField(max_length=100)),
                ('resistance_in_ohms_B', models.CharField(max_length=100)),
                ('vibration_NDE_axial', models.CharField(max_length=100)),
                ('vibration_NDE_horizontal', models.CharField(max_length=100)),
                ('vibration_NDE_vertical', models.CharField(max_length=100)),
                ('vibration_DE_axial', models.CharField(max_length=100)),
                ('vibration_DE_horizontal', models.CharField(max_length=100)),
                ('vibration_DE_vertical', models.CharField(max_length=100)),
                ('IR_in_M_ohms_R', models.CharField(max_length=100)),
                ('IR_in_M_ohms_Y', models.CharField(max_length=100)),
                ('IR_in_M_ohms_B', models.CharField(max_length=100)),
                ('run_out_in_MM_point_1', models.CharField(max_length=100)),
                ('run_out_in_MM_point_2', models.CharField(max_length=100)),
                ('run_out_in_MM_point_3', models.CharField(max_length=100)),
                ('run_out_in_MM_point_4', models.CharField(max_length=100)),
                ('run_out_in_MM_point_5', models.CharField(max_length=100)),
                ('run_out_in_MM_point_6', models.CharField(max_length=100)),
                ('shaft_od_in_MM_point_1', models.CharField(max_length=100)),
                ('shaft_od_in_MM_point_2', models.CharField(max_length=100)),
                ('shaft_od_in_MM_point_3', models.CharField(max_length=100)),
                ('shaft_od_in_MM_point_4', models.CharField(max_length=100)),
                ('shaft_od_in_MM_point_5', models.CharField(max_length=100)),
                ('housing_id_point_1', models.CharField(max_length=100)),
                ('housing_id_point_2', models.CharField(max_length=100)),
                ('housing_id_point_3', models.CharField(max_length=100)),
                ('housing_id_point_4', models.CharField(max_length=100)),
                ('final_observation', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader_app.jobregister')),
            ],
            options={
                'verbose_name_plural': 'Test Reports',
            },
        ),
    ]
