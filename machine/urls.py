from django.urls import path
from django.views.generic.base import RedirectView


from . import views


urlpatterns = [
        path('', views.main, name='machine-main'),
        path('deposits/', views.deposit_list, name='machine-deposit-list'),
        path('deposits/<int:deposit_id>', views.pick_up_deposit),
        path('closed/', RedirectView.as_view(pattern_name='machine-main'), name='machine-tray-closed'),
]
