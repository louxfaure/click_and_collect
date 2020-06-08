from django.urls import path, re_path, include

from . import views

urlpatterns = [
    
    path('accueil', views.cart_homepage, name='homepage'),  
    # path('confirmation', views.rdv, name='rdv'')
    path('rdv/<str:pickup_loc_id>/<str:user_id>/<str:date_rdv>', views.rdv, name='rdv'),
    path('validation/<str:pickup_loc_id>', views.cart_validation, name='cart-validation'),
    path('suppression-demande/<str:request_id>/<str:institution>/<str:pickup_loc_id>', views.request_delation ,name='request-delation'),
    path('<str:user_id>/<str:institution_id>', views.index, name='index'), 
    # path('liste-demandes/<str:pickup_loc>', views.rdv_list ,name='rdv-list'),
    # path('liste-demandes/<str:pickup_loc>/<str:date>', views.rdv_list ,name='rdv-list'),
    
]