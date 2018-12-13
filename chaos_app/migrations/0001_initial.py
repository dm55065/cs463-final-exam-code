# Generated by Django 2.1.2 on 2018-12-12 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=512)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField()),
                ('meet_date', models.DateTimeField(auto_now=True)),
                ('friend_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='chaos_app.Person')),
                ('friend_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chaos_app.Person')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='relation',
            unique_together={('friend_a', 'friend_b')},
        ),
    ]