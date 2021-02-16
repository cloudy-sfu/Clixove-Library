# Generated by Django 3.1.5 on 2021-02-15 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('papermanager', '0006_paper_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('papers', models.ManyToManyField(to='papermanager.Paper')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('users_to', models.ManyToManyField(related_name='_sharelink_users_to_+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]