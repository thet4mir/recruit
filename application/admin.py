from django.contrib import admin
from django.conf.urls import url
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.utils.html import format_html
from application import views
from django.http import HttpResponse
from django.template.loader import get_template

from .models import Job, General, Education, Experience, Computerskills, Otherskills, Country, City, Advantage, Abilityofsport, Languageknowledge, Awardsandprize, Maritalstatus, Youraddress, Gender, Address_type, Skills, Rate, SW_rate, Language, Degree, Relative

class EducationInline(admin.TabularInline):
    model = Education
    readonly_fields = ['school', 'end_date', 'degree', 'number', 'copy']
    can_delete = False
    def has_add_permission(self, request, obj=None):
        return False

class ExperienceInline(admin.TabularInline):
    model = Experience
    readonly_fields = ['position', 'company', 'worked_date', 'reason', 'work_task', 'achievements']
    can_delete = False
    def has_add_permission(self, request, obj=None):
        return False

class ComputerskillsInline(admin.TabularInline):
    model = Computerskills
    readonly_fields = ['skill_name', 'rate']
    can_delete = False
    def has_add_permission(self, request, obj=None):
        return False

class OtherskillsInline(admin.TabularInline):
    model = Otherskills
    readonly_fields = ['dissertation', 'dissertation_year']
    can_delete = False
    def has_add_permission(self, request, obj=None):
        return False

class LanguageknowledgeInline(admin.TabularInline):
    model = Languageknowledge
    readonly_fields = ['language_name', 'writing', 'reading', 'speaking', 'listening']
    can_delete = False
    def has_add_permission(self, request, obj=None):
        return False

class AdvantageInline(admin.TabularInline):
    model = Advantage
    readonly_fields = ['advantage', 'disadvantage', 'vision']
    can_delete = False
    def has_add_permission(self, request, obj=None):
        return False

class AbilityofsportInline(admin.TabularInline):
    model = Abilityofsport
    readonly_fields = ['typeofsport', 'traingyears', 'degreeandaward']
    can_delete = False
    def has_add_permission(self, request, obj=None):
        return False

class AwardsandprizeInline(admin.TabularInline):
    model = Awardsandprize
    readonly_fields = ['award_name', 'awarded_year', 'companyofaward']
    can_delete = False
    def has_add_permission(self, request, obj=None):
        return False

class MaritalstatusInline(admin.TabularInline):
    model = Maritalstatus
    readonly_fields = ['fl_name', 'relation', 'dateofbirth', 'current_position', 'cellphone']
    can_delete = False
    def has_add_permission(self, request, obj=None):
        return False

class YouraddressInline(admin.TabularInline):
    model = Youraddress
    readonly_fields = ['typeofaddress', 'country', 'city', 'address', 'phone1', 'phone2']
    can_delete = False
    def has_add_permission(self, request, obj=None):
        return False

class cv(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<account_id>.+)/PDF/$', self.process_deposit, name='account-deposit',
            ),
        ]
        return custom_urls + urls
    def account_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Download</a>&nbsp;',
            reverse('admin:account-deposit', args=[obj.pk]),
        )
    account_actions.short_description = 'PDF'
    account_actions.allow_tags = True

    def process_deposit(self, request, account_id):
        return self.process_action(
            request=request,
            account_id=account_id,
        )

    def process_action(self, request, account_id, *args, **kwargs):
        account = self.get_object(request, account_id)

        template = get_template('invoice.html')
        context = {}
        context['General'] = General.objects.get(pk=account_id)
        context['Experience'] = Experience.objects.filter(general=account_id)
        context['Education'] = Education.objects.get(general=account_id)

        html = template.render(context)
        return HttpResponse(html)

    def image_tag(self, obj):
        return format_html('<img src="{}" width="80"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_per_page = 15

    list_filter = (
        # for ordinary fields
        ('job'),
        # for choice fields
    )

    list_display = ('image_tag', 'last_name', 'first_name', 'register', 'job', 'gender', 'birth_day','account_actions')

    inlines = [ExperienceInline, EducationInline, ComputerskillsInline, OtherskillsInline, LanguageknowledgeInline, AdvantageInline, AbilityofsportInline, AwardsandprizeInline, MaritalstatusInline, YouraddressInline]

    readonly_fields = ['image', 'image_tag', 'last_name', 'first_name', 'register', 'job', 'gender', 'birth_day']

    search_fields = ['last_name', 'first_name', 'register', 'birth_place', 'job']

admin.site.register(Job)

admin.site.register(General, cv)
