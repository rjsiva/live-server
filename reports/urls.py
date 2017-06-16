from django.conf.urls import patterns, url
from reports.views import *
from reports.genderwise_reports import *
# from reports.moi_reports import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=login_required(BaseView.as_view()),
        name='base_report'
    ),

   # url(
   #      regex=r'^aadhaar_report/$',
   #      view=aadhaar_report.as_view(),
   #      name='aadhaar_report'
   #  ),
    
    url(regex=r'^state_level_aadhaar_report/$',
        view=login_required(state_level_aadhaar_report.as_view()),
        name='state_level_aadhaar_report'),

    url(regex=r'^block_overall_aadhaar_report/(?P<pk>\d+?)/(?P<pk1>\d+?)/$',
        view=login_required(block_overall_aadhaar_report.as_view()),
        name='block_overall_aadhaar_report'),

    url(regex=r'^school_level_aadhaar/(?P<pk>\d+?)/$',
        view=login_required(school_level_aadhaar.as_view()),
        name='school_level_aadhaar'),


    url(regex=r'^district_level_aadhaar_report/$',
        view=login_required(district_level_aadhaar_report.as_view()),
        name='district_level_aadhaar_report'),

    
    url(regex=r'^block_level_aadhaar_report/$',
        view=login_required(block_level_aadhaar_report.as_view()),
        name='block_level_aadhaar_report'),


# Genderwise Report

    url(regex=r'^state_level_genderwise_report/$',
        view=login_required(state_level_genderwise_report.as_view()),
        name='state_level_genderwise_report'),

    url(regex=r'^block_overall_genderwise_report/(?P<pk>\d+?)/(?P<pk1>\d+?)/(?P<pk2>\d+?)/$',
        view=login_required(block_overall_genderwise_report.as_view()),
        name='block_overall_genderwise_report'),

    url(regex=r'^school_level_genderwise/(?P<pk>\d+?)/$',
        view=login_required(school_level_genderwise.as_view()),
        name='school_level_genderwise'),

    # District Login
    url(regex=r'^district_level_genderwise_report/(?P<pk>\d+?)/$',
        view=login_required(district_level_genderwise_report.as_view()),
        name='district_level_genderwise_report'),
    
    # Block login
    url(regex=r'^block_level_genderwise_report/(?P<pk>\d+?)/$',
        view=login_required(block_level_genderwise_report.as_view()),
        name='block_level_genderwise_report'),    
    
# Medium Report
    # url(regex=r'^state_level_moi_report/$',
    #     view=login_required(state_level_moi_report.as_view()),
    #     name='state_level_moi_report'),

    
    # url(regex=r'^block_overall_moi_report/(?P<pk>\d+?)/(?P<pk1>\d+?)/(?P<pk2>\w+?)/$',
    #     view=login_required(block_overall_moi_report.as_view()),
    #     name='block_overall_moi_report'),

    # url(regex=r'^school_level_moi/(?P<pk>\d+?)/$',
    #     view=login_required(school_level_moi.as_view()),
    #     name='school_level_moi'),
    
    # District Login 
    # url(regex=r'^district_level_moi_report/(?P<pk>\d+?)/$',
    #     view=login_required(district_level_moi_report.as_view()),
    #     name='district_level_moi_report'),

    # # Block Login 
    # url(regex=r'^block_level_moi_report/(?P<pk>\d+?)/$',
    #     view=login_required(block_level_moi_report.as_view()),
    #     name='block_level_moi_report'),

# Profile Report
    # url(regex=r'^state_level_profile_report/$',
    #     view=login_required(state_level_profile_report.as_view()),
    #     name='state_level_profile_report'),

    
    # url(regex=r'^block_overall_profile_report/(?P<pk>\d+?)/(?P<pk1>\d+?)/(?P<pk2>\w+?)/$',
    #     view=login_required(block_overall_profile_report.as_view()),
    #     name='block_overall_profile_report'),

    # url(regex=r'^school_level_profile/(?P<pk>\d+?)/$',
    #     view=login_required(school_level_profile.as_view()),
    #     name='school_level_profile'),
    
    # # District Login 
    # url(regex=r'^district_level_profile_report/(?P<pk>\d+?)/$',
    #     view=login_required(district_level_profile_report.as_view()),
    #     name='district_level_profile_report'),

    # # Block Login 
    # url(regex=r'^block_level_profile_report/(?P<pk>\d+?)/$',
    #     view=login_required(block_level_profile_report.as_view()),
    #     name='block_level_profile_report'),




)


