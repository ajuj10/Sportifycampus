from django.urls import path,include
from WebAdmin import views
#from Administrator.views import admin

app_name = "WebAdmin"

urlpatterns = [
    path('Myprofile/',views.HomePage,name="HomePage"),

    path('HomePage/',views.HomePage,name="HomePage"),

    path('Department/', views.department,name="department"),
    path('delete_department/<int:id>',views.delete_department,name="delete_department"),
    path('edit_department/<int:id>',views.edit_department,name="edit_department"),


    path('AcademicYear/', views.AcademicYear,name="AcademicYear"),
    path('delAcademicYear/<int:id>',views.delAcademicYear,name="delAcademicYear"),
    path('editAcademicYear/<int:id>',views.editAcademicYear,name="editAcademicYear"),

    
    path('semesterInsertSelect/', views.semesterInsertSelect,name="semesterInsertSelect"),
    path('delete_sem/<int:id>',views.delete_sem,name="delete_sem"),
    path('edit_sem/<int:id>',views.edit_sem,name="edit_sem"),

    path('Course/', views.courserInsertSelect,name="courserInsertSelect"),
    path('delCourse/<int:id>',views.delCourse,name="delCourse"),

    path('category/',views.category,name="category"),
    path('deletecategory/<int:id>',views.delete_category,name="deletecategory"),
    path('editcategory/<int:id>',views.delete_category,name="editcategory"),
    path('ajaxcategory/',views.ajaxcategory,name="ajaxcategory"),
    
    path('Subcategory/',views.Subcategory,name="Subcategory"),
    path('deleteSubcategory/<int:id>',views.delete_subcategory,name="deleteSubcategory"),
    path('editSubcategory/<int:id>',views.edit_subcategory,name="editSubcategory"),
    

    path('StudentListNew/',views.studentListNew,name="studentListNew"),
    path('acceptstudent/<int:aid>',views.acceptstudent,name="acceptstudent"),
    path('rejectstudent/<int:rid>',views.rejectstudent,name="rejectstudent"),
    path('StudentListAccepted/',views.StudentListAccepted,name="StudentListAccepted"),
    path('StudentListRejected/',views.studentListRejected,name="studentListRejected"),


    
path('CoOrdinatorRegistration/',views.CoOrdinatorRegistration,name="CoOrdinatorRegistration"),
path('CoordinatorListNew/',views.CordinatorListNew,name="CoordinatorListNew"),
path('acceptcordinator/<int:aid>',views.acceptcordinator,name="acceptcordinator"),
path('rejectcordinator/<int:rid>',views.rejectcordinator,name="rejectcordinator"),
path('CoordinatorListAccepted/',views.CordinatorListAccepted,name="CoordinatorListAccepted"),
path('CoordinatorListRejected/',views.CordinatorListRejected,name="CoordinatorListRejected"),



path('Adminregistration/',views.Adminregistration,name="Adminregistration"),
path('delete_admin/<int:id>',views.delete_admin,name="delete_admin"),
path('edit_admin/<int:id>',views.edit_admin,name="edit_admin"),
path('admin/<int:id>',views.admin,name="admin"),                
path('logout/',views.logout,name="logout"),      


#Add new event
path('NewEvent/',views.eventInsertSelect,name="NewEvent"),  
path('eventdelete/<int:id>',views.eventdelete,name="eventdelete"),  

path('ajaxcategory/',views.ajaxcategory,name="ajaxcategory"),     



path('ComplaintReply/<int:cid>',views.ComplaintReply,name="ComplaintReply"),
path('ComplaintView/',views.complaintview,name="ComplaintView"),
path('feedbackSelect/',views.feedbackSelect,name="feedbackSelect"),
path('feedbackDelete/<int:id>',views.feedbackDelete,name="feedbackDelete"),


path('Notifications/',views.Notifications,name="Notifications"),
path('deletenotify/<int:id>',views.delete_Notifications,name="deletenotify"),

path('ViewAllresults/<int:id>',views.ViewAllResults,name="ViewAllresults"),
path('Publishresults/',views.Publishresults,name="Publishresults"),


path('deptresults/',views.deptresults,name="deptresults"),
path('PieReport/',views.PieReport,name="PieReport")
]
