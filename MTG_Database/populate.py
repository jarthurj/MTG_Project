# this is to populate the database

from mtg_app.models import *
import json

with open("newmtgdatabase.json") as file:
	data = json.load(file)
# data is a list filled with dicationaries
# each dictionary in the list is card object
count = 0

for card in data:
	print(count)
	try:
		color_identity = "".join(card['color_identity'])
	except:
		color_identity = None
	try:
		cmc = card['cmc']
	except:
		cmc = None
	try:
		colors = "".join(card['colors'])
	except:
		colors = None
	try:
		flavor_text = card['flavor_text']
	except:
		flavor_text = None
	try:
		keywords = ','.join(card['keywords'])
	except:
		keywords = None
	try:
		mana_cost = card['mana_cost']
	except:
		mana_cost = None
	try:
		oracle_text = card['oracle_text']
	except:
		oracle_text = None
	try:
		power = card['power']
	except:
		power = None

	try:
		toughness = card['toughness']
	except:
		toughness = None
	try:
		type_line = card['type_line']
	except:
		type_line = None
	name = card['name']
	artist = card['artist']
	card_id = card['id']
	try:
		img_art_crop_url = card['image_uris']['art_crop']
	except:
		img_art_crop_url = None
	try:
		img_border_crop_url = card['image_uris']['border_crop']
	except:
		img_border_crop_url = None
	try:
		img_large_url = card['image_uris']['large']
	except:
		img_large_url = None
	try:
		img_png_url = card['image_uris']['png']
	except:
		img_png_url = None
	try:
		img_small_url = card['image_uris']['small']
	except:
		img_small_url = None

	language = card['lang']
	digital = card['digital']
	rarity = card['rarity']
	set_acronym = card['set']
	set_name = card['set_name']
	set_search_uri = card['set_search_uri']
	set_type = card['set_type']


	legalities = ''
	for if_legal in card['legalities']:
		if card['legalities'][if_legal] == "legal":
			legalities += ',' + if_legal



	file.close()
