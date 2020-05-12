from . import views
from django.urls import path

urlpatterns = [
	path('all_computers/', views.all_computers, name = 'all_computers'),
	path('desktop/', views.desktop, name = 'desktop'),
	path('monoblock/', views.monoblock, name = 'monoblock'),

	path('delivery/', views.delivery, name = 'delivery'),
	path('busket/', views.busket, name = 'busket'),
]