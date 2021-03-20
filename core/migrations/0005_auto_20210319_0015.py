# Generated by Django 2.2.14 on 2021-03-18 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categories',
                'verbose_name_plural': 'Categoryies',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='itemid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category', verbose_name='categories'),
        ),
    ]