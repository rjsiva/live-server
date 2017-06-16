from django.views.generic import View
from students.views.child_detail_views import *
from django.contrib import messages
from django.shortcuts import render,redirect
from students.models import Child_detail
from baseapp.models import School
from django.db.models import Q
from baseapp.models import *
from reports.models import common_reports,medium_of_instrction
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger
from datetime import *
from django import template
from django.contrib import messages
from excel_response import ExcelResponse
from django.http import HttpResponse
from django.conf import settings
import cStringIO as StringIO
from django.template.loader import get_template
from django.template import Context
from django.utils import simplejson
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count, Sum
import os
import sys


state_level_profile_report

dse_govt=[[[1],[1,2,4,5],[3,5,6,7,8,9,10]],
[[2],[6,7],[3,5,6,7,8,9,10]],
[[3],[8,12,13,14,15,16,17],[3,5,6,7,8,9,10]],
[[4],[9],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
[[5],[10,11],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
[[6],[1,2,3,4,5],[1,2,4,11,15]],
[[7],[6,7],[1,2,4,11,15]],
[[8],[8,12,13,14,15,16,17],[1,2,4,11,15]]]
all_schools=School.objects.all()
mgmt_name=["DSE - Government",
"DSE - Private Aided",
"DSE - Private UnAided",
"Matriculation",
"CBSE/ICSE",
"DEE - Government",
"DEE - Private Aided",
"DEE - Private UnAided"]

class state_level_profile_report(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated():
            global all_schools          
            for i in range(0,len(dse_govt)):   
                dse_school_list=all_schools.filter(management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])
                if int(dse_govt[i][0][0])==1:     
                	
          

                 
        return render(request,'profile/s_l_profile_report.html',locals())
