from django.urls import path,include
from . import views 


urlpatterns = [
    # path('login/', views.login,name='login'),
    path('account_CD/', views.account_CD,name='account_CD'),
    path('entry/', views.entry,name='entry'),


    path("accounts/",include("django.contrib.auth.urls"))


]