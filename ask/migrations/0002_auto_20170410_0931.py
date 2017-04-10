# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-10 09:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('rating', models.IntegerField(default=0, verbose_name='Rating')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='question')),
                ('text', models.TextField(verbose_name='text')),
                ('rating', models.IntegerField(default=0, verbose_name='Rating')),
            ],
            options={
                'verbose_name': 'Ask',
                'verbose_name_plural': 'Asks',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tag title')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delta', models.IntegerField(verbose_name='delta')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='ask.Answer', verbose_name='Answer')),
                ('ask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='ask.Ask', verbose_name='Ask')),
            ],
            options={
                'verbose_name': 'User vote',
                'verbose_name_plural': 'User votes',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='has admin access'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, error_messages={'unique': 'User with this username exists'}, max_length=255, unique=True, verbose_name='Username'),
        ),
        migrations.AddField(
            model_name='uservote',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='ask',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='ask',
            name='tags',
            field=models.ManyToManyField(related_name='asks', to='ask.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='answer',
            name='ask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='ask.Ask', verbose_name='Ask'),
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
    ]
