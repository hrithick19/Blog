from django.urls import path
from . import views 
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
app_name="Post"
urlpatterns=[
    path('kavithai/',views.kavithai_page,name='kavithai'),
    path('kathai/',views.kathai_page,name='kathai'),
    path('katturai/',views.katturai_page,name='katturai'),
    path('katturai/<int:katturai_id>',views.full_katturai,name='full_katturai')
]


