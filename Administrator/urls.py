from django.urls import path,include
from Administrator import views
#from Administrator.views import admin

app_name = "webadmin"

urlpatterns = [

path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),

path('Adminregistration/',views.Adminregistration,name="Adminregistration"),
path('delete_admin/<int:id>',views.delete_admin,name="delete_admin"),
path('edit_admin/<int:id>',views.edit_admin,name="edit_admin"),

path('admin/',views.admin,name="admin"),




#path('Eventtype/',views.Eventtype,name="Eventtype"),
#path('delete_event/<int:id>',views.delete_event,name="delete_event"),
#path('edit_event/<int:id>',views.edit_event,name="edit_event"),

path('Place/', views.place,name="Place"),

path('Semester/', views.semester,name="Semester"),
path('delete_sem/<int:id>',views.delete_sem,name="delete_sem"),
path('edit_sem/<int:id>',views.edit_sem,name="edit_sem"),


path('Subject/',views.subject,name="Subject"),
path('delete_sub/<int:id>',views.delete_sub,name="delete_sub"),
path('edit_sub/<int:id>',views.edit_sub,name="edit_sub"),



path('CoOrdinatorRegistration/',views.CoOrdinatorRegistration,name="CoOrdinatorRegistration"),
path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
path('CoordinatorListNew/',views.CordinatorListNew,name="CoordinatorListNew"),
path('acceptcordinator/<int:aid>',views.acceptcordinator,name="acceptcordinator"),
path('rejectcordinator/<int:rid>',views.rejectcordinator,name="rejectcordinator"),
path('CoordinatorListAccepted/',views.CordinatorListAccepted,name="CoordinatorListAccepted"),
path('CoordinatorListRejected/',views.CordinatorListRejected,name="CoordinatorListRejected"),

path('StudentListNew/',views.studentListNew,name="studentListNew"),
path('acceptstudent/<int:aid>',views.acceptstudent,name="acceptstudent"),
path('rejectstudent/<int:rid>',views.rejectstudent,name="rejectstudent"),
path('StudentListAccepted/',views.StudentListAccepted,name="StudentListAccepted"),
path('StudentListRejected/',views.studentListRejected,name="studentListRejected"),

#path('ComplaintReply/<int:cid>',views.ComplaintReply,name="ComplaintReply"),
#path('ComplaintView/',views.complaintview,name="ComplaintView"),

path('ViewFeedbacklList/',views.feedbackSelect,name="ViewFeedbacklList"),
path('feedbackDelete/<int:did>',views.feedbackDelete,name="feedbackDelete"),



path('department/', views.department,name="department"),
path('delete_department/<int:id>',views.delete_department,name="delete_department"),
path('edit_department/<int:id>',views.edit_department,name="edit_department"),
]
