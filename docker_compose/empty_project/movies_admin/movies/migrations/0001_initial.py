# Generated by Django 3.2 on 2023-09-17 12:29
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL('CREATE SCHEMA content;'),
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('creation_date', models.DateField(null=True, verbose_name='creation_date')),
                ('rating', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='rating')),
                ('type', models.TextField(choices=[('movie', 'Movie'), ('tv_show', 'Tv Show')], verbose_name='type')),
                ('certificate', models.CharField(blank=True, max_length=512, verbose_name='certificate')),
                ('file_path', models.FileField(blank=True, null=True, upload_to='movies/', verbose_name='file')),
            ],
            options={
                'verbose_name': 'Киноработа',
                'verbose_name_plural': 'Киноработы',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'db_table': 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255, verbose_name='full_name')),
                ('gender', models.TextField(choices=[('male', 'male'), ('female', 'female')], null=True, verbose_name='gender')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
                'db_table': 'content"."person',
            },
        ),
        migrations.CreateModel(
            name='PersonFilmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.TextField(choices=[('director', 'director'), ('screenwriter', 'screenwriter'), ('actor', 'actor')], null=True, verbose_name='role')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
            options={
                'db_table': 'content"."person_film_work',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
            options={
                'db_table': 'content"."genre_film_work',
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmwork', to='movies.Genre'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(through='movies.PersonFilmwork', to='movies.Person'),
        ),
        migrations.AddIndex(
            model_name='personfilmwork',
            index=models.Index(fields=['created'], name='film_work_created_idx'),
        ),
        migrations.AddConstraint(
            model_name='personfilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'person', 'role'), name='film_work_person_idx'),
        ),
        migrations.AddConstraint(
            model_name='genrefilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'genre_id'), name='film_work_genre_idx'),
        ),
    ]
