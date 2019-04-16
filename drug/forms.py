from django import forms
from .models import Drug_detail, Emchilgee, Drug_important, Onosh, History
from account.models import User

class OnoshForm(forms.ModelForm):
    class Meta:
        model = Onosh

        fields = [
            'costumer',
            'name',
            'disc',
        ]
        widgets = {
            'costumer': forms.Select(attrs={'class': 'onosh-fields form-control form-control-sm'}),
            'name': forms.TextInput(attrs={'class': 'onosh-fields form-control form-control-sm'}),
            'disc': forms.TextInput(attrs={'class': 'onosh-fields form-control form-control-sm'}),
        }

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History

        fields = [
            'costumer',
            'date',
            'disc',
        ]
        widgets = {
            'costumer': forms.Select(attrs={'class': 'history-fields form-control form-control-sm'}),
            'date': forms.DateInput(attrs={"type": "date", 'class': 'history-fields form-control form-control-sm'}),
            'disc': forms.TextInput(attrs={'class': 'history-fields form-control form-control-sm'}),
        }

class Emchilgee_form(forms.ModelForm):
    class Meta:
        model = Emchilgee

        fields = [
            'duration',
            'costumer',
        ]
        widgets = {
            'duration': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'costumer': forms.Select(attrs={'class': 'form-control form-control-sm'}),
        }

        labels = {
            'duration': ('Эмчилгээ хийлгэх хоног'),
            'costumer': ('Өвчтөн'),
        }

class Drug_important_form(forms.ModelForm):
    class Meta:
        model = Drug_important

        fields = [
            'name',
            'shirheg',
            'category',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': "drug_important-fields form-control form-control-sm"}),
            'shirheg': forms.TextInput(attrs={'class': "drug_important-fields form-control form-control-sm"}),
            'category': forms.Select(attrs={'class': "drug_important-fields form-control form-control-sm"}),
        }


class Drug_detail_create_form(forms.ModelForm):
    class Meta:
        model = Drug_detail

        fields = [
            'name',
            'size',
            'nairlaga',
            'intro',
            'other_side',
            'zaavar',
            'age',
            'duration',
            'date',
            'factory',
            'price',
            'drug_catedory',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'size': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'nairlaga': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'intro': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'other_side': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'zaavar': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'age': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'duration': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'date': forms.DateInput(attrs={"type": "date", 'class': 'form-control form-control-sm'}),
            'factory': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'drug_catedory': forms.Select(attrs={'class': 'form-control form-control-sm'}),
        }

        labels = {
            'name': ('Эмийн нэр'),
            'size': ('Эмийн доз'),
            'nairlaga': ('Найрлага'),
            'intro': ('Ерөнхий үйлчлэл'),
            'other_side': ('Гаж нөлөө'),
            'zaavar': ('Хэрэглэх заавар'),
            'age': ('Хэрэглэж болох нас'),
            'duration': ('Хадгалах хугацаа'),
            'date': ('Үйлдвэрлэсэн он'),
            'factory': ('Үйлдвэрийн нэр'),
            'price': ('Үнэ'),
            'drug_catedory': ('Эмийн төрөл'),
        }
