from django.urls import path
from . import views
from . import e_views
urlpatterns=[
    # General Views
    path('',views.index,name='home'),
    path('jobs/',views.jobs,name='jobs'),
    path('job/detail/<int:job_id>',views.job_detail,name='job-detail'),
    path('job/apply',views.job_apply,name='job-apply'),
    # Company Views
    path('companies/',views.company_list,name='company-list'),
    path('company/detail/<int:id>',views.company_detail,name='company-detail'),
    path('company/register',views.company_register,name='company-register'),
    path('company/login',views.company_login,name='company-login'),
    path('company/logout',views.company_logout,name='company-logout'),
    path('company/profile',views.company_profile,name='company-profile'),
    path('company/post-job',views.post_job,name='post-job'),
    path('company/jobs',views.company_jobs,name='company-jobs'),
    path('company/applied/job/<int:id>',views.company_applied_jobs,name='company-applied-jobs'),
    path('company/jobs/detail/<int:job_id>',views.company_job_detail,name='company-job-detail'),
    path('company/jobs/update/<int:job_id>',views.company_job_update,name='company-job-update'),
    path('company/jobs/remove/<int:job_id>',views.company_job_remove,name='company-job-remove'),
    path('company/notifications',views.company_notifications,name='company-notifications'),
    # Employee Views
    path('register/',e_views.register,name='register'),
    path('login/',e_views.login,name='login'),
    path('profile',e_views.profile,name='profile'),
    path('p/profile/<int:id>/',e_views.public_profile,name='public-profile'),
    path('applied-jobs/',e_views.applied_jobs,name='applied-jobs'),
    path('recom-jobs/',e_views.recom_jobs,name='recom-jobs'),
    path('logout/',e_views.logout,name='logout'),
]
