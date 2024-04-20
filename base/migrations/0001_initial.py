# Generated by Django 5.0.4 on 2024-04-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=55)),
                ('role', models.IntegerField(choices=[(0, 'Role Admin'), (1, 'Role Customer')], default=1)),
                ('phone', models.CharField(default=None, max_length=15, null=True)),
                ('company', models.CharField(default=None, max_length=255, null=True)),
                ('profession', models.CharField(choices=[('авитолог', 'Avitolog'), ('менеджер', 'Manager')], default='авитолог', max_length=255)),
                ('tg', models.CharField(default=None, max_length=255, null=True)),
                ('image', models.CharField(default=None, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
