from django.http import HttpResponse
from django.shortcuts import render

from .models import *



def home(request):

	songs = Song.objects.all()
	topsongs = TopSong.objects.all()

	topsongs_new = []

	for topsong in topsongs:

		topsong_new = Song.objects.filter(identificator=topsong.identificator)

		topsongs_new.append(topsong_new[0])


	context = {

		"Songs": songs,
		"TopSongs": topsongs_new,

	}

	return render(request, 'music/home_test.html', context=context)
