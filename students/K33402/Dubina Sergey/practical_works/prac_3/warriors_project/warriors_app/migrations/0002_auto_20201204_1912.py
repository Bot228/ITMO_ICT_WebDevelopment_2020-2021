# Generated by Django 3.1.1 on 2020-12-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warriors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='warrior',
            field=models.ManyToManyField(blank=True, null=True, related_name='warrior_skills', through='warriors_app.SkillOfWarrior', to='warriors_app.Warrior', verbose_name='Воин'),
        ),
        migrations.AlterField(
            model_name='warrior',
            name='skill',
            field=models.ManyToManyField(related_name='warrior_skills', through='warriors_app.SkillOfWarrior', to='warriors_app.Skill', verbose_name='Умения'),
        ),
    ]
