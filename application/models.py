from django.db import models
from django.utils import timezone

# Create your models here.
class Address_type(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Gender(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Skills(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Rate(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class SW_rate(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Language(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Degree(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Relative(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Country(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class City(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Job(models.Model):
	job_title = models.CharField(max_length=160)

	def __str__(self):
		return self.job_title

class General(models.Model):
	image = models.FileField(upload_to='person/avatar/', blank=True, null=True, default="avatar.png")
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	register = models.CharField(max_length=10)
	job = models.CharField(max_length=60)
	gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)
	birth_day = models.DateField(default=timezone.now)

	def __str__(self):
		return self.first_name

	class Meta:
		db_table = "general"

class Experience(models.Model):
	general = models.ForeignKey(General, related_name = "experience", on_delete=models.CASCADE)
	position = models.CharField(max_length=150, null=True, blank=True)
	company = models.CharField(max_length=150, null=True, blank=True)
	worked_date = models.CharField(max_length=30,null=True, blank=True)
	reason = models.TextField(null=True, blank=True)
	work_task = models.TextField(null=True, blank=True)
	achievements = models.TextField(null=True, blank=True)

	def __str__(self):
		if self.position==None:
			return "null"
		return self.position

	class Meta:
		db_table = "experience"

class Education(models.Model):
	general = models.ForeignKey(General, related_name = "education", on_delete=models.CASCADE)
	school = models.CharField(max_length=160, null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, null=True, blank=True)
	number = models.CharField(max_length=20, null=True, blank=True)
	copy = models.FileField(upload_to='person/document/', null=True, blank=True)

	def __str__(self):
		if self.school==None:
			return "NULL"
		return self.school

	class Meta:
		db_table = "education"

class Computerskills(models.Model):
	general = models.ForeignKey(General, related_name = "computerskills", on_delete=models.CASCADE)
	skill_name = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True, blank=True)
	rate = models.ForeignKey(SW_rate, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		if self.skill_name==None:
			return "NULL"
		return self.skill_name

	class Meta:
		db_table = "computerskills"

class Otherskills(models.Model):
	general = models.ForeignKey(General, related_name = "otherskills", on_delete=models.CASCADE)
	dissertation = models.CharField(max_length=100, null=True, blank=True)
	dissertation_year = models.DateField(null=True, blank=True)

	def __str__(self):
		if self.dissertation==None:
			return "NULL"
		return self.dissertation

	class Meta:
		db_table = "otherskills"

class Languageknowledge(models.Model):
	general = models.ForeignKey(General, related_name="languageknowledge", on_delete=models.CASCADE)
	language_name = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
	writing = models.ForeignKey(Rate, related_name = "writing", on_delete=models.SET_NULL, null=True, blank=True)
	reading = models.ForeignKey(Rate, related_name = "reading", on_delete=models.SET_NULL, null=True, blank=True)
	speaking = models.ForeignKey(Rate, related_name = "speaking", on_delete=models.SET_NULL, null=True, blank=True)
	listening = models.ForeignKey(Rate, related_name = "listening", on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		if self.language_name==None:
			return "NULL"
		return self.language_name

	class Meta:
		db_table = "languageknowledge"

class Advantage(models.Model):
	general = models.ForeignKey(General, related_name="advantage", on_delete=models.CASCADE)
	advantage = models.TextField(null=True, blank=True)
	disadvantage = models.TextField(null=True, blank=True)
	vision = models.TextField(null=True, blank=True)

	def __str__(self):
		if self.advantage==None:
			return "NULL"
		return self.advantage

	class Meta:
		db_table = "advantage"

class Abilityofsport(models.Model):
	general = models.ForeignKey(General, related_name="abilityofsport", on_delete=models.CASCADE)
	typeofsport = models.CharField(max_length=60, null=True, blank=True)
	traingyears = models.CharField(max_length=10,null=True, blank=True)
	degreeandaward = models.CharField(max_length=250, null=True, blank=True)

	def __str__(self):
		if self.typeofsport==None:
			return "NULL"
		return self.typeofsport

	class Meta:
		db_table = "abilityofsport"

class Awardsandprize(models.Model):
	general = models.ForeignKey(General, related_name="awardsandprize", on_delete=models.CASCADE)
	award_name = models.CharField(max_length=150, null=True, blank=True)
	awarded_year = models.DateField(null=True, blank=True)
	companyofaward = models.CharField(max_length=150, null=True, blank=True)

	def __str__(self):
		if self.award_name==None:
			return "NULL"
		return self.award_name

	class Meta:
		db_table = 'awardsandprize'

class Maritalstatus(models.Model):
	general = models.ForeignKey(General, related_name="maritalstatus", on_delete=models.CASCADE)
	fl_name = models.CharField(max_length=150, null=True, blank=True)
	relation = models.ForeignKey(Relative, on_delete=models.SET_NULL, null=True, blank=True)
	dateofbirth = models.DateField(null=True, blank=True)
	current_position = models.CharField(max_length=150, null=True, blank=True)
	cellphone = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		if self.fl_name==None:
			return "NULL"
		return self.fl_name

	class Meta:
		db_table = 'maritalstatus'

class Youraddress(models.Model):
	general = models.ForeignKey(General, related_name="youraddress", on_delete=models.CASCADE)
	typeofaddress = models.ForeignKey(Address_type, on_delete=models.SET_NULL, null=True, blank=True)
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
	city = models.CharField(max_length=60, null=True, blank=True)
	address = models.CharField(max_length=150, null=True, blank=True)
	phone1 = models.CharField(max_length=10, null=True, blank=True)
	phone2 = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		if self.address==None:
			return "NULL"
		return self.address

	class Meta:
		db_table = 'youraddress'

class Driverskill(models.Model):
	general = models.ForeignKey(General, related_name="driverskill", on_delete=models.CASCADE)
	type = models.CharField(max_length=60, null=True, blank=True)
	driving_years = models.CharField(max_length=60, null=True, blank=True)
	pro_type = models.CharField(max_length=60, null=True, blank=True)
	protype_years = models.CharField(max_length=60, null=True, blank=True)

	def __str__(self):
		if self.type == None:
			return "NULL"
		return self.type

	class Meta:
		db_table = 'driverskill'

class Discription(models.Model):
	general = models.ForeignKey(General, related_name="discription", on_delete=models.CASCADE)
	name = models.CharField(max_length=60, null=True, blank=True)
	occupation = models.CharField(max_length=60, null=True, blank=True)
	position = models.CharField(max_length=60, null=True, blank=True)
	phonenumber = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		if self.name == None:
			return "NULL"
		return self.name

	class Meta:
		db_table = 'discription'

class Emergency_number(models.Model):
	general = models.ForeignKey(General, related_name="emergency_number", on_delete=models.CASCADE)
	name = models.CharField(max_length=60, null=True, blank=True)
	relative = models.ForeignKey(Relative, on_delete=models.SET_NULL, null=True, blank=True)
	phonenumber = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		if self.name == None:
			return "NULL"
		return self.name

	class Meta:
		db_table = 'emergency_number'
