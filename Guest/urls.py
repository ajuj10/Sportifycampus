from django.urls import path
from Guest import views
app_name = "Guest"

urlpatterns = [
path('Login/',views.Login,name="Login"),

path('StudentRegistration/',views.StudentRegistration,name="StudentRegistration"),
path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),

path('index/',views.index,name="index"),

#path('CoOrdinatorRegistration/',views.CoOrdinatorRegistration,name="CoOrdinatorRegistration"

]