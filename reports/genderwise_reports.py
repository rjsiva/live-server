from django.views.generic import View
from students.views.child_detail_views import *
from django.contrib import messages
from django.shortcuts import render,redirect
from students.models import Child_detail
from baseapp.models import School
from django.db.models import Q
from baseapp.models import *
from reports.models import common_reports
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
import itertools
import pandas as pd 
import StringIO

dse_govt=[[[1],[1,2,4,5],[3,5,6,7,8,9,10]],
[[2],[6,7],[3,5,6,7,8,9,10]],
[[3],[8,12,13,14,15,16,17],[3,5,6,7,8,9,10]],
[[4],[9],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
[[5],[10,11],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
[[6],[1,2,3,4,5],[1,2,4,11,15]],
[[7],[6,7],[1,2,4,11,15]],
[[8],[8,12,13,14,15,16,17],[1,2,4,11,15]]]
all_schools=School.objects.all()
gender_wise=common_reports.objects.all().order_by('school')
mgmt_name=["DSE - Government",
"DSE - Private Aided",
"DSE - Private UnAided",
"Matriculation",
"CBSE/ICSE",
"DEE - Government",
"DEE - Private Aided",
"DEE - Private UnAided"]



def report_child_count_transfer(instance1,request1,request2,request3):
    class_studying=instance1
    transfer_flag=request2
    gender=request3
    child = common_reports.objects.get(school_id=request1)
    
    if transfer_flag == 1:
        if str(class_studying)=='I':
            child.c1 -= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c1_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c1_g-=1
                child.c_total_g-=1
            else:
                child.c1_t-=1
                child.c_total_t-=1
            
        elif str(class_studying)=='II':
            child.c2 -= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c2_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c2_g-=1
                child.c_total_g-=1
            else:
                child.c2_t-=1
                child.c_total_t-=1
            
        elif str(class_studying)=='III':
            child.c3 -= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c3_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c3_g-=1
                child.c_total_g-=1
            else:
                child.c3_t-=1
                child.c_total_t-=1
            
        elif str(class_studying)=='IV':
            child.c4 -= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c4_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c4_g-=1
                child.c_total_g-=1
            else:
                child.c4_t-=1
                child.c_total_t-=1
            
        elif str(class_studying)=='V':
            child.c5 -= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c5_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c5_g-=1
                child.c_total_g-=1
            else:
                child.c5_t-=1
                child.c_total_t-=1
            
        elif str(class_studying)=='VI':
            child.c6 -= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c6_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c6_g-=1
                child.c_total_g-=1
            else:
                child.c6_t-=1
                child.c_total_t-=1
            
        elif str(class_studying)=='VII':
            child.c7 -= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c7_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c7_g-=1
                child.c_total_g-=1
            else:
                child.c7_t-=1
                child.c_total_t-=1
            
        elif str(class_studying)=='VIII':
            child.c8 -= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c8_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c8_g-=1
                child.c_total_g-=1
            else:
                child.c8_t-=1
                child.c_total_t-=1
            
        elif str(class_studying)=='IX':
            child.c9-= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c9_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c9_g-=1
                child.c_total_g-=1
            else:
                child.c9_t-=1
                child.c_total_t-=1
        elif str(class_studying)=='X':
            child.c10 -= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c10_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c10_g-=1
                child.c_total_g-=1
            else:
                child.c10_t-=1
                child.c_total_t-=1
        elif str(class_studying)=='XI':
            child.c11 -= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c11_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c11_g-=1
                child.c_total_g-=1
            else:
                child.c11_t-=1
                child.c_total_t-=1
        elif str(class_studying)=='XII':
            child.c12 -= 1
            child.c_total-=1
            if str(gender)=='Male':
                child.c12_b-=1
                child.c_total_b-=1
            elif str(gender)=='Female':
                child.c12_g-=1
                child.c_total_g-=1
            else:
                child.c12_t-=1
                child.c_total_t-=1
        child.save() 
    return


def report_child_count_admit(instance1,request1,request2,request3):  
    class_studying=instance1
    transfer_flag=request2
    gender=request3
    child = common_reports.objects.get(school_id=request1)
    
    if transfer_flag == 2:
        if str(class_studying)=='I':
            child.c1 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c1_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c1_g+=1
                child.c_total_g+=1
            else:
                child.c1_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='II':
            child.c2 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c2_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c2_g+=1
                child.c_total_g+=1
            else:
                child.c2_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='III':
            child.c3 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c3_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c3_g+=1
                child.c_total_g+=1
            else:
                child.c3_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='IV':
            child.c4 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c4_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c4_g+=1
                child.c_total_g+=1
            else:
                child.c4_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='V':
            child.c5 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c5_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c5_g+=1
                child.c_total_g+=1
            else:
                child.c5_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='VI':
            child.c6 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c6_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c6_g+=1
                child.c_total_g+=1
            else:
                child.c6_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='VII':
            child.c7 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c7_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c7_g+=1
                child.c_total_g+=1
            else:
                child.c7_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='VIII':
            child.c8 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c8_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c8_g+=1
                child.c_total_g+=1
            else:
                child.c8_t+=1
                child.c_total_t+=1
            
        elif str(class_studying)=='IX':
            child.c9+= 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c9_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c9_g+=1
                child.c_total_g+=1
            else:
                child.c9_t+=1
                child.c_total_t+=1
        elif str(class_studying)=='X':
            child.c10 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c10_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c10_g+=1
                child.c_total_g+=1
            else:
                child.c10_t+=1
                child.c_total_t+=1
        elif str(class_studying)=='XI':
            child.c11 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c11_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c11_g+=1
                child.c_total_g+=1
            else:
                child.c11_t+=1
                child.c_total_t+=1
        elif str(class_studying)=='XII':
            child.c12 += 1
            child.c_total+=1
            if str(gender)=='Male':
                child.c12_b+=1
                child.c_total_b+=1
            elif str(gender)=='Female':
                child.c12_g+=1
                child.c_total_g+=1
            else:
                child.c12_t+=1
                child.c_total_t+=1
        child.save() 
    return

def report_child_count_update(request1,request2,request3,request4,request5):

    child = common_reports.objects.get(school_id=request1) #school_id
    cls_studying=request2 #before update class studying
    clss_studying=request3#class to be updated
    gender=request4 #new
    old_gender=request5 #old
    print old_gender
    if (old_gender==gender) and (cls_studying!=clss_studying):
        update_class_based(child,cls_studying,clss_studying,old_gender,gender)
    elif(old_gender!=gender) and (cls_studying==clss_studying):
        update_gender_based(child,clss_studying,old_gender,gender)
    elif(old_gender!=gender) and(cls_studying!=clss_studying):
        update_class_based(child,cls_studying,clss_studying,old_gender,gender)


def update_class_based(child,cls_studying,clss_studying,old_gender,gender):
    if str(cls_studying)=='I':
        child.c1 -= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c1_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c1_g-=1
            child.c_total_g-=1
        else:
            child.c1_t-=1
            child.c_total_t-=1
        
    elif str(cls_studying)=='II':
        child.c2 -= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c2_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c2_g-=1
            child.c_total_g-=1
        else:
            child.c2_t-=1
            child.c_total_t-=1
        
    elif str(cls_studying)=='III':
        child.c3 -= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c3_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c3_g-=1
            child.c_total_g-=1
        else:
            child.c3_t-=1
            child.c_total_t-=1
        
    elif str(cls_studying)=='IV':
        child.c4 -= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c4_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c4_g-=1
            child.c_total_g-=1
        else:
            child.c4_t-=1
            child.c_total_t-=1
        
    elif str(cls_studying)=='V':
        child.c5 -= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c5_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c5_g-=1
            child.c_total_g-=1
        else:
            child.c5_t-=1
            child.c_total_t-=1
        
    elif str(cls_studying)=='VI':
        child.c6 -= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c6_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c6_g-=1
            child.c_total_g-=1
        else:
            child.c6_t-=1
            child.c_total_t-=1
        
    elif str(cls_studying)=='VII':
        child.c7 -= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c7_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c7_g-=1
            child.c_total_g-=1
        else:
            child.c7_t-=1
            child.c_total_t-=1
        
    elif str(cls_studying)=='VIII':
        child.c8 -= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c8_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c8_g-=1
            child.c_total_g-=1
        else:
            child.c8_t-=1
            child.c_total_t-=1
        
    elif str(cls_studying)=='IX':
        child.c9-= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c9_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c9_g-=1
            child.c_total_g-=1
        else:
            child.c9_t-=1
            child.c_total_t-=1
    elif str(cls_studying)=='X':
        child.c10 -= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c10_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c10_g-=1
            child.c_total_g-=1
        else:
            child.c10_t-=1
            child.c_total_t-=1
    elif str(cls_studying)=='XI':
        child.c11 -= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c11_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c11_g-=1
            child.c_total_g-=1
        else:
            child.c11_t-=1
            child.c_total_t-=1
    elif str(cls_studying)=='XII':
        child.c12 -= 1
        child.c_total-=1
        if str(old_gender)=='Male':
            child.c12_b-=1
            child.c_total_b-=1
        elif str(old_gender)=='Female':
            child.c12_g-=1
            child.c_total_g-=1
        else:
            child.c12_t-=1
            child.c_total_t-=1

    if str(clss_studying)=='I':
        child.c1 += 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c1_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c1_g+=1
            child.c_total_g+=1
        else:
            child.c1_t+=1
            child.c_total_t+=1
        
    elif str(clss_studying)=='II':
        child.c2 += 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c2_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c2_g+=1
            child.c_total_g+=1
        else:
            child.c2_t+=1
            child.c_total_t+=1
        
    elif str(clss_studying)=='III':
        child.c3 += 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c3_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c3_g+=1
            child.c_total_g+=1
        else:
            child.c3_t+=1
            child.c_total_t+=1
        
    elif str(clss_studying)=='IV':
        child.c4 += 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c4_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c4_g+=1
            child.c_total_g+=1
        else:
            child.c4_t+=1
            child.c_total_t+=1
        
    elif str(clss_studying)=='V':
        child.c5 += 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c5_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c5_g+=1
            child.c_total_g+=1
        else:
            child.c5_t+=1
            child.c_total_t+=1
        
    elif str(clss_studying)=='VI':
        child.c6 += 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c6_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c6_g+=1
            child.c_total_g+=1
        else:
            child.c6_t+=1
            child.c_total_t+=1
        
    elif str(clss_studying)=='VII':
        child.c7 += 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c7_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c7_g+=1
            child.c_total_g+=1
        else:
            child.c7_t+=1
            child.c_total_t+=1
        
    elif str(clss_studying)=='VIII':
        child.c8 += 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c8_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c8_g+=1
            child.c_total_g+=1
        else:
            child.c8_t+=1
            child.c_total_t+=1
        
    elif str(clss_studying)=='IX':
        child.c9+= 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c9_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c9_g+=1
            child.c_total_g+=1
        else:
            child.c9_t+=1
            child.c_total_t+=1
    elif str(clss_studying)=='X':
        child.c10 += 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c10_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c10_g+=1
            child.c_total_g+=1
        else:
            child.c10_t+=1
            child.c_total_t+=1
    elif str(clss_studying)=='XI':
        child.c11 += 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c11_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c11_g+=1
            child.c_total_g+=1
        else:
            child.c11_t+=1
            child.c_total_t+=1
    elif str(clss_studying)=='XII':
        child.c12 += 1
        child.c_total+=1
        if str(gender)=='Male':
            child.c12_b+=1
            child.c_total_b+=1
        elif str(gender)=='Female':
            child.c12_g+=1
            child.c_total_g+=1
        else:
            child.c12_t+=1
            child.c_total_t+=1
    child.save()
    return
    
def update_gender_based(child,clss_studying,old_gender,gender):
    
    if str(clss_studying)=='I':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c1_b-=1
            child.c_total_b-=1
            child.c1_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c1_g-=1
            child.c_total_g-=1
            child.c1_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c1_t-=1
            child.c_total_t-=1
            child.c1_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c1_t-=1
            child.c_total_t-=1
            child.c1_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c1_b-=1
            child.c_total_b-=1
            child.c1_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c1_g-=1
            child.c_total_g-=1
            child.c1_t+=1
            child.c_total_t+=1
    if str(clss_studying)=='II':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c2_b-=1
            child.c_total_b-=1
            child.c2_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c2_g-=1
            child.c_total_g-=1
            child.c2_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c2_t-=1
            child.c_total_t-=1
            child.c2_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c2_t-=1
            child.c_total_t-=1
            child.c2_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c2_b-=1
            child.c_total_b-=1
            child.c2_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c2_g-=1
            child.c_total_g-=1
            child.c2_t+=1
            child.c_total_t+=1
    if str(clss_studying)=='III':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c3_b-=1
            child.c_total_b-=1
            child.c3_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c3_g-=1
            child.c_total_g-=1
            child.c3_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c3_t-=1
            child.c_total_t-=1
            child.c3_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c3_t-=1
            child.c_total_t-=1
            child.c3_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c3_b-=1
            child.c_total_b-=1
            child.c3_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c3_g-=1
            child.c_total_g-=1
            child.c3_t+=1
            child.c_total_t+=1

    if str(clss_studying)=='IV':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c4_b-=1
            child.c_total_b-=1
            child.c4_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c4_g-=1
            child.c_total_g-=1
            child.c4_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c4_t-=1
            child.c_total_t-=1
            child.c4_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c4_t-=1
            child.c_total_t-=1
            child.c4_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c4_b-=1
            child.c_total_b-=1
            child.c4_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c4_g-=1
            child.c_total_g-=1
            child.c4_t+=1
            child.c_total_t+=1
    if str(clss_studying)=='V':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c5_b-=1
            child.c_total_b-=1
            child.c5_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c5_g-=1
            child.c_total_g-=1
            child.c5_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c5_t-=1
            child.c_total_t-=1
            child.c5_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c5_t-=1
            child.c_total_t-=1
            child.c5_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c5_b-=1
            child.c_total_b-=1
            child.c5_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c5_g-=1
            child.c_total_g-=1
            child.c5_t+=1
            child.c_total_t+=1
    if str(clss_studying)=='VI':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c6_b-=1
            child.c_total_b-=1
            child.c6_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c6_g-=1
            child.c_total_g-=1
            child.c6_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c6_t-=1
            child.c_total_t-=1
            child.c6_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c6_t-=1
            child.c_total_t-=1
            child.c6_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c6_b-=1
            child.c_total_b-=1
            child.c6_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c6_g-=1
            child.c_total_g-=1
            child.c6_t+=1
            child.c_total_t+=1

    if str(clss_studying)=='VII':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c7_b-=1
            child.c_total_b-=1
            child.c7_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c7_g-=1
            child.c_total_g-=1
            child.c7_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c7_t-=1
            child.c_total_t-=1
            child.c7_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c7_t-=1
            child.c_total_t-=1
            child.c7_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c7_b-=1
            child.c_total_b-=1
            child.c7_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c7_g-=1
            child.c_total_g-=1
            child.c7_t+=1
            child.c_total_t+=1
    if str(clss_studying)=='VIII':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c8_b-=1
            child.c_total_b-=1
            child.c8_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c8_g-=1
            child.c_total_g-=1
            child.c8_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c8_t-=1
            child.c_total_t-=1
            child.c8_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c8_t-=1
            child.c_total_t-=1
            child.c8_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c8_b-=1
            child.c_total_b-=1
            child.c8_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c8_g-=1
            child.c_total_g-=1
            child.c8_t+=1
            child.c_total_t+=1
    if str(clss_studying)=='IX':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c9_b-=1
            child.c_total_b-=1
            child.c9_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c9_g-=1
            child.c_total_g-=1
            child.c9_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c9_t-=1
            child.c_total_t-=1
            child.c9_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c9_t-=1
            child.c_total_t-=1
            child.c9_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c9_b-=1
            child.c_total_b-=1
            child.c9_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c9_g-=1
            child.c_total_g-=1
            child.c9_t+=1
            child.c_total_t+=1
    if str(clss_studying)=='X':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c10_b-=1
            child.c_total_b-=1
            child.c10_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c10_g-=1
            child.c_total_g-=1
            child.c10_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c10_t-=1
            child.c_total_t-=1
            child.c10_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c10_t-=1
            child.c_total_t-=1
            child.c10_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c10_b-=1
            child.c_total_b-=1
            child.c10_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c10_g-=1
            child.c_total_g-=1
            child.c10_t+=1
            child.c_total_t+=1
    if str(clss_studying)=='XI':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c11_b-=1
            child.c_total_b-=1
            child.c11_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c11_g-=1
            child.c_total_g-=1
            child.c11_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c11_t-=1
            child.c_total_t-=1
            child.c11_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c11_t-=1
            child.c_total_t-=1
            child.c11_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c11_b-=1
            child.c_total_b-=1
            child.c11_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c11_g-=1
            child.c_total_g-=1
            child.c11_t+=1
            child.c_total_t+=1
    if str(clss_studying)=='XII':
        if (str(old_gender)=='Male' and str(gender)=='Female'):
            child.c12_b-=1
            child.c_total_b-=1
            child.c12_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Female' and str(gender)=='Male'):
            child.c12_g-=1
            child.c_total_g-=1
            child.c12_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Male'):
            child.c12_t-=1
            child.c_total_t-=1
            child.c12_b+=1
            child.c_total_b+=1
        elif (str(old_gender)=='Transgender' and str(gender)=='Female'):       
            child.c12_t-=1
            child.c_total_t-=1
            child.c12_g+=1
            child.c_total_g+=1
        elif (str(old_gender)=='Male' and str(gender)=='Transgender'):
            child.c12_b-=1
            child.c_total_b-=1
            child.c12_t+=1
            child.c_total_t+=1
        elif (str(old_gender)=='Female' and str(gender)=='Transgender'):       
            child.c12_g-=1
            child.c_total_g-=1
            child.c12_t+=1
            child.c_total_t+=1
    child.save()

class state_level_genderwise_report(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated():
            global all_schools
            global gender_wise
            global dse_govt
            for i in range(0,len(dse_govt)):   
                dse_school_list=all_schools.filter(management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])
                dse=gender_wise.filter(school_id__in=dse_school_list)
                if int(dse_govt[i][0][0])==1:
                    ds_g_c1=ds_g_c2=ds_g_c3=ds_g_c4=ds_g_c5=ds_g_c6=ds_g_c7=ds_g_c8=ds_g_c9=ds_g_c10=ds_g_c11=ds_g_c12=ds_g_c_total=0 
                    ds_g_c1_b=ds_g_c2_b=ds_g_c3_b=ds_g_c4_b=ds_g_c5_b=ds_g_c6_b=ds_g_c7_b=ds_g_c8_b=ds_g_c9_b=ds_g_c10_b=ds_g_c11_b=ds_g_c12_b=ds_g_c_total_b=0 
                    ds_g_c1_g=ds_g_c2_g=ds_g_c3_g=ds_g_c4_g=ds_g_c5_g=ds_g_c6_g=ds_g_c7_g=ds_g_c8_g=ds_g_c9_g=ds_g_c10_g=ds_g_c11_g=ds_g_c12_g=ds_g_c_total_g=0 
                    ds_g_c1_t=ds_g_c2_t=ds_g_c3_t=ds_g_c4_t=ds_g_c5_t=ds_g_c6_t=ds_g_c7_t=ds_g_c8_t=ds_g_c9_t=ds_g_c10_t=ds_g_c11_t=ds_g_c12_t=ds_g_c_total_t=0
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

                        ds_g_c1_b+=j.c1_b
                        ds_g_c2_b+=j.c2_b
                        ds_g_c3_b+=j.c3_b
                        ds_g_c4_b+=j.c4_b
                        ds_g_c5_b+=j.c5_b
                        ds_g_c6_b+=j.c6_b
                        ds_g_c7_b+=j.c7_b
                        ds_g_c8_b+=j.c8_b
                        ds_g_c9_b+=j.c9_b
                        ds_g_c10_b+=j.c10_b
                        ds_g_c11_b+=j.c11_b
                        ds_g_c12_b+=j.c12_b
                        ds_g_c_total_b+=j.c_total_b

                        ds_g_c1_g+=j.c1_g
                        ds_g_c2_g+=j.c2_g
                        ds_g_c3_g+=j.c3_g
                        ds_g_c4_g+=j.c4_g
                        ds_g_c5_g+=j.c5_g
                        ds_g_c6_g+=j.c6_g
                        ds_g_c7_g+=j.c7_g
                        ds_g_c8_g+=j.c8_g
                        ds_g_c9_g+=j.c9_g
                        ds_g_c10_g+=j.c10_g
                        ds_g_c11_g+=j.c11_g
                        ds_g_c12_g+=j.c12_g
                        ds_g_c_total_g+=j.c_total_g

                        ds_g_c1_t+=j.c1_t
                        ds_g_c2_t+=j.c2_t
                        ds_g_c3_t+=j.c3_t
                        ds_g_c4_t+=j.c4_t
                        ds_g_c5_t+=j.c5_t
                        ds_g_c6_t+=j.c6_t
                        ds_g_c7_t+=j.c7_t
                        ds_g_c8_t+=j.c8_t
                        ds_g_c9_t+=j.c9_t
                        ds_g_c10_t+=j.c10_t
                        ds_g_c11_t+=j.c11_t
                        ds_g_c12_t+=j.c12_t
                        ds_g_c_total_t+=j.c_total_t

                if int(dse_govt[i][0][0])==2:
                    ds_pa_c1=ds_pa_c2=ds_pa_c3=ds_pa_c4=ds_pa_c5=ds_pa_c6=ds_pa_c7=ds_pa_c8=ds_pa_c9=ds_pa_c10=ds_pa_c11=ds_pa_c12=ds_pa_c_total=0 
                    ds_pa_c1_b=ds_pa_c2_b=ds_pa_c3_b=ds_pa_c4_b=ds_pa_c5_b=ds_pa_c6_b=ds_pa_c7_b=ds_pa_c8_b=ds_pa_c9_b=ds_pa_c10_b=ds_pa_c11_b=ds_pa_c12_b=ds_pa_c_total_b=0 
                    ds_pa_c1_g=ds_pa_c2_g=ds_pa_c3_g=ds_pa_c4_g=ds_pa_c5_g=ds_pa_c6_g=ds_pa_c7_g=ds_pa_c8_g=ds_pa_c9_g=ds_pa_c10_g=ds_pa_c11_g=ds_pa_c12_g=ds_pa_c_total_g=0 
                    ds_pa_c1_t=ds_pa_c2_t=ds_pa_c3_t=ds_pa_c4_t=ds_pa_c5_t=ds_pa_c6_t=ds_pa_c7_t=ds_pa_c8_t=ds_pa_c9_t=ds_pa_c10_t=ds_pa_c11_t=ds_pa_c12_t=ds_pa_c_total_t=0
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

                        ds_pa_c1_b+=j.c1_b
                        ds_pa_c2_b+=j.c2_b
                        ds_pa_c3_b+=j.c3_b
                        ds_pa_c4_b+=j.c4_b
                        ds_pa_c5_b+=j.c5_b
                        ds_pa_c6_b+=j.c6_b
                        ds_pa_c7_b+=j.c7_b
                        ds_pa_c8_b+=j.c8_b
                        ds_pa_c9_b+=j.c9_b
                        ds_pa_c10_b+=j.c10_b
                        ds_pa_c11_b+=j.c11_b
                        ds_pa_c12_b+=j.c12_b
                        ds_pa_c_total_b+=j.c_total_b

                        ds_pa_c1_g+=j.c1_g
                        ds_pa_c2_g+=j.c2_g
                        ds_pa_c3_g+=j.c3_g
                        ds_pa_c4_g+=j.c4_g
                        ds_pa_c5_g+=j.c5_g
                        ds_pa_c6_g+=j.c6_g
                        ds_pa_c7_g+=j.c7_g
                        ds_pa_c8_g+=j.c8_g
                        ds_pa_c9_g+=j.c9_g
                        ds_pa_c10_g+=j.c10_g
                        ds_pa_c11_g+=j.c11_g
                        ds_pa_c12_g+=j.c12_g
                        ds_pa_c_total_g+=j.c_total_g

                        ds_pa_c1_t+=j.c1_t
                        ds_pa_c2_t+=j.c2_t
                        ds_pa_c3_t+=j.c3_t
                        ds_pa_c4_t+=j.c4_t
                        ds_pa_c5_t+=j.c5_t
                        ds_pa_c6_t+=j.c6_t
                        ds_pa_c7_t+=j.c7_t
                        ds_pa_c8_t+=j.c8_t
                        ds_pa_c9_t+=j.c9_t
                        ds_pa_c10_t+=j.c10_t
                        ds_pa_c11_t+=j.c11_t
                        ds_pa_c12_t+=j.c12_t
                        ds_pa_c_total_t+=j.c_total_t
                if int(dse_govt[i][0][0])==3:
                    ds_pua_c1=ds_pua_c2=ds_pua_c3=ds_pua_c4=ds_pua_c5=ds_pua_c6=ds_pua_c7=ds_pua_c8=ds_pua_c9=ds_pua_c10=ds_pua_c11=ds_pua_c12=ds_pua_c_total=0 
                    ds_pua_c1_b=ds_pua_c2_b=ds_pua_c3_b=ds_pua_c4_b=ds_pua_c5_b=ds_pua_c6_b=ds_pua_c7_b=ds_pua_c8_b=ds_pua_c9_b=ds_pua_c10_b=ds_pua_c11_b=ds_pua_c12_b=ds_pua_c_total_b=0 
                    ds_pua_c1_g=ds_pua_c2_g=ds_pua_c3_g=ds_pua_c4_g=ds_pua_c5_g=ds_pua_c6_g=ds_pua_c7_g=ds_pua_c8_g=ds_pua_c9_g=ds_pua_c10_g=ds_pua_c11_g=ds_pua_c12_g=ds_pua_c_total_g=0 
                    ds_pua_c1_t=ds_pua_c2_t=ds_pua_c3_t=ds_pua_c4_t=ds_pua_c5_t=ds_pua_c6_t=ds_pua_c7_t=ds_pua_c8_t=ds_pua_c9_t=ds_pua_c10_t=ds_pua_c11_t=ds_pua_c12_t=ds_pua_c_total_t=0
                    for j in dse:
                        ds_pua_c1 +=j.c1
                        ds_pua_c2 +=j.c2
                        ds_pua_c3 +=j.c3
                        ds_pua_c4 +=j.c4
                        ds_pua_c5 +=j.c5
                        ds_pua_c6 +=j.c6
                        ds_pua_c7 +=j.c7
                        ds_pua_c8 +=j.c8
                        ds_pua_c9 +=j.c9
                        ds_pua_c10 +=j.c10
                        ds_pua_c11 +=j.c11
                        ds_pua_c12 +=j.c12
                        ds_pua_c_total+=j.c_total

                        ds_pua_c1_b+=j.c1_b
                        ds_pua_c2_b+=j.c2_b
                        ds_pua_c3_b+=j.c3_b
                        ds_pua_c4_b+=j.c4_b
                        ds_pua_c5_b+=j.c5_b
                        ds_pua_c6_b+=j.c6_b
                        ds_pua_c7_b+=j.c7_b
                        ds_pua_c8_b+=j.c8_b
                        ds_pua_c9_b+=j.c9_b
                        ds_pua_c10_b+=j.c10_b
                        ds_pua_c11_b+=j.c11_b
                        ds_pua_c12_b+=j.c12_b
                        ds_pua_c_total_b+=j.c_total_b

                        ds_pua_c1_g+=j.c1_g
                        ds_pua_c2_g+=j.c2_g
                        ds_pua_c3_g+=j.c3_g
                        ds_pua_c4_g+=j.c4_g
                        ds_pua_c5_g+=j.c5_g
                        ds_pua_c6_g+=j.c6_g
                        ds_pua_c7_g+=j.c7_g
                        ds_pua_c8_g+=j.c8_g
                        ds_pua_c9_g+=j.c9_g
                        ds_pua_c10_g+=j.c10_g
                        ds_pua_c11_g+=j.c11_g
                        ds_pua_c12_g+=j.c12_g
                        ds_pua_c_total_g+=j.c_total_g

                        ds_pua_c1_t+=j.c1_t
                        ds_pua_c2_t+=j.c2_t
                        ds_pua_c3_t+=j.c3_t
                        ds_pua_c4_t+=j.c4_t
                        ds_pua_c5_t+=j.c5_t
                        ds_pua_c6_t+=j.c6_t
                        ds_pua_c7_t+=j.c7_t
                        ds_pua_c8_t+=j.c8_t
                        ds_pua_c9_t+=j.c9_t
                        ds_pua_c10_t+=j.c10_t
                        ds_pua_c11_t+=j.c11_t
                        ds_pua_c12_t+=j.c12_t
                        ds_pua_c_total_t+=j.c_total_t

                if int(dse_govt[i][0][0])==4:
                    m_c1=m_c2=m_c3=m_c4=m_c5=m_c6=m_c7=m_c8=m_c9=m_c10=m_c11=m_c12=m_c_total=0 
                    m_c1_b=m_c2_b=m_c3_b=m_c4_b=m_c5_b=m_c6_b=m_c7_b=m_c8_b=m_c9_b=m_c10_b=m_c11_b=m_c12_b=m_c_total_b=0 
                    m_c1_g=m_c2_g=m_c3_g=m_c4_g=m_c5_g=m_c6_g=m_c7_g=m_c8_g=m_c9_g=m_c10_g=m_c11_g=m_c12_g=m_c_total_g=0 
                    m_c1_t=m_c2_t=m_c3_t=m_c4_t=m_c5_t=m_c6_t=m_c7_t=m_c8_t=m_c9_t=m_c10_t=m_c11_t=m_c12_t=m_c_total_t=0
                    for j in dse:
                        m_c1 +=j.c1
                        m_c2 +=j.c2
                        m_c3 +=j.c3
                        m_c4 +=j.c4
                        m_c5 +=j.c5
                        m_c6 +=j.c6
                        m_c7 +=j.c7
                        m_c8 +=j.c8
                        m_c9 +=j.c9
                        m_c10 +=j.c10
                        m_c11 +=j.c11
                        m_c12 +=j.c12
                        m_c_total+=j.c_total

                        m_c1_b+=j.c1_b
                        m_c2_b+=j.c2_b
                        m_c3_b+=j.c3_b
                        m_c4_b+=j.c4_b
                        m_c5_b+=j.c5_b
                        m_c6_b+=j.c6_b
                        m_c7_b+=j.c7_b
                        m_c8_b+=j.c8_b
                        m_c9_b+=j.c9_b
                        m_c10_b+=j.c10_b
                        m_c11_b+=j.c11_b
                        m_c12_b+=j.c12_b
                        m_c_total_b+=j.c_total_b

                        m_c1_g+=j.c1_g
                        m_c2_g+=j.c2_g
                        m_c3_g+=j.c3_g
                        m_c4_g+=j.c4_g
                        m_c5_g+=j.c5_g
                        m_c6_g+=j.c6_g
                        m_c7_g+=j.c7_g
                        m_c8_g+=j.c8_g
                        m_c9_g+=j.c9_g
                        m_c10_g+=j.c10_g
                        m_c11_g+=j.c11_g
                        m_c12_g+=j.c12_g
                        m_c_total_g+=j.c_total_g

                        m_c1_t+=j.c1_t
                        m_c2_t+=j.c2_t
                        m_c3_t+=j.c3_t
                        m_c4_t+=j.c4_t
                        m_c5_t+=j.c5_t
                        m_c6_t+=j.c6_t
                        m_c7_t+=j.c7_t
                        m_c8_t+=j.c8_t
                        m_c9_t+=j.c9_t
                        m_c10_t+=j.c10_t
                        m_c11_t+=j.c11_t
                        m_c12_t+=j.c12_t
                        m_c_total_t+=j.c_total_t

                if int(dse_govt[i][0][0])==5:
                    cbse_c1=cbse_c2=cbse_c3=cbse_c4=cbse_c5=cbse_c6=cbse_c7=cbse_c8=cbse_c9=cbse_c10=cbse_c11=cbse_c12=cbse_c_total=0 
                    cbse_c1_b=cbse_c2_b=cbse_c3_b=cbse_c4_b=cbse_c5_b=cbse_c6_b=cbse_c7_b=cbse_c8_b=cbse_c9_b=cbse_c10_b=cbse_c11_b=cbse_c12_b=cbse_c_total_b=0 
                    cbse_c1_g=cbse_c2_g=cbse_c3_g=cbse_c4_g=cbse_c5_g=cbse_c6_g=cbse_c7_g=cbse_c8_g=cbse_c9_g=cbse_c10_g=cbse_c11_g=cbse_c12_g=cbse_c_total_g=0 
                    cbse_c1_t=cbse_c2_t=cbse_c3_t=cbse_c4_t=cbse_c5_t=cbse_c6_t=cbse_c7_t=cbse_c8_t=cbse_c9_t=cbse_c10_t=cbse_c11_t=cbse_c12_t=cbse_c_total_t=0
                    for j in dse:
                        cbse_c1 +=j.c1
                        cbse_c2 +=j.c2
                        cbse_c3 +=j.c3
                        cbse_c4 +=j.c4
                        cbse_c5 +=j.c5
                        cbse_c6 +=j.c6
                        cbse_c7 +=j.c7
                        cbse_c8 +=j.c8
                        cbse_c9 +=j.c9
                        cbse_c10 +=j.c10
                        cbse_c11 +=j.c11
                        cbse_c12 +=j.c12
                        cbse_c_total+=j.c_total

                        cbse_c1_b+=j.c1_b
                        cbse_c2_b+=j.c2_b
                        cbse_c3_b+=j.c3_b
                        cbse_c4_b+=j.c4_b
                        cbse_c5_b+=j.c5_b
                        cbse_c6_b+=j.c6_b
                        cbse_c7_b+=j.c7_b
                        cbse_c8_b+=j.c8_b
                        cbse_c9_b+=j.c9_b
                        cbse_c10_b+=j.c10_b
                        cbse_c11_b+=j.c11_b
                        cbse_c12_b+=j.c12_b
                        cbse_c_total_b+=j.c_total_b

                        cbse_c1_g+=j.c1_g
                        cbse_c2_g+=j.c2_g
                        cbse_c3_g+=j.c3_g
                        cbse_c4_g+=j.c4_g
                        cbse_c5_g+=j.c5_g
                        cbse_c6_g+=j.c6_g
                        cbse_c7_g+=j.c7_g
                        cbse_c8_g+=j.c8_g
                        cbse_c9_g+=j.c9_g
                        cbse_c10_g+=j.c10_g
                        cbse_c11_g+=j.c11_g
                        cbse_c12_g+=j.c12_g
                        cbse_c_total_g+=j.c_total_g

                        cbse_c1_t+=j.c1_t
                        cbse_c2_t+=j.c2_t
                        cbse_c3_t+=j.c3_t
                        cbse_c4_t+=j.c4_t
                        cbse_c5_t+=j.c5_t
                        cbse_c6_t+=j.c6_t
                        cbse_c7_t+=j.c7_t
                        cbse_c8_t+=j.c8_t
                        cbse_c9_t+=j.c9_t
                        cbse_c10_t+=j.c10_t
                        cbse_c11_t+=j.c11_t
                        cbse_c12_t+=j.c12_t
                        cbse_c_total_t+=j.c_total_t
                if int(dse_govt[i][0][0])==6:
                    dee_g_c1=dee_g_c2=dee_g_c3=dee_g_c4=dee_g_c5=dee_g_c6=dee_g_c7=dee_g_c8=dee_g_c9=dee_g_c10=dee_g_c11=dee_g_c12=dee_g_c_total=0 
                    dee_g_c1_b=dee_g_c2_b=dee_g_c3_b=dee_g_c4_b=dee_g_c5_b=dee_g_c6_b=dee_g_c7_b=dee_g_c8_b=dee_g_c9_b=dee_g_c10_b=dee_g_c11_b=dee_g_c12_b=dee_g_c_total_b=0 
                    dee_g_c1_g=dee_g_c2_g=dee_g_c3_g=dee_g_c4_g=dee_g_c5_g=dee_g_c6_g=dee_g_c7_g=dee_g_c8_g=dee_g_c9_g=dee_g_c10_g=dee_g_c11_g=dee_g_c12_g=dee_g_c_total_g=0 
                    dee_g_c1_t=dee_g_c2_t=dee_g_c3_t=dee_g_c4_t=dee_g_c5_t=dee_g_c6_t=dee_g_c7_t=dee_g_c8_t=dee_g_c9_t=dee_g_c10_t=dee_g_c11_t=dee_g_c12_t=dee_g_c_total_t=0
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

                        dee_g_c1_b+=j.c1_b
                        dee_g_c2_b+=j.c2_b
                        dee_g_c3_b+=j.c3_b
                        dee_g_c4_b+=j.c4_b
                        dee_g_c5_b+=j.c5_b
                        dee_g_c6_b+=j.c6_b
                        dee_g_c7_b+=j.c7_b
                        dee_g_c8_b+=j.c8_b
                        dee_g_c9_b+=j.c9_b
                        dee_g_c10_b+=j.c10_b
                        dee_g_c11_b+=j.c11_b
                        dee_g_c12_b+=j.c12_b
                        dee_g_c_total_b+=j.c_total_b

                        dee_g_c1_g+=j.c1_g
                        dee_g_c2_g+=j.c2_g
                        dee_g_c3_g+=j.c3_g
                        dee_g_c4_g+=j.c4_g
                        dee_g_c5_g+=j.c5_g
                        dee_g_c6_g+=j.c6_g
                        dee_g_c7_g+=j.c7_g
                        dee_g_c8_g+=j.c8_g
                        dee_g_c9_g+=j.c9_g
                        dee_g_c10_g+=j.c10_g
                        dee_g_c11_g+=j.c11_g
                        dee_g_c12_g+=j.c12_g
                        dee_g_c_total_g+=j.c_total_g

                        dee_g_c1_t+=j.c1_t
                        dee_g_c2_t+=j.c2_t
                        dee_g_c3_t+=j.c3_t
                        dee_g_c4_t+=j.c4_t
                        dee_g_c5_t+=j.c5_t
                        dee_g_c6_t+=j.c6_t
                        dee_g_c7_t+=j.c7_t
                        dee_g_c8_t+=j.c8_t
                        dee_g_c9_t+=j.c9_t
                        dee_g_c10_t+=j.c10_t
                        dee_g_c11_t+=j.c11_t
                        dee_g_c12_t+=j.c12_t
                        dee_g_c_total_t+=j.c_total_t

                if int(dse_govt[i][0][0])==7:
                    dee_pa_c1=dee_pa_c2=dee_pa_c3=dee_pa_c4=dee_pa_c5=dee_pa_c6=dee_pa_c7=dee_pa_c8=dee_pa_c9=dee_pa_c10=dee_pa_c11=dee_pa_c12=dee_pa_c_total=0 
                    dee_pa_c1_b=dee_pa_c2_b=dee_pa_c3_b=dee_pa_c4_b=dee_pa_c5_b=dee_pa_c6_b=dee_pa_c7_b=dee_pa_c8_b=dee_pa_c9_b=dee_pa_c10_b=dee_pa_c11_b=dee_pa_c12_b=dee_pa_c_total_b=0 
                    dee_pa_c1_g=dee_pa_c2_g=dee_pa_c3_g=dee_pa_c4_g=dee_pa_c5_g=dee_pa_c6_g=dee_pa_c7_g=dee_pa_c8_g=dee_pa_c9_g=dee_pa_c10_g=dee_pa_c11_g=dee_pa_c12_g=dee_pa_c_total_g=0 
                    dee_pa_c1_t=dee_pa_c2_t=dee_pa_c3_t=dee_pa_c4_t=dee_pa_c5_t=dee_pa_c6_t=dee_pa_c7_t=dee_pa_c8_t=dee_pa_c9_t=dee_pa_c10_t=dee_pa_c11_t=dee_pa_c12_t=dee_pa_c_total_t=0
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

                        dee_pa_c1_b+=j.c1_b
                        dee_pa_c2_b+=j.c2_b
                        dee_pa_c3_b+=j.c3_b
                        dee_pa_c4_b+=j.c4_b
                        dee_pa_c5_b+=j.c5_b
                        dee_pa_c6_b+=j.c6_b
                        dee_pa_c7_b+=j.c7_b
                        dee_pa_c8_b+=j.c8_b
                        dee_pa_c9_b+=j.c9_b
                        dee_pa_c10_b+=j.c10_b
                        dee_pa_c11_b+=j.c11_b
                        dee_pa_c12_b+=j.c12_b
                        dee_pa_c_total_b+=j.c_total_b

                        dee_pa_c1_g+=j.c1_g
                        dee_pa_c2_g+=j.c2_g
                        dee_pa_c3_g+=j.c3_g
                        dee_pa_c4_g+=j.c4_g
                        dee_pa_c5_g+=j.c5_g
                        dee_pa_c6_g+=j.c6_g
                        dee_pa_c7_g+=j.c7_g
                        dee_pa_c8_g+=j.c8_g
                        dee_pa_c9_g+=j.c9_g
                        dee_pa_c10_g+=j.c10_g
                        dee_pa_c11_g+=j.c11_g
                        dee_pa_c12_g+=j.c12_g
                        dee_pa_c_total_g+=j.c_total_g

                        dee_pa_c1_t+=j.c1_t
                        dee_pa_c2_t+=j.c2_t
                        dee_pa_c3_t+=j.c3_t
                        dee_pa_c4_t+=j.c4_t
                        dee_pa_c5_t+=j.c5_t
                        dee_pa_c6_t+=j.c6_t
                        dee_pa_c7_t+=j.c7_t
                        dee_pa_c8_t+=j.c8_t
                        dee_pa_c9_t+=j.c9_t
                        dee_pa_c10_t+=j.c10_t
                        dee_pa_c11_t+=j.c11_t
                        dee_pa_c12_t+=j.c12_t
                        dee_pa_c_total_t+=j.c_total_t
                if int(dse_govt[i][0][0])==8:
                    dee_pua_c1=dee_pua_c2=dee_pua_c3=dee_pua_c4=dee_pua_c5=dee_pua_c6=dee_pua_c7=dee_pua_c8=dee_pua_c9=dee_pua_c10=dee_pua_c11=dee_pua_c12=dee_pua_c_total=0 
                    dee_pua_c1_b=dee_pua_c2_b=dee_pua_c3_b=dee_pua_c4_b=dee_pua_c5_b=dee_pua_c6_b=dee_pua_c7_b=dee_pua_c8_b=dee_pua_c9_b=dee_pua_c10_b=dee_pua_c11_b=dee_pua_c12_b=dee_pua_c_total_b=0 
                    dee_pua_c1_g=dee_pua_c2_g=dee_pua_c3_g=dee_pua_c4_g=dee_pua_c5_g=dee_pua_c6_g=dee_pua_c7_g=dee_pua_c8_g=dee_pua_c9_g=dee_pua_c10_g=dee_pua_c11_g=dee_pua_c12_g=dee_pua_c_total_g=0 
                    dee_pua_c1_t=dee_pua_c2_t=dee_pua_c3_t=dee_pua_c4_t=dee_pua_c5_t=dee_pua_c6_t=dee_pua_c7_t=dee_pua_c8_t=dee_pua_c9_t=dee_pua_c10_t=dee_pua_c11_t=dee_pua_c12_t=dee_pua_c_total_t=0
                    for j in dse:
                        dee_pua_c1 +=j.c1
                        dee_pua_c2 +=j.c2
                        dee_pua_c3 +=j.c3
                        dee_pua_c4 +=j.c4
                        dee_pua_c5 +=j.c5
                        dee_pua_c6 +=j.c6
                        dee_pua_c7 +=j.c7
                        dee_pua_c8 +=j.c8
                        dee_pua_c9 +=j.c9
                        dee_pua_c10 +=j.c10
                        dee_pua_c11 +=j.c11
                        dee_pua_c12 +=j.c12
                        dee_pua_c_total+=j.c_total

                        dee_pua_c1_b+=j.c1_b
                        dee_pua_c2_b+=j.c2_b
                        dee_pua_c3_b+=j.c3_b
                        dee_pua_c4_b+=j.c4_b
                        dee_pua_c5_b+=j.c5_b
                        dee_pua_c6_b+=j.c6_b
                        dee_pua_c7_b+=j.c7_b
                        dee_pua_c8_b+=j.c8_b
                        dee_pua_c9_b+=j.c9_b
                        dee_pua_c10_b+=j.c10_b
                        dee_pua_c11_b+=j.c11_b
                        dee_pua_c12_b+=j.c12_b
                        dee_pua_c_total_b+=j.c_total_b

                        dee_pua_c1_g+=j.c1_g
                        dee_pua_c2_g+=j.c2_g
                        dee_pua_c3_g+=j.c3_g
                        dee_pua_c4_g+=j.c4_g
                        dee_pua_c5_g+=j.c5_g
                        dee_pua_c6_g+=j.c6_g
                        dee_pua_c7_g+=j.c7_g
                        dee_pua_c8_g+=j.c8_g
                        dee_pua_c9_g+=j.c9_g
                        dee_pua_c10_g+=j.c10_g
                        dee_pua_c11_g+=j.c11_g
                        dee_pua_c12_g+=j.c12_g
                        dee_pua_c_total_g+=j.c_total_g

                        dee_pua_c1_t+=j.c1_t
                        dee_pua_c2_t+=j.c2_t
                        dee_pua_c3_t+=j.c3_t
                        dee_pua_c4_t+=j.c4_t
                        dee_pua_c5_t+=j.c5_t
                        dee_pua_c6_t+=j.c6_t
                        dee_pua_c7_t+=j.c7_t
                        dee_pua_c8_t+=j.c8_t
                        dee_pua_c9_t+=j.c9_t
                        dee_pua_c10_t+=j.c10_t
                        dee_pua_c11_t+=j.c11_t
                        dee_pua_c12_t+=j.c12_t
                        dee_pua_c_total_t+=j.c_total_t
        return render(request,'gender_wise/s_l_gender_wise_report.html',locals())


    def post(self,request,**kwargs):      
        di_id1 = request.POST.get('distt', False)

        split1=di_id1.split(',')
        di_id=split1[0]
        excel=split1[1]
        
        global dse_govt        
        global all_schools
        global gender_wise
        global mgmt_name
        dist_list=District.objects.all().order_by('district_name')

        blka=dist_list.count()    
           
        district_ids=[]
        district_names=[]        
        dt_c1,dt_c2,dt_c3,dt_c4,dt_c5,dt_c6,dt_c7,dt_c8,dt_c9,dt_c10,dt_c11,dt_c12,dt_c_total=([] for qq in range(13))         
        dt_c1_b,dt_c2_b,dt_c3_b,dt_c4_b,dt_c5_b,dt_c6_b,dt_c7_b,dt_c8_b,dt_c9_b,dt_c10_b,dt_c11_b,dt_c12_b,dt_c_total_b=([] for qq1 in range(13))
        dt_c1_g,dt_c2_g,dt_c3_g,dt_c4_g,dt_c5_g,dt_c6_g,dt_c7_g,dt_c8_g,dt_c9_g,dt_c10_g,dt_c11_g,dt_c12_g,dt_c_total_g=([] for qq2 in range(13))
        dt_c1_t,dt_c2_t,dt_c3_t,dt_c4_t,dt_c5_t,dt_c6_t,dt_c7_t,dt_c8_t,dt_c9_t,dt_c10_t,dt_c11_t,dt_c12_t,dt_c_total_t=([] for qq3 in range(13))

        for ii in range(0,len(dse_govt)):
            if str(dse_govt[ii][0][0])==str(di_id):
                mgmt=dse_govt[ii][1]
                aa=dse_govt[ii][0]                
                bb=sum(aa)
                cc=int(bb)-1
                dd=mgmt_name[cc]
              
                for jj in dist_list:                 
                    district_ids.append(jj.id)              
                    
                    district_names.append(jj.district_name)  
                    disttt=all_schools.filter(district_id=jj.id,management_id__in=dse_govt[ii][1],category_id__in=dse_govt[ii][2])

                    dist_schl_list=gender_wise.filter(school_id__in=disttt)  
                    a=dist_schl_list.aggregate(Sum('c1'))
                    b=dist_schl_list.aggregate(Sum('c2'))
                    c=dist_schl_list.aggregate(Sum('c3'))
                    d=dist_schl_list.aggregate(Sum('c4'))
                    e=dist_schl_list.aggregate(Sum('c5'))
                    f=dist_schl_list.aggregate(Sum('c6'))
                    g=dist_schl_list.aggregate(Sum('c7'))
                    h=dist_schl_list.aggregate(Sum('c8'))
                    i=dist_schl_list.aggregate(Sum('c9'))
                    j=dist_schl_list.aggregate(Sum('c10'))
                    k=dist_schl_list.aggregate(Sum('c11'))
                    l=dist_schl_list.aggregate(Sum('c12'))
                    m=dist_schl_list.aggregate(Sum('c_total'))
                    n=dist_schl_list.aggregate(Sum('c1_b'))
                    o=dist_schl_list.aggregate(Sum('c2_b'))
                    p=dist_schl_list.aggregate(Sum('c3_b'))
                    q=dist_schl_list.aggregate(Sum('c4_b'))
                    r=dist_schl_list.aggregate(Sum('c5_b'))
                    s=dist_schl_list.aggregate(Sum('c6_b'))
                    t=dist_schl_list.aggregate(Sum('c7_b'))
                    u=dist_schl_list.aggregate(Sum('c8_b'))
                    v=dist_schl_list.aggregate(Sum('c9_b'))
                    w=dist_schl_list.aggregate(Sum('c10_b')) 
                    x=dist_schl_list.aggregate(Sum('c11_b'))
                    y=dist_schl_list.aggregate(Sum('c12_b'))
                    z=dist_schl_list.aggregate(Sum('c_total_b'))
                    a1=dist_schl_list.aggregate(Sum('c1_g'))
                    b1=dist_schl_list.aggregate(Sum('c2_g'))
                    c1=dist_schl_list.aggregate(Sum('c3_g'))
                    d1=dist_schl_list.aggregate(Sum('c4_g'))
                    e1=dist_schl_list.aggregate(Sum('c5_g'))
                    f1=dist_schl_list.aggregate(Sum('c6_g'))
                    g1=dist_schl_list.aggregate(Sum('c7_g'))
                    h1=dist_schl_list.aggregate(Sum('c8_g'))
                    i1=dist_schl_list.aggregate(Sum('c9_g'))
                    j1=dist_schl_list.aggregate(Sum('c10_g'))
                    k1=dist_schl_list.aggregate(Sum('c11_g'))
                    l1=dist_schl_list.aggregate(Sum('c12_g'))
                    m1=dist_schl_list.aggregate(Sum('c_total_g'))
                    n1=dist_schl_list.aggregate(Sum('c1_t'))
                    o1=dist_schl_list.aggregate(Sum('c2_t'))
                    p1=dist_schl_list.aggregate(Sum('c3_t'))
                    q1=dist_schl_list.aggregate(Sum('c4_t'))
                    r1=dist_schl_list.aggregate(Sum('c5_t'))
                    s1=dist_schl_list.aggregate(Sum('c6_t'))
                    t1=dist_schl_list.aggregate(Sum('c7_t'))
                    u1=dist_schl_list.aggregate(Sum('c8_t'))
                    v1=dist_schl_list.aggregate(Sum('c9_t'))
                    w1=dist_schl_list.aggregate(Sum('c10_t'))
                    x1=dist_schl_list.aggregate(Sum('c11_t'))
                    y1=dist_schl_list.aggregate(Sum('c12_t'))
                    z1=dist_schl_list.aggregate(Sum('c_total_t'))

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

                    dt_c1_b+=n.values()
                    dt_c2_b+=o.values()
                    dt_c3_b+=p.values()
                    dt_c4_b+=q.values()
                    dt_c5_b+=r.values()
                    dt_c6_b+=s.values()
                    dt_c7_b+=t.values()
                    dt_c8_b+=u.values()
                    dt_c9_b+=v.values()
                    dt_c10_b+=w.values()
                    dt_c11_b+=x.values()
                    dt_c12_b+=y.values()
                    dt_c_total_b+=z.values()

                    dt_c1_g+=a1.values()
                    dt_c2_g+=b1.values()
                    dt_c3_g+=c1.values()
                    dt_c4_g+=d1.values()
                    dt_c5_g+=e1.values()
                    dt_c6_g+=f1.values()
                    dt_c7_g+=g1.values()
                    dt_c8_g+=h1.values()
                    dt_c9_g+=i1.values()
                    dt_c10_g+=j1.values()
                    dt_c11_g+=k1.values()
                    dt_c12_g+=l1.values()
                    dt_c_total_g+=m1.values() 

                    dt_c1_t+=n1.values()
                    dt_c2_t+=o1.values()
                    dt_c3_t+=p1.values()
                    dt_c4_t+=q1.values()
                    dt_c5_t+=r1.values()
                    dt_c6_t+=s1.values()
                    dt_c7_t+=t1.values()
                    dt_c8_t+=u1.values()
                    dt_c9_t+=v1.values()
                    dt_c10_t+=w1.values()
                    dt_c11_t+=x1.values()
                    dt_c12_t+=y1.values()
                    dt_c_total_t+=z1.values()                                               
        a_list=zip(district_ids,district_names,dt_c1_b,dt_c1_g,dt_c1_t,dt_c1,dt_c2_b,dt_c2_g,dt_c2_t,dt_c2,dt_c3_b,dt_c3_g,dt_c3_t,dt_c3,dt_c4_b,dt_c4_g,dt_c4_t,dt_c4,dt_c5_b,dt_c5_g,dt_c5_t,dt_c5,dt_c6_b,dt_c6_g,dt_c6_t,dt_c6,dt_c7_b,dt_c7_g,dt_c7_t,dt_c7,dt_c8_b,dt_c8_g,dt_c8_t,dt_c8,dt_c9_b,dt_c9_g,dt_c9_t,dt_c9,dt_c10_b,dt_c10_g,dt_c10_t,dt_c10,dt_c11_b,dt_c11_g,dt_c11_t,dt_c11,dt_c12_b,dt_c12_g,dt_c12_t,dt_c12,dt_c_total_b,dt_c_total_g,dt_c_total_t,dt_c_total)
        if int(excel) == 2 :

            df=pd.DataFrame(a_list,columns=["ID","District","I-BOYS","I-GIRLS","I-TRANS","I-TOTAL","II-BOYS","II-GIRLS","II-TRANS","II-TOTAL","III-BOYS","III-GIRLS","III-TRANS","III-TOTAL","IV-BOYS","IV-GIRLS","IV-TRANS","IV-TOTAL","V-BOYS","V-GIRLS","V-TRANS","V-TOTAL","VI-BOYS","VI-GIRLS","VI-TRANS","VI-TOTAL","VII-BOYS","VII-GIRLS","VII-TRANS","VII-TOTAL","VIII-BOYS","VIII-GIRLS","VIII-TRANS","VIII-TOTAL","IX-BOYS","IX-GIRLS","IX-TRANS","IX-TOTAL","X-BOYS","X-GIRLS","X-TRANS","X-TOTAL","XI-BOYS","XI-GIRLS","XI-TRANS","XI-TOTAL","XII-BOYS","XII-GIRLS","XII-TRANS","XII-TOTAL","BOYS TOTAL","GIRLS TOTAL","TRANSGENDER TOTAL","OVERALL TOTAL"])
            df.index=range(1,blka+1)
            df.set_index('ID')
            outputss = StringIO.StringIO()
            writer = pd.ExcelWriter(outputss,engine='xlsxwriter')
            df.to_excel(writer, startcol = 0, startrow = 3,sheet_name="district")
            worksheet=writer.sheets['district']
            worksheet.write_string(0, 5, dd+' '+'Districtwise Abstract')
            writer.save()
            writer.close()
            outputss.seek(0)
            response = HttpResponse(outputss.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=outputss.xlsx'
            return response
        else :        
            return render(request,'gender_wise/district_overall.html',locals())


class block_overall_genderwise_report(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated():
            user_access_level=[4,3]
            user=self.kwargs['pk']
            mgmt=self.kwargs['pk1']
            excel=self.kwargs['pk2']
            district=District.objects.get(id=user)    
            blocks=Block.objects.filter(district_id=user).order_by('block_name')           
            global dse_govt        
            global all_schools
            global gender_wise
            global mgmt_name
            blka=blocks.count()
            block_ids=[]
            block_names=[]
            blk_c1,blk_c2,blk_c3,blk_c4,blk_c5,blk_c6,blk_c7,blk_c8,blk_c9,blk_c10,blk_c11,blk_c12,blk_c_total=([] for zz1 in range(13))
            blk_c1_b,blk_c2_b,blk_c3_b,blk_c4_b,blk_c5_b,blk_c6_b,blk_c7_b,blk_c8_b,blk_c9_b,blk_c10_b,blk_c11_b,blk_c12_b,blk_c_total_b=([] for zz2 in range(13))
            blk_c1_g,blk_c2_g,blk_c3_g,blk_c4_g,blk_c5_g,blk_c6_g,blk_c7_g,blk_c8_g,blk_c9_g,blk_c10_g,blk_c11_g,blk_c12_g,blk_c_total_g=([] for zz3 in range(13))
            blk_c1_t,blk_c2_t,blk_c3_t,blk_c4_t,blk_c5_t,blk_c6_t,blk_c7_t,blk_c8_t,blk_c9_t,blk_c10_t,blk_c11_t,blk_c12_t,blk_c_total_t=([] for zz4 in range(13))
            for ii in range(0,len(dse_govt)):
                if str(dse_govt[ii][0][0])==str(mgmt):
                    aa=dse_govt[ii][0]
                    bb=sum(aa)
                    cc=int(bb)-1
                    dd=mgmt_name[cc]
                    for jj in blocks:
                        block_ids.append(str(jj.id))
                        block_names.append(jj.block_name)
                        school_list=all_schools.filter(block_id=jj.id,management_id__in=dse_govt[ii][1],category_id__in=dse_govt[ii][2])
                        g_blk=gender_wise.filter(school_id__in=school_list)

                        a=g_blk.aggregate(Sum('c1'))                    
                        b=g_blk.aggregate(Sum('c2'))
                        c=g_blk.aggregate(Sum('c3'))
                        d=g_blk.aggregate(Sum('c4'))
                        e=g_blk.aggregate(Sum('c5'))
                        f=g_blk.aggregate(Sum('c6'))
                        g=g_blk.aggregate(Sum('c7'))
                        h=g_blk.aggregate(Sum('c8'))
                        i=g_blk.aggregate(Sum('c9'))
                        j=g_blk.aggregate(Sum('c10'))
                        k=g_blk.aggregate(Sum('c11'))
                        l=g_blk.aggregate(Sum('c12'))
                        m=g_blk.aggregate(Sum('c_total'))
                        n=g_blk.aggregate(Sum('c1_b'))
                        o=g_blk.aggregate(Sum('c2_b'))
                        p=g_blk.aggregate(Sum('c3_b'))
                        q=g_blk.aggregate(Sum('c4_b'))
                        r=g_blk.aggregate(Sum('c5_b'))
                        s=g_blk.aggregate(Sum('c6_b'))
                        t=g_blk.aggregate(Sum('c7_b'))
                        u=g_blk.aggregate(Sum('c8_b'))
                        v=g_blk.aggregate(Sum('c9_b'))
                        w=g_blk.aggregate(Sum('c10_b')) 
                        x=g_blk.aggregate(Sum('c11_b'))
                        y=g_blk.aggregate(Sum('c12_b'))
                        z=g_blk.aggregate(Sum('c_total_b'))
                        a1=g_blk.aggregate(Sum('c1_g'))
                        b1=g_blk.aggregate(Sum('c2_g'))
                        c1=g_blk.aggregate(Sum('c3_g'))
                        d1=g_blk.aggregate(Sum('c4_g'))
                        e1=g_blk.aggregate(Sum('c5_g'))
                        f1=g_blk.aggregate(Sum('c6_g'))
                        g1=g_blk.aggregate(Sum('c7_g'))
                        h1=g_blk.aggregate(Sum('c8_g'))
                        i1=g_blk.aggregate(Sum('c9_g'))
                        j1=g_blk.aggregate(Sum('c10_g'))
                        k1=g_blk.aggregate(Sum('c11_g'))
                        l1=g_blk.aggregate(Sum('c12_g'))
                        m1=g_blk.aggregate(Sum('c_total_g'))
                        n1=g_blk.aggregate(Sum('c1_t'))
                        o1=g_blk.aggregate(Sum('c2_t'))
                        p1=g_blk.aggregate(Sum('c3_t'))
                        q1=g_blk.aggregate(Sum('c4_t'))
                        r1=g_blk.aggregate(Sum('c5_t'))
                        s1=g_blk.aggregate(Sum('c6_t'))
                        t1=g_blk.aggregate(Sum('c7_t'))
                        u1=g_blk.aggregate(Sum('c8_t'))
                        v1=g_blk.aggregate(Sum('c9_t'))
                        w1=g_blk.aggregate(Sum('c10_t'))
                        x1=g_blk.aggregate(Sum('c11_t'))
                        y1=g_blk.aggregate(Sum('c12_t'))
                        z1=g_blk.aggregate(Sum('c_total_t'))

                        blk_c1 += a.values()                        
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

                        blk_c1_b+=n.values()
                        blk_c2_b+=o.values()
                        blk_c3_b+=p.values()
                        blk_c4_b+=q.values()
                        blk_c5_b+=r.values()
                        blk_c6_b+=s.values()
                        blk_c7_b+=t.values()
                        blk_c8_b+=u.values()
                        blk_c9_b+=v.values()
                        blk_c10_b+=w.values()
                        blk_c11_b+=x.values()
                        blk_c12_b+=y.values()
                        blk_c_total_b+=z.values()

                        blk_c1_g+=a1.values()
                        blk_c2_g+=b1.values()
                        blk_c3_g+=c1.values()
                        blk_c4_g+=d1.values()
                        blk_c5_g+=e1.values()
                        blk_c6_g+=f1.values()
                        blk_c7_g+=g1.values()
                        blk_c8_g+=h1.values()
                        blk_c9_g+=i1.values()
                        blk_c10_g+=j1.values()
                        blk_c11_g+=k1.values()
                        blk_c12_g+=l1.values()
                        blk_c_total_g+=m1.values() 

                        blk_c1_t+=n1.values()
                        blk_c2_t+=o1.values()
                        blk_c3_t+=p1.values()
                        blk_c4_t+=q1.values()
                        blk_c5_t+=r1.values()
                        blk_c6_t+=s1.values()
                        blk_c7_t+=t1.values()
                        blk_c8_t+=u1.values()
                        blk_c9_t+=v1.values()
                        blk_c10_t+=w1.values()
                        blk_c11_t+=x1.values()
                        blk_c12_t+=y1.values()
                        blk_c_total_t+=z1.values()

                    a_list=zip(block_ids,block_names,blk_c1,blk_c2,blk_c3,blk_c4,blk_c5,blk_c6,blk_c7,blk_c8,blk_c9,blk_c10,blk_c11,blk_c12,blk_c_total,blk_c1_b,blk_c2_b,blk_c3_b,blk_c4_b,blk_c5_b,blk_c6_b,blk_c7_b,blk_c8_b,blk_c9_b,blk_c10_b,blk_c11_b,blk_c12_b,blk_c_total_b,blk_c1_g,blk_c2_g,blk_c3_g,blk_c4_g,blk_c5_g,blk_c6_g,blk_c7_g,blk_c8_g,blk_c9_g,blk_c10_g,blk_c11_g,blk_c12_g,blk_c_total_g,blk_c1_t,blk_c2_t,blk_c3_t,blk_c4_t,blk_c5_t,blk_c6_t,blk_c7_t,blk_c8_t,blk_c9_t,blk_c10_t,blk_c11_t,blk_c12_t,blk_c_total_t)

                    if int(excel) == 1 :
                       b_list=zip(block_ids,block_names,blk_c1,blk_c1_b,blk_c1_g,blk_c1_t,blk_c2,blk_c2_b,blk_c2_g,blk_c2_t,blk_c3,blk_c3_b,blk_c3_g,blk_c3_t,blk_c4,blk_c4_b,blk_c4_g,blk_c4_t,blk_c5,blk_c5_b,blk_c5_g,blk_c5_t,blk_c6,blk_c6_b,blk_c6_g,blk_c6_t,blk_c7,blk_c7_b,blk_c7_g,blk_c7_t,blk_c8,blk_c8_b,blk_c8_g,blk_c8_t,blk_c9,blk_c9_b,blk_c9_g,blk_c9_t,blk_c10,blk_c10_b,blk_c10_g,blk_c10_t,blk_c11,blk_c11_b,blk_c11_g,blk_c11_t,blk_c12,blk_c12_b,blk_c12_g,blk_c12_t,blk_c_total_b,blk_c_total_g,blk_c_total_t,blk_c_total)
                       df=pd.DataFrame(b_list,columns=["ID","Block","I-TOTAL","I-BOYS","I-GIRLS","I-TRANS","II-TOTAL","II-BOYS","II-GIRLS","II-TRANS","III-BOYS","III-TOTAL","III-GIRLS","III-TRANS","IV-TOTAL","IV-BOYS","IV-GIRLS","IV-TRANS","V-TOTAL","V-BOYS","V-GIRLS","V-TRANS","VI-TOTAL","VI-BOYS","VI-GIRLS","VI-TRANS","VII-TOTAL","VII-BOYS","VII-GIRLS","VII-TRANS","VIII-TOTAL","VIII-BOYS","VIII-GIRLS","VIII-TRANS","IX-TOTAL","IX-BOYS","IX-GIRLS","IX-TRANS","X-TOTAL","X-BOYS","X-GIRLS","X-TRANS","XI-TOTAL","XI-BOYS","XI-GIRLS","XI-TRANS","XII-TOTAL","XII-BOYS","XII-GIRLS","XII-TRANS","BOYS TOTAL","GIRLS TOTAL","TRANSGENDER TOTAL","OVERALL TOTAL"])
                       
                       df.index=range(1,blka+1)
                       df.set_index('ID')
                       outputss = StringIO.StringIO()
                       writer = pd.ExcelWriter(outputss,engine='xlsxwriter')
                       df.to_excel(writer, startcol = 0, startrow = 3,sheet_name="block")
                       worksheet=writer.sheets['block']
                       worksheet.write_string(0, 5, str(district)+' '+'Blockwise Abstract')
                       writer.save()
                       writer.close()
                       outputss.seek(0)
                       response = HttpResponse(outputss.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                       response['Content-Disposition'] = 'attachment; filename=outputss.xlsx'
                       return response
                       
                  
                    else:
                       return render(request,'gender_wise/block_overall_genderwise.html',locals())

    def post(self,request,**kwargs):
        global dse_govt        
        global all_schools
        global gender_wise
        global mgmt_name
        mgmt_id = request.POST.get('blks', False)
        mgmt_blk=mgmt_id.split(',')
        
        m_id=mgmt_blk[0]
        print "Management"
        print m_id
        b_id=mgmt_blk[1]
        excel=mgmt_blk[2]
        schl_ids=[]
        schl_names=[]
        blk_c1,blk_c2,blk_c3,blk_c4,blk_c5,blk_c6,blk_c7,blk_c8,blk_c9,blk_c10,blk_c11,blk_c12,blk_c_total=([] for zz1 in range(13))
        blk_c1_b,blk_c2_b,blk_c3_b,blk_c4_b,blk_c5_b,blk_c6_b,blk_c7_b,blk_c8_b,blk_c9_b,blk_c10_b,blk_c11_b,blk_c12_b,blk_c_total_b=([] for zz2 in range(13))
        blk_c1_g,blk_c2_g,blk_c3_g,blk_c4_g,blk_c5_g,blk_c6_g,blk_c7_g,blk_c8_g,blk_c9_g,blk_c10_g,blk_c11_g,blk_c12_g,blk_c_total_g=([] for zz3 in range(13))
        blk_c1_t,blk_c2_t,blk_c3_t,blk_c4_t,blk_c5_t,blk_c6_t,blk_c7_t,blk_c8_t,blk_c9_t,blk_c10_t,blk_c11_t,blk_c12_t,blk_c_total_t=([] for zz4 in range(13))
           
        for ii in range(0,len(dse_govt)):
            if str(dse_govt[ii][0][0])==str(m_id):
                aa=dse_govt[ii][0]
                bb=sum(aa)
                cc=int(bb)-1
                dd=mgmt_name[cc]
                block_name=Block.objects.get(id=mgmt_blk[1])
                school_list=all_schools.filter(block_id=mgmt_blk[1],management_id__in=dse_govt[ii][1],category_id__in=dse_govt[ii][2])
              
                sclka=school_list.count()
                
                g_blk=gender_wise.filter(school_id__in=school_list).order_by('school')
                
                
        if int(excel) == 2 :
            for kk in g_blk:
                schl_ids.append(str(kk.id))
                schl_names.append(kk.school.school_name)
                blk_c1.append(kk.c1)                        
                blk_c2.append(kk.c2)
                blk_c3.append(kk.c3)
                blk_c4.append(kk.c4)
                blk_c5.append(kk.c5)
                blk_c6.append(kk.c6)
                blk_c7.append(kk.c7)
                blk_c8.append(kk.c8) 
                blk_c9.append(kk.c9) 
                blk_c10.append(kk.c10) 
                blk_c11.append(kk.c11) 
                blk_c12.append(kk.c12)
                blk_c_total.append(kk.c_total)

                blk_c1_b.append(kk.c1_b) 
                blk_c2_b.append(kk.c2_b)
                blk_c3_b.append(kk.c3_b) 
                blk_c4_b.append(kk.c4_b) 
                blk_c5_b.append(kk.c5_b) 
                blk_c6_b.append(kk.c6_b) 
                blk_c7_b.append(kk.c7_b) 
                blk_c8_b.append(kk.c8_b) 
                blk_c9_b.append(kk.c9_b) 
                blk_c10_b.append(kk.c10_b)
                blk_c11_b.append(kk.c11_b) 
                blk_c12_b.append(kk.c12_b)
                blk_c_total_b.append(kk.c_total_b)

                blk_c1_g.append(kk.c1_g) 
                blk_c2_g.append(kk.c2_g)
                blk_c3_g.append(kk.c3_g) 
                blk_c4_g.append(kk.c4_g) 
                blk_c5_g.append(kk.c5_g) 
                blk_c6_g.append(kk.c6_g) 
                blk_c7_g.append(kk.c7_g) 
                blk_c8_g.append(kk.c8_g) 
                blk_c9_g.append(kk.c9_g) 
                blk_c10_g.append(kk.c10_g) 
                blk_c11_g.append(kk.c11_g) 
                blk_c12_g.append(kk.c12_g) 
                blk_c_total_g.append(kk.c_total_g)  

                blk_c1_t.append(kk.c1_t) 
                blk_c2_t.append(kk.c2_t) 
                blk_c3_t.append(kk.c3_t)
                blk_c4_t.append(kk.c4_t) 
                blk_c5_t.append(kk.c5_t) 
                blk_c6_t.append(kk.c6_t)
                blk_c7_t.append(kk.c7_t) 
                blk_c8_t.append(kk.c8_t)
                blk_c9_t.append(kk.c9_t) 
                blk_c10_t.append(kk.c10_t) 
                blk_c11_t.append(kk.c11_t)
                blk_c12_t.append(kk.c12_t) 
                blk_c_total_t.append(kk.c_total_t) 
        
            samp_list=zip(schl_ids,schl_names,blk_c1_b,blk_c1_g,blk_c1_t,blk_c2,blk_c2_b,blk_c2_g,blk_c2_t,blk_c2,blk_c3_b,blk_c3_g,blk_c3_t,blk_c3,blk_c4_b,blk_c4_g,blk_c4_t,blk_c4,blk_c5_b,blk_c5_g,blk_c5_t,blk_c5,blk_c6_b,blk_c6_g,blk_c6_t,blk_c6,blk_c7_b,blk_c7_g,blk_c7_t,blk_c7,blk_c8_b,blk_c8_g,blk_c8_t,blk_c8,blk_c9_b,blk_c9_g,blk_c9_t,blk_c9,blk_c10_b,blk_c10_g,blk_c10_t,blk_c10,blk_c11_b,blk_c11_g,blk_c11_t,blk_c11,blk_c12_b,blk_c12_g,blk_c12_t,blk_c12,blk_c_total_b,blk_c_total_g,blk_c_total_t,blk_c_total)
            df=pd.DataFrame(samp_list,columns=["ID","School Name","I-BOYS","I-GIRLS","I-TRANS","I-TOTAL","II-BOYS","II-GIRLS","II-TRANS","II-TOTAL","III-BOYS","III-GIRLS","III-TRANS","III-TOTAL","IV-BOYS","IV-GIRLS","IV-TRANS","IV-TOTAL","V-BOYS","V-GIRLS","V-TRANS","V-TOTAL","VI-BOYS","VI-GIRLS","VI-TRANS","VI-TOTAL","VII-BOYS","VII-GIRLS","VII-TRANS","VII-TOTAL","VIII-BOYS","VIII-GIRLS","VIII-TRANS","VIII-TOTAL","IX-BOYS","IX-GIRLS","IX-TRANS","IX-TOTAL","X-BOYS","X-GIRLS","X-TRANS","X-TOTAL","XI-BOYS","XI-GIRLS","XI-TRANS","XI-TOTAL","XII-BOYS","XII-GIRLS","XII-TRANS","XII-TOTAL","BOYS TOTAL","GIRLS TOTAL","TRANSGENDER TOTAL","OVERALL TOTAL"])
            df.index=range(1,sclka+1)
            df.set_index('ID')
            outputss = StringIO.StringIO()
            writer = pd.ExcelWriter(outputss,engine='xlsxwriter')
            df.to_excel(writer, startcol = 0, startrow = 3,sheet_name="Schools")
            worksheet=writer.sheets['Schools']
            worksheet.write_string(0, 5, dd+' '+'Schoolwise Abstract')
            writer.save()
            writer.close()
            outputss.seek(0)
            response = HttpResponse(outputss.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=Schoolwise Abstract.xlsx'
            return response
        else :        
            return render(request,'gender_wise/block_genderwise_school_report.html',locals())

class school_level_genderwise(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']
        gender=common_reports.objects.get(id=school)
        return render(request,'gender_wise/s_l_genderwise.html',locals())
   

# District Login

class district_level_genderwise_report(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated():
            global all_schools
            global gender_wise
            global dse_govt
            user=self.kwargs['pk']
            user_access_level=[4,3]
            district=District.objects.get(id=user)
            for i in range(0,len(dse_govt)):   
                d_l_school_list=all_schools.filter(district_id=user,management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])
                schl_list=gender_wise.filter(school_id__in=d_l_school_list)
                if int(dse_govt[i][0][0])==1:
                    dl_ds_g_c1=dl_ds_g_c2=dl_ds_g_c3=dl_ds_g_c4=dl_ds_g_c5=dl_ds_g_c6=dl_ds_g_c7=dl_ds_g_c8=dl_ds_g_c9=dl_ds_g_c10=dl_ds_g_c11=dl_ds_g_c12=dl_ds_g_c_total=0 
                    dl_ds_g_c1_b=dl_ds_g_c2_b=dl_ds_g_c3_b=dl_ds_g_c4_b=dl_ds_g_c5_b=dl_ds_g_c6_b=dl_ds_g_c7_b=dl_ds_g_c8_b=dl_ds_g_c9_b=dl_ds_g_c10_b=dl_ds_g_c11_b=dl_ds_g_c12_b=dl_ds_g_c_total_b=0 
                    dl_ds_g_c1_g=dl_ds_g_c2_g=dl_ds_g_c3_g=dl_ds_g_c4_g=dl_ds_g_c5_g=dl_ds_g_c6_g=dl_ds_g_c7_g=dl_ds_g_c8_g=dl_ds_g_c9_g=dl_ds_g_c10_g=dl_ds_g_c11_g=dl_ds_g_c12_g=dl_ds_g_c_total_g=0 
                    dl_ds_g_c1_t=dl_ds_g_c2_t=dl_ds_g_c3_t=dl_ds_g_c4_t=dl_ds_g_c5_t=dl_ds_g_c6_t=dl_ds_g_c7_t=dl_ds_g_c8_t=dl_ds_g_c9_t=dl_ds_g_c10_t=dl_ds_g_c11_t=dl_ds_g_c12_t=dl_ds_g_c_total_t=0
                    for j in schl_list:
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

                        dl_ds_g_c1_b+=j.c1_b
                        dl_ds_g_c2_b+=j.c2_b
                        dl_ds_g_c3_b+=j.c3_b
                        dl_ds_g_c4_b+=j.c4_b
                        dl_ds_g_c5_b+=j.c5_b
                        dl_ds_g_c6_b+=j.c6_b
                        dl_ds_g_c7_b+=j.c7_b
                        dl_ds_g_c8_b+=j.c8_b
                        dl_ds_g_c9_b+=j.c9_b
                        dl_ds_g_c10_b+=j.c10_b
                        dl_ds_g_c11_b+=j.c11_b
                        dl_ds_g_c12_b+=j.c12_b
                        dl_ds_g_c_total_b+=j.c_total_b

                        dl_ds_g_c1_g+=j.c1_g
                        dl_ds_g_c2_g+=j.c2_g
                        dl_ds_g_c3_g+=j.c3_g
                        dl_ds_g_c4_g+=j.c4_g
                        dl_ds_g_c5_g+=j.c5_g
                        dl_ds_g_c6_g+=j.c6_g
                        dl_ds_g_c7_g+=j.c7_g
                        dl_ds_g_c8_g+=j.c8_g
                        dl_ds_g_c9_g+=j.c9_g
                        dl_ds_g_c10_g+=j.c10_g
                        dl_ds_g_c11_g+=j.c11_g
                        dl_ds_g_c12_g+=j.c12_g
                        dl_ds_g_c_total_g+=j.c_total_g

                        dl_ds_g_c1_t+=j.c1_t
                        dl_ds_g_c2_t+=j.c2_t
                        dl_ds_g_c3_t+=j.c3_t
                        dl_ds_g_c4_t+=j.c4_t
                        dl_ds_g_c5_t+=j.c5_t
                        dl_ds_g_c6_t+=j.c6_t
                        dl_ds_g_c7_t+=j.c7_t
                        dl_ds_g_c8_t+=j.c8_t
                        dl_ds_g_c9_t+=j.c9_t
                        dl_ds_g_c10_t+=j.c10_t
                        dl_ds_g_c11_t+=j.c11_t
                        dl_ds_g_c12_t+=j.c12_t
                        dl_ds_g_c_total_t+=j.c_total_t
                if int(dse_govt[i][0][0])==2:
                    dl_ds_pa_c1=dl_ds_pa_c2=dl_ds_pa_c3=dl_ds_pa_c4=dl_ds_pa_c5=dl_ds_pa_c6=dl_ds_pa_c7=dl_ds_pa_c8=dl_ds_pa_c9=dl_ds_pa_c10=dl_ds_pa_c11=dl_ds_pa_c12=dl_ds_pa_c_total=0 
                    dl_ds_pa_c1_b=dl_ds_pa_c2_b=dl_ds_pa_c3_b=dl_ds_pa_c4_b=dl_ds_pa_c5_b=dl_ds_pa_c6_b=dl_ds_pa_c7_b=dl_ds_pa_c8_b=dl_ds_pa_c9_b=dl_ds_pa_c10_b=dl_ds_pa_c11_b=dl_ds_pa_c12_b=dl_ds_pa_c_total_b=0 
                    dl_ds_pa_c1_g=dl_ds_pa_c2_g=dl_ds_pa_c3_g=dl_ds_pa_c4_g=dl_ds_pa_c5_g=dl_ds_pa_c6_g=dl_ds_pa_c7_g=dl_ds_pa_c8_g=dl_ds_pa_c9_g=dl_ds_pa_c10_g=dl_ds_pa_c11_g=dl_ds_pa_c12_g=dl_ds_pa_c_total_g=0 
                    dl_ds_pa_c1_t=dl_ds_pa_c2_t=dl_ds_pa_c3_t=dl_ds_pa_c4_t=dl_ds_pa_c5_t=dl_ds_pa_c6_t=dl_ds_pa_c7_t=dl_ds_pa_c8_t=dl_ds_pa_c9_t=dl_ds_pa_c10_t=dl_ds_pa_c11_t=dl_ds_pa_c12_t=dl_ds_pa_c_total_t=0
                    for j in schl_list:
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

                        dl_ds_pa_c1_b+=j.c1_b
                        dl_ds_pa_c2_b+=j.c2_b
                        dl_ds_pa_c3_b+=j.c3_b
                        dl_ds_pa_c4_b+=j.c4_b
                        dl_ds_pa_c5_b+=j.c5_b
                        dl_ds_pa_c6_b+=j.c6_b
                        dl_ds_pa_c7_b+=j.c7_b
                        dl_ds_pa_c8_b+=j.c8_b
                        dl_ds_pa_c9_b+=j.c9_b
                        dl_ds_pa_c10_b+=j.c10_b
                        dl_ds_pa_c11_b+=j.c11_b
                        dl_ds_pa_c12_b+=j.c12_b
                        dl_ds_pa_c_total_b+=j.c_total_b

                        dl_ds_pa_c1_g+=j.c1_g
                        dl_ds_pa_c2_g+=j.c2_g
                        dl_ds_pa_c3_g+=j.c3_g
                        dl_ds_pa_c4_g+=j.c4_g
                        dl_ds_pa_c5_g+=j.c5_g
                        dl_ds_pa_c6_g+=j.c6_g
                        dl_ds_pa_c7_g+=j.c7_g
                        dl_ds_pa_c8_g+=j.c8_g
                        dl_ds_pa_c9_g+=j.c9_g
                        dl_ds_pa_c10_g+=j.c10_g
                        dl_ds_pa_c11_g+=j.c11_g
                        dl_ds_pa_c12_g+=j.c12_g
                        dl_ds_pa_c_total_g+=j.c_total_g

                        dl_ds_pa_c1_t+=j.c1_t
                        dl_ds_pa_c2_t+=j.c2_t
                        dl_ds_pa_c3_t+=j.c3_t
                        dl_ds_pa_c4_t+=j.c4_t
                        dl_ds_pa_c5_t+=j.c5_t
                        dl_ds_pa_c6_t+=j.c6_t
                        dl_ds_pa_c7_t+=j.c7_t
                        dl_ds_pa_c8_t+=j.c8_t
                        dl_ds_pa_c9_t+=j.c9_t
                        dl_ds_pa_c10_t+=j.c10_t
                        dl_ds_pa_c11_t+=j.c11_t
                        dl_ds_pa_c12_t+=j.c12_t
                        dl_ds_pa_c_total_t+=j.c_total_t
                if int(dse_govt[i][0][0])==3:
                    dl_ds_pua_c1=dl_ds_pua_c2=dl_ds_pua_c3=dl_ds_pua_c4=dl_ds_pua_c5=dl_ds_pua_c6=dl_ds_pua_c7=dl_ds_pua_c8=dl_ds_pua_c9=dl_ds_pua_c10=dl_ds_pua_c11=dl_ds_pua_c12=dl_ds_pua_c_total=0 
                    dl_ds_pua_c1_b=dl_ds_pua_c2_b=dl_ds_pua_c3_b=dl_ds_pua_c4_b=dl_ds_pua_c5_b=dl_ds_pua_c6_b=dl_ds_pua_c7_b=dl_ds_pua_c8_b=dl_ds_pua_c9_b=dl_ds_pua_c10_b=dl_ds_pua_c11_b=dl_ds_pua_c12_b=dl_ds_pua_c_total_b=0 
                    dl_ds_pua_c1_g=dl_ds_pua_c2_g=dl_ds_pua_c3_g=dl_ds_pua_c4_g=dl_ds_pua_c5_g=dl_ds_pua_c6_g=dl_ds_pua_c7_g=dl_ds_pua_c8_g=dl_ds_pua_c9_g=dl_ds_pua_c10_g=dl_ds_pua_c11_g=dl_ds_pua_c12_g=dl_ds_pua_c_total_g=0 
                    dl_ds_pua_c1_t=dl_ds_pua_c2_t=dl_ds_pua_c3_t=dl_ds_pua_c4_t=dl_ds_pua_c5_t=dl_ds_pua_c6_t=dl_ds_pua_c7_t=dl_ds_pua_c8_t=dl_ds_pua_c9_t=dl_ds_pua_c10_t=dl_ds_pua_c11_t=dl_ds_pua_c12_t=dl_ds_pua_c_total_t=0
                    for j in schl_list:
                        dl_ds_pua_c1 +=j.c1
                        dl_ds_pua_c2 +=j.c2
                        dl_ds_pua_c3 +=j.c3
                        dl_ds_pua_c4 +=j.c4
                        dl_ds_pua_c5 +=j.c5
                        dl_ds_pua_c6 +=j.c6
                        dl_ds_pua_c7 +=j.c7
                        dl_ds_pua_c8 +=j.c8
                        dl_ds_pua_c9 +=j.c9
                        dl_ds_pua_c10 +=j.c10
                        dl_ds_pua_c11 +=j.c11
                        dl_ds_pua_c12 +=j.c12
                        dl_ds_pua_c_total+=j.c_total

                        dl_ds_pua_c1_b+=j.c1_b
                        dl_ds_pua_c2_b+=j.c2_b
                        dl_ds_pua_c3_b+=j.c3_b
                        dl_ds_pua_c4_b+=j.c4_b
                        dl_ds_pua_c5_b+=j.c5_b
                        dl_ds_pua_c6_b+=j.c6_b
                        dl_ds_pua_c7_b+=j.c7_b
                        dl_ds_pua_c8_b+=j.c8_b
                        dl_ds_pua_c9_b+=j.c9_b
                        dl_ds_pua_c10_b+=j.c10_b
                        dl_ds_pua_c11_b+=j.c11_b
                        dl_ds_pua_c12_b+=j.c12_b
                        dl_ds_pua_c_total_b+=j.c_total_b

                        dl_ds_pua_c1_g+=j.c1_g
                        dl_ds_pua_c2_g+=j.c2_g
                        dl_ds_pua_c3_g+=j.c3_g
                        dl_ds_pua_c4_g+=j.c4_g
                        dl_ds_pua_c5_g+=j.c5_g
                        dl_ds_pua_c6_g+=j.c6_g
                        dl_ds_pua_c7_g+=j.c7_g
                        dl_ds_pua_c8_g+=j.c8_g
                        dl_ds_pua_c9_g+=j.c9_g
                        dl_ds_pua_c10_g+=j.c10_g
                        dl_ds_pua_c11_g+=j.c11_g
                        dl_ds_pua_c12_g+=j.c12_g
                        dl_ds_pua_c_total_g+=j.c_total_g

                        dl_ds_pua_c1_t+=j.c1_t
                        dl_ds_pua_c2_t+=j.c2_t
                        dl_ds_pua_c3_t+=j.c3_t
                        dl_ds_pua_c4_t+=j.c4_t
                        dl_ds_pua_c5_t+=j.c5_t
                        dl_ds_pua_c6_t+=j.c6_t
                        dl_ds_pua_c7_t+=j.c7_t
                        dl_ds_pua_c8_t+=j.c8_t
                        dl_ds_pua_c9_t+=j.c9_t
                        dl_ds_pua_c10_t+=j.c10_t
                        dl_ds_pua_c11_t+=j.c11_t
                        dl_ds_pua_c12_t+=j.c12_t
                        dl_ds_pua_c_total_t+=j.c_total_t

                if int(dse_govt[i][0][0])==4:
                    dl_m_c1=dl_m_c2=dl_m_c3=dl_m_c4=dl_m_c5=dl_m_c6=dl_m_c7=dl_m_c8=dl_m_c9=dl_m_c10=dl_m_c11=dl_m_c12=dl_m_c_total=0 
                    dl_m_c1_b=dl_m_c2_b=dl_m_c3_b=dl_m_c4_b=dl_m_c5_b=dl_m_c6_b=dl_m_c7_b=dl_m_c8_b=dl_m_c9_b=dl_m_c10_b=dl_m_c11_b=dl_m_c12_b=dl_m_c_total_b=0 
                    dl_m_c1_g=dl_m_c2_g=dl_m_c3_g=dl_m_c4_g=dl_m_c5_g=dl_m_c6_g=dl_m_c7_g=dl_m_c8_g=dl_m_c9_g=dl_m_c10_g=dl_m_c11_g=dl_m_c12_g=dl_m_c_total_g=0 
                    dl_m_c1_t=dl_m_c2_t=dl_m_c3_t=dl_m_c4_t=dl_m_c5_t=dl_m_c6_t=dl_m_c7_t=dl_m_c8_t=dl_m_c9_t=dl_m_c10_t=dl_m_c11_t=dl_m_c12_t=dl_m_c_total_t=0
                    for j in schl_list:
                        dl_m_c1 +=j.c1
                        dl_m_c2 +=j.c2
                        dl_m_c3 +=j.c3
                        dl_m_c4 +=j.c4
                        dl_m_c5 +=j.c5
                        dl_m_c6 +=j.c6
                        dl_m_c7 +=j.c7
                        dl_m_c8 +=j.c8
                        dl_m_c9 +=j.c9
                        dl_m_c10 +=j.c10
                        dl_m_c11 +=j.c11
                        dl_m_c12 +=j.c12
                        dl_m_c_total+=j.c_total

                        dl_m_c1_b+=j.c1_b
                        dl_m_c2_b+=j.c2_b
                        dl_m_c3_b+=j.c3_b
                        dl_m_c4_b+=j.c4_b
                        dl_m_c5_b+=j.c5_b
                        dl_m_c6_b+=j.c6_b
                        dl_m_c7_b+=j.c7_b
                        dl_m_c8_b+=j.c8_b
                        dl_m_c9_b+=j.c9_b
                        dl_m_c10_b+=j.c10_b
                        dl_m_c11_b+=j.c11_b
                        dl_m_c12_b+=j.c12_b
                        dl_m_c_total_b+=j.c_total_b

                        dl_m_c1_g+=j.c1_g
                        dl_m_c2_g+=j.c2_g
                        dl_m_c3_g+=j.c3_g
                        dl_m_c4_g+=j.c4_g
                        dl_m_c5_g+=j.c5_g
                        dl_m_c6_g+=j.c6_g
                        dl_m_c7_g+=j.c7_g
                        dl_m_c8_g+=j.c8_g
                        dl_m_c9_g+=j.c9_g
                        dl_m_c10_g+=j.c10_g
                        dl_m_c11_g+=j.c11_g
                        dl_m_c12_g+=j.c12_g
                        dl_m_c_total_g+=j.c_total_g

                        dl_m_c1_t+=j.c1_t
                        dl_m_c2_t+=j.c2_t
                        dl_m_c3_t+=j.c3_t
                        dl_m_c4_t+=j.c4_t
                        dl_m_c5_t+=j.c5_t
                        dl_m_c6_t+=j.c6_t
                        dl_m_c7_t+=j.c7_t
                        dl_m_c8_t+=j.c8_t
                        dl_m_c9_t+=j.c9_t
                        dl_m_c10_t+=j.c10_t
                        dl_m_c11_t+=j.c11_t
                        dl_m_c12_t+=j.c12_t
                        dl_m_c_total_t+=j.c_total_t

                if int(dse_govt[i][0][0])==5:
                    dl_cbse_c1=dl_cbse_c2=dl_cbse_c3=dl_cbse_c4=dl_cbse_c5=dl_cbse_c6=dl_cbse_c7=dl_cbse_c8=dl_cbse_c9=dl_cbse_c10=dl_cbse_c11=dl_cbse_c12=dl_cbse_c_total=0 
                    dl_cbse_c1_b=dl_cbse_c2_b=dl_cbse_c3_b=dl_cbse_c4_b=dl_cbse_c5_b=dl_cbse_c6_b=dl_cbse_c7_b=dl_cbse_c8_b=dl_cbse_c9_b=dl_cbse_c10_b=dl_cbse_c11_b=dl_cbse_c12_b=dl_cbse_c_total_b=0 
                    dl_cbse_c1_g=dl_cbse_c2_g=dl_cbse_c3_g=dl_cbse_c4_g=dl_cbse_c5_g=dl_cbse_c6_g=dl_cbse_c7_g=dl_cbse_c8_g=dl_cbse_c9_g=dl_cbse_c10_g=dl_cbse_c11_g=dl_cbse_c12_g=dl_cbse_c_total_g=0 
                    dl_cbse_c1_t=dl_cbse_c2_t=dl_cbse_c3_t=dl_cbse_c4_t=dl_cbse_c5_t=dl_cbse_c6_t=dl_cbse_c7_t=dl_cbse_c8_t=dl_cbse_c9_t=dl_cbse_c10_t=dl_cbse_c11_t=dl_cbse_c12_t=dl_cbse_c_total_t=0
                    for j in schl_list:
                        dl_cbse_c1 +=j.c1
                        dl_cbse_c2 +=j.c2
                        dl_cbse_c3 +=j.c3
                        dl_cbse_c4 +=j.c4
                        dl_cbse_c5 +=j.c5
                        dl_cbse_c6 +=j.c6
                        dl_cbse_c7 +=j.c7
                        dl_cbse_c8 +=j.c8
                        dl_cbse_c9 +=j.c9
                        dl_cbse_c10 +=j.c10
                        dl_cbse_c11 +=j.c11
                        dl_cbse_c12 +=j.c12
                        dl_cbse_c_total+=j.c_total

                        dl_cbse_c1_b+=j.c1_b
                        dl_cbse_c2_b+=j.c2_b
                        dl_cbse_c3_b+=j.c3_b
                        dl_cbse_c4_b+=j.c4_b
                        dl_cbse_c5_b+=j.c5_b
                        dl_cbse_c6_b+=j.c6_b
                        dl_cbse_c7_b+=j.c7_b
                        dl_cbse_c8_b+=j.c8_b
                        dl_cbse_c9_b+=j.c9_b
                        dl_cbse_c10_b+=j.c10_b
                        dl_cbse_c11_b+=j.c11_b
                        dl_cbse_c12_b+=j.c12_b
                        dl_cbse_c_total_b+=j.c_total_b

                        dl_cbse_c1_g+=j.c1_g
                        dl_cbse_c2_g+=j.c2_g
                        dl_cbse_c3_g+=j.c3_g
                        dl_cbse_c4_g+=j.c4_g
                        dl_cbse_c5_g+=j.c5_g
                        dl_cbse_c6_g+=j.c6_g
                        dl_cbse_c7_g+=j.c7_g
                        dl_cbse_c8_g+=j.c8_g
                        dl_cbse_c9_g+=j.c9_g
                        dl_cbse_c10_g+=j.c10_g
                        dl_cbse_c11_g+=j.c11_g
                        dl_cbse_c12_g+=j.c12_g
                        dl_cbse_c_total_g+=j.c_total_g

                        dl_cbse_c1_t+=j.c1_t
                        dl_cbse_c2_t+=j.c2_t
                        dl_cbse_c3_t+=j.c3_t
                        dl_cbse_c4_t+=j.c4_t
                        dl_cbse_c5_t+=j.c5_t
                        dl_cbse_c6_t+=j.c6_t
                        dl_cbse_c7_t+=j.c7_t
                        dl_cbse_c8_t+=j.c8_t
                        dl_cbse_c9_t+=j.c9_t
                        dl_cbse_c10_t+=j.c10_t
                        dl_cbse_c11_t+=j.c11_t
                        dl_cbse_c12_t+=j.c12_t
                        dl_cbse_c_total_t+=j.c_total_t
                if int(dse_govt[i][0][0])==6:
                    dl_dee_g_c1=dl_dee_g_c2=dl_dee_g_c3=dl_dee_g_c4=dl_dee_g_c5=dl_dee_g_c6=dl_dee_g_c7=dl_dee_g_c8=dl_dee_g_c9=dl_dee_g_c10=dl_dee_g_c11=dl_dee_g_c12=dl_dee_g_c_total=0 
                    dl_dee_g_c1_b=dl_dee_g_c2_b=dl_dee_g_c3_b=dl_dee_g_c4_b=dl_dee_g_c5_b=dl_dee_g_c6_b=dl_dee_g_c7_b=dl_dee_g_c8_b=dl_dee_g_c9_b=dl_dee_g_c10_b=dl_dee_g_c11_b=dl_dee_g_c12_b=dl_dee_g_c_total_b=0 
                    dl_dee_g_c1_g=dl_dee_g_c2_g=dl_dee_g_c3_g=dl_dee_g_c4_g=dl_dee_g_c5_g=dl_dee_g_c6_g=dl_dee_g_c7_g=dl_dee_g_c8_g=dl_dee_g_c9_g=dl_dee_g_c10_g=dl_dee_g_c11_g=dl_dee_g_c12_g=dl_dee_g_c_total_g=0 
                    dl_dee_g_c1_t=dl_dee_g_c2_t=dl_dee_g_c3_t=dl_dee_g_c4_t=dl_dee_g_c5_t=dl_dee_g_c6_t=dl_dee_g_c7_t=dl_dee_g_c8_t=dl_dee_g_c9_t=dl_dee_g_c10_t=dl_dee_g_c11_t=dl_dee_g_c12_t=dl_dee_g_c_total_t=0
                    for j in schl_list:
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

                        dl_dee_g_c1_b+=j.c1_b
                        dl_dee_g_c2_b+=j.c2_b
                        dl_dee_g_c3_b+=j.c3_b
                        dl_dee_g_c4_b+=j.c4_b
                        dl_dee_g_c5_b+=j.c5_b
                        dl_dee_g_c6_b+=j.c6_b
                        dl_dee_g_c7_b+=j.c7_b
                        dl_dee_g_c8_b+=j.c8_b
                        dl_dee_g_c9_b+=j.c9_b
                        dl_dee_g_c10_b+=j.c10_b
                        dl_dee_g_c11_b+=j.c11_b
                        dl_dee_g_c12_b+=j.c12_b
                        dl_dee_g_c_total_b+=j.c_total_b

                        dl_dee_g_c1_g+=j.c1_g
                        dl_dee_g_c2_g+=j.c2_g
                        dl_dee_g_c3_g+=j.c3_g
                        dl_dee_g_c4_g+=j.c4_g
                        dl_dee_g_c5_g+=j.c5_g
                        dl_dee_g_c6_g+=j.c6_g
                        dl_dee_g_c7_g+=j.c7_g
                        dl_dee_g_c8_g+=j.c8_g
                        dl_dee_g_c9_g+=j.c9_g
                        dl_dee_g_c10_g+=j.c10_g
                        dl_dee_g_c11_g+=j.c11_g
                        dl_dee_g_c12_g+=j.c12_g
                        dl_dee_g_c_total_g+=j.c_total_g

                        dl_dee_g_c1_t+=j.c1_t
                        dl_dee_g_c2_t+=j.c2_t
                        dl_dee_g_c3_t+=j.c3_t
                        dl_dee_g_c4_t+=j.c4_t
                        dl_dee_g_c5_t+=j.c5_t
                        dl_dee_g_c6_t+=j.c6_t
                        dl_dee_g_c7_t+=j.c7_t
                        dl_dee_g_c8_t+=j.c8_t
                        dl_dee_g_c9_t+=j.c9_t
                        dl_dee_g_c10_t+=j.c10_t
                        dl_dee_g_c11_t+=j.c11_t
                        dl_dee_g_c12_t+=j.c12_t
                        dl_dee_g_c_total_t+=j.c_total_t

                if int(dse_govt[i][0][0])==7:
                    dl_dee_pa_c1=dl_dee_pa_c2=dl_dee_pa_c3=dl_dee_pa_c4=dl_dee_pa_c5=dl_dee_pa_c6=dl_dee_pa_c7=dl_dee_pa_c8=dl_dee_pa_c9=dl_dee_pa_c10=dl_dee_pa_c11=dl_dee_pa_c12=dl_dee_pa_c_total=0 
                    dl_dee_pa_c1_b=dl_dee_pa_c2_b=dl_dee_pa_c3_b=dl_dee_pa_c4_b=dl_dee_pa_c5_b=dl_dee_pa_c6_b=dl_dee_pa_c7_b=dl_dee_pa_c8_b=dl_dee_pa_c9_b=dl_dee_pa_c10_b=dl_dee_pa_c11_b=dl_dee_pa_c12_b=dl_dee_pa_c_total_b=0 
                    dl_dee_pa_c1_g=dl_dee_pa_c2_g=dl_dee_pa_c3_g=dl_dee_pa_c4_g=dl_dee_pa_c5_g=dl_dee_pa_c6_g=dl_dee_pa_c7_g=dl_dee_pa_c8_g=dl_dee_pa_c9_g=dl_dee_pa_c10_g=dl_dee_pa_c11_g=dl_dee_pa_c12_g=dl_dee_pa_c_total_g=0 
                    dl_dee_pa_c1_t=dl_dee_pa_c2_t=dl_dee_pa_c3_t=dl_dee_pa_c4_t=dl_dee_pa_c5_t=dl_dee_pa_c6_t=dl_dee_pa_c7_t=dl_dee_pa_c8_t=dl_dee_pa_c9_t=dl_dee_pa_c10_t=dl_dee_pa_c11_t=dl_dee_pa_c12_t=dl_dee_pa_c_total_t=0
                    for j in schl_list:
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

                        dl_dee_pa_c1_b+=j.c1_b
                        dl_dee_pa_c2_b+=j.c2_b
                        dl_dee_pa_c3_b+=j.c3_b
                        dl_dee_pa_c4_b+=j.c4_b
                        dl_dee_pa_c5_b+=j.c5_b
                        dl_dee_pa_c6_b+=j.c6_b
                        dl_dee_pa_c7_b+=j.c7_b
                        dl_dee_pa_c8_b+=j.c8_b
                        dl_dee_pa_c9_b+=j.c9_b
                        dl_dee_pa_c10_b+=j.c10_b
                        dl_dee_pa_c11_b+=j.c11_b
                        dl_dee_pa_c12_b+=j.c12_b
                        dl_dee_pa_c_total_b+=j.c_total_b

                        dl_dee_pa_c1_g+=j.c1_g
                        dl_dee_pa_c2_g+=j.c2_g
                        dl_dee_pa_c3_g+=j.c3_g
                        dl_dee_pa_c4_g+=j.c4_g
                        dl_dee_pa_c5_g+=j.c5_g
                        dl_dee_pa_c6_g+=j.c6_g
                        dl_dee_pa_c7_g+=j.c7_g
                        dl_dee_pa_c8_g+=j.c8_g
                        dl_dee_pa_c9_g+=j.c9_g
                        dl_dee_pa_c10_g+=j.c10_g
                        dl_dee_pa_c11_g+=j.c11_g
                        dl_dee_pa_c12_g+=j.c12_g
                        dl_dee_pa_c_total_g+=j.c_total_g

                        dl_dee_pa_c1_t+=j.c1_t
                        dl_dee_pa_c2_t+=j.c2_t
                        dl_dee_pa_c3_t+=j.c3_t
                        dl_dee_pa_c4_t+=j.c4_t
                        dl_dee_pa_c5_t+=j.c5_t
                        dl_dee_pa_c6_t+=j.c6_t
                        dl_dee_pa_c7_t+=j.c7_t
                        dl_dee_pa_c8_t+=j.c8_t
                        dl_dee_pa_c9_t+=j.c9_t
                        dl_dee_pa_c10_t+=j.c10_t
                        dl_dee_pa_c11_t+=j.c11_t
                        dl_dee_pa_c12_t+=j.c12_t
                        dl_dee_pa_c_total_t+=j.c_total_t
                if int(dse_govt[i][0][0])==8:
                    dl_dee_pua_c1=dl_dee_pua_c2=dl_dee_pua_c3=dl_dee_pua_c4=dl_dee_pua_c5=dl_dee_pua_c6=dl_dee_pua_c7=dl_dee_pua_c8=dl_dee_pua_c9=dl_dee_pua_c10=dl_dee_pua_c11=dl_dee_pua_c12=dl_dee_pua_c_total=0 
                    dl_dee_pua_c1_b=dl_dee_pua_c2_b=dl_dee_pua_c3_b=dl_dee_pua_c4_b=dl_dee_pua_c5_b=dl_dee_pua_c6_b=dl_dee_pua_c7_b=dl_dee_pua_c8_b=dl_dee_pua_c9_b=dl_dee_pua_c10_b=dl_dee_pua_c11_b=dl_dee_pua_c12_b=dl_dee_pua_c_total_b=0 
                    dl_dee_pua_c1_g=dl_dee_pua_c2_g=dl_dee_pua_c3_g=dl_dee_pua_c4_g=dl_dee_pua_c5_g=dl_dee_pua_c6_g=dl_dee_pua_c7_g=dl_dee_pua_c8_g=dl_dee_pua_c9_g=dl_dee_pua_c10_g=dl_dee_pua_c11_g=dl_dee_pua_c12_g=dl_dee_pua_c_total_g=0 
                    dl_dee_pua_c1_t=dl_dee_pua_c2_t=dl_dee_pua_c3_t=dl_dee_pua_c4_t=dl_dee_pua_c5_t=dl_dee_pua_c6_t=dl_dee_pua_c7_t=dl_dee_pua_c8_t=dl_dee_pua_c9_t=dl_dee_pua_c10_t=dl_dee_pua_c11_t=dl_dee_pua_c12_t=dl_dee_pua_c_total_t=0
                    for j in schl_list:
                        dl_dee_pua_c1 +=j.c1
                        dl_dee_pua_c2 +=j.c2
                        dl_dee_pua_c3 +=j.c3
                        dl_dee_pua_c4 +=j.c4
                        dl_dee_pua_c5 +=j.c5
                        dl_dee_pua_c6 +=j.c6
                        dl_dee_pua_c7 +=j.c7
                        dl_dee_pua_c8 +=j.c8
                        dl_dee_pua_c9 +=j.c9
                        dl_dee_pua_c10 +=j.c10
                        dl_dee_pua_c11 +=j.c11
                        dl_dee_pua_c12 +=j.c12
                        dl_dee_pua_c_total+=j.c_total

                        dl_dee_pua_c1_b+=j.c1_b
                        dl_dee_pua_c2_b+=j.c2_b
                        dl_dee_pua_c3_b+=j.c3_b
                        dl_dee_pua_c4_b+=j.c4_b
                        dl_dee_pua_c5_b+=j.c5_b
                        dl_dee_pua_c6_b+=j.c6_b
                        dl_dee_pua_c7_b+=j.c7_b
                        dl_dee_pua_c8_b+=j.c8_b
                        dl_dee_pua_c9_b+=j.c9_b
                        dl_dee_pua_c10_b+=j.c10_b
                        dl_dee_pua_c11_b+=j.c11_b
                        dl_dee_pua_c12_b+=j.c12_b
                        dl_dee_pua_c_total_b+=j.c_total_b

                        dl_dee_pua_c1_g+=j.c1_g
                        dl_dee_pua_c2_g+=j.c2_g
                        dl_dee_pua_c3_g+=j.c3_g
                        dl_dee_pua_c4_g+=j.c4_g
                        dl_dee_pua_c5_g+=j.c5_g
                        dl_dee_pua_c6_g+=j.c6_g
                        dl_dee_pua_c7_g+=j.c7_g
                        dl_dee_pua_c8_g+=j.c8_g
                        dl_dee_pua_c9_g+=j.c9_g
                        dl_dee_pua_c10_g+=j.c10_g
                        dl_dee_pua_c11_g+=j.c11_g
                        dl_dee_pua_c12_g+=j.c12_g
                        dl_dee_pua_c_total_g+=j.c_total_g

                        dl_dee_pua_c1_t+=j.c1_t
                        dl_dee_pua_c2_t+=j.c2_t
                        dl_dee_pua_c3_t+=j.c3_t
                        dl_dee_pua_c4_t+=j.c4_t
                        dl_dee_pua_c5_t+=j.c5_t
                        dl_dee_pua_c6_t+=j.c6_t
                        dl_dee_pua_c7_t+=j.c7_t
                        dl_dee_pua_c8_t+=j.c8_t
                        dl_dee_pua_c9_t+=j.c9_t
                        dl_dee_pua_c10_t+=j.c10_t
                        dl_dee_pua_c11_t+=j.c11_t
                        dl_dee_pua_c12_t+=j.c12_t
                        dl_dee_pua_c_total_t+=j.c_total_t
        return render(request,'gender_wise/d_l_gender_wise_report.html',locals())

# Block Login 


class block_level_genderwise_report(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated():
            user_access_level=[4,3]
            user=self.kwargs['pk']
            block=Block.objects.get(id=user)
            blockk=block.block_name
            global dse_govt
            global all_schools
            global gender_wise
            global mgmt_name
            for i in range(0,len(dse_govt)):   
                b_l_school_list=all_schools.filter(block_id=user,management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])
                schl_list=gender_wise.filter(school_id__in=b_l_school_list).order_by('school')
                if int(dse_govt[i][0][0])==1:
                    bl_ds_g_c1=bl_ds_g_c2=bl_ds_g_c3=bl_ds_g_c4=bl_ds_g_c5=bl_ds_g_c6=bl_ds_g_c7=bl_ds_g_c8=bl_ds_g_c9=bl_ds_g_c10=bl_ds_g_c11=bl_ds_g_c12=bl_ds_g_c_total=0
                    bl_ds_g_c1_b=bl_ds_g_c2_b=bl_ds_g_c3_b=bl_ds_g_c4_b=bl_ds_g_c5_b=bl_ds_g_c6_b=bl_ds_g_c7_b=bl_ds_g_c8_b=bl_ds_g_c9_b=bl_ds_g_c10_b=bl_ds_g_c11_b=bl_ds_g_c12_b=bl_ds_g_c_total_b=0
                    bl_ds_g_c1_g=bl_ds_g_c2_g=bl_ds_g_c3_g=bl_ds_g_c4_g=bl_ds_g_c5_g=bl_ds_g_c6_g=bl_ds_g_c7_g=bl_ds_g_c8_g=bl_ds_g_c9_g=bl_ds_g_c10_g=bl_ds_g_c11_g=bl_ds_g_c12_g=bl_ds_g_c_total_g=0
                    bl_ds_g_c1_t=bl_ds_g_c2_t=bl_ds_g_c3_t=bl_ds_g_c4_t=bl_ds_g_c5_t=bl_ds_g_c6_t=bl_ds_g_c7_t=bl_ds_g_c8_t=bl_ds_g_c9_t=bl_ds_g_c10_t=bl_ds_g_c11_t=bl_ds_g_c12_t=bl_ds_g_c_total_t=0
                    for j in schl_list:
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

                        bl_ds_g_c1_b+=j.c1_b
                        bl_ds_g_c2_b+=j.c2_b
                        bl_ds_g_c3_b+=j.c3_b
                        bl_ds_g_c4_b+=j.c4_b
                        bl_ds_g_c5_b+=j.c5_b
                        bl_ds_g_c6_b+=j.c6_b
                        bl_ds_g_c7_b+=j.c7_b
                        bl_ds_g_c8_b+=j.c8_b
                        bl_ds_g_c9_b+=j.c9_b
                        bl_ds_g_c10_b+=j.c10_b
                        bl_ds_g_c11_b+=j.c11_b
                        bl_ds_g_c12_b+=j.c12_b
                        bl_ds_g_c_total_b+=j.c_total_b

                        bl_ds_g_c1_g+=j.c1_g
                        bl_ds_g_c2_g+=j.c2_g
                        bl_ds_g_c3_g+=j.c3_g
                        bl_ds_g_c4_g+=j.c4_g
                        bl_ds_g_c5_g+=j.c5_g
                        bl_ds_g_c6_g+=j.c6_g
                        bl_ds_g_c7_g+=j.c7_g
                        bl_ds_g_c8_g+=j.c8_g
                        bl_ds_g_c9_g+=j.c9_g
                        bl_ds_g_c10_g+=j.c10_g
                        bl_ds_g_c11_g+=j.c11_g
                        bl_ds_g_c12_g+=j.c12_g
                        bl_ds_g_c_total_g+=j.c_total_g

                        bl_ds_g_c1_t+=j.c1_t
                        bl_ds_g_c2_t+=j.c2_t
                        bl_ds_g_c3_t+=j.c3_t
                        bl_ds_g_c4_t+=j.c4_t
                        bl_ds_g_c5_t+=j.c5_t
                        bl_ds_g_c6_t+=j.c6_t
                        bl_ds_g_c7_t+=j.c7_t
                        bl_ds_g_c8_t+=j.c8_t
                        bl_ds_g_c9_t+=j.c9_t
                        bl_ds_g_c10_t+=j.c10_t
                        bl_ds_g_c11_t+=j.c11_t
                        bl_ds_g_c12_t+=j.c12_t
                        bl_ds_g_c_total_t+=j.c_total_t
                if int(dse_govt[i][0][0])==2:
                    bl_ds_pa_c1=bl_ds_pa_c2=bl_ds_pa_c3=bl_ds_pa_c4=bl_ds_pa_c5=bl_ds_pa_c6=bl_ds_pa_c7=bl_ds_pa_c8=bl_ds_pa_c9=bl_ds_pa_c10=bl_ds_pa_c11=bl_ds_pa_c12=bl_ds_pa_c_total=0
                    bl_ds_pa_c1_b=bl_ds_pa_c2_b=bl_ds_pa_c3_b=bl_ds_pa_c4_b=bl_ds_pa_c5_b=bl_ds_pa_c6_b=bl_ds_pa_c7_b=bl_ds_pa_c8_b=bl_ds_pa_c9_b=bl_ds_pa_c10_b=bl_ds_pa_c11_b=bl_ds_pa_c12_b=bl_ds_pa_c_total_b=0
                    bl_ds_pa_c1_g=bl_ds_pa_c2_g=bl_ds_pa_c3_g=bl_ds_pa_c4_g=bl_ds_pa_c5_g=bl_ds_pa_c6_g=bl_ds_pa_c7_g=bl_ds_pa_c8_g=bl_ds_pa_c9_g=bl_ds_pa_c10_g=bl_ds_pa_c11_g=bl_ds_pa_c12_g=bl_ds_pa_c_total_g=0
                    bl_ds_pa_c1_t=bl_ds_pa_c2_t=bl_ds_pa_c3_t=bl_ds_pa_c4_t=bl_ds_pa_c5_t=bl_ds_pa_c6_t=bl_ds_pa_c7_t=bl_ds_pa_c8_t=bl_ds_pa_c9_t=bl_ds_pa_c10_t=bl_ds_pa_c11_t=bl_ds_pa_c12_t=bl_ds_pa_c_total_t=0
                    for j in schl_list:
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

                        bl_ds_pa_c1_b+=j.c1_b
                        bl_ds_pa_c2_b+=j.c2_b
                        bl_ds_pa_c3_b+=j.c3_b
                        bl_ds_pa_c4_b+=j.c4_b
                        bl_ds_pa_c5_b+=j.c5_b
                        bl_ds_pa_c6_b+=j.c6_b
                        bl_ds_pa_c7_b+=j.c7_b
                        bl_ds_pa_c8_b+=j.c8_b
                        bl_ds_pa_c9_b+=j.c9_b
                        bl_ds_pa_c10_b+=j.c10_b
                        bl_ds_pa_c11_b+=j.c11_b
                        bl_ds_pa_c12_b+=j.c12_b
                        bl_ds_pa_c_total_b+=j.c_total_b

                        bl_ds_pa_c1_g+=j.c1_g
                        bl_ds_pa_c2_g+=j.c2_g
                        bl_ds_pa_c3_g+=j.c3_g
                        bl_ds_pa_c4_g+=j.c4_g
                        bl_ds_pa_c5_g+=j.c5_g
                        bl_ds_pa_c6_g+=j.c6_g
                        bl_ds_pa_c7_g+=j.c7_g
                        bl_ds_pa_c8_g+=j.c8_g
                        bl_ds_pa_c9_g+=j.c9_g
                        bl_ds_pa_c10_g+=j.c10_g
                        bl_ds_pa_c11_g+=j.c11_g
                        bl_ds_pa_c12_g+=j.c12_g
                        bl_ds_pa_c_total_g+=j.c_total_g

                        bl_ds_pa_c1_t+=j.c1_t
                        bl_ds_pa_c2_t+=j.c2_t
                        bl_ds_pa_c3_t+=j.c3_t
                        bl_ds_pa_c4_t+=j.c4_t
                        bl_ds_pa_c5_t+=j.c5_t
                        bl_ds_pa_c6_t+=j.c6_t
                        bl_ds_pa_c7_t+=j.c7_t
                        bl_ds_pa_c8_t+=j.c8_t
                        bl_ds_pa_c9_t+=j.c9_t
                        bl_ds_pa_c10_t+=j.c10_t
                        bl_ds_pa_c11_t+=j.c11_t
                        bl_ds_pa_c12_t+=j.c12_t
                        bl_ds_pa_c_total_t+=j.c_total_t
                if int(dse_govt[i][0][0])==3:
                    bl_ds_pua_c1=bl_ds_pua_c2=bl_ds_pua_c3=bl_ds_pua_c4=bl_ds_pua_c5=bl_ds_pua_c6=bl_ds_pua_c7=bl_ds_pua_c8=bl_ds_pua_c9=bl_ds_pua_c10=bl_ds_pua_c11=bl_ds_pua_c12=bl_ds_pua_c_total=0 
                    bl_ds_pua_c1_b=bl_ds_pua_c2_b=bl_ds_pua_c3_b=bl_ds_pua_c4_b=bl_ds_pua_c5_b=bl_ds_pua_c6_b=bl_ds_pua_c7_b=bl_ds_pua_c8_b=bl_ds_pua_c9_b=bl_ds_pua_c10_b=bl_ds_pua_c11_b=bl_ds_pua_c12_b=bl_ds_pua_c_total_b=0
                    bl_ds_pua_c1_g=bl_ds_pua_c2_g=bl_ds_pua_c3_g=bl_ds_pua_c4_g=bl_ds_pua_c5_g=bl_ds_pua_c6_g=bl_ds_pua_c7_g=bl_ds_pua_c8_g=bl_ds_pua_c9_g=bl_ds_pua_c10_g=bl_ds_pua_c11_g=bl_ds_pua_c12_g=bl_ds_pua_c_total_g=0
                    bl_ds_pua_c1_t=bl_ds_pua_c2_t=bl_ds_pua_c3_t=bl_ds_pua_c4_t=bl_ds_pua_c5_t=bl_ds_pua_c6_t=bl_ds_pua_c7_t=bl_ds_pua_c8_t=bl_ds_pua_c9_t=bl_ds_pua_c10_t=bl_ds_pua_c11_t=bl_ds_pua_c12_t=bl_ds_pua_c_total_t=0
                    for j in schl_list:
                        bl_ds_pua_c1 +=j.c1
                        bl_ds_pua_c2 +=j.c2
                        bl_ds_pua_c3 +=j.c3
                        bl_ds_pua_c4 +=j.c4
                        bl_ds_pua_c5 +=j.c5
                        bl_ds_pua_c6 +=j.c6
                        bl_ds_pua_c7 +=j.c7
                        bl_ds_pua_c8 +=j.c8
                        bl_ds_pua_c9 +=j.c9
                        bl_ds_pua_c10 +=j.c10
                        bl_ds_pua_c11 +=j.c11
                        bl_ds_pua_c12 +=j.c12
                        bl_ds_pua_c_total+=j.c_total

                        bl_ds_pua_c1_b+=j.c1_b
                        bl_ds_pua_c2_b+=j.c2_b
                        bl_ds_pua_c3_b+=j.c3_b
                        bl_ds_pua_c4_b+=j.c4_b
                        bl_ds_pua_c5_b+=j.c5_b
                        bl_ds_pua_c6_b+=j.c6_b
                        bl_ds_pua_c7_b+=j.c7_b
                        bl_ds_pua_c8_b+=j.c8_b
                        bl_ds_pua_c9_b+=j.c9_b
                        bl_ds_pua_c10_b+=j.c10_b
                        bl_ds_pua_c11_b+=j.c11_b
                        bl_ds_pua_c12_b+=j.c12_b
                        bl_ds_pua_c_total_b+=j.c_total_b

                        bl_ds_pua_c1_g+=j.c1_g
                        bl_ds_pua_c2_g+=j.c2_g
                        bl_ds_pua_c3_g+=j.c3_g
                        bl_ds_pua_c4_g+=j.c4_g
                        bl_ds_pua_c5_g+=j.c5_g
                        bl_ds_pua_c6_g+=j.c6_g
                        bl_ds_pua_c7_g+=j.c7_g
                        bl_ds_pua_c8_g+=j.c8_g
                        bl_ds_pua_c9_g+=j.c9_g
                        bl_ds_pua_c10_g+=j.c10_g
                        bl_ds_pua_c11_g+=j.c11_g
                        bl_ds_pua_c12_g+=j.c12_g
                        bl_ds_pua_c_total_g+=j.c_total_g

                        bl_ds_pua_c1_t+=j.c1_t
                        bl_ds_pua_c2_t+=j.c2_t
                        bl_ds_pua_c3_t+=j.c3_t
                        bl_ds_pua_c4_t+=j.c4_t
                        bl_ds_pua_c5_t+=j.c5_t
                        bl_ds_pua_c6_t+=j.c6_t
                        bl_ds_pua_c7_t+=j.c7_t
                        bl_ds_pua_c8_t+=j.c8_t
                        bl_ds_pua_c9_t+=j.c9_t
                        bl_ds_pua_c10_t+=j.c10_t
                        bl_ds_pua_c11_t+=j.c11_t
                        bl_ds_pua_c12_t+=j.c12_t
                        bl_ds_pua_c_total_t+=j.c_total_t

                if int(dse_govt[i][0][0])==4:
                    bl_m_c1=bl_m_c2=bl_m_c3=bl_m_c4=bl_m_c5=bl_m_c6=bl_m_c7=bl_m_c8=bl_m_c9=bl_m_c10=bl_m_c11=bl_m_c12=bl_m_c_total=0
                    bl_m_c1_b=bl_m_c2_b=bl_m_c3_b=bl_m_c4_b=bl_m_c5_b=bl_m_c6_b=bl_m_c7_b=bl_m_c8_b=bl_m_c9_b=bl_m_c10_b=bl_m_c11_b=bl_m_c12_b=bl_m_c_total_b=0
                    bl_m_c1_g=bl_m_c2_g=bl_m_c3_g=bl_m_c4_g=bl_m_c5_g=bl_m_c6_g=bl_m_c7_g=bl_m_c8_g=bl_m_c9_g=bl_m_c10_g=bl_m_c11_g=bl_m_c12_g=bl_m_c_total_g=0
                    bl_m_c1_t=bl_m_c2_t=bl_m_c3_t=bl_m_c4_t=bl_m_c5_t=bl_m_c6_t=bl_m_c7_t=bl_m_c8_t=bl_m_c9_t=bl_m_c10_t=bl_m_c11_t=bl_m_c12_t=bl_m_c_total_t=0
                    for j in schl_list:
                        bl_m_c1 +=j.c1
                        bl_m_c2 +=j.c2
                        bl_m_c3 +=j.c3
                        bl_m_c4 +=j.c4
                        bl_m_c5 +=j.c5
                        bl_m_c6 +=j.c6
                        bl_m_c7 +=j.c7
                        bl_m_c8 +=j.c8
                        bl_m_c9 +=j.c9
                        bl_m_c10 +=j.c10
                        bl_m_c11 +=j.c11
                        bl_m_c12 +=j.c12
                        bl_m_c_total+=j.c_total

                        bl_m_c1_b+=j.c1_b
                        bl_m_c2_b+=j.c2_b
                        bl_m_c3_b+=j.c3_b
                        bl_m_c4_b+=j.c4_b
                        bl_m_c5_b+=j.c5_b
                        bl_m_c6_b+=j.c6_b
                        bl_m_c7_b+=j.c7_b
                        bl_m_c8_b+=j.c8_b
                        bl_m_c9_b+=j.c9_b
                        bl_m_c10_b+=j.c10_b
                        bl_m_c11_b+=j.c11_b
                        bl_m_c12_b+=j.c12_b
                        bl_m_c_total_b+=j.c_total_b

                        bl_m_c1_g+=j.c1_g
                        bl_m_c2_g+=j.c2_g
                        bl_m_c3_g+=j.c3_g
                        bl_m_c4_g+=j.c4_g
                        bl_m_c5_g+=j.c5_g
                        bl_m_c6_g+=j.c6_g
                        bl_m_c7_g+=j.c7_g
                        bl_m_c8_g+=j.c8_g
                        bl_m_c9_g+=j.c9_g
                        bl_m_c10_g+=j.c10_g
                        bl_m_c11_g+=j.c11_g
                        bl_m_c12_g+=j.c12_g
                        bl_m_c_total_g+=j.c_total_g

                        bl_m_c1_t+=j.c1_t
                        bl_m_c2_t+=j.c2_t
                        bl_m_c3_t+=j.c3_t
                        bl_m_c4_t+=j.c4_t
                        bl_m_c5_t+=j.c5_t
                        bl_m_c6_t+=j.c6_t
                        bl_m_c7_t+=j.c7_t
                        bl_m_c8_t+=j.c8_t
                        bl_m_c9_t+=j.c9_t
                        bl_m_c10_t+=j.c10_t
                        bl_m_c11_t+=j.c11_t
                        bl_m_c12_t+=j.c12_t
                        bl_m_c_total_t+=j.c_total_t

                if int(dse_govt[i][0][0])==5:
                    bl_cbse_c1=bl_cbse_c2=bl_cbse_c3=bl_cbse_c4=bl_cbse_c5=bl_cbse_c6=bl_cbse_c7=bl_cbse_c8=bl_cbse_c9=bl_cbse_c10=bl_cbse_c11=bl_cbse_c12=bl_cbse_c_total=0
                    bl_cbse_c1_b=bl_cbse_c2_b=bl_cbse_c3_b=bl_cbse_c4_b=bl_cbse_c5_b=bl_cbse_c6_b=bl_cbse_c7_b=bl_cbse_c8_b=bl_cbse_c9_b=bl_cbse_c10_b=bl_cbse_c11_b=bl_cbse_c12_b=bl_cbse_c_total_b=0
                    bl_cbse_c1_g=bl_cbse_c2_g=bl_cbse_c3_g=bl_cbse_c4_g=bl_cbse_c5_g=bl_cbse_c6_g=bl_cbse_c7_g=bl_cbse_c8_g=bl_cbse_c9_g=bl_cbse_c10_g=bl_cbse_c11_g=bl_cbse_c12_g=bl_cbse_c_total_g=0
                    bl_cbse_c1_t=bl_cbse_c2_t=bl_cbse_c3_t=bl_cbse_c4_t=bl_cbse_c5_t=bl_cbse_c6_t=bl_cbse_c7_t=bl_cbse_c8_t=bl_cbse_c9_t=bl_cbse_c10_t=bl_cbse_c11_t=bl_cbse_c12_t=bl_cbse_c_total_t=0
                    for j in schl_list:
                        bl_cbse_c1 +=j.c1
                        bl_cbse_c2 +=j.c2
                        bl_cbse_c3 +=j.c3
                        bl_cbse_c4 +=j.c4
                        bl_cbse_c5 +=j.c5
                        bl_cbse_c6 +=j.c6
                        bl_cbse_c7 +=j.c7
                        bl_cbse_c8 +=j.c8
                        bl_cbse_c9 +=j.c9
                        bl_cbse_c10 +=j.c10
                        bl_cbse_c11 +=j.c11
                        bl_cbse_c12 +=j.c12
                        bl_cbse_c_total+=j.c_total

                        bl_cbse_c1_b+=j.c1_b
                        bl_cbse_c2_b+=j.c2_b
                        bl_cbse_c3_b+=j.c3_b
                        bl_cbse_c4_b+=j.c4_b
                        bl_cbse_c5_b+=j.c5_b
                        bl_cbse_c6_b+=j.c6_b
                        bl_cbse_c7_b+=j.c7_b
                        bl_cbse_c8_b+=j.c8_b
                        bl_cbse_c9_b+=j.c9_b
                        bl_cbse_c10_b+=j.c10_b
                        bl_cbse_c11_b+=j.c11_b
                        bl_cbse_c12_b+=j.c12_b
                        bl_cbse_c_total_b+=j.c_total_b

                        bl_cbse_c1_g+=j.c1_g
                        bl_cbse_c2_g+=j.c2_g
                        bl_cbse_c3_g+=j.c3_g
                        bl_cbse_c4_g+=j.c4_g
                        bl_cbse_c5_g+=j.c5_g
                        bl_cbse_c6_g+=j.c6_g
                        bl_cbse_c7_g+=j.c7_g
                        bl_cbse_c8_g+=j.c8_g
                        bl_cbse_c9_g+=j.c9_g
                        bl_cbse_c10_g+=j.c10_g
                        bl_cbse_c11_g+=j.c11_g
                        bl_cbse_c12_g+=j.c12_g
                        bl_cbse_c_total_g+=j.c_total_g

                        bl_cbse_c1_t+=j.c1_t
                        bl_cbse_c2_t+=j.c2_t
                        bl_cbse_c3_t+=j.c3_t
                        bl_cbse_c4_t+=j.c4_t
                        bl_cbse_c5_t+=j.c5_t
                        bl_cbse_c6_t+=j.c6_t
                        bl_cbse_c7_t+=j.c7_t
                        bl_cbse_c8_t+=j.c8_t
                        bl_cbse_c9_t+=j.c9_t
                        bl_cbse_c10_t+=j.c10_t
                        bl_cbse_c11_t+=j.c11_t
                        bl_cbse_c12_t+=j.c12_t
                        bl_cbse_c_total_t+=j.c_total_t
                if int(dse_govt[i][0][0])==6:
                    bl_dee_g_c1=bl_dee_g_c2=bl_dee_g_c3=bl_dee_g_c4=bl_dee_g_c5=bl_dee_g_c6=bl_dee_g_c7=bl_dee_g_c8=bl_dee_g_c9=bl_dee_g_c10=bl_dee_g_c11=bl_dee_g_c12=bl_dee_g_c_total=0 
                    bl_dee_g_c1_b=bl_dee_g_c2_b=bl_dee_g_c3_b=bl_dee_g_c4_b=bl_dee_g_c5_b=bl_dee_g_c6_b=bl_dee_g_c7_b=bl_dee_g_c8_b=bl_dee_g_c9_b=bl_dee_g_c10_b=bl_dee_g_c11_b=bl_dee_g_c12_b=bl_dee_g_c_total_b=0 
                    bl_dee_g_c1_g=bl_dee_g_c2_g=bl_dee_g_c3_g=bl_dee_g_c4_g=bl_dee_g_c5_g=bl_dee_g_c6_g=bl_dee_g_c7_g=bl_dee_g_c8_g=bl_dee_g_c9_g=bl_dee_g_c10_g=bl_dee_g_c11_g=bl_dee_g_c12_g=bl_dee_g_c_total_g=0
                    bl_dee_g_c1_t=bl_dee_g_c2_t=bl_dee_g_c3_t=bl_dee_g_c4_t=bl_dee_g_c5_t=bl_dee_g_c6_t=bl_dee_g_c7_t=bl_dee_g_c8_t=bl_dee_g_c9_t=bl_dee_g_c10_t=bl_dee_g_c11_t=bl_dee_g_c12_t=bl_dee_g_c_total_t=0
                    for j in schl_list:
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

                        bl_dee_g_c1_b+=j.c1_b
                        bl_dee_g_c2_b+=j.c2_b
                        bl_dee_g_c3_b+=j.c3_b
                        bl_dee_g_c4_b+=j.c4_b
                        bl_dee_g_c5_b+=j.c5_b
                        bl_dee_g_c6_b+=j.c6_b
                        bl_dee_g_c7_b+=j.c7_b
                        bl_dee_g_c8_b+=j.c8_b
                        bl_dee_g_c9_b+=j.c9_b
                        bl_dee_g_c10_b+=j.c10_b
                        bl_dee_g_c11_b+=j.c11_b
                        bl_dee_g_c12_b+=j.c12_b
                        bl_dee_g_c_total_b+=j.c_total_b

                        bl_dee_g_c1_g+=j.c1_g
                        bl_dee_g_c2_g+=j.c2_g
                        bl_dee_g_c3_g+=j.c3_g
                        bl_dee_g_c4_g+=j.c4_g
                        bl_dee_g_c5_g+=j.c5_g
                        bl_dee_g_c6_g+=j.c6_g
                        bl_dee_g_c7_g+=j.c7_g
                        bl_dee_g_c8_g+=j.c8_g
                        bl_dee_g_c9_g+=j.c9_g
                        bl_dee_g_c10_g+=j.c10_g
                        bl_dee_g_c11_g+=j.c11_g
                        bl_dee_g_c12_g+=j.c12_g
                        bl_dee_g_c_total_g+=j.c_total_g

                        bl_dee_g_c1_t+=j.c1_t
                        bl_dee_g_c2_t+=j.c2_t
                        bl_dee_g_c3_t+=j.c3_t
                        bl_dee_g_c4_t+=j.c4_t
                        bl_dee_g_c5_t+=j.c5_t
                        bl_dee_g_c6_t+=j.c6_t
                        bl_dee_g_c7_t+=j.c7_t
                        bl_dee_g_c8_t+=j.c8_t
                        bl_dee_g_c9_t+=j.c9_t
                        bl_dee_g_c10_t+=j.c10_t
                        bl_dee_g_c11_t+=j.c11_t
                        bl_dee_g_c12_t+=j.c12_t
                        bl_dee_g_c_total_t+=j.c_total_t

                if int(dse_govt[i][0][0])==7:
                    bl_dee_pa_c1=bl_dee_pa_c2=bl_dee_pa_c3=bl_dee_pa_c4=bl_dee_pa_c5=bl_dee_pa_c6=bl_dee_pa_c7=bl_dee_pa_c8=bl_dee_pa_c9=bl_dee_pa_c10=bl_dee_pa_c11=bl_dee_pa_c12=bl_dee_pa_c_total=0
                    bl_dee_pa_c1_b=bl_dee_pa_c2_b=bl_dee_pa_c3_b=bl_dee_pa_c4_b=bl_dee_pa_c5_b=bl_dee_pa_c6_b=bl_dee_pa_c7_b=bl_dee_pa_c8_b=bl_dee_pa_c9_b=bl_dee_pa_c10_b=bl_dee_pa_c11_b=bl_dee_pa_c12_b=bl_dee_pa_c_total_b=0
                    bl_dee_pa_c1_g=bl_dee_pa_c2_g=bl_dee_pa_c3_g=bl_dee_pa_c4_g=bl_dee_pa_c5_g=bl_dee_pa_c6_g=bl_dee_pa_c7_g=bl_dee_pa_c8_g=bl_dee_pa_c9_g=bl_dee_pa_c10_g=bl_dee_pa_c11_g=bl_dee_pa_c12_g=bl_dee_pa_c_total_g=0
                    bl_dee_pa_c1_t=bl_dee_pa_c2_t=bl_dee_pa_c3_t=bl_dee_pa_c4_t=bl_dee_pa_c5_t=bl_dee_pa_c6_t=bl_dee_pa_c7_t=bl_dee_pa_c8_t=bl_dee_pa_c9_t=bl_dee_pa_c10_t=bl_dee_pa_c11_t=bl_dee_pa_c12_t=bl_dee_pa_c_total_t=0                    
                    for j in schl_list:
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

                        bl_dee_pa_c1_b+=j.c1_b
                        bl_dee_pa_c2_b+=j.c2_b
                        bl_dee_pa_c3_b+=j.c3_b
                        bl_dee_pa_c4_b+=j.c4_b
                        bl_dee_pa_c5_b+=j.c5_b
                        bl_dee_pa_c6_b+=j.c6_b
                        bl_dee_pa_c7_b+=j.c7_b
                        bl_dee_pa_c8_b+=j.c8_b
                        bl_dee_pa_c9_b+=j.c9_b
                        bl_dee_pa_c10_b+=j.c10_b
                        bl_dee_pa_c11_b+=j.c11_b
                        bl_dee_pa_c12_b+=j.c12_b
                        bl_dee_pa_c_total_b+=j.c_total_b

                        bl_dee_pa_c1_g+=j.c1_g
                        bl_dee_pa_c2_g+=j.c2_g
                        bl_dee_pa_c3_g+=j.c3_g
                        bl_dee_pa_c4_g+=j.c4_g
                        bl_dee_pa_c5_g+=j.c5_g
                        bl_dee_pa_c6_g+=j.c6_g
                        bl_dee_pa_c7_g+=j.c7_g
                        bl_dee_pa_c8_g+=j.c8_g
                        bl_dee_pa_c9_g+=j.c9_g
                        bl_dee_pa_c10_g+=j.c10_g
                        bl_dee_pa_c11_g+=j.c11_g
                        bl_dee_pa_c12_g+=j.c12_g
                        bl_dee_pa_c_total_g+=j.c_total_g

                        bl_dee_pa_c1_t+=j.c1_t
                        bl_dee_pa_c2_t+=j.c2_t
                        bl_dee_pa_c3_t+=j.c3_t
                        bl_dee_pa_c4_t+=j.c4_t
                        bl_dee_pa_c5_t+=j.c5_t
                        bl_dee_pa_c6_t+=j.c6_t
                        bl_dee_pa_c7_t+=j.c7_t
                        bl_dee_pa_c8_t+=j.c8_t
                        bl_dee_pa_c9_t+=j.c9_t
                        bl_dee_pa_c10_t+=j.c10_t
                        bl_dee_pa_c11_t+=j.c11_t
                        bl_dee_pa_c12_t+=j.c12_t
                        bl_dee_pa_c_total_t+=j.c_total_t
                if int(dse_govt[i][0][0])==8:
                    bl_dee_pua_c1=bl_dee_pua_c2=bl_dee_pua_c3=bl_dee_pua_c4=bl_dee_pua_c5=bl_dee_pua_c6=bl_dee_pua_c7=bl_dee_pua_c8=bl_dee_pua_c9=bl_dee_pua_c10=bl_dee_pua_c11=bl_dee_pua_c12=bl_dee_pua_c_total=0
                    bl_dee_pua_c1_b=bl_dee_pua_c2_b=bl_dee_pua_c3_b=bl_dee_pua_c4_b=bl_dee_pua_c5_b=bl_dee_pua_c6_b=bl_dee_pua_c7_b=bl_dee_pua_c8_b=bl_dee_pua_c9_b=bl_dee_pua_c10_b=bl_dee_pua_c11_b=bl_dee_pua_c12_b=bl_dee_pua_c_total_b=0
                    bl_dee_pua_c1_g=bl_dee_pua_c2_g=bl_dee_pua_c3_g=bl_dee_pua_c4_g=bl_dee_pua_c5_g=bl_dee_pua_c6_g=bl_dee_pua_c7_g=bl_dee_pua_c8_g=bl_dee_pua_c9_g=bl_dee_pua_c10_g=bl_dee_pua_c11_g=bl_dee_pua_c12_g=bl_dee_pua_c_total_g=0
                    bl_dee_pua_c1_t=bl_dee_pua_c2_t=bl_dee_pua_c3_t=bl_dee_pua_c4_t=bl_dee_pua_c5_t=bl_dee_pua_c6_t=bl_dee_pua_c7_t=bl_dee_pua_c8_t=bl_dee_pua_c9_t=bl_dee_pua_c10_t=bl_dee_pua_c11_t=bl_dee_pua_c12_t=bl_dee_pua_c_total_t=0
                    for j in schl_list:
                        bl_dee_pua_c1 +=j.c1
                        bl_dee_pua_c2 +=j.c2
                        bl_dee_pua_c3 +=j.c3
                        bl_dee_pua_c4 +=j.c4
                        bl_dee_pua_c5 +=j.c5
                        bl_dee_pua_c6 +=j.c6
                        bl_dee_pua_c7 +=j.c7
                        bl_dee_pua_c8 +=j.c8
                        bl_dee_pua_c9 +=j.c9
                        bl_dee_pua_c10 +=j.c10
                        bl_dee_pua_c11 +=j.c11
                        bl_dee_pua_c12 +=j.c12
                        bl_dee_pua_c_total+=j.c_total

                        bl_dee_pua_c1_b+=j.c1_b
                        bl_dee_pua_c2_b+=j.c2_b
                        bl_dee_pua_c3_b+=j.c3_b
                        bl_dee_pua_c4_b+=j.c4_b
                        bl_dee_pua_c5_b+=j.c5_b
                        bl_dee_pua_c6_b+=j.c6_b
                        bl_dee_pua_c7_b+=j.c7_b
                        bl_dee_pua_c8_b+=j.c8_b
                        bl_dee_pua_c9_b+=j.c9_b
                        bl_dee_pua_c10_b+=j.c10_b
                        bl_dee_pua_c11_b+=j.c11_b
                        bl_dee_pua_c12_b+=j.c12_b
                        bl_dee_pua_c_total_b+=j.c_total_b

                        bl_dee_pua_c1_g+=j.c1_g
                        bl_dee_pua_c2_g+=j.c2_g
                        bl_dee_pua_c3_g+=j.c3_g
                        bl_dee_pua_c4_g+=j.c4_g
                        bl_dee_pua_c5_g+=j.c5_g
                        bl_dee_pua_c6_g+=j.c6_g
                        bl_dee_pua_c7_g+=j.c7_g
                        bl_dee_pua_c8_g+=j.c8_g
                        bl_dee_pua_c9_g+=j.c9_g
                        bl_dee_pua_c10_g+=j.c10_g
                        bl_dee_pua_c11_g+=j.c11_g
                        bl_dee_pua_c12_g+=j.c12_g
                        bl_dee_pua_c_total_g+=j.c_total_g

                        bl_dee_pua_c1_t+=j.c1_t
                        bl_dee_pua_c2_t+=j.c2_t
                        bl_dee_pua_c3_t+=j.c3_t
                        bl_dee_pua_c4_t+=j.c4_t
                        bl_dee_pua_c5_t+=j.c5_t
                        bl_dee_pua_c6_t+=j.c6_t
                        bl_dee_pua_c7_t+=j.c7_t
                        bl_dee_pua_c8_t+=j.c8_t
                        bl_dee_pua_c9_t+=j.c9_t
                        bl_dee_pua_c10_t+=j.c10_t
                        bl_dee_pua_c11_t+=j.c11_t
                        bl_dee_pua_c12_t+=j.c12_t
                        bl_dee_pua_c_total_t+=j.c_total_t
    

            return render(request,'gender_wise/b_l_genderwise_report.html',locals())
    def post(self,request,**kwargs):
        global dse_govt        
        global all_schools
        global gender_wise
        global mgmt_name
        mgmt_id = request.POST.get('blks', False)
        mgmt_blk=mgmt_id.split(',')
        
        m_id=mgmt_blk[0]
        b_id=mgmt_blk[1]
        excel=mgmt_blk[2]
        
        print excel
        schl_ids=[]
        schl_names=[]
        blk_c1,blk_c2,blk_c3,blk_c4,blk_c5,blk_c6,blk_c7,blk_c8,blk_c9,blk_c10,blk_c11,blk_c12,blk_c_total=([] for zz1 in range(13))
        blk_c1_b,blk_c2_b,blk_c3_b,blk_c4_b,blk_c5_b,blk_c6_b,blk_c7_b,blk_c8_b,blk_c9_b,blk_c10_b,blk_c11_b,blk_c12_b,blk_c_total_b=([] for zz2 in range(13))
        blk_c1_g,blk_c2_g,blk_c3_g,blk_c4_g,blk_c5_g,blk_c6_g,blk_c7_g,blk_c8_g,blk_c9_g,blk_c10_g,blk_c11_g,blk_c12_g,blk_c_total_g=([] for zz3 in range(13))
        blk_c1_t,blk_c2_t,blk_c3_t,blk_c4_t,blk_c5_t,blk_c6_t,blk_c7_t,blk_c8_t,blk_c9_t,blk_c10_t,blk_c11_t,blk_c12_t,blk_c_total_t=([] for zz4 in range(13))
           
        for ii in range(0,len(dse_govt)):
            if str(dse_govt[ii][0][0])==str(m_id):
                aa=dse_govt[ii][0]
                bb=sum(aa)
                cc=int(bb)-1
                dd=mgmt_name[cc]
                block_name=Block.objects.get(id=mgmt_blk[1])
                school_list=all_schools.filter(block_id=mgmt_blk[1],management_id__in=dse_govt[ii][1],category_id__in=dse_govt[ii][2])
              
                sclka=school_list.count()
                
                g_blk=gender_wise.filter(school_id__in=school_list).order_by('school')
                
                
        if int(excel) == 2 :
            for kk in g_blk:
                schl_ids.append(str(kk.id))
                schl_names.append(kk.school.school_name)
                blk_c1.append(kk.c1)                        
                blk_c2.append(kk.c2)
                blk_c3.append(kk.c3)
                blk_c4.append(kk.c4)
                blk_c5.append(kk.c5)
                blk_c6.append(kk.c6)
                blk_c7.append(kk.c7)
                blk_c8.append(kk.c8) 
                blk_c9.append(kk.c9) 
                blk_c10.append(kk.c10) 
                blk_c11.append(kk.c11) 
                blk_c12.append(kk.c12)
                blk_c_total.append(kk.c_total)

                blk_c1_b.append(kk.c1_b) 
                blk_c2_b.append(kk.c2_b)
                blk_c3_b.append(kk.c3_b) 
                blk_c4_b.append(kk.c4_b) 
                blk_c5_b.append(kk.c5_b) 
                blk_c6_b.append(kk.c6_b) 
                blk_c7_b.append(kk.c7_b) 
                blk_c8_b.append(kk.c8_b) 
                blk_c9_b.append(kk.c9_b) 
                blk_c10_b.append(kk.c10_b)
                blk_c11_b.append(kk.c11_b) 
                blk_c12_b.append(kk.c12_b)
                blk_c_total_b.append(kk.c_total_b)

                blk_c1_g.append(kk.c1_g) 
                blk_c2_g.append(kk.c2_g)
                blk_c3_g.append(kk.c3_g) 
                blk_c4_g.append(kk.c4_g) 
                blk_c5_g.append(kk.c5_g) 
                blk_c6_g.append(kk.c6_g) 
                blk_c7_g.append(kk.c7_g) 
                blk_c8_g.append(kk.c8_g) 
                blk_c9_g.append(kk.c9_g) 
                blk_c10_g.append(kk.c10_g) 
                blk_c11_g.append(kk.c11_g) 
                blk_c12_g.append(kk.c12_g) 
                blk_c_total_g.append(kk.c_total_g)  

                blk_c1_t.append(kk.c1_t) 
                blk_c2_t.append(kk.c2_t) 
                blk_c3_t.append(kk.c3_t)
                blk_c4_t.append(kk.c4_t) 
                blk_c5_t.append(kk.c5_t) 
                blk_c6_t.append(kk.c6_t)
                blk_c7_t.append(kk.c7_t) 
                blk_c8_t.append(kk.c8_t)
                blk_c9_t.append(kk.c9_t) 
                blk_c10_t.append(kk.c10_t) 
                blk_c11_t.append(kk.c11_t)
                blk_c12_t.append(kk.c12_t) 
                blk_c_total_t.append(kk.c_total_t) 
        
            samp_list=zip(schl_ids,schl_names,blk_c1_b,blk_c1_g,blk_c1_t,blk_c2,blk_c2_b,blk_c2_g,blk_c2_t,blk_c2,blk_c3_b,blk_c3_g,blk_c3_t,blk_c3,blk_c4_b,blk_c4_g,blk_c4_t,blk_c4,blk_c5_b,blk_c5_g,blk_c5_t,blk_c5,blk_c6_b,blk_c6_g,blk_c6_t,blk_c6,blk_c7_b,blk_c7_g,blk_c7_t,blk_c7,blk_c8_b,blk_c8_g,blk_c8_t,blk_c8,blk_c9_b,blk_c9_g,blk_c9_t,blk_c9,blk_c10_b,blk_c10_g,blk_c10_t,blk_c10,blk_c11_b,blk_c11_g,blk_c11_t,blk_c11,blk_c12_b,blk_c12_g,blk_c12_t,blk_c12,blk_c_total_b,blk_c_total_g,blk_c_total_t,blk_c_total)
            df=pd.DataFrame(samp_list,columns=["ID","School Name","I-BOYS","I-GIRLS","I-TRANS","I-TOTAL","II-BOYS","II-GIRLS","II-TRANS","II-TOTAL","III-BOYS","III-GIRLS","III-TRANS","III-TOTAL","IV-BOYS","IV-GIRLS","IV-TRANS","IV-TOTAL","V-BOYS","V-GIRLS","V-TRANS","V-TOTAL","VI-BOYS","VI-GIRLS","VI-TRANS","VI-TOTAL","VII-BOYS","VII-GIRLS","VII-TRANS","VII-TOTAL","VIII-BOYS","VIII-GIRLS","VIII-TRANS","VIII-TOTAL","IX-BOYS","IX-GIRLS","IX-TRANS","IX-TOTAL","X-BOYS","X-GIRLS","X-TRANS","X-TOTAL","XI-BOYS","XI-GIRLS","XI-TRANS","XI-TOTAL","XII-BOYS","XII-GIRLS","XII-TRANS","XII-TOTAL","BOYS TOTAL","GIRLS TOTAL","TRANSGENDER TOTAL","OVERALL TOTAL"])
            df.index=range(1,sclka+1)
            df.set_index('ID')
            outputss = StringIO.StringIO()
            writer = pd.ExcelWriter(outputss,engine='xlsxwriter')
            df.to_excel(writer, startcol = 0, startrow = 3,sheet_name="Schools")
            worksheet=writer.sheets['Schools']
            worksheet.write_string(0, 5, dd+' '+'Schoolwise Abstract')
            writer.save()
            writer.close()
            outputss.seek(0)
            response = HttpResponse(outputss.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=Schoolwise Abstract.xlsx'
            return response
        else :        
            return render(request,'gender_wise/block_genderwise_school_report.html',locals())


    # def post(self,request,**kwargs):
    #     global dse_govt        
    #     global all_schools
    #     global gender_wise
    #     global mgmt_name
    #     mgmt_id = request.POST.get('blks', False)
    #     mgmt_blk=mgmt_id.split(',')
    #     for ii in range(0,len(dse_govt)):
    #         if str(dse_govt[ii][0][0])==str(mgmt_blk[0]):
    #             aa=dse_govt[ii][0]
    #             bb=sum(aa)
    #             cc=int(bb)-1
    #             dd=mgmt_name[cc]
    #             block_name=Block.objects.get(id=mgmt_blk[1])
    #             school_list=all_schools.filter(block_id=mgmt_blk[1],management_id__in=dse_govt[ii][1],category_id__in=dse_govt[ii][2])
    #             blk_schl=gender_wise.filter(school_id__in=school_list).order_by('school')

    #             blk_s_c1=blk_schl.aggregate(Sum('c1')).values()[0]                      
    #             blk_s_c2=blk_schl.aggregate(Sum('c2')).values()[0]
    #             blk_s_c3=blk_schl.aggregate(Sum('c3')).values()[0]
    #             blk_s_c4=blk_schl.aggregate(Sum('c4')).values()[0]
    #             blk_s_c5=blk_schl.aggregate(Sum('c5')).values()[0]
    #             blk_s_c6=blk_schl.aggregate(Sum('c6')).values()[0]
    #             blk_s_c7=blk_schl.aggregate(Sum('c7')).values()[0]
    #             blk_s_c8=blk_schl.aggregate(Sum('c8')).values()[0]
    #             blk_s_c9=blk_schl.aggregate(Sum('c9')).values()[0]
    #             blk_s_c10=blk_schl.aggregate(Sum('c10')).values()[0]
    #             blk_s_c11=blk_schl.aggregate(Sum('c11')).values()[0]
    #             blk_s_c12=blk_schl.aggregate(Sum('c12')).values()[0]
    #             blk_s_c_total=blk_schl.aggregate(Sum('c_total')).values()[0]

    #             blk_s_c1_b=blk_schl.aggregate(Sum('c1_b')).values()[0]
    #             blk_s_c2_b=blk_schl.aggregate(Sum('c2_b')).values()[0]
    #             blk_s_c3_b=blk_schl.aggregate(Sum('c3_b')).values()[0]
    #             blk_s_c4_b=blk_schl.aggregate(Sum('c4_b')).values()[0]
    #             blk_s_c5_b=blk_schl.aggregate(Sum('c5_b')).values()[0]
    #             blk_s_c6_b=blk_schl.aggregate(Sum('c6_b')).values()[0]
    #             blk_s_c7_b=blk_schl.aggregate(Sum('c7_b')).values()[0]
    #             blk_s_c8_b=blk_schl.aggregate(Sum('c8_b')).values()[0]
    #             blk_s_c9_b=blk_schl.aggregate(Sum('c9_b')).values()[0]
    #             blk_s_c10_b=blk_schl.aggregate(Sum('c10_b')).values()[0]
    #             blk_s_c11_b=blk_schl.aggregate(Sum('c11_b')).values()[0]
    #             blk_s_c12_b=blk_schl.aggregate(Sum('c12_b')).values()[0]               
    #             blk_s_c_total_b=blk_schl.aggregate(Sum('c_total_b')).values()[0]

    #             blk_s_c1_g=blk_schl.aggregate(Sum('c1_g')).values()[0]
    #             blk_s_c2_g=blk_schl.aggregate(Sum('c2_g')).values()[0]
    #             blk_s_c3_g=blk_schl.aggregate(Sum('c3_g')).values()[0]
    #             blk_s_c4_g=blk_schl.aggregate(Sum('c4_g')).values()[0]
    #             blk_s_c5_g=blk_schl.aggregate(Sum('c5_g')).values()[0]
    #             blk_s_c6_g=blk_schl.aggregate(Sum('c6_g')).values()[0]
    #             blk_s_c7_g=blk_schl.aggregate(Sum('c7_g')).values()[0]
    #             blk_s_c8_g=blk_schl.aggregate(Sum('c8_g')).values()[0]
    #             blk_s_c9_g=blk_schl.aggregate(Sum('c9_g')).values()[0]
    #             blk_s_c1_g0_g=blk_schl.aggregate(Sum('c10_g')).values()[0]
    #             blk_s_c1_g1_g=blk_schl.aggregate(Sum('c11_g')).values()[0]
    #             blk_s_c1_g2_g=blk_schl.aggregate(Sum('c12_g')).values()[0]
    #             blk_s_c_total_g=blk_schl.aggregate(Sum('c_total_g')).values()[0]

    #             blk_s_c1_t=blk_schl.aggregate(Sum('c1_t')).values()[0]
    #             blk_s_c2_t=blk_schl.aggregate(Sum('c2_t')).values()[0]
    #             blk_s_c3_t=blk_schl.aggregate(Sum('c3_t')).values()[0]
    #             blk_s_c4_t=blk_schl.aggregate(Sum('c4_t')).values()[0]
    #             blk_s_c5_t=blk_schl.aggregate(Sum('c5_t')).values()[0]
    #             blk_s_c6_t=blk_schl.aggregate(Sum('c6_t')).values()[0]
    #             blk_s_c7_t=blk_schl.aggregate(Sum('c7_t')).values()[0]
    #             blk_s_c8_t=blk_schl.aggregate(Sum('c8_t')).values()[0]
    #             blk_s_c9_t=blk_schl.aggregate(Sum('c9_t')).values()[0]
    #             blk_s_c1_t0_t=blk_schl.aggregate(Sum('c10_t')).values()[0]
    #             blk_s_c1_t1_t=blk_schl.aggregate(Sum('c11_t')).values()[0]
    #             blk_s_c1_t2_t=blk_schl.aggregate(Sum('c12_t')).values()[0]
    #             blk_s_c_total_t=blk_schl.aggregate(Sum('c_total_t')).values()[0]             
                
    #     return render(request,'gender_wise/block_genderwise_school_report.html',locals())

    
