# Generated by Django 3.2.9 on 2021-11-16 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0005_auto_20211116_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinformation',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Komedia'), (1, 'Horror'), (4, 'Drama'), (0, 'Inne'), (3, 'Sci-fi')], default=0),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, default='')),
                ('stars', models.PositiveSmallIntegerField(default=5)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmyweb.film')),
            ],
        ),
    ]
