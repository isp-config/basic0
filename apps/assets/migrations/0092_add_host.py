# Generated by Django 3.1.14 on 2022-03-30 10:35

import uuid
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0091_auto_20220629_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='info',
            field=models.JSONField(blank=True, default=dict, verbose_name='Info'),
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='hostname',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ['name'], 'permissions': [('refresh_assethardwareinfo', 'Can refresh asset hardware info'), ('test_assetconnectivity', 'Can test asset connectivity'), ('push_assetsystemuser', 'Can push system user to asset'), ('match_asset', 'Can match asset'), ('add_assettonode', 'Add asset to node'), ('move_assettonode', 'Move asset to node')], 'verbose_name': 'Asset'},
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='ip',
            new_name='address',
        ),
        migrations.AddField(
            model_name='asset',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date updated'),
        ),
        migrations.AddField(
            model_name='asset',
            name='updated_by',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='created_by',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by'),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.asset')),
            ],
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.asset')),
                ('db_name', models.CharField(blank=True, max_length=1024, verbose_name='Database')),
            ],
            options={
                'verbose_name': 'Database',
            },
            bases=('assets.asset',),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.asset')),
            ],
            options={
                'abstract': False,
            },
            bases=('assets.asset',),
        ),
        migrations.CreateModel(
            name='Cloud',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.asset')),
            ],
            options={
                'abstract': False,
            },
            bases=('assets.asset',),
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.asset')),
                ('autofill', models.CharField(choices=[('no', 'Disabled'), ('basic', 'Basic'), ('script', 'Script')], default='basic', max_length=16, verbose_name='Autofill')),
                ('password_selector', models.CharField(blank=True, default='', max_length=128, verbose_name='Password selector')),
                ('submit_selector', models.CharField(blank=True, default='', max_length=128, verbose_name='Submit selector')),
                ('username_selector', models.CharField(blank=True, default='', max_length=128, verbose_name='Username selector')),
                ('script', models.JSONField(blank=True, default=list, verbose_name='Script')),
            ],
            options={
                'abstract': False,
            },
            bases=('assets.asset',),
        ),
    ]
