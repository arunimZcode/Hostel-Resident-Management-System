from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login_view, name='login'),
    
    # Registration
    path('register/student/', views.register_student, name='register_student'),
    path('register/authority/', views.register_authority, name='register_authority'),

    path('student_home/', views.student_home, name='student_home'),
    path('authority_home/', views.authority_home, name='authority_home'),
    path('logout/', views.logout_view, name='logout'),

    # Student actions
    path('complaint/new/', views.create_complaint, name='create_complaint'),
    path('leave/new/', views.create_leave_request, name='create_leave_request'),

    # Authority actions
    path('authority/complaints/', views.authority_complaints, name='authority_complaints'),
    path('authority/complaints/<int:complaint_id>/resolve/', views.resolve_complaint, name='resolve_complaint'),

    path('authority/leaves/', views.authority_leaves, name='authority_leaves'),
    path('authority/leaves/<int:leave_id>/approve/', views.approve_leave, name='approve_leave'),
    path('authority/leaves/<int:leave_id>/reject/', views.reject_leave, name='reject_leave'),
    path('authority/student/<int:student_id>/', views.authority_student_detail, name='authority_student_detail'),
    path('watchman/', views.watchman_view, name='watchman_view'),

    # Reports
    path('authority/complaints/report/', views.download_complaint_report, name='download_complaint_report'),
    path('authority/leaves/report/', views.download_leave_report, name='download_leave_report'),
    path("predict-supply/", views.run_supply_prediction, name="predict_supply"),
    path("trigger-maintenance-alert/", views.trigger_maintenance_alert, name="trigger_maintenance_alert"),

]
