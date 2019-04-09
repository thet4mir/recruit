from django import forms
from .models import Drug_detail

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
