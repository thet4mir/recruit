from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Drug_add, Drug_category, Drug_detail, Drug_order, Drug_order_status
from .forms import Drug_detail_create_form

# Create your views here.

def drug_detail_list(request, template_name='drug/drug_detail_list.html'):
    drug_detail = Drug_detail.objects.all()
    data = {}
    data['drug_detail'] = drug_detail
    return render(request, template_name, data)

def drug_detail_create(request, template_name='drug/drug_detail_create.html'):
    form = Drug_detail_create_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('drug:drug_detail_list')
    return render(request, template_name, {'form':form})

def book_update(request, pk, template_name='drug/drug_detail_create.html'):
    book= get_object_or_404(Drug_detail, pk=pk)
    form = BookForm(request.POST or None, instance=drug_detail)
    if form.is_valid():
        form.save()
        return redirect('books_fbv:book_list')
    return render(request, template_name, {'form':form})
