from django.shortcuts import render, redirect
from .models import General, Experience, Education, Computerskills, Otherskills, City, Country, Languageknowledge, Advantage, Abilityofsport, Awardsandprize, Maritalstatus, Youraddress, Discription, Driverskill, Emergency_number
from .forms import GeneralForm, ExperienceForm, EducationForm, ComputerskillsForm, OtherskillsForm, LanguageknowledgeForm, AdvantageForm, AbilityofsportForm, AwardsandprizeForm, AbilityofsportForm, MaritalstatusForm, YouraddressForm, DiscriptionForm, DriverskillForm, Emergency_numberForm
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from django.urls import reverse_lazy

def exportPDF(request):
	context = {}
	return render(request, 'application/exportPDF.html', context)
def create(request):
	context = {}
	EducationFormset = modelformset_factory(Education, form=EducationForm)
	ExperienceFormset = modelformset_factory(Experience, form=ExperienceForm)
	ComputerskillsFormset = modelformset_factory(Computerskills, form=ComputerskillsForm)
	OtherskillsFormset = modelformset_factory(Otherskills, form=OtherskillsForm)
	LanguageFormset = modelformset_factory(Languageknowledge, form=LanguageknowledgeForm)
	AbilityofsportFormset = modelformset_factory(Abilityofsport, form=AbilityofsportForm)
	AwardsandprizeFormset = modelformset_factory(Awardsandprize, form=AwardsandprizeForm)
	MaritalstatusFormset = modelformset_factory(Maritalstatus, form=MaritalstatusForm)
	AdvantageFormset = modelformset_factory(Advantage, form=AdvantageForm)
	YouraddressFormset = modelformset_factory(Youraddress, form=YouraddressForm)
	DiscriptionFormset = modelformset_factory(Discription, form=DiscriptionForm)
	DriverskillFormset = modelformset_factory(Driverskill, form=DriverskillForm)
	Emergency_numberFormset =  modelformset_factory(Emergency_number, form=Emergency_numberForm)

	form = GeneralForm(request.POST or None, request.FILES or None)
	formset1 = EducationFormset(request.POST or None, request.FILES or None, queryset= Education.objects.none(), prefix='education')
	formset2 = ExperienceFormset(request.POST or None, queryset= Experience.objects.none(), prefix='experience')
	formset3 = ComputerskillsFormset(request.POST or None, queryset= Computerskills.objects.none(), prefix='computerskills')
	formset4 = OtherskillsFormset(request.POST or None, queryset= Otherskills.objects.none(), prefix='otherskills')
	formset5 = LanguageFormset(request.POST or None, queryset=Languageknowledge.objects.none(), prefix='languageknowledge')
	formset6 = AbilityofsportFormset(request.POST or None, queryset=Abilityofsport.objects.none(), prefix='abilityofsport')
	formset7 = AwardsandprizeFormset(request.POST or None, queryset=Awardsandprize.objects.none(), prefix='awardsandprize')
	formset8 = MaritalstatusFormset(request.POST or None, queryset=Maritalstatus.objects.none(), prefix='maritalstatus')
	formset9 = AdvantageFormset(request.POST or None, queryset=Advantage.objects.none(), prefix='advantage')
	formset10 = YouraddressFormset(request.POST or None, queryset=Youraddress.objects.none(), prefix='youraddress')
	formset11 = DiscriptionFormset(request.POST or None, queryset=Discription.objects.none(), prefix='discription')
	formset12 = DriverskillFormset(request.POST or None, queryset=Driverskill.objects.none(), prefix='driverskill')
	formset13 = Emergency_numberFormset(request.POST or None, queryset=Emergency_number.objects.none(), prefix='emergency_number')

	if request.method == "POST":
		if form.is_valid():
			try:
				with transaction.atomic():
					general = form.save(commit=False)
					general.save()

					if formset2.is_valid():
						for experience in formset2:
							data = experience.save(commit=False)
							data.general = general
							data.save()

					if formset1.is_valid():
						for education in formset1:
							data = education.save(commit=False)
							data.general = general
							data.save()

					if formset3.is_valid():
						for computerskills in formset3:
							data = computerskills.save(commit=False)
							data.general = general
							data.save()

					if formset4.is_valid():
						for otherskills in formset4:
							data = otherskills.save(commit=False)
							data.general = general
							data.save()

					if formset5.is_valid():
						for Language in formset5:
							data = Language.save(commit=False)
							data.general = general
							data.save()

					if formset6.is_valid():
						for abilityofsport in formset6:
							data = abilityofsport.save(commit=False)
							data.general = general
							data.save()

					if formset7.is_valid():
						for awardsandprize in formset7:
							data = awardsandprize.save(commit=False)
							data.general = general
							data.save()

					if formset8.is_valid():
						for maritalstatus in formset8:
							data = maritalstatus.save(commit=False)
							data.general = general
							data.save()

					if formset9.is_valid():
						for advantage in formset9:
							data = advantage.save(commit=False)
							data.general = general
							data.save()

					if formset10.is_valid():
						for youraddress in formset10:
							data = youraddress.save(commit=False)
							data.general = general
							data.save()

					if formset11.is_valid():
						for discription in formset11:
							data = discription.save(commit=False)
							data.general = general
							data.save()

					if formset12.is_valid():
						for driverskill in formset12:
							data = driverskill.save(commit=False)
							data.general = general
							data.save()

					if formset13.is_valid():
						for emergency_number in formset13:
							data = emergency_number.save(commit=False)
							data.general = general
							data.save()

			except IntegrityError:
				print("Error Encountered")

			return redirect('application:endofpage')

	context['formset13'] = formset13
	context['formset12'] = formset12
	context['formset11'] = formset11
	context['formset10'] = formset10
	context['formset9'] = formset9
	context['formset8'] = formset8
	context['formset7'] = formset7
	context['formset6'] = formset6
	context['formset5'] = formset5
	context['formset4'] = formset4
	context['formset3'] = formset3
	context['formset2'] = formset2
	context['formset1'] = formset1
	context['form'] = form

	return render(request, 'application/create.html', context)
