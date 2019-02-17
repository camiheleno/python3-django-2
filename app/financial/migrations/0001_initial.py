# Generated by Django 2.0.10 on 2019-02-16 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('name', models.TextField()),
                ('value', models.FloatField()),
            ],
            options={
                'ordering': ('created_at', 'name'),
            },
        ),
        migrations.CreateModel(
            name='FinancialType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='financial',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.FinancialType'),
        ),
    ]