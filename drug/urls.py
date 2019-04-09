from django.conf.urls import url
from . import views

app_name = "drug"

urlpatterns = [
    url(r'^$', views.drug_detail_list, name="drug_detail_list"),
    url(r'^new/$', views.drug_detail_create, name="drug_detail_create"),
]
