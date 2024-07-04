from django.urls import path
from CourseAdmin import views
app_name = "CourseAdmin"

urlpatterns = [
path('AddCourses/',views.courseInsertSelect,name="AddCourses"),

]