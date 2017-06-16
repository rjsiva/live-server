from django.db import models 
from django.db.models.fields import *
from baseapp.models import School,Block,District,Class_Studying
from students.models import Child_detail,School_child_count
import caching.base
from django.db.models.signals import post_save, post_delete

# Create your models here.
class aadhaar_student_count(models.Model):
    school=models.ForeignKey(School,blank=True, null=True)                        
    c1 = models.PositiveIntegerField(blank=True, null=True)
    c2 = models.PositiveIntegerField(blank=True, null=True)
    c3 = models.PositiveIntegerField(blank=True, null=True)
    c4 = models.PositiveIntegerField(blank=True, null=True)
    c5 = models.PositiveIntegerField(blank=True, null=True)
    c6 = models.PositiveIntegerField(blank=True, null=True)
    c7 = models.PositiveIntegerField(blank=True, null=True)
    c8 = models.PositiveIntegerField(blank=True, null=True)
    c9 = models.PositiveIntegerField(blank=True, null=True)
    c10 = models.PositiveIntegerField(blank=True, null=True)
    c11 = models.PositiveIntegerField(blank=True, null=True)
    c12 = models.PositiveIntegerField(blank=True, null=True)
    school_total = models.PositiveIntegerField(blank=True, null=True)
    a_c1 = models.PositiveIntegerField(blank=True, null=True)
    a_c2 = models.PositiveIntegerField(blank=True, null=True)
    a_c3 = models.PositiveIntegerField(blank=True, null=True)
    a_c4 = models.PositiveIntegerField(blank=True, null=True)
    a_c5 = models.PositiveIntegerField(blank=True, null=True)
    a_c6 = models.PositiveIntegerField(blank=True, null=True)
    a_c7 = models.PositiveIntegerField(blank=True, null=True)
    a_c8 = models.PositiveIntegerField(blank=True, null=True)
    a_c9 = models.PositiveIntegerField(blank=True, null=True)
    a_c10 = models.PositiveIntegerField(blank=True, null=True)
    a_c11 = models.PositiveIntegerField(blank=True, null=True)
    a_c12 = models.PositiveIntegerField(blank=True, null=True)
    a_school_total = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.school)

class common_reports(models.Model):
    school=models.ForeignKey(School,blank=True, null=True)
    c1 = models.PositiveIntegerField(blank=True, null=True)
    c2 = models.PositiveIntegerField(blank=True, null=True)
    c3 = models.PositiveIntegerField(blank=True, null=True)
    c4 = models.PositiveIntegerField(blank=True, null=True)
    c5 = models.PositiveIntegerField(blank=True, null=True)
    c6 = models.PositiveIntegerField(blank=True, null=True)
    c7 = models.PositiveIntegerField(blank=True, null=True)
    c8 = models.PositiveIntegerField(blank=True, null=True)
    c9 = models.PositiveIntegerField(blank=True, null=True)
    c10 = models.PositiveIntegerField(blank=True, null=True)
    c11 = models.PositiveIntegerField(blank=True, null=True)
    c12 = models.PositiveIntegerField(blank=True, null=True)
    c_total = models.PositiveIntegerField(blank=True, null=True)
    c1_b = models.PositiveIntegerField(blank=True, null=True)
    c2_b = models.PositiveIntegerField(blank=True, null=True)
    c3_b = models.PositiveIntegerField(blank=True, null=True)
    c4_b = models.PositiveIntegerField(blank=True, null=True)
    c5_b = models.PositiveIntegerField(blank=True, null=True)
    c6_b = models.PositiveIntegerField(blank=True, null=True)
    c7_b = models.PositiveIntegerField(blank=True, null=True)
    c8_b = models.PositiveIntegerField(blank=True, null=True)
    c9_b = models.PositiveIntegerField(blank=True, null=True)
    c10_b = models.PositiveIntegerField(blank=True, null=True)
    c11_b = models.PositiveIntegerField(blank=True, null=True)
    c12_b = models.PositiveIntegerField(blank=True, null=True)
    c_total_b = models.PositiveIntegerField(blank=True, null=True)
    c1_g = models.PositiveIntegerField(blank=True, null=True)
    c2_g = models.PositiveIntegerField(blank=True, null=True)
    c3_g = models.PositiveIntegerField(blank=True, null=True)
    c4_g = models.PositiveIntegerField(blank=True, null=True)
    c5_g = models.PositiveIntegerField(blank=True, null=True)
    c6_g = models.PositiveIntegerField(blank=True, null=True)
    c7_g = models.PositiveIntegerField(blank=True, null=True)
    c8_g = models.PositiveIntegerField(blank=True, null=True)
    c9_g = models.PositiveIntegerField(blank=True, null=True)
    c10_g = models.PositiveIntegerField(blank=True, null=True)
    c11_g = models.PositiveIntegerField(blank=True, null=True)
    c12_g = models.PositiveIntegerField(blank=True, null=True)
    c_total_g = models.PositiveIntegerField(blank=True, null=True)
    c1_t = models.PositiveIntegerField(blank=True, null=True)
    c2_t = models.PositiveIntegerField(blank=True, null=True)
    c3_t = models.PositiveIntegerField(blank=True, null=True)
    c4_t = models.PositiveIntegerField(blank=True, null=True)
    c5_t = models.PositiveIntegerField(blank=True, null=True)
    c6_t = models.PositiveIntegerField(blank=True, null=True)
    c7_t = models.PositiveIntegerField(blank=True, null=True)
    c8_t = models.PositiveIntegerField(blank=True, null=True)
    c9_t = models.PositiveIntegerField(blank=True, null=True)
    c10_t = models.PositiveIntegerField(blank=True, null=True)
    c11_t = models.PositiveIntegerField(blank=True, null=True)
    c12_t = models.PositiveIntegerField(blank=True, null=True)
    c_total_t = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
            return u'%s %s' % (self.school.school_name,self.c_total_t)

def report_child_count_increase(sender, instance, **kwargs):
    if kwargs.get('created', True):
        try:
            child = common_reports.objects.get(school_id=instance.school_id)
        except common_reports.DoesNotExist:
            child=common_reports.objects.create(school=instance.school,c1=0,c2=0,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0,c9=0,c10=0,c11=0,c12=0,c_total=0)
        class_studying= instance.class_studying
        gender=instance.gender

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
post_save.connect(report_child_count_increase, sender=Child_detail)

def report_child_count_decrease(sender, instance, **kwargs):
    
    child = common_reports.objects.get(school_id=instance.school_id)
    class_studying= instance.class_studying
    gender=instance.gender
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
post_delete.connect(report_child_count_decrease, sender=Child_detail)
    
