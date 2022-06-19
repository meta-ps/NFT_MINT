from django.urls import path
from nftmint.views import *

urlpatterns = [
    path('', Home,name='home')

]
