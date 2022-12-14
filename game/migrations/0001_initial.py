# Generated by Django 4.1.2 on 2022-10-14 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x1', models.CharField(choices=[('X', 'X'), ('O', 'O')], max_length=2, null=True)),
                ('x2', models.CharField(choices=[('X', 'X'), ('O', 'O')], max_length=2, null=True)),
                ('x3', models.CharField(choices=[('X', 'X'), ('O', 'O')], max_length=2, null=True)),
                ('y1', models.CharField(choices=[('X', 'X'), ('O', 'O')], max_length=2, null=True)),
                ('y2', models.CharField(choices=[('X', 'X'), ('O', 'O')], max_length=2, null=True)),
                ('y3', models.CharField(choices=[('X', 'X'), ('O', 'O')], max_length=2, null=True)),
                ('z1', models.CharField(choices=[('X', 'X'), ('O', 'O')], max_length=2, null=True)),
                ('z2', models.CharField(choices=[('X', 'X'), ('O', 'O')], max_length=2, null=True)),
                ('z3', models.CharField(choices=[('X', 'X'), ('O', 'O')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('uname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.board')),
                ('player_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.player')),
                ('player_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.player')),
            ],
        ),
    ]
