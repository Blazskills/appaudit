# Generated by Django 3.2.9 on 2021-12-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logisticapp', '0003_auditlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='user_language',
            field=models.CharField(default='en-US,en;q=0.9', max_length=255, verbose_name='User Language'),
            preserve_default=False,
        ),
    ]
