from django.db import models

class Language(models.Model):
	language = models.CharField(max_length=15)
	def __str__(self):
		return f"{self.language}"

class Legalities(models.Model):
	legalities = models.CharField(max_length=100, blank=True, null=True)
	def __str__(self):
		return f"{self.legalities}"

class Color_identity(models.Model):
	color_identity = models.CharField(max_length=5, blank=True, null=True)
	def __str__(self):
		return f"{self.color_identity}"

class Colors(models.Model):
	colors = models.CharField(max_length=5, blank=True, null=True)
	def __str__(self):
		return f"{self.colors}"

class Keywords(models.Model):
	keywords = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return f"{self.keywords}"
# creat separate table for sets? Normalize the table as set_type is definitely repeated

class Set_type(models.Model):
	set_type = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return f"{self.set_type}"

class Set_acronym(models.Model):
	set_acronym = models.CharField(max_length=50, blank=True, null=True)
	set_type = models.ForeignKey(Set_type, related_name= 'acronyms',on_delete=models.CASCADE,null=True)
	def __str__(self):
		return f"{self.set_acronym}"

class Set_name(models.Model):
	set_name = models.CharField(max_length=50, blank=True, null=True)
	# set_acronym = models.OneToOneField(Set_acronym,on_delete=models.CASCADE, primary_key=True,null=True)
	# set_type = models.ForeignKey(Set_type, related_name= 'sets',on_delete=models.CASCADE,null=True)
	def __str__(self):
		return f"{self.set_name}"

class Rarity(models.Model):
	rarity = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return f"{self.rarity}"

class Type_line(models.Model):
	type_line = models.CharField(max_length=100, blank=True, null=True)
	def __str__(self):
		return f"{self.type_line}"

class Artist(models.Model):
	artist = models.CharField(max_length=100, blank=True, null=True)
	def __str__(self):
		return f"{self.artist}"

class Digital(models.Model):
	digital = models.BooleanField()
	def __str__(self):
		return f"{self.digital}"

class Manacost(models.Model):
	manacost = models.CharField(max_length=20, blank=True, null=True) 
	def __str__(self):
		return f"{self.manacost}"

class Card(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	card_id = models.CharField(max_length=100, blank=True, null=True)
	cmc = models.CharField(max_length=5,blank=True, null=True)
	power = models.CharField(max_length=3,blank=True, null=True)
	toughness = models.CharField(max_length=3,blank=True, null=True)
	flavor_text = models.TextField(blank=True, null=True)
	oracle_text = models.TextField(blank=True, null=True)

	img_art_crop_url = models.URLField(max_length=300, null=True)
	img_border_crop_url = models.URLField(max_length=300, null=True)
	img_large_url = models.URLField(max_length=300, null=True)
	img_png_url = models.URLField(max_length=300, null=True)
	img_small_url = models.URLField(max_length=300, null=True)

	language = models.ForeignKey(Language, related_name= 'cards',on_delete=models.CASCADE,null=True)
	legalities = models.ForeignKey(Legalities, related_name= 'cards',on_delete=models.CASCADE,null=True)
	# not using color identity for the data base. It has entries but not connecting any of them to cards 
	# only using color
	color_identity = models.ForeignKey(Color_identity, related_name= 'cards',on_delete=models.CASCADE,null=True)
	colors = models.ForeignKey(Colors, related_name= 'cards',on_delete=models.CASCADE,null=True)
	keywords = models.ForeignKey(Keywords, related_name= 'cards',on_delete=models.CASCADE,null=True)
	set_acronym = models.ForeignKey(Set_acronym, related_name= 'cards',on_delete=models.CASCADE,null=True)
	rarity = models.ForeignKey(Rarity, related_name= 'cards',on_delete=models.CASCADE,null=True)
	type_line = models.ForeignKey(Type_line, related_name= 'cards',on_delete=models.CASCADE,null=True)
	artist = models.ForeignKey(Artist, related_name= 'cards',on_delete=models.CASCADE,null=True)
	digital = models.ForeignKey(Digital, related_name= 'cards',on_delete=models.CASCADE,null=True)
	manacost = models.ForeignKey(Manacost, related_name= 'cards',on_delete=models.CASCADE,null=True)

	def __str__(self):
		return f"{self.name}"


