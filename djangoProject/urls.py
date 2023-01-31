"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


from polls import views
from polls.views import title_list, title_detail, loan_list, order_form, test_app
from machine.urls import urlpatterns as machine_urls

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='title_list')),
    path('admin/', admin.site.urls),
    path('registration/', include('django.contrib.auth.urls')),
    path('titles/', title_list, name='title_list'),
    path('titles/<int:title_id>/', title_detail, name='title_detail'),
    path('loans/<int:customer_id>/', loan_list, name='loan_list'),
    path('order/<int:copy_id>/', order_form, name='order_form'),
    path('machine/', include(machine_urls))
]
