from django.db import models
from datetime import date



class TopSong(models.Model):

	identificator = models.CharField(max_length=30, db_index=True)

	def __str__(self):

		return self.identificator


class Song(models.Model):

	name = models.CharField(max_length=30, db_index=True)
	author = models.CharField(max_length=30, db_index=True)
	bpm = models.CharField(max_length=30, db_index=True)
	genre = models.CharField(max_length=30, db_index=True)
	likes = models.CharField(max_length=30, db_index=True)
	version = models.CharField(max_length=30, db_index=True)
	identificator = models.CharField(max_length=30, db_index=True)
	downloads = models.CharField(max_length=30, db_index=True)
	date = models.DateField("Дата загрузки трека", default=date.today)
	audio = models.FileField("Песня", upload_to='audio/')

	def __str__(self):

		return self.name + '_' + self.author + '_' + self.version
