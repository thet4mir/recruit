from django.conf.urls import url
from application import views
from django.views.generic import TemplateView

app_name = "application"

urlpatterns = [
    url(r'^$', views.create, name="create"),
    url(r'^endofpage/$', TemplateView.as_view(template_name='application/endofpage.html'), name="endofpage"),
]
