from django.shortcuts import render, HttpResponse
from .models import *
import pickle

keys = pickle.load(open('mtg_app/key_pickle.p','rb'))

def index(request):
	context = {
				'keywords':Keywords.objects.all(),
				'rarities': Rarity.objects.all(),
				'types': Type_line.objects.all(),
				
				}

	return render(request,'index.html', context)