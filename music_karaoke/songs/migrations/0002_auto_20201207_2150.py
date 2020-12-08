# Generated by Django 3.1.3 on 2020-12-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfavouritesong',
            name='id_song',
        ),
        migrations.RemoveField(
            model_name='userfavouritesong',
            name='id_user',
        ),
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', upload_to='media/audio_files'),
        ),
        migrations.AddField(
            model_name='song',
            name='song_image',
            field=models.ImageField(default='', upload_to='media/song_images'),
        ),
        migrations.DeleteModel(
            name='Ranking',
        ),
        migrations.DeleteModel(
            name='UserFavouriteSong',
        ),
    ]