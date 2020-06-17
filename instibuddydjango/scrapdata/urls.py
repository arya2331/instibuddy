from django.urls import path,include
from rest_framework import routers
from . import views

# router= routers.DefaultRouter()
# router.register(r'scrapcodes',views.ScrapcodeViewSet)

urlpatterns = [
    path('dept/',views.api_detail_scrapcode_view,name='detail'),
    path('name/',views.api_name_scrapcode_view,name='name'),
    path('search/',views.api_search_scrapcode_view,name='search'),
    #path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('cese/', views.get_Recipe_cese, name='get_Recipe_cese'),
    path('chem/', views.get_Recipe_chem, name='get_Recipe_chem'),
    path('mech/', views.get_Recipe_mech, name='get_Recipe_mech'),
    path('elec/', views.get_Recipe_elec, name='get_Recipe_elec'),
    path('aero/', views.get_Recipe_aero, name='get_Recipe_aero'),
    path('ctara/', views.get_Recipe_ctara, name='get_Recipe_ctara'),
    path('edtech/', views.get_Recipe_edtech, name='get_Recipe_edtech'),
    path('maths/', views.get_Recipe_maths, name='get_Recipe_maths'),
    path('chemistry/', views.get_Recipe_chemistry, name='get_Recipe_chemistry'),
    path('cse/', views.get_Recipe_cse, name='get_Recipe_cse'),
    path('hss/', views.get_Recipe_hss, name='get_Recipe_hss'),
    path('monash/', views.get_Recipe_monash, name='get_Recipe_monash'),
    path('physics/', views.get_Recipe_physics, name='get_Recipe_physics'),
    path('syscon/', views.get_Recipe_syscon, name='get_Recipe_syscon'),

]
