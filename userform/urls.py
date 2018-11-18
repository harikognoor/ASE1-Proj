from django.urls import path
from userform import views

#template urls
app_name='userform'
urlpatterns=[path ('register/',views.register,name='register'),
path ('login/',views.user_login,name='login'),
]
