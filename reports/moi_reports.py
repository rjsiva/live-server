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

dse_govt=[[[1],[1,2,4,5],[3,5,6,7,8,9,10]],
[[2],[6,7],[3,5,6,7,8,9,10]],
[[3],[8,12,13,14,15,16,17],[3,5,6,7,8,9,10]],
[[4],[9],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
[[5],[10,11],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
[[6],[1,2,3,4,5],[1,2,4,11,15]],
[[7],[6,7],[1,2,4,11,15]],
[[8],[8,12,13,14,15,16,17],[1,2,4,11,15]]]
all_schools=School.objects.all()
moi=medium_of_instrction.objects.all()
enroll=common_reports.objects.all()
mgmt_name=["DSE - Government",
"DSE - Private Aided",
"DSE - Private UnAided",
"Matriculation",
"CBSE/ICSE",
"DEE - Government",
"DEE - Private Aided",
"DEE - Private UnAided"]


def medium_count_transfer(child,cls_study,trans_flag,mediumm):
    child = medium_of_instrction.objects.get(school_id=child)
    class_studying=cls_study
    transfer_flag=trans_flag
    mediuum=mediumm
    if transfer_flag == 1:
        if str(class_studying)=='I':
            if int(medium)==1:
                child.c1_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c1_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c1_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c1_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c1_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c1_urdu-=1
                child.total_urdu-=1
        elif str(class_studying)=='II':
            if int(medium)==1:
                child.c2_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c2_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c2_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c2_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c2_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c2_urdu-=1
                child.total_urdu-=1 
        elif str(class_studying)=='III':
            if int(medium)==1:
                child.c3_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c3_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c3_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c3_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c3_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c3_urdu-=1
                child.total_urdu-=1
        elif str(class_studying)=='IV':
            if int(medium)==1:
                child.c4_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c4_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c4_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c4_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c4_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c4_urdu-=1
                child.total_urdu-=1
        elif str(class_studying)=='V':
            if int(medium)==1:
                child.c5_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c5_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c5_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c5_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c5_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c5_urdu-=1
                child.total_urdu-=1
        elif str(class_studying)=='VI':
            if int(medium)==1:
                child.c6_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c6_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c6_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c6_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c6_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c6_urdu-=1
                child.total_urdu-=1
        elif str(class_studying)=='VII':
            if int(medium)==1:
                child.c7_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c7_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c7_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c7_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c7_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c7_urdu-=1
                child.total_urdu-=1
        elif str(class_studying)=='VIII':
            if int(medium)==1:
                child.c8_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c8_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c8_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c8_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c8_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c8_urdu-=1
                child.total_urdu-=1
        elif str(class_studying)=='IX':
            if int(medium)==1:
                child.c9_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c9_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c9_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c9_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c9_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c9_urdu-=1
                child.total_urdu-=1        
        elif str(class_studying)=='X':
            if int(medium)==1:
                child.c10_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c10_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c10_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c10_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c10_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c10_urdu-=1
                child.total_urdu-=1
        elif str(class_studying)=='XI':
            if int(medium)==1:
                child.c11_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c11_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c11_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c11_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c11_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c11_urdu-=1
                child.total_urdu-=1
        elif str(class_studying)=='XII':
            if int(medium)==1:
                child.c12_tamil-=1
                child.total_tamil-=1
            elif int(medium)==2:
                child.c12_eng-=1
                child.total_eng-=1
            elif int(medium)==4:
                child.c12_telugu-=1
                child.total_telugu-=1
            elif int(medium)==5:
                child.c12_mlym-=1
                child.total_mlym-=1
            elif int(medium)==6:
                child.c12_kanada-=1
                child.total_kanada-=1
            elif int(medium)==7:
                child.c12_urdu-=1
                child.total_urdu-=1
        child.save()

def medium_count_admit(child,cls_study,trans_flag,mediumm):  
    child = medium_of_instrction.objects.get(school_id=child)
    class_studying=cls_study
    transfer_flag=trans_flag
    medium=mediumm
    
    if transfer_flag == 2:
        if str(class_studying)=='I':
            if int(medium)==1:
                child.c1_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c1_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c1_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c1_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c1_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c1_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='II':
            if int(medium)==1:
                child.c2_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c2_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c2_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c2_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c2_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c2_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='III':
            if int(medium)==1:
                child.c3_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c3_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c3_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c3_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c3_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c4_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='IV':
            if int(medium)==1:
                child.c4_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c4_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c4_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c4_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c4_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c4_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='V`':
            if int(medium)==1:
                child.c5_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c5_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c5_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c5_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c5_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c5_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='VI':
            if int(medium)==1:
                child.c6_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c6_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c6_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c6_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c6_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c6_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='VII':
            if int(medium)==1:
                child.c7_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c7_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c7_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c7_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c7_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c7_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='VIII':
            if int(medium)==1:
                child.c8_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c8_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c8_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c8_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c8_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c8_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='IX':
            if int(medium)==1:
                child.c9_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c9_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c9_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c9_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c9_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c9_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='X':
            if int(medium)==1:
                child.c10_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c10_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c10_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c10_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c10_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c10_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='XI':
            if int(medium)==1:
                child.c11_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c11_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c11_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c11_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c11_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c11_urdu+=1
                child.total_urdu+=1
        elif str(class_studying)=='XII':
            if int(medium)==1:
                child.c12_tamil+=1
                child.total_tamil+=1
            elif int(medium)==2:
                child.c12_eng+=1
                child.total_eng+=1
            elif int(medium)==4:
                child.c12_telugu+=1
                child.total_telugu+=1
            elif int(medium)==5:
                child.c12_mlym+=1
                child.total_mlym+=1
            elif int(medium)==6:
                child.c12_kanada+=1
                child.total_kanada+=1
            elif int(medium)==7:
                child.c12_urdu+=1
                child.total_urdu+=1                
        child.save()

def medium_count_update(child,request2,request3,request4,request5):

    child = medium_of_instrction.objects.get(school_id=request1) #school_id
    cls_studying=request2 #before update class studying
    clss_studying=request3#class to be updated
    mediumm=request4 #new
    old_medium=request5 #old
    
    if str(cls_studying)=='I':
        if int(old_medium)==1:
            child.c1_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c1_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c1_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c1_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c1_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c1_urdu-=1
            child.total_urdu-=1
    elif str(cls_studying)=='II':
        if int(old_medium)==1:
            child.c2_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c2_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c2_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c2_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c2_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c2_urdu-=1
            child.total_urdu-=1 
    elif str(cls_studying)=='III':
        if int(old_medium)==1:
            child.c3_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c3_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c3_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c3_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c3_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c3_urdu-=1
            child.total_urdu-=1
    elif str(cls_studying)=='IV':
        if int(old_medium)==1:
            child.c4_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c4_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c4_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c4_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c4_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c4_urdu-=1
            child.total_urdu-=1
    elif str(cls_studying)=='V':
        if int(old_medium)==1:
            child.c5_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c5_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c5_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c5_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c5_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c5_urdu-=1
            child.total_urdu-=1
    elif str(cls_studying)=='VI':
        if int(old_medium)==1:
            child.c6_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c6_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c6_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c6_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c6_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c6_urdu-=1
            child.total_urdu-=1
    elif str(cls_studying)=='VII':
        if int(old_medium)==1:
            child.c7_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c7_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c7_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c7_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c7_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c7_urdu-=1
            child.total_urdu-=1
    elif str(cls_studying)=='VIII':
        if int(old_medium)==1:
            child.c8_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c8_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c8_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c8_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c8_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c8_urdu-=1
            child.total_urdu-=1
    elif str(cls_studying)=='IX':
        if int(old_medium)==1:
            child.c9_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c9_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c9_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c9_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c9_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c9_urdu-=1
            child.total_urdu-=1        
    elif str(cls_studying)=='X':
        if int(old_medium)==1:
            child.c10_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c10_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c10_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c10_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c10_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c10_urdu-=1
            child.total_urdu-=1
    elif str(cls_studying)=='XI':
        if int(old_medium)==1:
            child.c11_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c11_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c11_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c11_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c11_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c11_urdu-=1
            child.total_urdu-=1
    elif str(cls_studying)=='XII':
        if int(old_medium)==1:
            child.c12_tamil-=1
            child.total_tamil-=1
        elif int(old_medium)==2:
            child.c12_eng-=1
            child.total_eng-=1
        elif int(old_medium)==4:
            child.c12_telugu-=1
            child.total_telugu-=1
        elif int(old_medium)==5:
            child.c12_mlym-=1
            child.total_mlym-=1
        elif int(old_medium)==6:
            child.c12_kanada-=1
            child.total_kanada-=1
        elif int(old_medium)==7:
            child.c12_urdu-=1
            child.total_urdu-=1

    if str(clss_studying)=='I':
        if int(old_medium)==1:
            child.c1_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c1_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c1_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c1_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c1_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c1_urdu+=1
            child.total_urdu+=1
    elif str(clss_studying)=='II':
        if int(old_medium)==1:
            child.c2_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c2_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c2_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c2_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c2_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c2_urdu+=1
            child.total_urdu+=1
    elif str(clss_studying)=='III':
        if int(old_medium)==1:
            child.c3_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c3_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c3_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c3_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c3_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c4_urdu+=1
            child.total_urdu+=1
    elif str(clss_studying)=='IV':
        if int(old_medium)==1:
            child.c4_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c4_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c4_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c4_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c4_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c4_urdu+=1
            child.total_urdu+=1
    elif str(clss_studying)=='V`':
        if int(old_medium)==1:
            child.c5_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c5_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c5_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c5_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c5_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c5_urdu+=1
            child.total_urdu+=1
    elif str(clss_studying)=='VI':
        if int(old_medium)==1:
            child.c6_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c6_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c6_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c6_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c6_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c6_urdu+=1
            child.total_urdu+=1
    elif str(clss_studying)=='VII':
        if int(old_medium)==1:
            child.c7_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c7_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c7_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c7_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c7_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c7_urdu+=1
            child.total_urdu+=1
    elif str(clss_studying)=='VIII':
        if int(old_medium)==1:
            child.c8_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c8_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c8_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c8_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c8_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c8_urdu+=1
            child.total_urdu+=1
    elif str(clss_studying)=='IX':
        if int(old_medium)==1:
            child.c9_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c9_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c9_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c9_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c9_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c9_urdu+=1
            child.total_urdu+=1
    elif str(clss_studying)=='X':
        if int(old_medium)==1:
            child.c10_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c10_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c10_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c10_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c10_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c10_urdu+=1
            child.total_urdu+=1
    elif str(clss_studying)=='XI':
        if int(old_medium)==1:
            child.c11_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c11_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c11_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c11_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c11_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c11_urdu+=1
            child.total_urdu+=1
    elif str(clss_studying)=='XII':
        if int(old_medium)==1:
            child.c12_tamil+=1
            child.total_tamil+=1
        elif int(old_medium)==2:
            child.c12_eng+=1
            child.total_eng+=1
        elif int(old_medium)==4:
            child.c12_telugu+=1
            child.total_telugu+=1
        elif int(old_medium)==5:
            child.c12_mlym+=1
            child.total_mlym+=1
        elif int(old_medium)==6:
            child.c12_kanada+=1
            child.total_kanada+=1
        elif int(old_medium)==7:
            child.c12_urdu+=1
            child.total_urdu+=1

class state_level_moi_report(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated():
            global all_schools
            global moi
            global dse_govt
            for i in range(0,len(dse_govt)):   
                dse_school_list=all_schools.filter(management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])
                dse=moi.filter(school_id__in=dse_school_list)
                if int(dse_govt[i][0][0])==1:
                    ds_g_c1_tam=ds_g_c2_tam=ds_g_c3_tam=ds_g_c4_tam=ds_g_c5_tam=ds_g_c6_tam=ds_g_c7_tam=ds_g_c8_tam=ds_g_c9_tam=ds_g_c10_tam=ds_g_c11_tam=ds_g_c12_tam=ds_g_total_tam=0 
                    ds_g_c1_eng=ds_g_c2_eng=ds_g_c3_eng=ds_g_c4_eng=ds_g_c5_eng=ds_g_c6_eng=ds_g_c7_eng=ds_g_c8_eng=ds_g_c9_eng=ds_g_c10_eng=ds_g_c11_eng=ds_g_c12_eng=ds_g_total_eng=0 
                    ds_g_c1_telgu=ds_g_c2_telgu=ds_g_c3_telgu=ds_g_c4_telgu=ds_g_c5_telgu=ds_g_c6_telgu=ds_g_c7_telgu=ds_g_c8_telgu=ds_g_c9_telgu=ds_g_c10_telgu=ds_g_c11_telgu=ds_g_c12_telgu=ds_g_total_telgu=0 
                    ds_g_c1_malam=ds_g_c2_malam=ds_g_c3_malam=ds_g_c4_malam=ds_g_c5_malam=ds_g_c6_malam=ds_g_c7_malam=ds_g_c8_malam=ds_g_c9_malam=ds_g_c10_malam=ds_g_c11_malam=ds_g_c12_malam=ds_g_total_malam=0 
                    ds_g_c1_kanada=ds_g_c2_kanada=ds_g_c3_kanada=ds_g_c4_kanada=ds_g_c5_kanada=ds_g_c6_kanada=ds_g_c7_kanada=ds_g_c8_kanada=ds_g_c9_kanada=ds_g_c10_kanada=ds_g_c11_kanada=ds_g_c12_kanada=ds_g_total_kanada=0 
                    ds_g_c1_urudu=ds_g_c2_urudu=ds_g_c3_urudu=ds_g_c4_urudu=ds_g_c5_urudu=ds_g_c6_urudu=ds_g_c7_urudu=ds_g_c8_urudu=ds_g_c9_urudu=ds_g_c10_urudu=ds_g_c11_urudu=ds_g_c12_urudu=ds_g_total_urudu=0 
                    for j in dse:
                        ds_g_c1_tam +=j.c1_tamil
                        ds_g_c2_tam +=j.c2_tamil
                        ds_g_c3_tam +=j.c3_tamil
                        ds_g_c4_tam +=j.c4_tamil
                        ds_g_c5_tam +=j.c5_tamil
                        ds_g_c6_tam +=j.c6_tamil
                        ds_g_c7_tam +=j.c7_tamil
                        ds_g_c8_tam +=j.c8_tamil
                        ds_g_c9_tam +=j.c9_tamil
                        ds_g_c10_tam +=j.c10_tamil
                        ds_g_c11_tam +=j.c11_tamil
                        ds_g_c12_tam +=j.c12_tamil
                        ds_g_total_tam+=j.total_tamil

                        ds_g_c1_eng +=j.c1_eng
                        ds_g_c2_eng +=j.c2_eng
                        ds_g_c3_eng +=j.c3_eng
                        ds_g_c4_eng +=j.c4_eng
                        ds_g_c5_eng +=j.c5_eng
                        ds_g_c6_eng +=j.c6_eng
                        ds_g_c7_eng +=j.c7_eng
                        ds_g_c8_eng +=j.c8_eng
                        ds_g_c9_eng +=j.c9_eng
                        ds_g_c10_eng +=j.c10_eng
                        ds_g_c11_eng +=j.c11_eng
                        ds_g_c12_eng +=j.c12_eng
                        ds_g_total_eng+=j.total_eng

                        ds_g_c1_telgu +=j.c1_telugu
                        ds_g_c2_telgu +=j.c2_telugu
                        ds_g_c3_telgu +=j.c3_telugu
                        ds_g_c4_telgu +=j.c4_telugu
                        ds_g_c5_telgu +=j.c5_telugu
                        ds_g_c6_telgu +=j.c6_telugu
                        ds_g_c7_telgu +=j.c7_telugu
                        ds_g_c8_telgu +=j.c8_telugu
                        ds_g_c9_telgu +=j.c9_telugu
                        ds_g_c10_telgu +=j.c10_telugu
                        ds_g_c11_telgu +=j.c11_telugu
                        ds_g_c12_telgu +=j.c12_telugu
                        ds_g_total_telgu+=j.total_telugu
                        
                        ds_g_c1_malam +=j.c1_mlym
                        ds_g_c2_malam +=j.c2_mlym
                        ds_g_c3_malam +=j.c3_mlym
                        ds_g_c4_malam +=j.c4_mlym
                        ds_g_c5_malam +=j.c5_mlym
                        ds_g_c6_malam +=j.c6_mlym
                        ds_g_c7_malam +=j.c7_mlym
                        ds_g_c8_malam +=j.c8_mlym
                        ds_g_c9_malam +=j.c9_mlym
                        ds_g_c10_malam +=j.c10_mlym
                        ds_g_c11_malam +=j.c11_mlym
                        ds_g_c12_malam +=j.c12_mlym
                        ds_g_total_malam+=j.total_mlym

                        ds_g_c1_kanada +=j.c1_kanada
                        ds_g_c2_kanada +=j.c2_kanada
                        ds_g_c3_kanada +=j.c3_kanada
                        ds_g_c4_kanada +=j.c4_kanada
                        ds_g_c5_kanada +=j.c5_kanada
                        ds_g_c6_kanada +=j.c6_kanada
                        ds_g_c7_kanada +=j.c7_kanada
                        ds_g_c8_kanada +=j.c8_kanada
                        ds_g_c9_kanada +=j.c9_kanada
                        ds_g_c10_kanada +=j.c10_kanada
                        ds_g_c11_kanada +=j.c11_kanada
                        ds_g_c12_kanada +=j.c12_kanada
                        ds_g_total_kanada+=j.total_kanada

                        ds_g_c1_urudu +=j.c1_urdu
                        ds_g_c2_urudu +=j.c2_urdu
                        ds_g_c3_urudu +=j.c3_urdu
                        ds_g_c4_urudu +=j.c4_urdu
                        ds_g_c5_urudu +=j.c5_urdu
                        ds_g_c6_urudu +=j.c6_urdu
                        ds_g_c7_urudu +=j.c7_urdu
                        ds_g_c8_urudu +=j.c8_urdu
                        ds_g_c9_urudu +=j.c9_urdu
                        ds_g_c10_urudu +=j.c10_urdu
                        ds_g_c11_urudu +=j.c11_urdu
                        ds_g_c12_urudu +=j.c12_urdu
                        ds_g_total_urudu+=j.total_urdu

                if int(dse_govt[i][0][0])==2:
                    ds_pa_c1_tam=ds_pa_c2_tam=ds_pa_c3_tam=ds_pa_c4_tam=ds_pa_c5_tam=ds_pa_c6_tam=ds_pa_c7_tam=ds_pa_c8_tam=ds_pa_c9_tam=ds_pa_c10_tam=ds_pa_c11_tam=ds_pa_c12_tam=ds_pa_total_tam=0
                    ds_pa_c1_eng=ds_pa_c2_eng=ds_pa_c3_eng=ds_pa_c4_eng=ds_pa_c5_eng=ds_pa_c6_eng=ds_pa_c7_eng=ds_pa_c8_eng=ds_pa_c9_eng=ds_pa_c10_eng=ds_pa_c11_eng=ds_pa_c12_eng=ds_pa_total_eng=0 
                    ds_pa_c1_telgu=ds_pa_c2_telgu=ds_pa_c3_telgu=ds_pa_c4_telgu=ds_pa_c5_telgu=ds_pa_c6_telgu=ds_pa_c7_telgu=ds_pa_c8_telgu=ds_pa_c9_telgu=ds_pa_c10_telgu=ds_pa_c11_telgu=ds_pa_c12_telgu=ds_pa_total_telgu=0 
                    ds_pa_c1_malam=ds_pa_c2_malam=ds_pa_c3_malam=ds_pa_c4_malam=ds_pa_c5_malam=ds_pa_c6_malam=ds_pa_c7_malam=ds_pa_c8_malam=ds_pa_c9_malam=ds_pa_c10_malam=ds_pa_c11_malam=ds_pa_c12_malam=ds_pa_total_malam=0 
                    ds_pa_c1_kanada=ds_pa_c2_kanada=ds_pa_c3_kanada=ds_pa_c4_kanada=ds_pa_c5_kanada=ds_pa_c6_kanada=ds_pa_c7_kanada=ds_pa_c8_kanada=ds_pa_c9_kanada=ds_pa_c10_kanada=ds_pa_c11_kanada=ds_pa_c12_kanada=ds_pa_total_kanada=0 
                    ds_pa_c1_urudu=ds_pa_c2_urudu=ds_pa_c3_urudu=ds_pa_c4_urudu=ds_pa_c5_urudu=ds_pa_c6_urudu=ds_pa_c7_urudu=ds_pa_c8_urudu=ds_pa_c9_urudu=ds_pa_c10_urudu=ds_pa_c11_urudu=ds_pa_c12_urudu=ds_pa_total_urudu=0 
                    for j in dse:
                        ds_pa_c1_tam +=j.c1_tamil
                        ds_pa_c2_tam +=j.c2_tamil
                        ds_pa_c3_tam +=j.c3_tamil
                        ds_pa_c4_tam +=j.c4_tamil
                        ds_pa_c5_tam +=j.c5_tamil
                        ds_pa_c6_tam +=j.c6_tamil
                        ds_pa_c7_tam +=j.c7_tamil
                        ds_pa_c8_tam +=j.c8_tamil
                        ds_pa_c9_tam +=j.c9_tamil
                        ds_pa_c10_tam +=j.c10_tamil
                        ds_pa_c11_tam +=j.c11_tamil
                        ds_pa_c12_tam +=j.c12_tamil
                        ds_pa_total_tam+=j.total_tamil

                        ds_pa_c1_eng +=j.c1_eng
                        ds_pa_c2_eng +=j.c2_eng
                        ds_pa_c3_eng +=j.c3_eng
                        ds_pa_c4_eng +=j.c4_eng
                        ds_pa_c5_eng +=j.c5_eng
                        ds_pa_c6_eng +=j.c6_eng
                        ds_pa_c7_eng +=j.c7_eng
                        ds_pa_c8_eng +=j.c8_eng
                        ds_pa_c9_eng +=j.c9_eng
                        ds_pa_c10_eng +=j.c10_eng
                        ds_pa_c11_eng +=j.c11_eng
                        ds_pa_c12_eng +=j.c12_eng
                        ds_pa_total_eng+=j.total_eng

                        ds_pa_c1_telgu +=j.c1_telugu
                        ds_pa_c2_telgu +=j.c2_telugu
                        ds_pa_c3_telgu +=j.c3_telugu
                        ds_pa_c4_telgu +=j.c4_telugu
                        ds_pa_c5_telgu +=j.c5_telugu
                        ds_pa_c6_telgu +=j.c6_telugu
                        ds_pa_c7_telgu +=j.c7_telugu
                        ds_pa_c8_telgu +=j.c8_telugu
                        ds_pa_c9_telgu +=j.c9_telugu
                        ds_pa_c10_telgu +=j.c10_telugu
                        ds_pa_c11_telgu +=j.c11_telugu
                        ds_pa_c12_telgu +=j.c12_telugu
                        ds_pa_total_telgu+=j.total_telugu
                        
                        ds_pa_c1_malam +=j.c1_mlym
                        ds_pa_c2_malam +=j.c2_mlym
                        ds_pa_c3_malam +=j.c3_mlym
                        ds_pa_c4_malam +=j.c4_mlym
                        ds_pa_c5_malam +=j.c5_mlym
                        ds_pa_c6_malam +=j.c6_mlym
                        ds_pa_c7_malam +=j.c7_mlym
                        ds_pa_c8_malam +=j.c8_mlym
                        ds_pa_c9_malam +=j.c9_mlym
                        ds_pa_c10_malam +=j.c10_mlym
                        ds_pa_c11_malam +=j.c11_mlym
                        ds_pa_c12_malam +=j.c12_mlym
                        ds_pa_total_malam+=j.total_mlym

                        ds_pa_c1_kanada +=j.c1_kanada
                        ds_pa_c2_kanada +=j.c2_kanada
                        ds_pa_c3_kanada +=j.c3_kanada
                        ds_pa_c4_kanada +=j.c4_kanada
                        ds_pa_c5_kanada +=j.c5_kanada
                        ds_pa_c6_kanada +=j.c6_kanada
                        ds_pa_c7_kanada +=j.c7_kanada
                        ds_pa_c8_kanada +=j.c8_kanada
                        ds_pa_c9_kanada +=j.c9_kanada
                        ds_pa_c10_kanada +=j.c10_kanada
                        ds_pa_c11_kanada +=j.c11_kanada
                        ds_pa_c12_kanada +=j.c12_kanada
                        ds_pa_total_kanada+=j.total_kanada

                        ds_pa_c1_urudu +=j.c1_urdu
                        ds_pa_c2_urudu +=j.c2_urdu
                        ds_pa_c3_urudu +=j.c3_urdu
                        ds_pa_c4_urudu +=j.c4_urdu
                        ds_pa_c5_urudu +=j.c5_urdu
                        ds_pa_c6_urudu +=j.c6_urdu
                        ds_pa_c7_urudu +=j.c7_urdu
                        ds_pa_c8_urudu +=j.c8_urdu
                        ds_pa_c9_urudu +=j.c9_urdu
                        ds_pa_c10_urudu +=j.c10_urdu
                        ds_pa_c11_urudu +=j.c11_urdu
                        ds_pa_c12_urudu +=j.c12_urdu
                        ds_pa_total_urudu+=j.total_urdu
                if int(dse_govt[i][0][0])==6:
                    dee_g_c1_tam=dee_g_c2_tam=dee_g_c3_tam=dee_g_c4_tam=dee_g_c5_tam=dee_g_c6_tam=dee_g_c7_tam=dee_g_c8_tam=dee_g_c9_tam=dee_g_c10_tam=dee_g_c11_tam=dee_g_c12_tam=dee_g_total_tam=0
                    dee_g_c1_eng=dee_g_c2_eng=dee_g_c3_eng=dee_g_c4_eng=dee_g_c5_eng=dee_g_c6_eng=dee_g_c7_eng=dee_g_c8_eng=dee_g_c9_eng=dee_g_c10_eng=dee_g_c11_eng=dee_g_c12_eng=dee_g_total_eng=0 
                    dee_g_c1_telgu=dee_g_c2_telgu=dee_g_c3_telgu=dee_g_c4_telgu=dee_g_c5_telgu=dee_g_c6_telgu=dee_g_c7_telgu=dee_g_c8_telgu=dee_g_c9_telgu=dee_g_c10_telgu=dee_g_c11_telgu=dee_g_c12_telgu=dee_g_total_telgu=0 
                    dee_g_c1_malam=dee_g_c2_malam=dee_g_c3_malam=dee_g_c4_malam=dee_g_c5_malam=dee_g_c6_malam=dee_g_c7_malam=dee_g_c8_malam=dee_g_c9_malam=dee_g_c10_malam=dee_g_c11_malam=dee_g_c12_malam=dee_g_total_malam=0 
                    dee_g_c1_kanada=dee_g_c2_kanada=dee_g_c3_kanada=dee_g_c4_kanada=dee_g_c5_kanada=dee_g_c6_kanada=dee_g_c7_kanada=dee_g_c8_kanada=dee_g_c9_kanada=dee_g_c10_kanada=dee_g_c11_kanada=dee_g_c12_kanada=dee_g_total_kanada=0 
                    dee_g_c1_urudu=dee_g_c2_urudu=dee_g_c3_urudu=dee_g_c4_urudu=dee_g_c5_urudu=dee_g_c6_urudu=dee_g_c7_urudu=dee_g_c8_urudu=dee_g_c9_urudu=dee_g_c10_urudu=dee_g_c11_urudu=dee_g_c12_urudu=dee_g_total_urudu=0 
                    for j in dse:
                        dee_g_c1_tam +=j.c1_tamil
                        dee_g_c2_tam +=j.c2_tamil
                        dee_g_c3_tam +=j.c3_tamil
                        dee_g_c4_tam +=j.c4_tamil
                        dee_g_c5_tam +=j.c5_tamil
                        dee_g_c6_tam +=j.c6_tamil
                        dee_g_c7_tam +=j.c7_tamil
                        dee_g_c8_tam +=j.c8_tamil
                        dee_g_c9_tam +=j.c9_tamil
                        dee_g_c10_tam +=j.c10_tamil
                        dee_g_c11_tam +=j.c11_tamil
                        dee_g_c12_tam +=j.c12_tamil
                        dee_g_total_tam+=j.total_tamil

                        dee_g_c1_eng +=j.c1_eng
                        dee_g_c2_eng +=j.c2_eng
                        dee_g_c3_eng +=j.c3_eng
                        dee_g_c4_eng +=j.c4_eng
                        dee_g_c5_eng +=j.c5_eng
                        dee_g_c6_eng +=j.c6_eng
                        dee_g_c7_eng +=j.c7_eng
                        dee_g_c8_eng +=j.c8_eng
                        dee_g_c9_eng +=j.c9_eng
                        dee_g_c10_eng +=j.c10_eng
                        dee_g_c11_eng +=j.c11_eng
                        dee_g_c12_eng +=j.c12_eng
                        dee_g_total_eng+=j.total_eng

                        dee_g_c1_telgu +=j.c1_telugu
                        dee_g_c2_telgu +=j.c2_telugu
                        dee_g_c3_telgu +=j.c3_telugu
                        dee_g_c4_telgu +=j.c4_telugu
                        dee_g_c5_telgu +=j.c5_telugu
                        dee_g_c6_telgu +=j.c6_telugu
                        dee_g_c7_telgu +=j.c7_telugu
                        dee_g_c8_telgu +=j.c8_telugu
                        dee_g_c9_telgu +=j.c9_telugu
                        dee_g_c10_telgu +=j.c10_telugu
                        dee_g_c11_telgu +=j.c11_telugu
                        dee_g_c12_telgu +=j.c12_telugu
                        dee_g_total_telgu+=j.total_telugu
                        
                        dee_g_c1_malam +=j.c1_mlym
                        dee_g_c2_malam +=j.c2_mlym
                        dee_g_c3_malam +=j.c3_mlym
                        dee_g_c4_malam +=j.c4_mlym
                        dee_g_c5_malam +=j.c5_mlym
                        dee_g_c6_malam +=j.c6_mlym
                        dee_g_c7_malam +=j.c7_mlym
                        dee_g_c8_malam +=j.c8_mlym
                        dee_g_c9_malam +=j.c9_mlym
                        dee_g_c10_malam +=j.c10_mlym
                        dee_g_c11_malam +=j.c11_mlym
                        dee_g_c12_malam +=j.c12_mlym
                        dee_g_total_malam+=j.total_mlym

                        dee_g_c1_kanada +=j.c1_kanada
                        dee_g_c2_kanada +=j.c2_kanada
                        dee_g_c3_kanada +=j.c3_kanada
                        dee_g_c4_kanada +=j.c4_kanada
                        dee_g_c5_kanada +=j.c5_kanada
                        dee_g_c6_kanada +=j.c6_kanada
                        dee_g_c7_kanada +=j.c7_kanada
                        dee_g_c8_kanada +=j.c8_kanada
                        dee_g_c9_kanada +=j.c9_kanada
                        dee_g_c10_kanada +=j.c10_kanada
                        dee_g_c11_kanada +=j.c11_kanada
                        dee_g_c12_kanada +=j.c12_kanada
                        dee_g_total_kanada+=j.total_kanada

                        dee_g_c1_urudu +=j.c1_urdu
                        dee_g_c2_urudu +=j.c2_urdu
                        dee_g_c3_urudu +=j.c3_urdu
                        dee_g_c4_urudu +=j.c4_urdu
                        dee_g_c5_urudu +=j.c5_urdu
                        dee_g_c6_urudu +=j.c6_urdu
                        dee_g_c7_urudu +=j.c7_urdu
                        dee_g_c8_urudu +=j.c8_urdu
                        dee_g_c9_urudu +=j.c9_urdu
                        dee_g_c10_urudu +=j.c10_urdu
                        dee_g_c11_urudu +=j.c11_urdu
                        dee_g_c12_urudu +=j.c12_urdu
                        dee_g_total_urudu+=j.total_urdu
                if int(dse_govt[i][0][0])==7:
                    dee_pa_c1_tam=dee_pa_c2_tam=dee_pa_c3_tam=dee_pa_c4_tam=dee_pa_c5_tam=dee_pa_c6_tam=dee_pa_c7_tam=dee_pa_c8_tam=dee_pa_c9_tam=dee_pa_c10_tam=dee_pa_c11_tam=dee_pa_c12_tam=dee_pa_total_tam=0
                    dee_pa_c1_eng=dee_pa_c2_eng=dee_pa_c3_eng=dee_pa_c4_eng=dee_pa_c5_eng=dee_pa_c6_eng=dee_pa_c7_eng=dee_pa_c8_eng=dee_pa_c9_eng=dee_pa_c10_eng=dee_pa_c11_eng=dee_pa_c12_eng=dee_pa_total_eng=0 
                    dee_pa_c1_telgu=dee_pa_c2_telgu=dee_pa_c3_telgu=dee_pa_c4_telgu=dee_pa_c5_telgu=dee_pa_c6_telgu=dee_pa_c7_telgu=dee_pa_c8_telgu=dee_pa_c9_telgu=dee_pa_c10_telgu=dee_pa_c11_telgu=dee_pa_c12_telgu=dee_pa_total_telgu=0 
                    dee_pa_c1_malam=dee_pa_c2_malam=dee_pa_c3_malam=dee_pa_c4_malam=dee_pa_c5_malam=dee_pa_c6_malam=dee_pa_c7_malam=dee_pa_c8_malam=dee_pa_c9_malam=dee_pa_c10_malam=dee_pa_c11_malam=dee_pa_c12_malam=dee_pa_total_malam=0 
                    dee_pa_c1_kanada=dee_pa_c2_kanada=dee_pa_c3_kanada=dee_pa_c4_kanada=dee_pa_c5_kanada=dee_pa_c6_kanada=dee_pa_c7_kanada=dee_pa_c8_kanada=dee_pa_c9_kanada=dee_pa_c10_kanada=dee_pa_c11_kanada=dee_pa_c12_kanada=dee_pa_total_kanada=0 
                    dee_pa_c1_urudu=dee_pa_c2_urudu=dee_pa_c3_urudu=dee_pa_c4_urudu=dee_pa_c5_urudu=dee_pa_c6_urudu=dee_pa_c7_urudu=dee_pa_c8_urudu=dee_pa_c9_urudu=dee_pa_c10_urudu=dee_pa_c11_urudu=dee_pa_c12_urudu=dee_pa_total_urudu=0 
                    for j in dse:
                        dee_pa_c1_tam +=j.c1_tamil
                        dee_pa_c2_tam +=j.c2_tamil
                        dee_pa_c3_tam +=j.c3_tamil
                        dee_pa_c4_tam +=j.c4_tamil
                        dee_pa_c5_tam +=j.c5_tamil
                        dee_pa_c6_tam +=j.c6_tamil
                        dee_pa_c7_tam +=j.c7_tamil
                        dee_pa_c8_tam +=j.c8_tamil
                        dee_pa_c9_tam +=j.c9_tamil
                        dee_pa_c10_tam +=j.c10_tamil
                        dee_pa_c11_tam +=j.c11_tamil
                        dee_pa_c12_tam +=j.c12_tamil
                        dee_pa_total_tam+=j.total_tamil

                        dee_pa_c1_eng +=j.c1_eng
                        dee_pa_c2_eng +=j.c2_eng
                        dee_pa_c3_eng +=j.c3_eng
                        dee_pa_c4_eng +=j.c4_eng
                        dee_pa_c5_eng +=j.c5_eng
                        dee_pa_c6_eng +=j.c6_eng
                        dee_pa_c7_eng +=j.c7_eng
                        dee_pa_c8_eng +=j.c8_eng
                        dee_pa_c9_eng +=j.c9_eng
                        dee_pa_c10_eng +=j.c10_eng
                        dee_pa_c11_eng +=j.c11_eng
                        dee_pa_c12_eng +=j.c12_eng
                        dee_pa_total_eng+=j.total_eng

                        dee_pa_c1_telgu +=j.c1_telugu
                        dee_pa_c2_telgu +=j.c2_telugu
                        dee_pa_c3_telgu +=j.c3_telugu
                        dee_pa_c4_telgu +=j.c4_telugu
                        dee_pa_c5_telgu +=j.c5_telugu
                        dee_pa_c6_telgu +=j.c6_telugu
                        dee_pa_c7_telgu +=j.c7_telugu
                        dee_pa_c8_telgu +=j.c8_telugu
                        dee_pa_c9_telgu +=j.c9_telugu
                        dee_pa_c10_telgu +=j.c10_telugu
                        dee_pa_c11_telgu +=j.c11_telugu
                        dee_pa_c12_telgu +=j.c12_telugu
                        dee_pa_total_telgu+=j.total_telugu
                        
                        dee_pa_c1_malam +=j.c1_mlym
                        dee_pa_c2_malam +=j.c2_mlym
                        dee_pa_c3_malam +=j.c3_mlym
                        dee_pa_c4_malam +=j.c4_mlym
                        dee_pa_c5_malam +=j.c5_mlym
                        dee_pa_c6_malam +=j.c6_mlym
                        dee_pa_c7_malam +=j.c7_mlym
                        dee_pa_c8_malam +=j.c8_mlym
                        dee_pa_c9_malam +=j.c9_mlym
                        dee_pa_c10_malam +=j.c10_mlym
                        dee_pa_c11_malam +=j.c11_mlym
                        dee_pa_c12_malam +=j.c12_mlym
                        dee_pa_total_malam+=j.total_mlym

                        dee_pa_c1_kanada +=j.c1_kanada
                        dee_pa_c2_kanada +=j.c2_kanada
                        dee_pa_c3_kanada +=j.c3_kanada
                        dee_pa_c4_kanada +=j.c4_kanada
                        dee_pa_c5_kanada +=j.c5_kanada
                        dee_pa_c6_kanada +=j.c6_kanada
                        dee_pa_c7_kanada +=j.c7_kanada
                        dee_pa_c8_kanada +=j.c8_kanada
                        dee_pa_c9_kanada +=j.c9_kanada
                        dee_pa_c10_kanada +=j.c10_kanada
                        dee_pa_c11_kanada +=j.c11_kanada
                        dee_pa_c12_kanada +=j.c12_kanada
                        dee_pa_total_kanada+=j.total_kanada

                        dee_pa_c1_urudu +=j.c1_urdu
                        dee_pa_c2_urudu +=j.c2_urdu
                        dee_pa_c3_urudu +=j.c3_urdu
                        dee_pa_c4_urudu +=j.c4_urdu
                        dee_pa_c5_urudu +=j.c5_urdu
                        dee_pa_c6_urudu +=j.c6_urdu
                        dee_pa_c7_urudu +=j.c7_urdu
                        dee_pa_c8_urudu +=j.c8_urdu
                        dee_pa_c9_urudu +=j.c9_urdu
                        dee_pa_c10_urudu +=j.c10_urdu
                        dee_pa_c11_urudu +=j.c11_urdu
                        dee_pa_c12_urudu +=j.c12_urdu
                        dee_pa_total_urudu+=j.total_urdu
            for i in range(0,len(dse_govt)):   
                dse_school_list=all_schools.filter(management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])
                dse=enroll.filter(school_id__in=dse_school_list)
                if int(dse_govt[i][0][0])==1:
                    ds_g_c1=ds_g_c2=ds_g_c3=ds_g_c4=ds_g_c5=ds_g_c6=ds_g_c7=ds_g_c8=ds_g_c9=ds_g_c10=ds_g_c11=ds_g_c12=ds_g_c_total=0 
                    for j in dse:
                        ds_g_c1 +=j.c1
                        ds_g_c2 +=j.c2
                        ds_g_c3 +=j.c3
                        ds_g_c4 +=j.c4
                        ds_g_c5 +=j.c5
                        ds_g_c6 +=j.c6
                        ds_g_c7 +=j.c7
                        ds_g_c8 +=j.c8
                        ds_g_c9 +=j.c9
                        ds_g_c10 +=j.c10
                        ds_g_c11 +=j.c11
                        ds_g_c12 +=j.c12
                        ds_g_c_total+=j.c_total
                if int(dse_govt[i][0][0])==2:
                    ds_pa_c1=ds_pa_c2=ds_pa_c3=ds_pa_c4=ds_pa_c5=ds_pa_c6=ds_pa_c7=ds_pa_c8=ds_pa_c9=ds_pa_c10=ds_pa_c11=ds_pa_c12=ds_pa_c_total=0 
                    for j in dse:
                        ds_pa_c1 +=j.c1
                        ds_pa_c2 +=j.c2
                        ds_pa_c3 +=j.c3
                        ds_pa_c4 +=j.c4
                        ds_pa_c5 +=j.c5
                        ds_pa_c6 +=j.c6
                        ds_pa_c7 +=j.c7
                        ds_pa_c8 +=j.c8
                        ds_pa_c9 +=j.c9
                        ds_pa_c10 +=j.c10
                        ds_pa_c11 +=j.c11
                        ds_pa_c12 +=j.c12
                        ds_pa_c_total+=j.c_total
                if int(dse_govt[i][0][0])==6:
                    dee_g_c1=dee_g_c2=dee_g_c3=dee_g_c4=dee_g_c5=dee_g_c6=dee_g_c7=dee_g_c8=dee_g_c9=dee_g_c10=dee_g_c11=dee_g_c12=dee_g_c_total=0 
                    for j in dse:
                        dee_g_c1 +=j.c1
                        dee_g_c2 +=j.c2
                        dee_g_c3 +=j.c3
                        dee_g_c4 +=j.c4
                        dee_g_c5 +=j.c5
                        dee_g_c6 +=j.c6
                        dee_g_c7 +=j.c7
                        dee_g_c8 +=j.c8
                        dee_g_c9 +=j.c9
                        dee_g_c10 +=j.c10
                        dee_g_c11 +=j.c11
                        dee_g_c12 +=j.c12
                        dee_g_c_total+=j.c_total
                if int(dse_govt[i][0][0])==7:
                    dee_pa_c1=dee_pa_c2=dee_pa_c3=dee_pa_c4=dee_pa_c5=dee_pa_c6=dee_pa_c7=dee_pa_c8=dee_pa_c9=dee_pa_c10=dee_pa_c11=dee_pa_c12=dee_pa_c_total=0 
                    for j in dse:
                        dee_pa_c1 +=j.c1
                        dee_pa_c2 +=j.c2
                        dee_pa_c3 +=j.c3
                        dee_pa_c4 +=j.c4
                        dee_pa_c5 +=j.c5
                        dee_pa_c6 +=j.c6
                        dee_pa_c7 +=j.c7
                        dee_pa_c8 +=j.c8
                        dee_pa_c9 +=j.c9
                        dee_pa_c10 +=j.c10
                        dee_pa_c11 +=j.c11
                        dee_pa_c12 +=j.c12
                        dee_pa_c_total+=j.c_total

                 
        return render(request,'moi/s_l_moi_report.html',locals())

    def post(self,request,**kwargs):      
        di_id1 = request.POST.get('distt', False)
        doc_r=di_id1.split(',')
        di_id=doc_r[0]
        doc_ready=doc_r[1]
        global dse_govt  
        global all_schools
        global enroll
        global mgmt_name
        global moi
        dist_list=District.objects.all().order_by('district_name')        
        district_ids=[]
        district_names=[]        
        dt_c1,dt_c2,dt_c3,dt_c4,dt_c5,dt_c6,dt_c7,dt_c8,dt_c9,dt_c10,dt_c11,dt_c12,dt_c_total=([] for qq in range(13))
        dt_c1_tam,dt_c2_tam,dt_c3_tam,dt_c4_tam,dt_c5_tam,dt_c6_tam,dt_c7_tam,dt_c8_tam,dt_c9_tam,dt_c10_tam,dt_c11_tam,dt_c12_tam,dt_total_tam=([] for qq1 in range(13))
        dt_c1_eng,dt_c2_eng,dt_c3_eng,dt_c4_eng,dt_c5_eng,dt_c6_eng,dt_c7_eng,dt_c8_eng,dt_c9_eng,dt_c10_eng,dt_c11_eng,dt_c12_eng,dt_total_eng=([] for qq2 in range(13))
        dt_c1_telugu,dt_c2_telugu,dt_c3_telugu,dt_c4_telugu,dt_c5_telugu,dt_c6_telugu,dt_c7_telugu,dt_c8_telugu,dt_c9_telugu,dt_c10_telugu,dt_c11_telugu,dt_c12_telugu,dt_total_telugu=([] for qq3 in range(13))
        dt_c1_mlym,dt_c2_mlym,dt_c3_mlym,dt_c4_mlym,dt_c5_mlym,dt_c6_mlym,dt_c7_mlym,dt_c8_mlym,dt_c9_mlym,dt_c10_mlym,dt_c11_mlym,dt_c12_mlym,dt_total_mlym=([] for qq1 in range(13))
        dt_c1_kanada,dt_c2_kanada,dt_c3_kanada,dt_c4_kanada,dt_c5_kanada,dt_c6_kanada,dt_c7_kanada,dt_c8_kanada,dt_c9_kanada,dt_c10_kanada,dt_c11_kanada,dt_c12_kanada,dt_total_kanada=([] for qq2 in range(13))
        dt_c1_urudu,dt_c2_urudu,dt_c3_urudu,dt_c4_urudu,dt_c5_urudu,dt_c6_urudu,dt_c7_urudu,dt_c8_urudu,dt_c9_urudu,dt_c10_urudu,dt_c11_urudu,dt_c12_urudu,dt_total_urudu=([] for qq3 in range(13))

        for ii in range(0,len(dse_govt)):
            if str(dse_govt[ii][0][0])==str(doc_r[0]):
                mgmt=dse_govt[ii][1]
                aa=dse_govt[ii][0]                
                bb=sum(aa)
                cc=int(bb)-1
                dd=mgmt_name[cc]
                for mm in dist_list:
                    district_ids.append(mm.id)              
                    district_names.append(mm.district_name)  
                    disttt=all_schools.filter(district_id=mm.id,management_id__in=dse_govt[ii][1],category_id__in=dse_govt[ii][2])
                    dist_enrol_list=enroll.filter(school_id__in=disttt) 

                    a=dist_enrol_list.aggregate(Sum('c1'))
                    b=dist_enrol_list.aggregate(Sum('c2'))
                    c=dist_enrol_list.aggregate(Sum('c3'))
                    d=dist_enrol_list.aggregate(Sum('c4'))
                    e=dist_enrol_list.aggregate(Sum('c5'))
                    f=dist_enrol_list.aggregate(Sum('c6'))
                    g=dist_enrol_list.aggregate(Sum('c7'))
                    h=dist_enrol_list.aggregate(Sum('c8'))
                    i=dist_enrol_list.aggregate(Sum('c9'))
                    j=dist_enrol_list.aggregate(Sum('c10'))
                    k=dist_enrol_list.aggregate(Sum('c11'))
                    l=dist_enrol_list.aggregate(Sum('c12'))
                    m=dist_enrol_list.aggregate(Sum('c_total'))

                    dt_c1+=a.values()                    
                    dt_c2+=b.values()
                    dt_c3+=c.values()
                    dt_c4+=d.values()
                    dt_c5+=e.values()
                    dt_c6+=f.values()
                    dt_c7+=g.values()
                    dt_c8+=h.values()
                    dt_c9+=i.values()
                    dt_c10+=j.values()
                    dt_c11+=k.values()
                    dt_c12+=l.values()
                    dt_c_total+=m.values()
     

                for jj in dist_list:                 
                    district_ids.append(jj.id)              
                    district_names.append(jj.district_name)  
                    disttt=all_schools.filter(district_id=jj.id,management_id__in=dse_govt[ii][1],category_id__in=dse_govt[ii][2])
                    dist_schl_list=moi.filter(school_id__in=disttt)  

                    n=dist_schl_list.aggregate(Sum('c1_tamil'))
                    o=dist_schl_list.aggregate(Sum('c2_tamil'))
                    p=dist_schl_list.aggregate(Sum('c3_tamil'))
                    q=dist_schl_list.aggregate(Sum('c4_tamil'))
                    r=dist_schl_list.aggregate(Sum('c5_tamil'))
                    s=dist_schl_list.aggregate(Sum('c6_tamil'))
                    t=dist_schl_list.aggregate(Sum('c7_tamil'))
                    u=dist_schl_list.aggregate(Sum('c8_tamil'))
                    v=dist_schl_list.aggregate(Sum('c9_tamil'))
                    w=dist_schl_list.aggregate(Sum('c10_tamil')) 
                    x=dist_schl_list.aggregate(Sum('c11_tamil'))
                    y=dist_schl_list.aggregate(Sum('c12_tamil'))
                    z=dist_schl_list.aggregate(Sum('total_tamil'))
                    a1=dist_schl_list.aggregate(Sum('c1_eng'))
                    b1=dist_schl_list.aggregate(Sum('c2_eng'))
                    c1=dist_schl_list.aggregate(Sum('c3_eng'))
                    d1=dist_schl_list.aggregate(Sum('c4_eng'))
                    e1=dist_schl_list.aggregate(Sum('c5_eng'))
                    f1=dist_schl_list.aggregate(Sum('c6_eng'))
                    g1=dist_schl_list.aggregate(Sum('c7_eng'))
                    h1=dist_schl_list.aggregate(Sum('c8_eng'))
                    i1=dist_schl_list.aggregate(Sum('c9_eng'))
                    j1=dist_schl_list.aggregate(Sum('c10_eng'))
                    k1=dist_schl_list.aggregate(Sum('c11_eng'))
                    l1=dist_schl_list.aggregate(Sum('c12_eng'))
                    m1=dist_schl_list.aggregate(Sum('total_eng'))
                    n1=dist_schl_list.aggregate(Sum('c1_telugu'))
                    o1=dist_schl_list.aggregate(Sum('c2_telugu'))
                    p1=dist_schl_list.aggregate(Sum('c3_telugu'))
                    q1=dist_schl_list.aggregate(Sum('c4_telugu'))
                    r1=dist_schl_list.aggregate(Sum('c5_telugu'))
                    s1=dist_schl_list.aggregate(Sum('c6_telugu'))
                    t1=dist_schl_list.aggregate(Sum('c7_telugu'))
                    u1=dist_schl_list.aggregate(Sum('c8_telugu'))
                    v1=dist_schl_list.aggregate(Sum('c9_telugu'))
                    w1=dist_schl_list.aggregate(Sum('c10_telugu'))
                    x1=dist_schl_list.aggregate(Sum('c11_telugu'))
                    y1=dist_schl_list.aggregate(Sum('c12_telugu'))
                    z1=dist_schl_list.aggregate(Sum('total_telugu'))
                    a2=dist_schl_list.aggregate(Sum('c1_mlym'))
                    b2=dist_schl_list.aggregate(Sum('c2_mlym'))
                    ccc=dist_schl_list.aggregate(Sum('c3_mlym'))
                    d2=dist_schl_list.aggregate(Sum('c4_mlym'))
                    e2=dist_schl_list.aggregate(Sum('c5_mlym'))
                    f2=dist_schl_list.aggregate(Sum('c6_mlym'))
                    g2=dist_schl_list.aggregate(Sum('c7_mlym'))
                    h2=dist_schl_list.aggregate(Sum('c8_mlym'))
                    iii=dist_schl_list.aggregate(Sum('c9_mlym'))
                    j2=dist_schl_list.aggregate(Sum('c10_mlym')) 
                    k2=dist_schl_list.aggregate(Sum('c11_mlym'))
                    l2=dist_schl_list.aggregate(Sum('c12_mlym'))
                    m2=dist_schl_list.aggregate(Sum('total_mlym'))
                    n2=dist_schl_list.aggregate(Sum('c1_kanada'))
                    o2=dist_schl_list.aggregate(Sum('c2_kanada'))
                    p2=dist_schl_list.aggregate(Sum('c3_kanada'))
                    q2=dist_schl_list.aggregate(Sum('c4_kanada'))
                    r2=dist_schl_list.aggregate(Sum('c5_kanada'))
                    s2=dist_schl_list.aggregate(Sum('c6_kanada'))
                    t2=dist_schl_list.aggregate(Sum('c7_kanada'))
                    u2=dist_schl_list.aggregate(Sum('c8_kanada'))
                    v2=dist_schl_list.aggregate(Sum('c9_kanada'))
                    w2=dist_schl_list.aggregate(Sum('c10_kanada'))
                    x2=dist_schl_list.aggregate(Sum('c11_kanada'))
                    y2=dist_schl_list.aggregate(Sum('c12_kanada'))
                    z2=dist_schl_list.aggregate(Sum('total_kanada'))
                    a3=dist_schl_list.aggregate(Sum('c1_urdu'))
                    b3=dist_schl_list.aggregate(Sum('c2_urdu'))
                    cccc=dist_schl_list.aggregate(Sum('c3_urdu'))
                    d3=dist_schl_list.aggregate(Sum('c4_urdu'))
                    e3=dist_schl_list.aggregate(Sum('c5_urdu'))
                    f3=dist_schl_list.aggregate(Sum('c6_urdu'))
                    g3=dist_schl_list.aggregate(Sum('c7_urdu'))
                    h3=dist_schl_list.aggregate(Sum('c8_urdu'))
                    iiii=dist_schl_list.aggregate(Sum('c9_urdu'))
                    j3=dist_schl_list.aggregate(Sum('c10_urdu'))
                    k3=dist_schl_list.aggregate(Sum('c11_urdu'))
                    l3=dist_schl_list.aggregate(Sum('c12_urdu'))
                    m3=dist_schl_list.aggregate(Sum('total_urdu'))

                    
                    dt_c1_tam+=n.values()
                    dt_c2_tam+=o.values()
                    dt_c3_tam+=p.values()
                    dt_c4_tam+=q.values()
                    dt_c5_tam+=r.values()
                    dt_c6_tam+=s.values()
                    dt_c7_tam+=t.values()
                    dt_c8_tam+=u.values()
                    dt_c9_tam+=v.values()
                    dt_c10_tam+=w.values()
                    dt_c11_tam+=x.values()
                    dt_c12_tam+=y.values()
                    dt_total_tam+=z.values()

                    dt_c1_eng+=a1.values()
                    dt_c2_eng+=b1.values()
                    dt_c3_eng+=c1.values()
                    dt_c4_eng+=d1.values()
                    dt_c5_eng+=e1.values()
                    dt_c6_eng+=f1.values()
                    dt_c7_eng+=g1.values()
                    dt_c8_eng+=h1.values()
                    dt_c9_eng+=i1.values()
                    dt_c10_eng+=j1.values()
                    dt_c11_eng+=k1.values()
                    dt_c12_eng+=l1.values()
                    dt_total_eng+=m1.values() 

                    dt_c1_telugu+=n1.values()
                    dt_c2_telugu+=o1.values()
                    dt_c3_telugu+=p1.values()
                    dt_c4_telugu+=q1.values()
                    dt_c5_telugu+=r1.values()
                    dt_c6_telugu+=s1.values()
                    dt_c7_telugu+=t1.values()
                    dt_c8_telugu+=u1.values()
                    dt_c9_telugu+=v1.values()
                    dt_c10_telugu+=w1.values()
                    dt_c11_telugu+=x1.values()
                    dt_c12_telugu+=y1.values()
                    dt_total_telugu+=z1.values()

                    dt_c1_mlym+=a2.values()
                    dt_c2_mlym+=b2.values()
                    dt_c3_mlym+=ccc.values()
                    dt_c4_mlym+=d2.values()
                    dt_c5_mlym+=e2.values()
                    dt_c6_mlym+=f2.values()
                    dt_c7_mlym+=g2.values()
                    dt_c8_mlym+=h2.values()
                    dt_c9_mlym+=iii.values()
                    dt_c10_mlym+=j2.values()
                    dt_c11_mlym+=k2.values()
                    dt_c12_mlym+=l2.values()
                    dt_total_mlym+=m2.values()

                    dt_c1_kanada+=n2.values()
                    dt_c2_kanada+=o2.values()
                    dt_c3_kanada+=p2.values()
                    dt_c4_kanada+=q2.values()
                    dt_c5_kanada+=r2.values()
                    dt_c6_kanada+=s2.values()
                    dt_c7_kanada+=t2.values()
                    dt_c8_kanada+=u2.values()
                    dt_c9_kanada+=v2.values()
                    dt_c10_kanada+=w2.values()
                    dt_c11_kanada+=x2.values()
                    dt_c12_kanada+=y2.values()
                    dt_total_kanada+=z2.values() 

                    dt_c1_urudu+=a3.values()
                    dt_c2_urudu+=b3.values()
                    dt_c3_urudu+=cccc.values()
                    dt_c4_urudu+=d3.values()
                    dt_c5_urudu+=e3.values()
                    dt_c6_urudu+=f3.values()
                    dt_c7_urudu+=g3.values()
                    dt_c8_urudu+=h3.values()
                    dt_c9_urudu+=iiii.values()
                    dt_c10_urudu+=j3.values()
                    dt_c11_urudu+=k3.values()
                    dt_c12_urudu+=l3.values()
                    dt_total_urudu+=m3.values()                                                 
        # a_list=zip(district_ids,district_names,dt_c1,dt_c2,dt_c3,dt_c4,dt_c5,dt_c6,dt_c7,dt_c8,dt_c9,dt_c10,dt_c11,dt_c12,dt_c_total,dt_c1_tam,dt_c2_tam,dt_c3_tam,dt_c4_tam,dt_c5_tam,dt_c6_tam,dt_c7_tam,dt_c8_tam,dt_c9_tam,dt_c10_tam,dt_c11_tam,dt_c12_tam,dt_c_total_tam,dt_c1_eng,dt_c2_eng,dt_c3_eng,dt_c4_eng,dt_c5_eng,dt_c6_eng,dt_c7_eng,dt_c8_eng,dt_c9_eng,dt_c10_eng,dt_c11_eng,dt_c12_eng,dt_c_total_eng,dt_c1_telugu,dt_c2_telugu,dt_c3_telugu,dt_c4_telugu,dt_c5_telugu,dt_c6_telugu,dt_c7_telugu,dt_c8_telugu,dt_c9_telugu,dt_c10_telugu,dt_c11_telugu,dt_c12_telugu,dt_c_total_telugu,dt_c1_mlym,dt_c2_mlym,dt_c3_mlym,dt_c4_mlym,dt_c5_mlym,dt_c6_mlym,dt_c7_mlym,dt_c8_mlym,dt_c9_mlym,dt_c10_mlym,dt_c11_mlym,dt_c12_mlym,dt_c_total_mlym,dt_c1_kanada,dt_c2_kanada,dt_c3_kanada,dt_c4_kanada,dt_c5_kanada,dt_c6_kanada,dt_c7_kanada,dt_c8_kanada,dt_c9_kanada,dt_c10_kanada,dt_c11_kanada,dt_c12_kanada,dt_c_total_kanada,dt_c1_urudu,dt_c2_urudu,dt_c3_urudu,dt_c4_urudu,dt_c5_urudu,dt_c6_urudu,dt_c7_urudu,dt_c8_urudu,dt_c9_urudu,dt_c10_urudu,dt_c11_urudu,dt_c12_urudu,dt_c_total_urudu)
        tamil_list=zip(district_ids,district_names,dt_c1_tam,dt_c2_tam,dt_c3_tam,dt_c4_tam,dt_c5_tam,dt_c6_tam,dt_c7_tam,dt_c8_tam,dt_c9_tam,dt_c10_tam,dt_c11_tam,dt_c12_tam,dt_total_tam)
        english_list=zip(district_ids,district_names,dt_c1_eng,dt_c2_eng,dt_c3_eng,dt_c4_eng,dt_c5_eng,dt_c6_eng,dt_c7_eng,dt_c8_eng,dt_c9_eng,dt_c10_eng,dt_c11_eng,dt_c12_eng,dt_total_eng)
        telugu_list=zip(district_ids,district_names,dt_c1_telugu,dt_c2_telugu,dt_c3_telugu,dt_c4_telugu,dt_c5_telugu,dt_c6_telugu,dt_c7_telugu,dt_c8_telugu,dt_c9_telugu,dt_c10_telugu,dt_c11_telugu,dt_c12_telugu,dt_total_telugu)
        mlym_list=zip(district_ids,district_names,dt_c1_mlym,dt_c2_mlym,dt_c3_mlym,dt_c4_mlym,dt_c5_mlym,dt_c6_mlym,dt_c7_mlym,dt_c8_mlym,dt_c9_mlym,dt_c10_mlym,dt_c11_mlym,dt_c12_mlym,dt_total_mlym)
        kannada_list=zip(district_ids,district_names,dt_c1_kanada,dt_c2_kanada,dt_c3_kanada,dt_c4_kanada,dt_c5_kanada,dt_c6_kanada,dt_c7_kanada,dt_c8_kanada,dt_c9_kanada,dt_c10_kanada,dt_c11_kanada,dt_c12_kanada,dt_total_kanada)
        urudu_list=zip(district_ids,district_names,dt_c1_urudu,dt_c2_urudu,dt_c3_urudu,dt_c4_urudu,dt_c5_urudu,dt_c6_urudu,dt_c7_urudu,dt_c8_urudu,dt_c9_urudu,dt_c10_urudu,dt_c11_urudu,dt_c12_urudu,dt_total_urudu)
        enrol_list=zip(district_ids,district_names,dt_c1,dt_c2,dt_c3,dt_c4,dt_c5,dt_c6,dt_c7,dt_c8,dt_c9,dt_c10,dt_c11,dt_c12,dt_c_total)
        return render(request,'moi/district_overall.html',locals())


class block_overall_moi_report(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated():
            user_access_level=[4,3]
            user=self.kwargs['pk']
            mgmt=self.kwargs['pk1']
            lang=self.kwargs['pk2']
            district=District.objects.get(id=user)    
            blocks=Block.objects.filter(district_id=user).order_by('block_name')           
            global dse_govt        
            global all_schools
            global enroll
            global mgmt_name
            global moi
            block_ids=[]
            block_names=[]
            blk_c1,blk_c2,blk_c3,blk_c4,blk_c5,blk_c6,blk_c7,blk_c8,blk_c9,blk_c10,blk_c11,blk_c12,blk_c_total=([] for zz1 in range(13))
            blk_c1_tam,blk_c2_tam,blk_c3_tam,blk_c4_tam,blk_c5_tam,blk_c6_tam,blk_c7_tam,blk_c8_tam,blk_c9_tam,blk_c10_tam,blk_c11_tam,blk_c12_tam,blk_total_tam=([] for zz2 in range(13))
            blk_c1_eng,blk_c2_eng,blk_c3_eng,blk_c4_eng,blk_c5_eng,blk_c6_eng,blk_c7_eng,blk_c8_eng,blk_c9_eng,blk_c10_eng,blk_c11_eng,blk_c12_eng,blk_total_eng=([] for zz3 in range(13))
            blk_c1_mlym,blk_c2_mlym,blk_c3_mlym,blk_c4_mlym,blk_c5_mlym,blk_c6_mlym,blk_c7_mlym,blk_c8_mlym,blk_c9_mlym,blk_c10_mlym,blk_c11_mlym,blk_c12_mlym,blk_total_mlym=([] for zz4 in range(13))
            blk_c1_telugu,blk_c2_telugu,blk_c3_telugu,blk_c4_telugu,blk_c5_telugu,blk_c6_telugu,blk_c7_telugu,blk_c8_telugu,blk_c9_telugu,blk_c10_telugu,blk_c11_telugu,blk_c12_telugu,blk_total_telugu=([] for zz5 in range(13))
            blk_c1_kanada,blk_c2_kanada,blk_c3_kanada,blk_c4_kanada,blk_c5_kanada,blk_c6_kanada,blk_c7_kanada,blk_c8_kanada,blk_c9_kanada,blk_c10_kanada,blk_c11_kanada,blk_c12_kanada,blk_total_kanada=([] for zz6 in range(13))
            blk_c1_urudu,blk_c2_urudu,blk_c3_urudu,blk_c4_urudu,blk_c5_urudu,blk_c6_urudu,blk_c7_urudu,blk_c8_urudu,blk_c9_urudu,blk_c10_urudu,blk_c11_urudu,blk_c12_urudu,blk_total_urudu=([] for zz7 in range(13))
            
            for ii in range(0,len(dse_govt)):
                if str(dse_govt[ii][0][0])==str(mgmt):
                    # mgmt=dse_govt[ii][1]
                    aa=dse_govt[ii][0]                
                    bb=sum(aa)
                    cc=int(bb)-1
                    dd=mgmt_name[cc]
                    for mm in blocks:
                        block_ids.append(str(mm.id))
                        block_names.append(mm.block_name)
                        school_list=all_schools.filter(block_id=mm.id,management_id__in=dse_govt[ii][1],category_id__in=dse_govt[ii][2])
                        blk_enrol=enroll.filter(school_id__in=school_list)

                        a=blk_enrol.aggregate(Sum('c1'))
                        b=blk_enrol.aggregate(Sum('c2'))
                        c=blk_enrol.aggregate(Sum('c3'))
                        d=blk_enrol.aggregate(Sum('c4'))
                        e=blk_enrol.aggregate(Sum('c5'))
                        f=blk_enrol.aggregate(Sum('c6'))
                        g=blk_enrol.aggregate(Sum('c7'))
                        h=blk_enrol.aggregate(Sum('c8'))
                        i=blk_enrol.aggregate(Sum('c9'))
                        j=blk_enrol.aggregate(Sum('c10'))
                        k=blk_enrol.aggregate(Sum('c11'))
                        l=blk_enrol.aggregate(Sum('c12'))
                        m=blk_enrol.aggregate(Sum('c_total'))

                        blk_c1+=a.values()                    
                        blk_c2+=b.values()
                        blk_c3+=c.values()
                        blk_c4+=d.values()
                        blk_c5+=e.values()
                        blk_c6+=f.values()
                        blk_c7+=g.values()
                        blk_c8+=h.values()
                        blk_c9+=i.values()
                        blk_c10+=j.values()
                        blk_c11+=k.values()
                        blk_c12+=l.values()
                        blk_c_total+=m.values()

                    for jj in blocks:
                        block_ids.append(str(jj.id))
                        block_names.append(jj.block_name)
                        school_list=all_schools.filter(block_id=jj.id,management_id__in=dse_govt[ii][1],category_id__in=dse_govt[ii][2])
                        g_blk=moi.filter(school_id__in=school_list)

                        a=g_blk.aggregate(Sum('c1_tamil'))                    
                        b=g_blk.aggregate(Sum('c2_tamil'))
                        c=g_blk.aggregate(Sum('c3_tamil'))
                        d=g_blk.aggregate(Sum('c4_tamil'))
                        e=g_blk.aggregate(Sum('c5_tamil'))
                        f=g_blk.aggregate(Sum('c6_tamil'))
                        g=g_blk.aggregate(Sum('c7_tamil'))
                        h=g_blk.aggregate(Sum('c8_tamil'))
                        i=g_blk.aggregate(Sum('c9_tamil'))
                        j=g_blk.aggregate(Sum('c10_tamil'))
                        k=g_blk.aggregate(Sum('c11_tamil'))
                        l=g_blk.aggregate(Sum('c12_tamil'))
                        m=g_blk.aggregate(Sum('total_tamil'))
                        a1=g_blk.aggregate(Sum('c1_eng'))
                        b1=g_blk.aggregate(Sum('c2_eng'))
                        c1=g_blk.aggregate(Sum('c3_eng'))
                        d1=g_blk.aggregate(Sum('c4_eng'))
                        e1=g_blk.aggregate(Sum('c5_eng'))
                        f1=g_blk.aggregate(Sum('c6_eng'))
                        g1=g_blk.aggregate(Sum('c7_eng'))
                        h1=g_blk.aggregate(Sum('c8_eng'))
                        i1=g_blk.aggregate(Sum('c9_eng'))
                        j1=g_blk.aggregate(Sum('c10_eng'))
                        k1=g_blk.aggregate(Sum('c11_eng'))
                        l1=g_blk.aggregate(Sum('c12_eng'))
                        m1=g_blk.aggregate(Sum('total_eng'))
                        n1=g_blk.aggregate(Sum('c1_telugu'))
                        o1=g_blk.aggregate(Sum('c2_telugu'))
                        p1=g_blk.aggregate(Sum('c3_telugu'))
                        q1=g_blk.aggregate(Sum('c4_telugu'))
                        r1=g_blk.aggregate(Sum('c5_telugu'))
                        s1=g_blk.aggregate(Sum('c6_telugu'))
                        t1=g_blk.aggregate(Sum('c7_telugu'))
                        u1=g_blk.aggregate(Sum('c8_telugu'))
                        v1=g_blk.aggregate(Sum('c9_telugu'))
                        w1=g_blk.aggregate(Sum('c10_telugu'))
                        x1=g_blk.aggregate(Sum('c11_telugu'))
                        y1=g_blk.aggregate(Sum('c12_telugu'))
                        z1=g_blk.aggregate(Sum('total_telugu'))
                        a2=g_blk.aggregate(Sum('c1_mlym'))
                        b2=g_blk.aggregate(Sum('c2_mlym'))
                        ccc=g_blk.aggregate(Sum('c3_mlym'))
                        d2=g_blk.aggregate(Sum('c4_mlym'))
                        e2=g_blk.aggregate(Sum('c5_mlym'))
                        f2=g_blk.aggregate(Sum('c6_mlym'))
                        g2=g_blk.aggregate(Sum('c7_mlym'))
                        h2=g_blk.aggregate(Sum('c8_mlym'))
                        iii=g_blk.aggregate(Sum('c9_mlym'))
                        j2=g_blk.aggregate(Sum('c10_mlym')) 
                        k2=g_blk.aggregate(Sum('c11_mlym'))
                        l2=g_blk.aggregate(Sum('c12_mlym'))
                        m2=g_blk.aggregate(Sum('total_mlym'))
                        n2=g_blk.aggregate(Sum('c1_kanada'))
                        o2=g_blk.aggregate(Sum('c2_kanada'))
                        p2=g_blk.aggregate(Sum('c3_kanada'))
                        q2=g_blk.aggregate(Sum('c4_kanada'))
                        r2=g_blk.aggregate(Sum('c5_kanada'))
                        s2=g_blk.aggregate(Sum('c6_kanada'))
                        t2=g_blk.aggregate(Sum('c7_kanada'))
                        u2=g_blk.aggregate(Sum('c8_kanada'))
                        v2=g_blk.aggregate(Sum('c9_kanada'))
                        w2=g_blk.aggregate(Sum('c10_kanada'))
                        x2=g_blk.aggregate(Sum('c11_kanada'))
                        y2=g_blk.aggregate(Sum('c12_kanada'))
                        z2=g_blk.aggregate(Sum('total_kanada'))
                        a3=g_blk.aggregate(Sum('c1_urdu'))
                        b3=g_blk.aggregate(Sum('c2_urdu'))
                        cccc=g_blk.aggregate(Sum('c3_urdu'))
                        d3=g_blk.aggregate(Sum('c4_urdu'))
                        e3=g_blk.aggregate(Sum('c5_urdu'))
                        f3=g_blk.aggregate(Sum('c6_urdu'))
                        g3=g_blk.aggregate(Sum('c7_urdu'))
                        h3=g_blk.aggregate(Sum('c8_urdu'))
                        iiii=g_blk.aggregate(Sum('c9_urdu'))
                        j3=g_blk.aggregate(Sum('c10_urdu'))
                        k3=g_blk.aggregate(Sum('c11_urdu'))
                        l3=g_blk.aggregate(Sum('c12_urdu'))
                        m3=g_blk.aggregate(Sum('total_urdu'))

                        blk_c1_tam+= a.values()                        
                        blk_c2_tam+=b.values()
                        blk_c3_tam+=c.values()
                        blk_c4_tam+=d.values()
                        blk_c5_tam+=e.values()
                        blk_c6_tam+=f.values()
                        blk_c7_tam+=g.values()
                        blk_c8_tam+=h.values()
                        blk_c9_tam+=i.values()
                        blk_c10_tam+=j.values()
                        blk_c11_tam+=k.values()
                        blk_c12_tam+=l.values()
                        blk_total_tam+=m.values()

                        blk_c1_eng+=a1.values()
                        blk_c2_eng+=b1.values()
                        blk_c3_eng+=c1.values()
                        blk_c4_eng+=d1.values()
                        blk_c5_eng+=e1.values()
                        blk_c6_eng+=f1.values()
                        blk_c7_eng+=g1.values()
                        blk_c8_eng+=h1.values()
                        blk_c9_eng+=i1.values()
                        blk_c10_eng+=j1.values()
                        blk_c11_eng+=k1.values()
                        blk_c12_eng+=l1.values()
                        blk_total_eng+=m1.values() 

                        blk_c1_telugu+=n1.values()
                        blk_c2_telugu+=o1.values()
                        blk_c3_telugu+=p1.values()
                        blk_c4_telugu+=q1.values()
                        blk_c5_telugu+=r1.values()
                        blk_c6_telugu+=s1.values()
                        blk_c7_telugu+=t1.values()
                        blk_c8_telugu+=u1.values()
                        blk_c9_telugu+=v1.values()
                        blk_c10_telugu+=w1.values()
                        blk_c11_telugu+=x1.values()
                        blk_c12_telugu+=y1.values()
                        blk_total_telugu+=z1.values()

                        blk_c1_mlym+=a2.values()
                        blk_c2_mlym+=b2.values()
                        blk_c3_mlym+=ccc.values()
                        blk_c4_mlym+=d2.values()
                        blk_c5_mlym+=e2.values()
                        blk_c6_mlym+=f2.values()
                        blk_c7_mlym+=g2.values()
                        blk_c8_mlym+=h2.values()
                        blk_c9_mlym+=iii.values()
                        blk_c10_mlym+=j2.values()
                        blk_c11_mlym+=k2.values()
                        blk_c12_mlym+=l2.values()
                        blk_total_mlym+=m2.values()

                        blk_c1_kanada+=n2.values()
                        blk_c2_kanada+=o2.values()
                        blk_c3_kanada+=p2.values()
                        blk_c4_kanada+=q2.values()
                        blk_c5_kanada+=r2.values()
                        blk_c6_kanada+=s2.values()
                        blk_c7_kanada+=t2.values()
                        blk_c8_kanada+=u2.values()
                        blk_c9_kanada+=v2.values()
                        blk_c10_kanada+=w2.values()
                        blk_c11_kanada+=x2.values()
                        blk_c12_kanada+=y2.values()
                        blk_total_kanada+=z2.values() 

                        blk_c1_urudu+=a3.values()
                        blk_c2_urudu+=b3.values()
                        blk_c3_urudu+=cccc.values()
                        blk_c4_urudu+=d3.values()
                        blk_c5_urudu+=e3.values()
                        blk_c6_urudu+=f3.values()
                        blk_c7_urudu+=g3.values()
                        blk_c8_urudu+=h3.values()
                        blk_c9_urudu+=iiii.values()
                        blk_c10_urudu+=j3.values()
                        blk_c11_urudu+=k3.values()
                        blk_c12_urudu+=l3.values()
                        blk_total_urudu+=m3.values()

            tamil_list=zip(block_ids,block_names,blk_c1_tam,blk_c2_tam,blk_c3_tam,blk_c4_tam,blk_c5_tam,blk_c6_tam,blk_c7_tam,blk_c8_tam,blk_c9_tam,blk_c10_tam,blk_c11_tam,blk_c12_tam,blk_total_tam,)
            english_list=zip(block_ids,block_names,blk_c1_eng,blk_c2_eng,blk_c3_eng,blk_c4_eng,blk_c5_eng,blk_c6_eng,blk_c7_eng,blk_c8_eng,blk_c9_eng,blk_c10_eng,blk_c11_eng,blk_c12_eng,blk_total_eng)
            telugu_list=zip(block_ids,block_names,blk_c1_telugu,blk_c2_telugu,blk_c3_telugu,blk_c4_telugu,blk_c5_telugu,blk_c6_telugu,blk_c7_telugu,blk_c8_telugu,blk_c9_telugu,blk_c10_telugu,blk_c11_telugu,blk_c12_telugu,blk_total_telugu)
            mlym_list=zip(block_ids,block_names,blk_c1_mlym,blk_c2_mlym,blk_c3_mlym,blk_c4_mlym,blk_c5_mlym,blk_c6_mlym,blk_c7_mlym,blk_c8_mlym,blk_c9_mlym,blk_c10_mlym,blk_c11_mlym,blk_c12_mlym,blk_total_mlym)
            kannada_list=zip(block_ids,block_names,blk_c1_kanada,blk_c2_kanada,blk_c3_kanada,blk_c4_kanada,blk_c5_kanada,blk_c6_kanada,blk_c7_kanada,blk_c8_kanada,blk_c9_kanada,blk_c10_kanada,blk_c11_kanada,blk_c12_kanada,blk_total_kanada)
            urudu_list=zip(block_ids,block_names,blk_c1_urudu,blk_c2_urudu,blk_c3_urudu,blk_c4_urudu,blk_c5_urudu,blk_c6_urudu,blk_c7_urudu,blk_c8_urudu,blk_c9_urudu,blk_c10_urudu,blk_c11_urudu,blk_c12_urudu,blk_total_urudu)
            enrol_list=zip(block_ids,block_names,blk_c1,blk_c2,blk_c3,blk_c4,blk_c5,blk_c6,blk_c7,blk_c8,blk_c9,blk_c10,blk_c11,blk_c12,blk_c_total)
        
            return render(request,'moi/block_overall_moi_report.html',locals())

    def post(self,request,**kwargs):
        global dse_govt        
        global all_schools
        global gender_wise
        global mgmt_name
        global enroll
        global moi

        mgmt_id = request.POST.get('blks', False)
        mgmt_blk=mgmt_id.split(',')
        lang=mgmt_blk[2]
        for ii in range(0,len(dse_govt)):
            if str(dse_govt[ii][0][0])==str(mgmt_blk[0]):
                aa=dse_govt[ii][0]
                bb=sum(aa)
                cc=int(bb)-1
                dd=mgmt_name[cc]
                block_name=Block.objects.get(id=mgmt_blk[1])
                school_list=all_schools.filter(block_id=mgmt_blk[1],management_id__in=dse_govt[ii][1],category_id__in=dse_govt[ii][2])
                blk_enroll=enroll.filter(school_id__in=school_list).order_by('school')
                

        for ff in range(0,len(dse_govt)):
            if str(dse_govt[ff][0][0])==str(mgmt_blk[0]):
                aa=dse_govt[ff][0]
                bb=sum(aa)
                cc=int(bb)-1
                dd=mgmt_name[cc]
                block_name=Block.objects.get(id=mgmt_blk[1])
                school_list=all_schools.filter(block_id=mgmt_blk[1],management_id__in=dse_govt[ff][1],category_id__in=dse_govt[ff][2])
                blk_schl=moi.filter(school_id__in=school_list).order_by('school')
                
            return render(request,'moi/block_moi_school_report.html',locals())

class school_level_moi(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']
        enroll=common_reports.objects.get(id=school) 
        medi=medium_of_instrction.objects.get(id=school)  
        return render(request,'moi/school_l_mediumwise.html',locals())

class district_level_moi_report(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated():
            global all_schools
            global moi
            global dse_govt
            user=self.kwargs['pk']
            user_access_level=[4,3]
            district=District.objects.get(id=user)
            for i in range(0,len(dse_govt)):   
                d_l_school_list=all_schools.filter(district_id=user,management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])
                schl_list=moi.filter(school_id__in=d_l_school_list)
                if int(dse_govt[i][0][0])==1:
                    dl_ds_g_c1_tam=dl_ds_g_c2_tam=dl_ds_g_c3_tam=dl_ds_g_c4_tam=dl_ds_g_c5_tam=dl_ds_g_c6_tam=dl_ds_g_c7_tam=dl_ds_g_c8_tam=dl_ds_g_c9_tam=dl_ds_g_c10_tam=dl_ds_g_c11_tam=dl_ds_g_c12_tam=dl_ds_g_total_tam=0 
                    dl_ds_g_c1_eng=dl_ds_g_c2_eng=dl_ds_g_c3_eng=dl_ds_g_c4_eng=dl_ds_g_c5_eng=dl_ds_g_c6_eng=dl_ds_g_c7_eng=dl_ds_g_c8_eng=dl_ds_g_c9_eng=dl_ds_g_c10_eng=dl_ds_g_c11_eng=dl_ds_g_c12_eng=dl_ds_g_total_eng=0 
                    dl_ds_g_c1_telgu=dl_ds_g_c2_telgu=dl_ds_g_c3_telgu=dl_ds_g_c4_telgu=dl_ds_g_c5_telgu=dl_ds_g_c6_telgu=dl_ds_g_c7_telgu=dl_ds_g_c8_telgu=dl_ds_g_c9_telgu=dl_ds_g_c10_telgu=dl_ds_g_c11_telgu=dl_ds_g_c12_telgu=dl_ds_g_total_telgu=0 
                    dl_ds_g_c1_malam=dl_ds_g_c2_malam=dl_ds_g_c3_malam=dl_ds_g_c4_malam=dl_ds_g_c5_malam=dl_ds_g_c6_malam=dl_ds_g_c7_malam=dl_ds_g_c8_malam=dl_ds_g_c9_malam=dl_ds_g_c10_malam=dl_ds_g_c11_malam=dl_ds_g_c12_malam=dl_ds_g_total_malam=0 
                    dl_ds_g_c1_kanada=dl_ds_g_c2_kanada=dl_ds_g_c3_kanada=dl_ds_g_c4_kanada=dl_ds_g_c5_kanada=dl_ds_g_c6_kanada=dl_ds_g_c7_kanada=dl_ds_g_c8_kanada=dl_ds_g_c9_kanada=dl_ds_g_c10_kanada=dl_ds_g_c11_kanada=dl_ds_g_c12_kanada=dl_ds_g_total_kanada=0 
                    dl_ds_g_c1_urudu=dl_ds_g_c2_urudu=dl_ds_g_c3_urudu=dl_ds_g_c4_urudu=dl_ds_g_c5_urudu=dl_ds_g_c6_urudu=dl_ds_g_c7_urudu=dl_ds_g_c8_urudu=dl_ds_g_c9_urudu=dl_ds_g_c10_urudu=dl_ds_g_c11_urudu=dl_ds_g_c12_urudu=dl_ds_g_total_urudu=0 
                    for j in schl_list:
                        dl_ds_g_c1_tam +=j.c1_tamil
                        dl_ds_g_c2_tam +=j.c2_tamil
                        dl_ds_g_c3_tam +=j.c3_tamil
                        dl_ds_g_c4_tam +=j.c4_tamil
                        dl_ds_g_c5_tam +=j.c5_tamil
                        dl_ds_g_c6_tam +=j.c6_tamil
                        dl_ds_g_c7_tam +=j.c7_tamil
                        dl_ds_g_c8_tam +=j.c8_tamil
                        dl_ds_g_c9_tam +=j.c9_tamil
                        dl_ds_g_c10_tam +=j.c10_tamil
                        dl_ds_g_c11_tam +=j.c11_tamil
                        dl_ds_g_c12_tam +=j.c12_tamil
                        dl_ds_g_total_tam+=j.total_tamil

                        dl_ds_g_c1_eng +=j.c1_eng
                        dl_ds_g_c2_eng +=j.c2_eng
                        dl_ds_g_c3_eng +=j.c3_eng
                        dl_ds_g_c4_eng +=j.c4_eng
                        dl_ds_g_c5_eng +=j.c5_eng
                        dl_ds_g_c6_eng +=j.c6_eng
                        dl_ds_g_c7_eng +=j.c7_eng
                        dl_ds_g_c8_eng +=j.c8_eng
                        dl_ds_g_c9_eng +=j.c9_eng
                        dl_ds_g_c10_eng +=j.c10_eng
                        dl_ds_g_c11_eng +=j.c11_eng
                        dl_ds_g_c12_eng +=j.c12_eng
                        dl_ds_g_total_eng+=j.total_eng

                        dl_ds_g_c1_telgu +=j.c1_telugu
                        dl_ds_g_c2_telgu +=j.c2_telugu
                        dl_ds_g_c3_telgu +=j.c3_telugu
                        dl_ds_g_c4_telgu +=j.c4_telugu
                        dl_ds_g_c5_telgu +=j.c5_telugu
                        dl_ds_g_c6_telgu +=j.c6_telugu
                        dl_ds_g_c7_telgu +=j.c7_telugu
                        dl_ds_g_c8_telgu +=j.c8_telugu
                        dl_ds_g_c9_telgu +=j.c9_telugu
                        dl_ds_g_c10_telgu +=j.c10_telugu
                        dl_ds_g_c11_telgu +=j.c11_telugu
                        dl_ds_g_c12_telgu +=j.c12_telugu
                        dl_ds_g_total_telgu+=j.total_telugu
                        
                        dl_ds_g_c1_malam +=j.c1_mlym
                        dl_ds_g_c2_malam +=j.c2_mlym
                        dl_ds_g_c3_malam +=j.c3_mlym
                        dl_ds_g_c4_malam +=j.c4_mlym
                        dl_ds_g_c5_malam +=j.c5_mlym
                        dl_ds_g_c6_malam +=j.c6_mlym
                        dl_ds_g_c7_malam +=j.c7_mlym
                        dl_ds_g_c8_malam +=j.c8_mlym
                        dl_ds_g_c9_malam +=j.c9_mlym
                        dl_ds_g_c10_malam +=j.c10_mlym
                        dl_ds_g_c11_malam +=j.c11_mlym
                        dl_ds_g_c12_malam +=j.c12_mlym
                        dl_ds_g_total_malam+=j.total_mlym

                        dl_ds_g_c1_kanada +=j.c1_kanada
                        dl_ds_g_c2_kanada +=j.c2_kanada
                        dl_ds_g_c3_kanada +=j.c3_kanada
                        dl_ds_g_c4_kanada +=j.c4_kanada
                        dl_ds_g_c5_kanada +=j.c5_kanada
                        dl_ds_g_c6_kanada +=j.c6_kanada
                        dl_ds_g_c7_kanada +=j.c7_kanada
                        dl_ds_g_c8_kanada +=j.c8_kanada
                        dl_ds_g_c9_kanada +=j.c9_kanada
                        dl_ds_g_c10_kanada +=j.c10_kanada
                        dl_ds_g_c11_kanada +=j.c11_kanada
                        dl_ds_g_c12_kanada +=j.c12_kanada
                        dl_ds_g_total_kanada+=j.total_kanada

                        dl_ds_g_c1_urudu +=j.c1_urdu
                        dl_ds_g_c2_urudu +=j.c2_urdu
                        dl_ds_g_c3_urudu +=j.c3_urdu
                        dl_ds_g_c4_urudu +=j.c4_urdu
                        dl_ds_g_c5_urudu +=j.c5_urdu
                        dl_ds_g_c6_urudu +=j.c6_urdu
                        dl_ds_g_c7_urudu +=j.c7_urdu
                        dl_ds_g_c8_urudu +=j.c8_urdu
                        dl_ds_g_c9_urudu +=j.c9_urdu
                        dl_ds_g_c10_urudu +=j.c10_urdu
                        dl_ds_g_c11_urudu +=j.c11_urdu
                        dl_ds_g_c12_urudu +=j.c12_urdu
                        dl_ds_g_total_urudu+=j.total_urdu

                if int(dse_govt[i][0][0])==2:
                    dl_ds_pa_c1_tam=dl_ds_pa_c2_tam=dl_ds_pa_c3_tam=dl_ds_pa_c4_tam=dl_ds_pa_c5_tam=dl_ds_pa_c6_tam=dl_ds_pa_c7_tam=dl_ds_pa_c8_tam=dl_ds_pa_c9_tam=dl_ds_pa_c10_tam=dl_ds_pa_c11_tam=dl_ds_pa_c12_tam=dl_ds_pa_total_tam=0
                    dl_ds_pa_c1_eng=dl_ds_pa_c2_eng=dl_ds_pa_c3_eng=dl_ds_pa_c4_eng=dl_ds_pa_c5_eng=dl_ds_pa_c6_eng=dl_ds_pa_c7_eng=dl_ds_pa_c8_eng=dl_ds_pa_c9_eng=dl_ds_pa_c10_eng=dl_ds_pa_c11_eng=dl_ds_pa_c12_eng=dl_ds_pa_total_eng=0 
                    dl_ds_pa_c1_telgu=dl_ds_pa_c2_telgu=dl_ds_pa_c3_telgu=dl_ds_pa_c4_telgu=dl_ds_pa_c5_telgu=dl_ds_pa_c6_telgu=dl_ds_pa_c7_telgu=dl_ds_pa_c8_telgu=dl_ds_pa_c9_telgu=dl_ds_pa_c10_telgu=dl_ds_pa_c11_telgu=dl_ds_pa_c12_telgu=dl_ds_pa_total_telgu=0 
                    dl_ds_pa_c1_malam=dl_ds_pa_c2_malam=dl_ds_pa_c3_malam=dl_ds_pa_c4_malam=dl_ds_pa_c5_malam=dl_ds_pa_c6_malam=dl_ds_pa_c7_malam=dl_ds_pa_c8_malam=dl_ds_pa_c9_malam=dl_ds_pa_c10_malam=dl_ds_pa_c11_malam=dl_ds_pa_c12_malam=dl_ds_pa_total_malam=0 
                    dl_ds_pa_c1_kanada=dl_ds_pa_c2_kanada=dl_ds_pa_c3_kanada=dl_ds_pa_c4_kanada=dl_ds_pa_c5_kanada=dl_ds_pa_c6_kanada=dl_ds_pa_c7_kanada=dl_ds_pa_c8_kanada=dl_ds_pa_c9_kanada=dl_ds_pa_c10_kanada=dl_ds_pa_c11_kanada=dl_ds_pa_c12_kanada=dl_ds_pa_total_kanada=0 
                    dl_ds_pa_c1_urudu=dl_ds_pa_c2_urudu=dl_ds_pa_c3_urudu=dl_ds_pa_c4_urudu=dl_ds_pa_c5_urudu=dl_ds_pa_c6_urudu=dl_ds_pa_c7_urudu=dl_ds_pa_c8_urudu=dl_ds_pa_c9_urudu=dl_ds_pa_c10_urudu=dl_ds_pa_c11_urudu=dl_ds_pa_c12_urudu=dl_ds_pa_total_urudu=0 
                    for j in schl_list:
                        dl_ds_pa_c1_tam +=j.c1_tamil
                        dl_ds_pa_c2_tam +=j.c2_tamil
                        dl_ds_pa_c3_tam +=j.c3_tamil
                        dl_ds_pa_c4_tam +=j.c4_tamil
                        dl_ds_pa_c5_tam +=j.c5_tamil
                        dl_ds_pa_c6_tam +=j.c6_tamil
                        dl_ds_pa_c7_tam +=j.c7_tamil
                        dl_ds_pa_c8_tam +=j.c8_tamil
                        dl_ds_pa_c9_tam +=j.c9_tamil
                        dl_ds_pa_c10_tam +=j.c10_tamil
                        dl_ds_pa_c11_tam +=j.c11_tamil
                        dl_ds_pa_c12_tam +=j.c12_tamil
                        dl_ds_pa_total_tam+=j.total_tamil

                        dl_ds_pa_c1_eng +=j.c1_eng
                        dl_ds_pa_c2_eng +=j.c2_eng
                        dl_ds_pa_c3_eng +=j.c3_eng
                        dl_ds_pa_c4_eng +=j.c4_eng
                        dl_ds_pa_c5_eng +=j.c5_eng
                        dl_ds_pa_c6_eng +=j.c6_eng
                        dl_ds_pa_c7_eng +=j.c7_eng
                        dl_ds_pa_c8_eng +=j.c8_eng
                        dl_ds_pa_c9_eng +=j.c9_eng
                        dl_ds_pa_c10_eng +=j.c10_eng
                        dl_ds_pa_c11_eng +=j.c11_eng
                        dl_ds_pa_c12_eng +=j.c12_eng
                        dl_ds_pa_total_eng+=j.total_eng

                        dl_ds_pa_c1_telgu +=j.c1_telugu
                        dl_ds_pa_c2_telgu +=j.c2_telugu
                        dl_ds_pa_c3_telgu +=j.c3_telugu
                        dl_ds_pa_c4_telgu +=j.c4_telugu
                        dl_ds_pa_c5_telgu +=j.c5_telugu
                        dl_ds_pa_c6_telgu +=j.c6_telugu
                        dl_ds_pa_c7_telgu +=j.c7_telugu
                        dl_ds_pa_c8_telgu +=j.c8_telugu
                        dl_ds_pa_c9_telgu +=j.c9_telugu
                        dl_ds_pa_c10_telgu +=j.c10_telugu
                        dl_ds_pa_c11_telgu +=j.c11_telugu
                        dl_ds_pa_c12_telgu +=j.c12_telugu
                        dl_ds_pa_total_telgu+=j.total_telugu
                        
                        dl_ds_pa_c1_malam +=j.c1_mlym
                        dl_ds_pa_c2_malam +=j.c2_mlym
                        dl_ds_pa_c3_malam +=j.c3_mlym
                        dl_ds_pa_c4_malam +=j.c4_mlym
                        dl_ds_pa_c5_malam +=j.c5_mlym
                        dl_ds_pa_c6_malam +=j.c6_mlym
                        dl_ds_pa_c7_malam +=j.c7_mlym
                        dl_ds_pa_c8_malam +=j.c8_mlym
                        dl_ds_pa_c9_malam +=j.c9_mlym
                        dl_ds_pa_c10_malam +=j.c10_mlym
                        dl_ds_pa_c11_malam +=j.c11_mlym
                        dl_ds_pa_c12_malam +=j.c12_mlym
                        dl_ds_pa_total_malam+=j.total_mlym

                        dl_ds_pa_c1_kanada +=j.c1_kanada
                        dl_ds_pa_c2_kanada +=j.c2_kanada
                        dl_ds_pa_c3_kanada +=j.c3_kanada
                        dl_ds_pa_c4_kanada +=j.c4_kanada
                        dl_ds_pa_c5_kanada +=j.c5_kanada
                        dl_ds_pa_c6_kanada +=j.c6_kanada
                        dl_ds_pa_c7_kanada +=j.c7_kanada
                        dl_ds_pa_c8_kanada +=j.c8_kanada
                        dl_ds_pa_c9_kanada +=j.c9_kanada
                        dl_ds_pa_c10_kanada +=j.c10_kanada
                        dl_ds_pa_c11_kanada +=j.c11_kanada
                        dl_ds_pa_c12_kanada +=j.c12_kanada
                        dl_ds_pa_total_kanada+=j.total_kanada

                        dl_ds_pa_c1_urudu +=j.c1_urdu
                        dl_ds_pa_c2_urudu +=j.c2_urdu
                        dl_ds_pa_c3_urudu +=j.c3_urdu
                        dl_ds_pa_c4_urudu +=j.c4_urdu
                        dl_ds_pa_c5_urudu +=j.c5_urdu
                        dl_ds_pa_c6_urudu +=j.c6_urdu
                        dl_ds_pa_c7_urudu +=j.c7_urdu
                        dl_ds_pa_c8_urudu +=j.c8_urdu
                        dl_ds_pa_c9_urudu +=j.c9_urdu
                        dl_ds_pa_c10_urudu +=j.c10_urdu
                        dl_ds_pa_c11_urudu +=j.c11_urdu
                        dl_ds_pa_c12_urudu +=j.c12_urdu
                        dl_ds_pa_total_urudu+=j.total_urdu
                if int(dse_govt[i][0][0])==6:
                    dl_dee_g_c1_tam=dl_dee_g_c2_tam=dl_dee_g_c3_tam=dl_dee_g_c4_tam=dl_dee_g_c5_tam=dl_dee_g_c6_tam=dl_dee_g_c7_tam=dl_dee_g_c8_tam=dl_dee_g_c9_tam=dl_dee_g_c10_tam=dl_dee_g_c11_tam=dl_dee_g_c12_tam=dl_dee_g_total_tam=0
                    dl_dee_g_c1_eng=dl_dee_g_c2_eng=dl_dee_g_c3_eng=dl_dee_g_c4_eng=dl_dee_g_c5_eng=dl_dee_g_c6_eng=dl_dee_g_c7_eng=dl_dee_g_c8_eng=dl_dee_g_c9_eng=dl_dee_g_c10_eng=dl_dee_g_c11_eng=dl_dee_g_c12_eng=dl_dee_g_total_eng=0 
                    dl_dee_g_c1_telgu=dl_dee_g_c2_telgu=dl_dee_g_c3_telgu=dl_dee_g_c4_telgu=dl_dee_g_c5_telgu=dl_dee_g_c6_telgu=dl_dee_g_c7_telgu=dl_dee_g_c8_telgu=dl_dee_g_c9_telgu=dl_dee_g_c10_telgu=dl_dee_g_c11_telgu=dl_dee_g_c12_telgu=dl_dee_g_total_telgu=0 
                    dl_dee_g_c1_malam=dl_dee_g_c2_malam=dl_dee_g_c3_malam=dl_dee_g_c4_malam=dl_dee_g_c5_malam=dl_dee_g_c6_malam=dl_dee_g_c7_malam=dl_dee_g_c8_malam=dl_dee_g_c9_malam=dl_dee_g_c10_malam=dl_dee_g_c11_malam=dl_dee_g_c12_malam=dl_dee_g_total_malam=0 
                    dl_dee_g_c1_kanada=dl_dee_g_c2_kanada=dl_dee_g_c3_kanada=dl_dee_g_c4_kanada=dl_dee_g_c5_kanada=dl_dee_g_c6_kanada=dl_dee_g_c7_kanada=dl_dee_g_c8_kanada=dl_dee_g_c9_kanada=dl_dee_g_c10_kanada=dl_dee_g_c11_kanada=dl_dee_g_c12_kanada=dl_dee_g_total_kanada=0 
                    dl_dee_g_c1_urudu=dl_dee_g_c2_urudu=dl_dee_g_c3_urudu=dl_dee_g_c4_urudu=dl_dee_g_c5_urudu=dl_dee_g_c6_urudu=dl_dee_g_c7_urudu=dl_dee_g_c8_urudu=dl_dee_g_c9_urudu=dl_dee_g_c10_urudu=dl_dee_g_c11_urudu=dl_dee_g_c12_urudu=dl_dee_g_total_urudu=0 
                    for j in schl_list:
                        dl_dee_g_c1_tam +=j.c1_tamil
                        dl_dee_g_c2_tam +=j.c2_tamil
                        dl_dee_g_c3_tam +=j.c3_tamil
                        dl_dee_g_c4_tam +=j.c4_tamil
                        dl_dee_g_c5_tam +=j.c5_tamil
                        dl_dee_g_c6_tam +=j.c6_tamil
                        dl_dee_g_c7_tam +=j.c7_tamil
                        dl_dee_g_c8_tam +=j.c8_tamil
                        dl_dee_g_c9_tam +=j.c9_tamil
                        dl_dee_g_c10_tam +=j.c10_tamil
                        dl_dee_g_c11_tam +=j.c11_tamil
                        dl_dee_g_c12_tam +=j.c12_tamil
                        dl_dee_g_total_tam+=j.total_tamil

                        dl_dee_g_c1_eng +=j.c1_eng
                        dl_dee_g_c2_eng +=j.c2_eng
                        dl_dee_g_c3_eng +=j.c3_eng
                        dl_dee_g_c4_eng +=j.c4_eng
                        dl_dee_g_c5_eng +=j.c5_eng
                        dl_dee_g_c6_eng +=j.c6_eng
                        dl_dee_g_c7_eng +=j.c7_eng
                        dl_dee_g_c8_eng +=j.c8_eng
                        dl_dee_g_c9_eng +=j.c9_eng
                        dl_dee_g_c10_eng +=j.c10_eng
                        dl_dee_g_c11_eng +=j.c11_eng
                        dl_dee_g_c12_eng +=j.c12_eng
                        dl_dee_g_total_eng+=j.total_eng

                        dl_dee_g_c1_telgu +=j.c1_telugu
                        dl_dee_g_c2_telgu +=j.c2_telugu
                        dl_dee_g_c3_telgu +=j.c3_telugu
                        dl_dee_g_c4_telgu +=j.c4_telugu
                        dl_dee_g_c5_telgu +=j.c5_telugu
                        dl_dee_g_c6_telgu +=j.c6_telugu
                        dl_dee_g_c7_telgu +=j.c7_telugu
                        dl_dee_g_c8_telgu +=j.c8_telugu
                        dl_dee_g_c9_telgu +=j.c9_telugu
                        dl_dee_g_c10_telgu +=j.c10_telugu
                        dl_dee_g_c11_telgu +=j.c11_telugu
                        dl_dee_g_c12_telgu +=j.c12_telugu
                        dl_dee_g_total_telgu+=j.total_telugu
                        
                        dl_dee_g_c1_malam +=j.c1_mlym
                        dl_dee_g_c2_malam +=j.c2_mlym
                        dl_dee_g_c3_malam +=j.c3_mlym
                        dl_dee_g_c4_malam +=j.c4_mlym
                        dl_dee_g_c5_malam +=j.c5_mlym
                        dl_dee_g_c6_malam +=j.c6_mlym
                        dl_dee_g_c7_malam +=j.c7_mlym
                        dl_dee_g_c8_malam +=j.c8_mlym
                        dl_dee_g_c9_malam +=j.c9_mlym
                        dl_dee_g_c10_malam +=j.c10_mlym
                        dl_dee_g_c11_malam +=j.c11_mlym
                        dl_dee_g_c12_malam +=j.c12_mlym
                        dl_dee_g_total_malam+=j.total_mlym

                        dl_dee_g_c1_kanada +=j.c1_kanada
                        dl_dee_g_c2_kanada +=j.c2_kanada
                        dl_dee_g_c3_kanada +=j.c3_kanada
                        dl_dee_g_c4_kanada +=j.c4_kanada
                        dl_dee_g_c5_kanada +=j.c5_kanada
                        dl_dee_g_c6_kanada +=j.c6_kanada
                        dl_dee_g_c7_kanada +=j.c7_kanada
                        dl_dee_g_c8_kanada +=j.c8_kanada
                        dl_dee_g_c9_kanada +=j.c9_kanada
                        dl_dee_g_c10_kanada +=j.c10_kanada
                        dl_dee_g_c11_kanada +=j.c11_kanada
                        dl_dee_g_c12_kanada +=j.c12_kanada
                        dl_dee_g_total_kanada+=j.total_kanada

                        dl_dee_g_c1_urudu +=j.c1_urdu
                        dl_dee_g_c2_urudu +=j.c2_urdu
                        dl_dee_g_c3_urudu +=j.c3_urdu
                        dl_dee_g_c4_urudu +=j.c4_urdu
                        dl_dee_g_c5_urudu +=j.c5_urdu
                        dl_dee_g_c6_urudu +=j.c6_urdu
                        dl_dee_g_c7_urudu +=j.c7_urdu
                        dl_dee_g_c8_urudu +=j.c8_urdu
                        dl_dee_g_c9_urudu +=j.c9_urdu
                        dl_dee_g_c10_urudu +=j.c10_urdu
                        dl_dee_g_c11_urudu +=j.c11_urdu
                        dl_dee_g_c12_urudu +=j.c12_urdu
                        dl_dee_g_total_urudu+=j.total_urdu
                if int(dse_govt[i][0][0])==7:
                    dl_dee_pa_c1_tam=dl_dee_pa_c2_tam=dl_dee_pa_c3_tam=dl_dee_pa_c4_tam=dl_dee_pa_c5_tam=dl_dee_pa_c6_tam=dl_dee_pa_c7_tam=dl_dee_pa_c8_tam=dl_dee_pa_c9_tam=dl_dee_pa_c10_tam=dl_dee_pa_c11_tam=dl_dee_pa_c12_tam=dl_dee_pa_total_tam=0
                    dl_dee_pa_c1_eng=dl_dee_pa_c2_eng=dl_dee_pa_c3_eng=dl_dee_pa_c4_eng=dl_dee_pa_c5_eng=dl_dee_pa_c6_eng=dl_dee_pa_c7_eng=dl_dee_pa_c8_eng=dl_dee_pa_c9_eng=dl_dee_pa_c10_eng=dl_dee_pa_c11_eng=dl_dee_pa_c12_eng=dl_dee_pa_total_eng=0 
                    dl_dee_pa_c1_telgu=dl_dee_pa_c2_telgu=dl_dee_pa_c3_telgu=dl_dee_pa_c4_telgu=dl_dee_pa_c5_telgu=dl_dee_pa_c6_telgu=dl_dee_pa_c7_telgu=dl_dee_pa_c8_telgu=dl_dee_pa_c9_telgu=dl_dee_pa_c10_telgu=dl_dee_pa_c11_telgu=dl_dee_pa_c12_telgu=dl_dee_pa_total_telgu=0 
                    dl_dee_pa_c1_malam=dl_dee_pa_c2_malam=dl_dee_pa_c3_malam=dl_dee_pa_c4_malam=dl_dee_pa_c5_malam=dl_dee_pa_c6_malam=dl_dee_pa_c7_malam=dl_dee_pa_c8_malam=dl_dee_pa_c9_malam=dl_dee_pa_c10_malam=dl_dee_pa_c11_malam=dl_dee_pa_c12_malam=dl_dee_pa_total_malam=0 
                    dl_dee_pa_c1_kanada=dl_dee_pa_c2_kanada=dl_dee_pa_c3_kanada=dl_dee_pa_c4_kanada=dl_dee_pa_c5_kanada=dl_dee_pa_c6_kanada=dl_dee_pa_c7_kanada=dl_dee_pa_c8_kanada=dl_dee_pa_c9_kanada=dl_dee_pa_c10_kanada=dl_dee_pa_c11_kanada=dl_dee_pa_c12_kanada=dl_dee_pa_total_kanada=0 
                    dl_dee_pa_c1_urudu=dl_dee_pa_c2_urudu=dl_dee_pa_c3_urudu=dl_dee_pa_c4_urudu=dl_dee_pa_c5_urudu=dl_dee_pa_c6_urudu=dl_dee_pa_c7_urudu=dl_dee_pa_c8_urudu=dl_dee_pa_c9_urudu=dl_dee_pa_c10_urudu=dl_dee_pa_c11_urudu=dl_dee_pa_c12_urudu=dl_dee_pa_total_urudu=0 
                    for j in schl_list:
                        dl_dee_pa_c1_tam +=j.c1_tamil
                        dl_dee_pa_c2_tam +=j.c2_tamil
                        dl_dee_pa_c3_tam +=j.c3_tamil
                        dl_dee_pa_c4_tam +=j.c4_tamil
                        dl_dee_pa_c5_tam +=j.c5_tamil
                        dl_dee_pa_c6_tam +=j.c6_tamil
                        dl_dee_pa_c7_tam +=j.c7_tamil
                        dl_dee_pa_c8_tam +=j.c8_tamil
                        dl_dee_pa_c9_tam +=j.c9_tamil
                        dl_dee_pa_c10_tam +=j.c10_tamil
                        dl_dee_pa_c11_tam +=j.c11_tamil
                        dl_dee_pa_c12_tam +=j.c12_tamil
                        dl_dee_pa_total_tam+=j.total_tamil

                        dl_dee_pa_c1_eng +=j.c1_eng
                        dl_dee_pa_c2_eng +=j.c2_eng
                        dl_dee_pa_c3_eng +=j.c3_eng
                        dl_dee_pa_c4_eng +=j.c4_eng
                        dl_dee_pa_c5_eng +=j.c5_eng
                        dl_dee_pa_c6_eng +=j.c6_eng
                        dl_dee_pa_c7_eng +=j.c7_eng
                        dl_dee_pa_c8_eng +=j.c8_eng
                        dl_dee_pa_c9_eng +=j.c9_eng
                        dl_dee_pa_c10_eng +=j.c10_eng
                        dl_dee_pa_c11_eng +=j.c11_eng
                        dl_dee_pa_c12_eng +=j.c12_eng
                        dl_dee_pa_total_eng+=j.total_eng

                        dl_dee_pa_c1_telgu +=j.c1_telugu
                        dl_dee_pa_c2_telgu +=j.c2_telugu
                        dl_dee_pa_c3_telgu +=j.c3_telugu
                        dl_dee_pa_c4_telgu +=j.c4_telugu
                        dl_dee_pa_c5_telgu +=j.c5_telugu
                        dl_dee_pa_c6_telgu +=j.c6_telugu
                        dl_dee_pa_c7_telgu +=j.c7_telugu
                        dl_dee_pa_c8_telgu +=j.c8_telugu
                        dl_dee_pa_c9_telgu +=j.c9_telugu
                        dl_dee_pa_c10_telgu +=j.c10_telugu
                        dl_dee_pa_c11_telgu +=j.c11_telugu
                        dl_dee_pa_c12_telgu +=j.c12_telugu
                        dl_dee_pa_total_telgu+=j.total_telugu
                        
                        dl_dee_pa_c1_malam +=j.c1_mlym
                        dl_dee_pa_c2_malam +=j.c2_mlym
                        dl_dee_pa_c3_malam +=j.c3_mlym
                        dl_dee_pa_c4_malam +=j.c4_mlym
                        dl_dee_pa_c5_malam +=j.c5_mlym
                        dl_dee_pa_c6_malam +=j.c6_mlym
                        dl_dee_pa_c7_malam +=j.c7_mlym
                        dl_dee_pa_c8_malam +=j.c8_mlym
                        dl_dee_pa_c9_malam +=j.c9_mlym
                        dl_dee_pa_c10_malam +=j.c10_mlym
                        dl_dee_pa_c11_malam +=j.c11_mlym
                        dl_dee_pa_c12_malam +=j.c12_mlym
                        dl_dee_pa_total_malam+=j.total_mlym

                        dl_dee_pa_c1_kanada +=j.c1_kanada
                        dl_dee_pa_c2_kanada +=j.c2_kanada
                        dl_dee_pa_c3_kanada +=j.c3_kanada
                        dl_dee_pa_c4_kanada +=j.c4_kanada
                        dl_dee_pa_c5_kanada +=j.c5_kanada
                        dl_dee_pa_c6_kanada +=j.c6_kanada
                        dl_dee_pa_c7_kanada +=j.c7_kanada
                        dl_dee_pa_c8_kanada +=j.c8_kanada
                        dl_dee_pa_c9_kanada +=j.c9_kanada
                        dl_dee_pa_c10_kanada +=j.c10_kanada
                        dl_dee_pa_c11_kanada +=j.c11_kanada
                        dl_dee_pa_c12_kanada +=j.c12_kanada
                        dl_dee_pa_total_kanada+=j.total_kanada

                        dl_dee_pa_c1_urudu +=j.c1_urdu
                        dl_dee_pa_c2_urudu +=j.c2_urdu
                        dl_dee_pa_c3_urudu +=j.c3_urdu
                        dl_dee_pa_c4_urudu +=j.c4_urdu
                        dl_dee_pa_c5_urudu +=j.c5_urdu
                        dl_dee_pa_c6_urudu +=j.c6_urdu
                        dl_dee_pa_c7_urudu +=j.c7_urdu
                        dl_dee_pa_c8_urudu +=j.c8_urdu
                        dl_dee_pa_c9_urudu +=j.c9_urdu
                        dl_dee_pa_c10_urudu +=j.c10_urdu
                        dl_dee_pa_c11_urudu +=j.c11_urdu
                        dl_dee_pa_c12_urudu +=j.c12_urdu
                        dl_dee_pa_total_urudu+=j.total_urdu
            for i in range(0,len(dse_govt)):   
                dse_school_list=all_schools.filter(district_id=user,management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])
                dse=enroll.filter(school_id__in=dse_school_list)
                if int(dse_govt[i][0][0])==1:
                    dl_ds_g_c1=dl_ds_g_c2=dl_ds_g_c3=dl_ds_g_c4=dl_ds_g_c5=dl_ds_g_c6=dl_ds_g_c7=dl_ds_g_c8=dl_ds_g_c9=dl_ds_g_c10=dl_ds_g_c11=dl_ds_g_c12=dl_ds_g_c_total=0 
                    for j in dse:
                        dl_ds_g_c1 +=j.c1
                        dl_ds_g_c2 +=j.c2
                        dl_ds_g_c3 +=j.c3
                        dl_ds_g_c4 +=j.c4
                        dl_ds_g_c5 +=j.c5
                        dl_ds_g_c6 +=j.c6
                        dl_ds_g_c7 +=j.c7
                        dl_ds_g_c8 +=j.c8
                        dl_ds_g_c9 +=j.c9
                        dl_ds_g_c10 +=j.c10
                        dl_ds_g_c11 +=j.c11
                        dl_ds_g_c12 +=j.c12
                        dl_ds_g_c_total+=j.c_total
                if int(dse_govt[i][0][0])==2:
                    dl_ds_pa_c1=dl_ds_pa_c2=dl_ds_pa_c3=dl_ds_pa_c4=dl_ds_pa_c5=dl_ds_pa_c6=dl_ds_pa_c7=dl_ds_pa_c8=dl_ds_pa_c9=dl_ds_pa_c10=dl_ds_pa_c11=dl_ds_pa_c12=dl_ds_pa_c_total=0 
                    for j in dse:
                        dl_ds_pa_c1 +=j.c1
                        dl_ds_pa_c2 +=j.c2
                        dl_ds_pa_c3 +=j.c3
                        dl_ds_pa_c4 +=j.c4
                        dl_ds_pa_c5 +=j.c5
                        dl_ds_pa_c6 +=j.c6
                        dl_ds_pa_c7 +=j.c7
                        dl_ds_pa_c8 +=j.c8
                        dl_ds_pa_c9 +=j.c9
                        dl_ds_pa_c10 +=j.c10
                        dl_ds_pa_c11 +=j.c11
                        dl_ds_pa_c12 +=j.c12
                        dl_ds_pa_c_total+=j.c_total
                if int(dse_govt[i][0][0])==6:
                    dl_dee_g_c1=dl_dee_g_c2=dl_dee_g_c3=dl_dee_g_c4=dl_dee_g_c5=dl_dee_g_c6=dl_dee_g_c7=dl_dee_g_c8=dl_dee_g_c9=dl_dee_g_c10=dl_dee_g_c11=dl_dee_g_c12=dl_dee_g_c_total=0 
                    for j in dse:
                        dl_dee_g_c1 +=j.c1
                        dl_dee_g_c2 +=j.c2
                        dl_dee_g_c3 +=j.c3
                        dl_dee_g_c4 +=j.c4
                        dl_dee_g_c5 +=j.c5
                        dl_dee_g_c6 +=j.c6
                        dl_dee_g_c7 +=j.c7
                        dl_dee_g_c8 +=j.c8
                        dl_dee_g_c9 +=j.c9
                        dl_dee_g_c10 +=j.c10
                        dl_dee_g_c11 +=j.c11
                        dl_dee_g_c12 +=j.c12
                        dl_dee_g_c_total+=j.c_total
                if int(dse_govt[i][0][0])==7:
                    dl_dee_pa_c1=dl_dee_pa_c2=dl_dee_pa_c3=dl_dee_pa_c4=dl_dee_pa_c5=dl_dee_pa_c6=dl_dee_pa_c7=dl_dee_pa_c8=dl_dee_pa_c9=dl_dee_pa_c10=dl_dee_pa_c11=dl_dee_pa_c12=dl_dee_pa_c_total=0 
                    for j in dse:
                        dl_dee_pa_c1 +=j.c1
                        dl_dee_pa_c2 +=j.c2
                        dl_dee_pa_c3 +=j.c3
                        dl_dee_pa_c4 +=j.c4
                        dl_dee_pa_c5 +=j.c5
                        dl_dee_pa_c6 +=j.c6
                        dl_dee_pa_c7 +=j.c7
                        dl_dee_pa_c8 +=j.c8
                        dl_dee_pa_c9 +=j.c9
                        dl_dee_pa_c10 +=j.c10
                        dl_dee_pa_c11 +=j.c11
                        dl_dee_pa_c12 +=j.c12
                        dl_dee_pa_c_total+=j.c_total                 
        return render(request,'moi/d_l_moi_report.html',locals())

class block_level_moi_report(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated():
            global all_schools
            global moi
            global dse_govt
            user_access_level=[4,3]
            user=self.kwargs['pk']
            block=Block.objects.get(id=user)
            blockk=block.block_name
            for i in range(0,len(dse_govt)):   
                b_l_school_list=all_schools.filter(block_id=user,management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])
                schl_list=moi.filter(school_id__in=b_l_school_list).order_by('school')
                if int(dse_govt[i][0][0])==1:
                    bl_ds_g_c1_tam=bl_ds_g_c2_tam=bl_ds_g_c3_tam=bl_ds_g_c4_tam=bl_ds_g_c5_tam=bl_ds_g_c6_tam=bl_ds_g_c7_tam=bl_ds_g_c8_tam=bl_ds_g_c9_tam=bl_ds_g_c10_tam=bl_ds_g_c11_tam=bl_ds_g_c12_tam=bl_ds_g_total_tam=0 
                    bl_ds_g_c1_eng=bl_ds_g_c2_eng=bl_ds_g_c3_eng=bl_ds_g_c4_eng=bl_ds_g_c5_eng=bl_ds_g_c6_eng=bl_ds_g_c7_eng=bl_ds_g_c8_eng=bl_ds_g_c9_eng=bl_ds_g_c10_eng=bl_ds_g_c11_eng=bl_ds_g_c12_eng=bl_ds_g_total_eng=0 
                    bl_ds_g_c1_telgu=bl_ds_g_c2_telgu=bl_ds_g_c3_telgu=bl_ds_g_c4_telgu=bl_ds_g_c5_telgu=bl_ds_g_c6_telgu=bl_ds_g_c7_telgu=bl_ds_g_c8_telgu=bl_ds_g_c9_telgu=bl_ds_g_c10_telgu=bl_ds_g_c11_telgu=bl_ds_g_c12_telgu=bl_ds_g_total_telgu=0 
                    bl_ds_g_c1_malam=bl_ds_g_c2_malam=bl_ds_g_c3_malam=bl_ds_g_c4_malam=bl_ds_g_c5_malam=bl_ds_g_c6_malam=bl_ds_g_c7_malam=bl_ds_g_c8_malam=bl_ds_g_c9_malam=bl_ds_g_c10_malam=bl_ds_g_c11_malam=bl_ds_g_c12_malam=bl_ds_g_total_malam=0 
                    bl_ds_g_c1_kanada=bl_ds_g_c2_kanada=bl_ds_g_c3_kanada=bl_ds_g_c4_kanada=bl_ds_g_c5_kanada=bl_ds_g_c6_kanada=bl_ds_g_c7_kanada=bl_ds_g_c8_kanada=bl_ds_g_c9_kanada=bl_ds_g_c10_kanada=bl_ds_g_c11_kanada=bl_ds_g_c12_kanada=bl_ds_g_total_kanada=0 
                    bl_ds_g_c1_urudu=bl_ds_g_c2_urudu=bl_ds_g_c3_urudu=bl_ds_g_c4_urudu=bl_ds_g_c5_urudu=bl_ds_g_c6_urudu=bl_ds_g_c7_urudu=bl_ds_g_c8_urudu=bl_ds_g_c9_urudu=bl_ds_g_c10_urudu=bl_ds_g_c11_urudu=bl_ds_g_c12_urudu=bl_ds_g_total_urudu=0 
                    for j in schl_list:
                        bl_ds_g_c1_tam +=j.c1_tamil
                        bl_ds_g_c2_tam +=j.c2_tamil
                        bl_ds_g_c3_tam +=j.c3_tamil
                        bl_ds_g_c4_tam +=j.c4_tamil
                        bl_ds_g_c5_tam +=j.c5_tamil
                        bl_ds_g_c6_tam +=j.c6_tamil
                        bl_ds_g_c7_tam +=j.c7_tamil
                        bl_ds_g_c8_tam +=j.c8_tamil
                        bl_ds_g_c9_tam +=j.c9_tamil
                        bl_ds_g_c10_tam +=j.c10_tamil
                        bl_ds_g_c11_tam +=j.c11_tamil
                        bl_ds_g_c12_tam +=j.c12_tamil
                        bl_ds_g_total_tam+=j.total_tamil

                        bl_ds_g_c1_eng +=j.c1_eng
                        bl_ds_g_c2_eng +=j.c2_eng
                        bl_ds_g_c3_eng +=j.c3_eng
                        bl_ds_g_c4_eng +=j.c4_eng
                        bl_ds_g_c5_eng +=j.c5_eng
                        bl_ds_g_c6_eng +=j.c6_eng
                        bl_ds_g_c7_eng +=j.c7_eng
                        bl_ds_g_c8_eng +=j.c8_eng
                        bl_ds_g_c9_eng +=j.c9_eng
                        bl_ds_g_c10_eng +=j.c10_eng
                        bl_ds_g_c11_eng +=j.c11_eng
                        bl_ds_g_c12_eng +=j.c12_eng
                        bl_ds_g_total_eng+=j.total_eng

                        bl_ds_g_c1_telgu +=j.c1_telugu
                        bl_ds_g_c2_telgu +=j.c2_telugu
                        bl_ds_g_c3_telgu +=j.c3_telugu
                        bl_ds_g_c4_telgu +=j.c4_telugu
                        bl_ds_g_c5_telgu +=j.c5_telugu
                        bl_ds_g_c6_telgu +=j.c6_telugu
                        bl_ds_g_c7_telgu +=j.c7_telugu
                        bl_ds_g_c8_telgu +=j.c8_telugu
                        bl_ds_g_c9_telgu +=j.c9_telugu
                        bl_ds_g_c10_telgu +=j.c10_telugu
                        bl_ds_g_c11_telgu +=j.c11_telugu
                        bl_ds_g_c12_telgu +=j.c12_telugu
                        bl_ds_g_total_telgu+=j.total_telugu
                        
                        bl_ds_g_c1_malam +=j.c1_mlym
                        bl_ds_g_c2_malam +=j.c2_mlym
                        bl_ds_g_c3_malam +=j.c3_mlym
                        bl_ds_g_c4_malam +=j.c4_mlym
                        bl_ds_g_c5_malam +=j.c5_mlym
                        bl_ds_g_c6_malam +=j.c6_mlym
                        bl_ds_g_c7_malam +=j.c7_mlym
                        bl_ds_g_c8_malam +=j.c8_mlym
                        bl_ds_g_c9_malam +=j.c9_mlym
                        bl_ds_g_c10_malam +=j.c10_mlym
                        bl_ds_g_c11_malam +=j.c11_mlym
                        bl_ds_g_c12_malam +=j.c12_mlym
                        bl_ds_g_total_malam+=j.total_mlym

                        bl_ds_g_c1_kanada +=j.c1_kanada
                        bl_ds_g_c2_kanada +=j.c2_kanada
                        bl_ds_g_c3_kanada +=j.c3_kanada
                        bl_ds_g_c4_kanada +=j.c4_kanada
                        bl_ds_g_c5_kanada +=j.c5_kanada
                        bl_ds_g_c6_kanada +=j.c6_kanada
                        bl_ds_g_c7_kanada +=j.c7_kanada
                        bl_ds_g_c8_kanada +=j.c8_kanada
                        bl_ds_g_c9_kanada +=j.c9_kanada
                        bl_ds_g_c10_kanada +=j.c10_kanada
                        bl_ds_g_c11_kanada +=j.c11_kanada
                        bl_ds_g_c12_kanada +=j.c12_kanada
                        bl_ds_g_total_kanada+=j.total_kanada

                        bl_ds_g_c1_urudu +=j.c1_urdu
                        bl_ds_g_c2_urudu +=j.c2_urdu
                        bl_ds_g_c3_urudu +=j.c3_urdu
                        bl_ds_g_c4_urudu +=j.c4_urdu
                        bl_ds_g_c5_urudu +=j.c5_urdu
                        bl_ds_g_c6_urudu +=j.c6_urdu
                        bl_ds_g_c7_urudu +=j.c7_urdu
                        bl_ds_g_c8_urudu +=j.c8_urdu
                        bl_ds_g_c9_urudu +=j.c9_urdu
                        bl_ds_g_c10_urudu +=j.c10_urdu
                        bl_ds_g_c11_urudu +=j.c11_urdu
                        bl_ds_g_c12_urudu +=j.c12_urdu
                        bl_ds_g_total_urudu+=j.total_urdu

                if int(dse_govt[i][0][0])==2:
                    bl_ds_pa_c1_tam=bl_ds_pa_c2_tam=bl_ds_pa_c3_tam=bl_ds_pa_c4_tam=bl_ds_pa_c5_tam=bl_ds_pa_c6_tam=bl_ds_pa_c7_tam=bl_ds_pa_c8_tam=bl_ds_pa_c9_tam=bl_ds_pa_c10_tam=bl_ds_pa_c11_tam=bl_ds_pa_c12_tam=bl_ds_pa_total_tam=0
                    bl_ds_pa_c1_eng=bl_ds_pa_c2_eng=bl_ds_pa_c3_eng=bl_ds_pa_c4_eng=bl_ds_pa_c5_eng=bl_ds_pa_c6_eng=bl_ds_pa_c7_eng=bl_ds_pa_c8_eng=bl_ds_pa_c9_eng=bl_ds_pa_c10_eng=bl_ds_pa_c11_eng=bl_ds_pa_c12_eng=bl_ds_pa_total_eng=0 
                    bl_ds_pa_c1_telgu=bl_ds_pa_c2_telgu=bl_ds_pa_c3_telgu=bl_ds_pa_c4_telgu=bl_ds_pa_c5_telgu=bl_ds_pa_c6_telgu=bl_ds_pa_c7_telgu=bl_ds_pa_c8_telgu=bl_ds_pa_c9_telgu=bl_ds_pa_c10_telgu=bl_ds_pa_c11_telgu=bl_ds_pa_c12_telgu=bl_ds_pa_total_telgu=0 
                    bl_ds_pa_c1_malam=bl_ds_pa_c2_malam=bl_ds_pa_c3_malam=bl_ds_pa_c4_malam=bl_ds_pa_c5_malam=bl_ds_pa_c6_malam=bl_ds_pa_c7_malam=bl_ds_pa_c8_malam=bl_ds_pa_c9_malam=bl_ds_pa_c10_malam=bl_ds_pa_c11_malam=bl_ds_pa_c12_malam=bl_ds_pa_total_malam=0 
                    bl_ds_pa_c1_kanada=bl_ds_pa_c2_kanada=bl_ds_pa_c3_kanada=bl_ds_pa_c4_kanada=bl_ds_pa_c5_kanada=bl_ds_pa_c6_kanada=bl_ds_pa_c7_kanada=bl_ds_pa_c8_kanada=bl_ds_pa_c9_kanada=bl_ds_pa_c10_kanada=bl_ds_pa_c11_kanada=bl_ds_pa_c12_kanada=bl_ds_pa_total_kanada=0 
                    bl_ds_pa_c1_urudu=bl_ds_pa_c2_urudu=bl_ds_pa_c3_urudu=bl_ds_pa_c4_urudu=bl_ds_pa_c5_urudu=bl_ds_pa_c6_urudu=bl_ds_pa_c7_urudu=bl_ds_pa_c8_urudu=bl_ds_pa_c9_urudu=bl_ds_pa_c10_urudu=bl_ds_pa_c11_urudu=bl_ds_pa_c12_urudu=bl_ds_pa_total_urudu=0 
                    for j in schl_list:
                        bl_ds_pa_c1_tam +=j.c1_tamil
                        bl_ds_pa_c2_tam +=j.c2_tamil
                        bl_ds_pa_c3_tam +=j.c3_tamil
                        bl_ds_pa_c4_tam +=j.c4_tamil
                        bl_ds_pa_c5_tam +=j.c5_tamil
                        bl_ds_pa_c6_tam +=j.c6_tamil
                        bl_ds_pa_c7_tam +=j.c7_tamil
                        bl_ds_pa_c8_tam +=j.c8_tamil
                        bl_ds_pa_c9_tam +=j.c9_tamil
                        bl_ds_pa_c10_tam +=j.c10_tamil
                        bl_ds_pa_c11_tam +=j.c11_tamil
                        bl_ds_pa_c12_tam +=j.c12_tamil
                        bl_ds_pa_total_tam+=j.total_tamil

                        bl_ds_pa_c1_eng +=j.c1_eng
                        bl_ds_pa_c2_eng +=j.c2_eng
                        bl_ds_pa_c3_eng +=j.c3_eng
                        bl_ds_pa_c4_eng +=j.c4_eng
                        bl_ds_pa_c5_eng +=j.c5_eng
                        bl_ds_pa_c6_eng +=j.c6_eng
                        bl_ds_pa_c7_eng +=j.c7_eng
                        bl_ds_pa_c8_eng +=j.c8_eng
                        bl_ds_pa_c9_eng +=j.c9_eng
                        bl_ds_pa_c10_eng +=j.c10_eng
                        bl_ds_pa_c11_eng +=j.c11_eng
                        bl_ds_pa_c12_eng +=j.c12_eng
                        bl_ds_pa_total_eng+=j.total_eng

                        bl_ds_pa_c1_telgu +=j.c1_telugu
                        bl_ds_pa_c2_telgu +=j.c2_telugu
                        bl_ds_pa_c3_telgu +=j.c3_telugu
                        bl_ds_pa_c4_telgu +=j.c4_telugu
                        bl_ds_pa_c5_telgu +=j.c5_telugu
                        bl_ds_pa_c6_telgu +=j.c6_telugu
                        bl_ds_pa_c7_telgu +=j.c7_telugu
                        bl_ds_pa_c8_telgu +=j.c8_telugu
                        bl_ds_pa_c9_telgu +=j.c9_telugu
                        bl_ds_pa_c10_telgu +=j.c10_telugu
                        bl_ds_pa_c11_telgu +=j.c11_telugu
                        bl_ds_pa_c12_telgu +=j.c12_telugu
                        bl_ds_pa_total_telgu+=j.total_telugu
                        
                        bl_ds_pa_c1_malam +=j.c1_mlym
                        bl_ds_pa_c2_malam +=j.c2_mlym
                        bl_ds_pa_c3_malam +=j.c3_mlym
                        bl_ds_pa_c4_malam +=j.c4_mlym
                        bl_ds_pa_c5_malam +=j.c5_mlym
                        bl_ds_pa_c6_malam +=j.c6_mlym
                        bl_ds_pa_c7_malam +=j.c7_mlym
                        bl_ds_pa_c8_malam +=j.c8_mlym
                        bl_ds_pa_c9_malam +=j.c9_mlym
                        bl_ds_pa_c10_malam +=j.c10_mlym
                        bl_ds_pa_c11_malam +=j.c11_mlym
                        bl_ds_pa_c12_malam +=j.c12_mlym
                        bl_ds_pa_total_malam+=j.total_mlym

                        bl_ds_pa_c1_kanada +=j.c1_kanada
                        bl_ds_pa_c2_kanada +=j.c2_kanada
                        bl_ds_pa_c3_kanada +=j.c3_kanada
                        bl_ds_pa_c4_kanada +=j.c4_kanada
                        bl_ds_pa_c5_kanada +=j.c5_kanada
                        bl_ds_pa_c6_kanada +=j.c6_kanada
                        bl_ds_pa_c7_kanada +=j.c7_kanada
                        bl_ds_pa_c8_kanada +=j.c8_kanada
                        bl_ds_pa_c9_kanada +=j.c9_kanada
                        bl_ds_pa_c10_kanada +=j.c10_kanada
                        bl_ds_pa_c11_kanada +=j.c11_kanada
                        bl_ds_pa_c12_kanada +=j.c12_kanada
                        bl_ds_pa_total_kanada+=j.total_kanada

                        bl_ds_pa_c1_urudu +=j.c1_urdu
                        bl_ds_pa_c2_urudu +=j.c2_urdu
                        bl_ds_pa_c3_urudu +=j.c3_urdu
                        bl_ds_pa_c4_urudu +=j.c4_urdu
                        bl_ds_pa_c5_urudu +=j.c5_urdu
                        bl_ds_pa_c6_urudu +=j.c6_urdu
                        bl_ds_pa_c7_urudu +=j.c7_urdu
                        bl_ds_pa_c8_urudu +=j.c8_urdu
                        bl_ds_pa_c9_urudu +=j.c9_urdu
                        bl_ds_pa_c10_urudu +=j.c10_urdu
                        bl_ds_pa_c11_urudu +=j.c11_urdu
                        bl_ds_pa_c12_urudu +=j.c12_urdu
                        bl_ds_pa_total_urudu+=j.total_urdu
                if int(dse_govt[i][0][0])==6:
                    bl_dee_g_c1_tam=bl_dee_g_c2_tam=bl_dee_g_c3_tam=bl_dee_g_c4_tam=bl_dee_g_c5_tam=bl_dee_g_c6_tam=bl_dee_g_c7_tam=bl_dee_g_c8_tam=bl_dee_g_c9_tam=bl_dee_g_c10_tam=bl_dee_g_c11_tam=bl_dee_g_c12_tam=bl_dee_g_total_tam=0
                    bl_dee_g_c1_eng=bl_dee_g_c2_eng=bl_dee_g_c3_eng=bl_dee_g_c4_eng=bl_dee_g_c5_eng=bl_dee_g_c6_eng=bl_dee_g_c7_eng=bl_dee_g_c8_eng=bl_dee_g_c9_eng=bl_dee_g_c10_eng=bl_dee_g_c11_eng=bl_dee_g_c12_eng=bl_dee_g_total_eng=0 
                    bl_dee_g_c1_telgu=bl_dee_g_c2_telgu=bl_dee_g_c3_telgu=bl_dee_g_c4_telgu=bl_dee_g_c5_telgu=bl_dee_g_c6_telgu=bl_dee_g_c7_telgu=bl_dee_g_c8_telgu=bl_dee_g_c9_telgu=bl_dee_g_c10_telgu=bl_dee_g_c11_telgu=bl_dee_g_c12_telgu=bl_dee_g_total_telgu=0 
                    bl_dee_g_c1_malam=bl_dee_g_c2_malam=bl_dee_g_c3_malam=bl_dee_g_c4_malam=bl_dee_g_c5_malam=bl_dee_g_c6_malam=bl_dee_g_c7_malam=bl_dee_g_c8_malam=bl_dee_g_c9_malam=bl_dee_g_c10_malam=bl_dee_g_c11_malam=bl_dee_g_c12_malam=bl_dee_g_total_malam=0 
                    bl_dee_g_c1_kanada=bl_dee_g_c2_kanada=bl_dee_g_c3_kanada=bl_dee_g_c4_kanada=bl_dee_g_c5_kanada=bl_dee_g_c6_kanada=bl_dee_g_c7_kanada=bl_dee_g_c8_kanada=bl_dee_g_c9_kanada=bl_dee_g_c10_kanada=bl_dee_g_c11_kanada=bl_dee_g_c12_kanada=bl_dee_g_total_kanada=0 
                    bl_dee_g_c1_urudu=bl_dee_g_c2_urudu=bl_dee_g_c3_urudu=bl_dee_g_c4_urudu=bl_dee_g_c5_urudu=bl_dee_g_c6_urudu=bl_dee_g_c7_urudu=bl_dee_g_c8_urudu=bl_dee_g_c9_urudu=bl_dee_g_c10_urudu=bl_dee_g_c11_urudu=bl_dee_g_c12_urudu=bl_dee_g_total_urudu=0 
                    for j in schl_list:
                        bl_dee_g_c1_tam +=j.c1_tamil
                        bl_dee_g_c2_tam +=j.c2_tamil
                        bl_dee_g_c3_tam +=j.c3_tamil
                        bl_dee_g_c4_tam +=j.c4_tamil
                        bl_dee_g_c5_tam +=j.c5_tamil
                        bl_dee_g_c6_tam +=j.c6_tamil
                        bl_dee_g_c7_tam +=j.c7_tamil
                        bl_dee_g_c8_tam +=j.c8_tamil
                        bl_dee_g_c9_tam +=j.c9_tamil
                        bl_dee_g_c10_tam +=j.c10_tamil
                        bl_dee_g_c11_tam +=j.c11_tamil
                        bl_dee_g_c12_tam +=j.c12_tamil
                        bl_dee_g_total_tam+=j.total_tamil

                        bl_dee_g_c1_eng +=j.c1_eng
                        bl_dee_g_c2_eng +=j.c2_eng
                        bl_dee_g_c3_eng +=j.c3_eng
                        bl_dee_g_c4_eng +=j.c4_eng
                        bl_dee_g_c5_eng +=j.c5_eng
                        bl_dee_g_c6_eng +=j.c6_eng
                        bl_dee_g_c7_eng +=j.c7_eng
                        bl_dee_g_c8_eng +=j.c8_eng
                        bl_dee_g_c9_eng +=j.c9_eng
                        bl_dee_g_c10_eng +=j.c10_eng
                        bl_dee_g_c11_eng +=j.c11_eng
                        bl_dee_g_c12_eng +=j.c12_eng
                        bl_dee_g_total_eng+=j.total_eng

                        bl_dee_g_c1_telgu +=j.c1_telugu
                        bl_dee_g_c2_telgu +=j.c2_telugu
                        bl_dee_g_c3_telgu +=j.c3_telugu
                        bl_dee_g_c4_telgu +=j.c4_telugu
                        bl_dee_g_c5_telgu +=j.c5_telugu
                        bl_dee_g_c6_telgu +=j.c6_telugu
                        bl_dee_g_c7_telgu +=j.c7_telugu
                        bl_dee_g_c8_telgu +=j.c8_telugu
                        bl_dee_g_c9_telgu +=j.c9_telugu
                        bl_dee_g_c10_telgu +=j.c10_telugu
                        bl_dee_g_c11_telgu +=j.c11_telugu
                        bl_dee_g_c12_telgu +=j.c12_telugu
                        bl_dee_g_total_telgu+=j.total_telugu
                        
                        bl_dee_g_c1_malam +=j.c1_mlym
                        bl_dee_g_c2_malam +=j.c2_mlym
                        bl_dee_g_c3_malam +=j.c3_mlym
                        bl_dee_g_c4_malam +=j.c4_mlym
                        bl_dee_g_c5_malam +=j.c5_mlym
                        bl_dee_g_c6_malam +=j.c6_mlym
                        bl_dee_g_c7_malam +=j.c7_mlym
                        bl_dee_g_c8_malam +=j.c8_mlym
                        bl_dee_g_c9_malam +=j.c9_mlym
                        bl_dee_g_c10_malam +=j.c10_mlym
                        bl_dee_g_c11_malam +=j.c11_mlym
                        bl_dee_g_c12_malam +=j.c12_mlym
                        bl_dee_g_total_malam+=j.total_mlym

                        bl_dee_g_c1_kanada +=j.c1_kanada
                        bl_dee_g_c2_kanada +=j.c2_kanada
                        bl_dee_g_c3_kanada +=j.c3_kanada
                        bl_dee_g_c4_kanada +=j.c4_kanada
                        bl_dee_g_c5_kanada +=j.c5_kanada
                        bl_dee_g_c6_kanada +=j.c6_kanada
                        bl_dee_g_c7_kanada +=j.c7_kanada
                        bl_dee_g_c8_kanada +=j.c8_kanada
                        bl_dee_g_c9_kanada +=j.c9_kanada
                        bl_dee_g_c10_kanada +=j.c10_kanada
                        bl_dee_g_c11_kanada +=j.c11_kanada
                        bl_dee_g_c12_kanada +=j.c12_kanada
                        bl_dee_g_total_kanada+=j.total_kanada

                        bl_dee_g_c1_urudu +=j.c1_urdu
                        bl_dee_g_c2_urudu +=j.c2_urdu
                        bl_dee_g_c3_urudu +=j.c3_urdu
                        bl_dee_g_c4_urudu +=j.c4_urdu
                        bl_dee_g_c5_urudu +=j.c5_urdu
                        bl_dee_g_c6_urudu +=j.c6_urdu
                        bl_dee_g_c7_urudu +=j.c7_urdu
                        bl_dee_g_c8_urudu +=j.c8_urdu
                        bl_dee_g_c9_urudu +=j.c9_urdu
                        bl_dee_g_c10_urudu +=j.c10_urdu
                        bl_dee_g_c11_urudu +=j.c11_urdu
                        bl_dee_g_c12_urudu +=j.c12_urdu
                        bl_dee_g_total_urudu+=j.total_urdu
                if int(dse_govt[i][0][0])==7:
                    bl_dee_pa_c1_tam=bl_dee_pa_c2_tam=bl_dee_pa_c3_tam=bl_dee_pa_c4_tam=bl_dee_pa_c5_tam=bl_dee_pa_c6_tam=bl_dee_pa_c7_tam=bl_dee_pa_c8_tam=bl_dee_pa_c9_tam=bl_dee_pa_c10_tam=bl_dee_pa_c11_tam=bl_dee_pa_c12_tam=bl_dee_pa_total_tam=0
                    bl_dee_pa_c1_eng=bl_dee_pa_c2_eng=bl_dee_pa_c3_eng=bl_dee_pa_c4_eng=bl_dee_pa_c5_eng=bl_dee_pa_c6_eng=bl_dee_pa_c7_eng=bl_dee_pa_c8_eng=bl_dee_pa_c9_eng=bl_dee_pa_c10_eng=bl_dee_pa_c11_eng=bl_dee_pa_c12_eng=bl_dee_pa_total_eng=0 
                    bl_dee_pa_c1_telgu=bl_dee_pa_c2_telgu=bl_dee_pa_c3_telgu=bl_dee_pa_c4_telgu=bl_dee_pa_c5_telgu=bl_dee_pa_c6_telgu=bl_dee_pa_c7_telgu=bl_dee_pa_c8_telgu=bl_dee_pa_c9_telgu=bl_dee_pa_c10_telgu=bl_dee_pa_c11_telgu=bl_dee_pa_c12_telgu=bl_dee_pa_total_telgu=0 
                    bl_dee_pa_c1_malam=bl_dee_pa_c2_malam=bl_dee_pa_c3_malam=bl_dee_pa_c4_malam=bl_dee_pa_c5_malam=bl_dee_pa_c6_malam=bl_dee_pa_c7_malam=bl_dee_pa_c8_malam=bl_dee_pa_c9_malam=bl_dee_pa_c10_malam=bl_dee_pa_c11_malam=bl_dee_pa_c12_malam=bl_dee_pa_total_malam=0 
                    bl_dee_pa_c1_kanada=bl_dee_pa_c2_kanada=bl_dee_pa_c3_kanada=bl_dee_pa_c4_kanada=bl_dee_pa_c5_kanada=bl_dee_pa_c6_kanada=bl_dee_pa_c7_kanada=bl_dee_pa_c8_kanada=bl_dee_pa_c9_kanada=bl_dee_pa_c10_kanada=bl_dee_pa_c11_kanada=bl_dee_pa_c12_kanada=bl_dee_pa_total_kanada=0 
                    bl_dee_pa_c1_urudu=bl_dee_pa_c2_urudu=bl_dee_pa_c3_urudu=bl_dee_pa_c4_urudu=bl_dee_pa_c5_urudu=bl_dee_pa_c6_urudu=bl_dee_pa_c7_urudu=bl_dee_pa_c8_urudu=bl_dee_pa_c9_urudu=bl_dee_pa_c10_urudu=bl_dee_pa_c11_urudu=bl_dee_pa_c12_urudu=bl_dee_pa_total_urudu=0 
                    for j in schl_list:
                        bl_dee_pa_c1_tam +=j.c1_tamil
                        bl_dee_pa_c2_tam +=j.c2_tamil
                        bl_dee_pa_c3_tam +=j.c3_tamil
                        bl_dee_pa_c4_tam +=j.c4_tamil
                        bl_dee_pa_c5_tam +=j.c5_tamil
                        bl_dee_pa_c6_tam +=j.c6_tamil
                        bl_dee_pa_c7_tam +=j.c7_tamil
                        bl_dee_pa_c8_tam +=j.c8_tamil
                        bl_dee_pa_c9_tam +=j.c9_tamil
                        bl_dee_pa_c10_tam +=j.c10_tamil
                        bl_dee_pa_c11_tam +=j.c11_tamil
                        bl_dee_pa_c12_tam +=j.c12_tamil
                        bl_dee_pa_total_tam+=j.total_tamil

                        bl_dee_pa_c1_eng +=j.c1_eng
                        bl_dee_pa_c2_eng +=j.c2_eng
                        bl_dee_pa_c3_eng +=j.c3_eng
                        bl_dee_pa_c4_eng +=j.c4_eng
                        bl_dee_pa_c5_eng +=j.c5_eng
                        bl_dee_pa_c6_eng +=j.c6_eng
                        bl_dee_pa_c7_eng +=j.c7_eng
                        bl_dee_pa_c8_eng +=j.c8_eng
                        bl_dee_pa_c9_eng +=j.c9_eng
                        bl_dee_pa_c10_eng +=j.c10_eng
                        bl_dee_pa_c11_eng +=j.c11_eng
                        bl_dee_pa_c12_eng +=j.c12_eng
                        bl_dee_pa_total_eng+=j.total_eng

                        bl_dee_pa_c1_telgu +=j.c1_telugu
                        bl_dee_pa_c2_telgu +=j.c2_telugu
                        bl_dee_pa_c3_telgu +=j.c3_telugu
                        bl_dee_pa_c4_telgu +=j.c4_telugu
                        bl_dee_pa_c5_telgu +=j.c5_telugu
                        bl_dee_pa_c6_telgu +=j.c6_telugu
                        bl_dee_pa_c7_telgu +=j.c7_telugu
                        bl_dee_pa_c8_telgu +=j.c8_telugu
                        bl_dee_pa_c9_telgu +=j.c9_telugu
                        bl_dee_pa_c10_telgu +=j.c10_telugu
                        bl_dee_pa_c11_telgu +=j.c11_telugu
                        bl_dee_pa_c12_telgu +=j.c12_telugu
                        bl_dee_pa_total_telgu+=j.total_telugu
                        
                        bl_dee_pa_c1_malam +=j.c1_mlym
                        bl_dee_pa_c2_malam +=j.c2_mlym
                        bl_dee_pa_c3_malam +=j.c3_mlym
                        bl_dee_pa_c4_malam +=j.c4_mlym
                        bl_dee_pa_c5_malam +=j.c5_mlym
                        bl_dee_pa_c6_malam +=j.c6_mlym
                        bl_dee_pa_c7_malam +=j.c7_mlym
                        bl_dee_pa_c8_malam +=j.c8_mlym
                        bl_dee_pa_c9_malam +=j.c9_mlym
                        bl_dee_pa_c10_malam +=j.c10_mlym
                        bl_dee_pa_c11_malam +=j.c11_mlym
                        bl_dee_pa_c12_malam +=j.c12_mlym
                        bl_dee_pa_total_malam+=j.total_mlym

                        bl_dee_pa_c1_kanada +=j.c1_kanada
                        bl_dee_pa_c2_kanada +=j.c2_kanada
                        bl_dee_pa_c3_kanada +=j.c3_kanada
                        bl_dee_pa_c4_kanada +=j.c4_kanada
                        bl_dee_pa_c5_kanada +=j.c5_kanada
                        bl_dee_pa_c6_kanada +=j.c6_kanada
                        bl_dee_pa_c7_kanada +=j.c7_kanada
                        bl_dee_pa_c8_kanada +=j.c8_kanada
                        bl_dee_pa_c9_kanada +=j.c9_kanada
                        bl_dee_pa_c10_kanada +=j.c10_kanada
                        bl_dee_pa_c11_kanada +=j.c11_kanada
                        bl_dee_pa_c12_kanada +=j.c12_kanada
                        bl_dee_pa_total_kanada+=j.total_kanada

                        bl_dee_pa_c1_urudu +=j.c1_urdu
                        bl_dee_pa_c2_urudu +=j.c2_urdu
                        bl_dee_pa_c3_urudu +=j.c3_urdu
                        bl_dee_pa_c4_urudu +=j.c4_urdu
                        bl_dee_pa_c5_urudu +=j.c5_urdu
                        bl_dee_pa_c6_urudu +=j.c6_urdu
                        bl_dee_pa_c7_urudu +=j.c7_urdu
                        bl_dee_pa_c8_urudu +=j.c8_urdu
                        bl_dee_pa_c9_urudu +=j.c9_urdu
                        bl_dee_pa_c10_urudu +=j.c10_urdu
                        bl_dee_pa_c11_urudu +=j.c11_urdu
                        bl_dee_pa_c12_urudu +=j.c12_urdu
                        bl_dee_pa_total_urudu+=j.total_urdu
            for i in range(0,len(dse_govt)):   
                dse_school_list=all_schools.filter(block_id=user,management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])
                dse=enroll.filter(school_id__in=dse_school_list)
                if int(dse_govt[i][0][0])==1:
                    bl_ds_g_c1=bl_ds_g_c2=bl_ds_g_c3=bl_ds_g_c4=bl_ds_g_c5=bl_ds_g_c6=bl_ds_g_c7=bl_ds_g_c8=bl_ds_g_c9=bl_ds_g_c10=bl_ds_g_c11=bl_ds_g_c12=bl_ds_g_c_total=0 
                    for j in dse:
                        bl_ds_g_c1 +=j.c1
                        bl_ds_g_c2 +=j.c2
                        bl_ds_g_c3 +=j.c3
                        bl_ds_g_c4 +=j.c4
                        bl_ds_g_c5 +=j.c5
                        bl_ds_g_c6 +=j.c6
                        bl_ds_g_c7 +=j.c7
                        bl_ds_g_c8 +=j.c8
                        bl_ds_g_c9 +=j.c9
                        bl_ds_g_c10 +=j.c10
                        bl_ds_g_c11 +=j.c11
                        bl_ds_g_c12 +=j.c12
                        bl_ds_g_c_total+=j.c_total
                if int(dse_govt[i][0][0])==2:
                    bl_ds_pa_c1=bl_ds_pa_c2=bl_ds_pa_c3=bl_ds_pa_c4=bl_ds_pa_c5=bl_ds_pa_c6=bl_ds_pa_c7=bl_ds_pa_c8=bl_ds_pa_c9=bl_ds_pa_c10=bl_ds_pa_c11=bl_ds_pa_c12=bl_ds_pa_c_total=0 
                    for j in dse:
                        bl_ds_pa_c1 +=j.c1
                        bl_ds_pa_c2 +=j.c2
                        bl_ds_pa_c3 +=j.c3
                        bl_ds_pa_c4 +=j.c4
                        bl_ds_pa_c5 +=j.c5
                        bl_ds_pa_c6 +=j.c6
                        bl_ds_pa_c7 +=j.c7
                        bl_ds_pa_c8 +=j.c8
                        bl_ds_pa_c9 +=j.c9
                        bl_ds_pa_c10 +=j.c10
                        bl_ds_pa_c11 +=j.c11
                        bl_ds_pa_c12 +=j.c12
                        bl_ds_pa_c_total+=j.c_total
                if int(dse_govt[i][0][0])==6:
                    bl_dee_g_c1=bl_dee_g_c2=bl_dee_g_c3=bl_dee_g_c4=bl_dee_g_c5=bl_dee_g_c6=bl_dee_g_c7=bl_dee_g_c8=bl_dee_g_c9=bl_dee_g_c10=bl_dee_g_c11=bl_dee_g_c12=bl_dee_g_c_total=0 
                    for j in dse:
                        bl_dee_g_c1 +=j.c1
                        bl_dee_g_c2 +=j.c2
                        bl_dee_g_c3 +=j.c3
                        bl_dee_g_c4 +=j.c4
                        bl_dee_g_c5 +=j.c5
                        bl_dee_g_c6 +=j.c6
                        bl_dee_g_c7 +=j.c7
                        bl_dee_g_c8 +=j.c8
                        bl_dee_g_c9 +=j.c9
                        bl_dee_g_c10 +=j.c10
                        bl_dee_g_c11 +=j.c11
                        bl_dee_g_c12 +=j.c12
                        bl_dee_g_c_total+=j.c_total
                if int(dse_govt[i][0][0])==7:
                    bl_dee_pa_c1=bl_dee_pa_c2=bl_dee_pa_c3=bl_dee_pa_c4=bl_dee_pa_c5=bl_dee_pa_c6=bl_dee_pa_c7=bl_dee_pa_c8=bl_dee_pa_c9=bl_dee_pa_c10=bl_dee_pa_c11=bl_dee_pa_c12=bl_dee_pa_c_total=0 
                    for j in dse:
                        bl_dee_pa_c1 +=j.c1
                        bl_dee_pa_c2 +=j.c2
                        bl_dee_pa_c3 +=j.c3
                        bl_dee_pa_c4 +=j.c4
                        bl_dee_pa_c5 +=j.c5
                        bl_dee_pa_c6 +=j.c6
                        bl_dee_pa_c7 +=j.c7
                        bl_dee_pa_c8 +=j.c8
                        bl_dee_pa_c9 +=j.c9
                        bl_dee_pa_c10 +=j.c10
                        bl_dee_pa_c11 +=j.c11
                        bl_dee_pa_c12 +=j.c12
                        bl_dee_pa_c_total+=j.c_total                 
        return render(request,'moi/b_l_moi_report.html',locals())
    def post(self,request,**kwargs):
        global dse_govt        
        global all_schools
        global gender_wise
        global mgmt_name
        global enroll
        global moi

        mgmt_id = request.POST.get('blks', False)
        mgmt_blk=mgmt_id.split(',')
        for ii in range(0,len(dse_govt)):
            if str(dse_govt[ii][0][0])==str(mgmt_blk[0]):
                aa=dse_govt[ii][0]
                bb=sum(aa)
                cc=int(bb)-1
                dd=mgmt_name[cc]
                block_name=Block.objects.get(id=mgmt_blk[1])
                school_list=all_schools.filter(block_id=mgmt_blk[1],management_id__in=dse_govt[ii][1],category_id__in=dse_govt[ii][2])
                blk_enroll=enroll.filter(school_id__in=school_list).order_by('school')
                

        for ff in range(0,len(dse_govt)):
            if str(dse_govt[ff][0][0])==str(mgmt_blk[0]):
                aa=dse_govt[ff][0]
                bb=sum(aa)
                cc=int(bb)-1
                dd=mgmt_name[cc]
                block_name=Block.objects.get(id=mgmt_blk[1])
                school_list=all_schools.filter(block_id=mgmt_blk[1],management_id__in=dse_govt[ff][1],category_id__in=dse_govt[ff][2])
                blk_schl=moi.filter(school_id__in=school_list).order_by('school')
                
            return render(request,'moi/block_moi_school_report.html',locals())



