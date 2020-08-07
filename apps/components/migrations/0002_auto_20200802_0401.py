# Generated by Django 3.0.8 on 2020-08-02 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0001_initial'),
        ('components', '0001_initial'),
        ('django_module_attr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Device'),
        ),
        migrations.AddField(
            model_name='component',
            name='metadata',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='django_module_attr.GenericData'),
        ),
        migrations.AddField(
            model_name='component',
            name='tags',
            field=models.ManyToManyField(related_name='_component_tags_+', to='django_module_attr.Tag'),
        ),
    ]
