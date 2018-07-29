
from django.conf.urls import url
from app1 import views

app_name = 'app1'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login_form,name='login_form')

]
