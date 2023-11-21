from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('VJ/',VJ,name='VJ'),
    path('JV/',JV,name='JV')
]