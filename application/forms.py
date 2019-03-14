from django import forms
from crispy_forms.helper import FormHelper
from .models import General, Experience, Education, Computerskills, Otherskills, City, Country, Languageknowledge, Advantage, Abilityofsport, Awardsandprize, Maritalstatus, Youraddress, Emergency_number, Discription, Driverskill

class GeneralForm(forms.ModelForm):
	class Meta:
		model = General

		fields = [
			'image',
			'first_name',
			'last_name',
			'register',
			'job',
			'gender',
			'birth_day',
		]
		widgets = {
			'image': forms.FileInput(attrs={'class': 'form-control form-control-sm'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
			'register': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
			'job': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
			'gender': forms.Select(attrs={'class': 'form-control form-control-sm'}),
			'birth_day': forms.DateInput(attrs={
											"type":		"date",
											'class': 'computerskills-fields form-control form-control-sm'}),
		}

		labels = {
			'image': ('Цээж зураг'),
            'first_name': ('Нэр'),
			'last_name': ('Овог'),
			'register': ('Регистрийн дугаар'),
			'job': ('Сонирхож буй ажлын байр'),
			'gender': ('Хүйс'),
			'birth_day': ('Төрсөн он сар'),
        }

class EducationForm(forms.ModelForm):
	class Meta:
		model = Education

		fields = [
			'school',
			'end_date',
			'degree',
			'number',
			'copy',
		]

		widgets = {
			'school': forms.TextInput(attrs={
											"class": "education-fields form-control"
											}),
			'end_date': forms.DateInput(attrs={
											"type":		"date",
											"class": "education-fields form-control"}),
			'degree': forms.Select(attrs={"class": "education-fields form-control"}),
			'number': forms.TextInput(attrs={"class": "education-fields form-control"}),
			'copy': forms.FileInput(attrs={"class": "education-fields form-control"})
		}

class ExperienceForm(forms.ModelForm):
	class Meta:
		model = Experience

		fields = [
			'position',
			'company',
			'worked_date',
			'reason',
			'work_task',
			'achievements',
		]

		widgets = {
			'position': forms.TextInput(attrs={'class': 'experience-fields form-control'}),
			'company': forms.TextInput(attrs={'class': 'experience-fields form-control'}),
			'worked_date': forms.TextInput(attrs={'class': 'experience-fields form-control'}),
			'reason': forms.TextInput(attrs={'class': 'experience-fields form-control'}),
			'work_task': forms.Textarea(attrs={'class': 'experience-fields form-control ta_height'}),
			'achievements': forms.Textarea(attrs={'class': 'experience-fields form-control ta_height'})
		}
	def __init__(self, *args, **kwargs):
		super(ExperienceForm, self).__init__(*args, **kwargs)
		self.fields['position'].error_messages = {'required': 'custom required message'}

class ComputerskillsForm(forms.ModelForm):
	class Meta:
		model = Computerskills

		fields = [
			'skill_name',
			'rate',
		]

		widgets = {
			'skill_name': forms.Select(attrs={'class': 'computerskills-fields form-control'}),
			'rate': forms.Select(attrs={'class': 'computerskills-fields form-control'}),
		}
class OtherskillsForm(forms.ModelForm):
	class Meta:
		model = Otherskills

		fields = [
			'dissertation',
			'dissertation_year',
		]
		widgets = {
			'dissertation': forms.TextInput(attrs={'class': 'otherskills-fields form-control'}),
			'dissertation_year': forms.DateInput(attrs={
											"type":		"date",
											'class': 'otherskills-fields form-control'}),
		}
class LanguageknowledgeForm(forms.ModelForm):
	class Meta:
		model = Languageknowledge

		fields = [
			'language_name',
			'writing',
			'reading',
			'speaking',
			'listening',
		]

		widgets = {
			'language_name': forms.Select(attrs={'class': 'language-fields form-control'}),
			'writing': forms.Select(attrs={'class': 'language-fields form-control'}),
			'reading': forms.Select(attrs={'class': 'language-fields form-control'}),
			'speaking': forms.Select(attrs={'class': 'language-fields form-control'}),
			'listening': forms.Select(attrs={'class': 'language-fields form-control'}),
		}

class AdvantageForm(forms.ModelForm):
	class Meta:
		model = Advantage

		fields = [
			'advantage',
			'disadvantage',
			'vision',
		]

		widgets = {
			'advantage': forms.Textarea(attrs={'class': 'form-control cosheight'}),
			'disadvantage': forms.Textarea(attrs={'class': 'form-control cosheight'}),
			'vision': forms.Textarea(attrs={'class': 'form-control cosheight'}),
		}

class AbilityofsportForm(forms.ModelForm):
	class Meta:
		model = Abilityofsport

		fields = [
			'typeofsport',
			'traingyears',
			'degreeandaward',
		]

		widgets = {
			'typeofsport': forms.TextInput(attrs={'class': 'abilityofsport-fields form-control'}),
			'traingyears': forms.TextInput(attrs={'class': 'abilityofsport-fields form-control'}),
			'degreeandaward': forms.TextInput(attrs={'class': 'abilityofsport-fields form-control'}),
		}

class AwardsandprizeForm(forms.ModelForm):
	class Meta:
		model = Awardsandprize

		fields = [
			'award_name',
			'awarded_year',
			'companyofaward',
		]

		widgets = {
			'award_name': forms.TextInput(attrs={'class': 'awardsandprize-fields form-control'}),
			'awarded_year': forms.DateInput(attrs={"type":		"date", 'class': 'awardsandprize-fields form-control'}),
			'companyofaward': forms.TextInput(attrs={'class': 'awardsandprize-fields form-control'}),
		}

class MaritalstatusForm(forms.ModelForm):
	class Meta:
		model = Maritalstatus

		fields = [
			'fl_name',
			'relation',
			'dateofbirth',
			'current_position',
			'cellphone',
		]

		widgets = {
			'fl_name': forms.TextInput(attrs={'class': 'maritalstatus-fields form-control'}),
			'relation': forms.Select(attrs={'class': 'maritalstatus-fields form-control'}),
			'dateofbirth': forms.DateInput(attrs={
												"type":		"date",
												'class': 'maritalstatus-fields form-control'}),
			'current_position': forms.TextInput(attrs={'class': 'maritalstatus-fields form-control'}),
			'cellphone': forms.TextInput(attrs={'class': 'maritalstatus-fields form-control'}),
		}

class YouraddressForm(forms.ModelForm):
	class Meta:
		model = Youraddress

		fields = [
			'typeofaddress',
			'country',
			'city',
			'address',
			'phone1',
			'phone2',
		]

		widgets = {
			'typeofaddress': forms.Select(attrs={'class': 'form-control'}),
			'country': forms.Select(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
			'address': forms.TextInput(attrs={'class': 'form-control'}),
			'phone1': forms.TextInput(attrs={'class': 'form-control'}),
			'phone2': forms.TextInput(attrs={'class': 'form-control'}),
		}

class DiscriptionForm(forms.ModelForm):
	class Meta:
		model = Discription

		fields = [
			'name',
			'occupation',
			'position',
			'phonenumber',
		]

		widgets = {
			'name': forms.TextInput(attrs={'class': 'discription-fields form-control'}),
			'occupation': forms.TextInput(attrs={'class': 'discription-fields form-control'}),
			'position': forms.TextInput(attrs={'class': 'discription-fields form-control'}),
			'phonenumber': forms.TextInput(attrs={'class': 'discription-fields form-control'}),
		}

class Emergency_numberForm(forms.ModelForm):
	class Meta:
		model = Emergency_number

		fields = [
			'name',
			'relative',
			'phonenumber',
		]

		widgets = {
			'name': forms.TextInput(attrs={'class': 'emergency_number-fields form-control'}),
			'relative': forms.Select(attrs={'class': 'emergency_number-fields form-control'}),
			'phonenumber': forms.TextInput(attrs={'class': 'emergency_number-fields form-control'}),
		}

class DriverskillForm(forms.ModelForm):
	class Meta:
		model = Driverskill

		fields = [
			'type',
			'driving_years',
			'pro_type',
			'protype_years',
		]

		widgets = {
			'type': forms.TextInput(attrs={'class': 'form-control'}),
			'driving_years': forms.TextInput(attrs={'class': 'form-control'}),
			'pro_type': forms.TextInput(attrs={'class': 'form-control'}),
			'protype_years': forms.TextInput(attrs={'class': 'form-control'}),
		}
