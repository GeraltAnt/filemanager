# Generated by Django 5.1.2 on 2024-10-18 12:33

import django.db.models.deletion
import filer.fields.file
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0017_image__transparent'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='流程阶段名称')),
                ('order', models.PositiveIntegerField(verbose_name='阶段顺序')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='物品名称')),
                ('description', models.TextField(blank=True, verbose_name='描述')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='站点名称')),
                ('description', models.TextField(blank=True, verbose_name='描述')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.CASCADE, related_name='process_files', to='filer.file', verbose_name='文件')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_app.item', verbose_name='所属物品')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_app.businessprocess', verbose_name='业务流程')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_app.site', verbose_name='所属站点'),
        ),
    ]
