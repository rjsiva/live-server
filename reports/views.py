from django.shortcuts import render
from django.views.generic import View
from baseapp.models import *
from students.models import Child_detail,School_child_count   
from django.template.loader import get_template
from django.template import Context
import cStringIO as StringIO
import xhtml2pdf.pisa as pisa
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, PageNotAnInteger
from django.db.models import Count, Sum
from reports.models import * 
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import never_cache
 
dse_govt=[[[1],[1,2,4,5],[3,5,6,7,8,9,10]],
[[2],[6,7],[3,5,6,7,8,9,10]],
[[3],[8,12,13,14,15,16,17],[3,5,6,7,8,9,10]],
[[4],[9],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
[[5],[10,11],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
[[6],[1,2,3,4,5],[1,2,4,11,15]],
[[7],[6,7],[1,2,4,11,15]],[[8],[8,12,13,14,15,16,17],[1,2,4,11,15]]]
state_schools=School.objects.all()
aadhaar=aadhaar_student_count.objects.all()
mgmt_name=["DSE - Government",
"DSE - Private Aided",
"DSE - Private UnAided",
"Matriculation",
"CBSE/ICSE",
"DEE - Government",
"DEE - Private Aided",
"DEE - Private UnAided"]

class BaseView(View):
    def get(self,request,**kwargs):  
        
        return render(request,'base1.html',locals())

class district_level_aadhaar_report(View):
    def get(self,request,**kwargs):        
        return render(request,'aadhaar/district_login.html',locals())


class block_level_aadhaar_report(View):
    def get(self,request,**kwargs):
        return render(request,'aadhaar/block_login.html',locals())
    def post(self,request,**kwargs):
        global dse_govt
        global state_schools
        global aadhaar

        mgmt_id = request.POST.get('blks', False)
        mgmt_blk=mgmt_id.split(',')
        for i in range(0,len(dse_govt)):
            if str(dse_govt[i][0][0])==str(mgmt_blk[0]):
                block_name=Block.objects.get(id=mgmt_blk[1])
                school_list=state_schools.filter(block_id=mgmt_blk[1],management_id__in=dse_govt[i][1],category_id__in=dse_govt[i][2])
                blk_schl=aadhaar.filter(school_id__in=school_list)
                blk_schl_emis=blk_schl.aggregate(Sum('school_total')).values()[0]
                blk_schl_aadhaar=blk_schl.aggregate(Sum('a_school_total')).values()[0]
        return render(request,'aadhaar/blockwise_school_aadhaar.html',locals())

class aadhaar_report(View):
    def get(self,request,**kwargs):
        
        return render(request,'aadhaar/base.html',locals())

class state_level_aadhaar_report(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated():
            global state_schools
            global aadhaar
            global dse_govt
            all_emis=0
            all_aadhaar=0
            all_not_aadhar=0
            
            for i in range(0,len(dse_govt)):   
                dse_school_list=state_schools.filter(management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])
                dse=aadhaar.filter(school_id__in=dse_school_list)
                if int(dse_govt[i][0][0])==1:
                    dse_emis=0
                    dse_aadhaar=0
                    dse_not_aadhaar=0
                    for j in dse:
                        dse_emis=dse_emis+j.school_total
                        dse_aadhaar=dse_aadhaar+j.a_school_total
                    dse_not_aadhaar=dse_emis-dse_aadhaar 
                if int(dse_govt[i][0][0])==2:
                    pvt_aided_emis=0
                    pvt_aided_aadhaar=0
                    pvt_aided_not_aadhaar=0
                    for k in dse:
                        pvt_aided_emis=pvt_aided_emis+k.school_total
                        pvt_aided_aadhaar=pvt_aided_aadhaar+k.a_school_total 
                    pvt_aided_not_aadhaar=pvt_aided_emis-pvt_aided_aadhaar
                if int(dse_govt[i][0][0])==3:
                    pvt_unaided_emis=0
                    pvt_unaided_aadhaar=0
                    pvt_unaided_not_aadhaar=0
                    for l in dse:
                        pvt_unaided_emis=pvt_unaided_emis+l.school_total
                        pvt_unaided_aadhaar=pvt_unaided_aadhaar+l.a_school_total
                    pvt_unaided_not_aadhaar=pvt_unaided_emis-pvt_unaided_aadhaar
                if int(dse_govt[i][0][0])==4:
                    matric_emis=0
                    matric_aadhaar=0
                    matric_not_aadhaar=0
                    for m in dse:
                        matric_emis=matric_emis+m.school_total
                        matric_aadhaar=matric_aadhaar+m.a_school_total
                    matric_not_aadhaar=matric_emis-matric_aadhaar
                if int(dse_govt[i][0][0])==5:
                    cbse_emis=0
                    cbse_aadhaar=0
                    cbse_not_aadhaar=0
                    for n in dse:
                        cbse_emis=cbse_emis+n.school_total
                        cbse_aadhaar=cbse_aadhaar+n.a_school_total
                    cbse_not_aadhaar=cbse_emis-cbse_aadhaar                            
                if int(dse_govt[i][0][0])==6:
                    dee_emis=0
                    dee_aadhaar=0
                    dee_not_aadhaar=0
                    for j in dse:
                        dee_emis=dee_emis+j.school_total
                        dee_aadhaar=dee_aadhaar+j.a_school_total
                    dee_not_aadhaar=dee_emis-dee_aadhaar
                if int(dse_govt[i][0][0])==7:
                    dee_p_a_emis=0
                    dee_p_a_aadhaar=0
                    dee_p_a_not_aadhaar=0
                    for j in dse:
                        dee_p_a_emis=dee_p_a_emis+j.school_total
                        dee_p_a_aadhaar=dee_p_a_aadhaar+j.a_school_total
                    dee_p_a_not_aadhaar=dee_p_a_emis-dee_p_a_aadhaar
                if int(dse_govt[i][0][0])==8:
                    dee_n_emis=0
                    dee_n_aadhaar=0
                    dee_n_not_aadhaar=0
                    for j in dse:
                        dee_n_emis=dee_n_emis+j.school_total
                        dee_n_aadhaar=dee_n_aadhaar+j.a_school_total
                    dee_n_not_aadhaar=dee_n_emis-dee_n_aadhaar                  
            all_emis=dse_emis+pvt_aided_emis+pvt_unaided_emis+dee_emis+dee_p_a_emis+dee_n_emis+matric_emis+cbse_emis
            all_aadhaar=dse_aadhaar+pvt_aided_aadhaar+pvt_unaided_aadhaar+cbse_aadhaar+dee_aadhaar+dee_p_a_aadhaar+dee_n_aadhaar+matric_aadhaar
            all_not_aadhar=dse_not_aadhaar+pvt_aided_not_aadhaar+pvt_unaided_not_aadhaar+cbse_not_aadhaar+dee_not_aadhaar+dee_p_a_not_aadhaar+dee_n_not_aadhaar+matric_not_aadhaar
            return render(request,'aadhaar/aadhaar_report.html',locals())
    def post(self,request,**kwargs):      
        di_id = request.POST.get('distt', False)
        global dse_govt
        global state_schools
        global aadhaar
        global mgmt_name
        dist_list=District.objects.all().order_by('district_name')
        district_ids=[]
        district_names=[]
        emis=[]
        aadhaar_v=[]
        for i in range(0,len(dse_govt)):
            if str(dse_govt[i][0][0])==str(di_id):
                mgmt=dse_govt[i][1]
                a=dse_govt[i][0]
                b=sum(a)
                c=int(b)-1
                d=mgmt_name[c]
                for j in dist_list:
                    district_ids.append(str(j.id))              
                    district_names.append(j.district_name)
                    dist=state_schools.filter(district_id=j.id,management_id__in= dse_govt[i][1],category_id__in=dse_govt[i][2])              
                    dist_schl_list=aadhaar.filter(school_id__in=dist)       
                    x=dist_schl_list.aggregate(Sum('school_total'))
                    y=dist_schl_list.aggregate(Sum('a_school_total'))
                    emis+=x.values()
                    aadhaar_v+=y.values()           
                a_list=zip(district_ids,district_names,emis,aadhaar_v)

        return render(request,'aadhaar/d_l_aadhaar.html',locals())

class block_overall_aadhaar_report(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated():
            user_access_level=[4,3]
            user=self.kwargs['pk']
            mgmt=self.kwargs['pk1']
            blocks=Block.objects.filter(district_id=user)
            global dse_govt
            global state_schools
            global aadhaar
            global mgmt_name
            block_ids=[]
            block_names=[]
            blk_emis=[]
            blk_aadhaar=[]
            for i in range(0,len(dse_govt)):
                if str(dse_govt[i][0][0])==str(mgmt):
                    a=dse_govt[i][0]
                    b=sum(a)
                    c=int(b)-1
                    d=mgmt_name[c]
                    for j in blocks:
                        block_ids.append(str(j.id))
                        block_names.append(j.block_name)
                        school_list=state_schools.filter(block_id=j.id,management_id__in=dse_govt[i][1],category_id__in=dse_govt[i][2])
                        a_blk=aadhaar.filter(school_id__in=school_list)
                        x=a_blk.aggregate(Sum('school_total'))
                        y=a_blk.aggregate(Sum('a_school_total'))
                        blk_emis+=x.values()
                        blk_aadhaar+=y.values()
                    a_list=zip(block_ids,block_names,blk_emis,blk_aadhaar)
            return render(request,'aadhaar/block_overall_aadhaar.html',locals())
    def post(self,request,**kwargs):
        global dse_govt
        global state_schools
        global aadhaar
        global mgmt_name
        mgmt_id = request.POST.get('blks', False)
        mgmt_blk=mgmt_id.split(',')
        for i in range(0,len(dse_govt)):
            if str(dse_govt[i][0][0])==str(mgmt_blk[0]):
                a=dse_govt[i][0]
                b=sum(a)
                c=int(b)-1
                d=mgmt_name[c]
                block_name=Block.objects.get(id=mgmt_blk[1])
                school_list=state_schools.filter(block_id=mgmt_blk[1],management_id__in=dse_govt[i][1],category_id__in=dse_govt[i][2])
                blk_schl=aadhaar.filter(school_id__in=school_list)
                blk_schl_emis=blk_schl.aggregate(Sum('school_total')).values()[0]
                blk_schl_aadhaar=blk_schl.aggregate(Sum('a_school_total')).values()[0]
                
        return render(request,'aadhaar/blockwise_school_aadhaar.html',locals())

class school_level_aadhaar(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']
        aadhaar_1=aadhaar_student_count.objects.get(id=school)       
        return render(request,'aadhaar/s_l_aadhaar.html',locals())

# def render_to_pdf(template_src, context_dict, filename):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html = template.render(context)
#     result = StringIO.StringIO()
#     pdf = pisa.pisaDocument(
#         StringIO.StringIO(html.encode("UTF-8")), result, link_callback=fetch_resources)
#     if not pdf.err:
#         outfile = HttpResponse(result.getvalue(), mimetype="application/pdf")
#         outfile['Content-Disposition'] = 'attachment; filename=' + \
#             filename + '.pdf'
#         return outfile
#     return http.HttpResponse('We had some error on report generation<pre>%s</pre>' % cgi.escape(html))

# def fetch_resources(uri, rel):
#     path = os.path.join(
#         settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
#     return path

# def download_child_profile(request,ch_id):
#     child = Child_detail.objects.get(id=ch_id)
#     pagesize = 'A4'
#     title = 'Child Profile'
#     return render_to_pdf('download_child_profile.html', locals(), 'Child_Profile')

# class ReportView(View):
#     def get(self,request,**kwargs):
#         if request.user.account.user_category_id == 2 or request.user.account.user_category_id == 5:
#             school_list = School.objects.filter(block_id=request.user.account.associated_with).order_by('school_name')
#             return render(request,'report_list.html',{'school_list':school_list})
#         elif request.user.account.user_category_id == 3 or request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
#             block_list = Block.objects.filter(district_id=request.user.account.associated_with).order_by('block_name')
#             return render(request,'report_list.html',{'block_list':block_list})
#         elif request.user.account.user_category_id == 4 or request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17:
#             district_list = District.objects.all().order_by('district_name')
#             block_list = Block.objects.all().order_by('block_name')
#             return render(request,'report_list.html',{'block_list':block_list,'district_list':district_list})
#         else:
#             class_studying_list = Class_Studying.objects.all().order_by('id')
#             academic_year_list = Academic_Year.objects.all().order_by('id')
#             community_list = Community.objects.all().order_by('community_name')
#             religion_list = Religion.objects.all().order_by('religion_name')
#             language_list = Language.objects.all().order_by('language_name')
#             nationality_list = Nationality.objects.all().order_by('nationality')
#             education_medium_list = Education_medium.objects.all().order_by('education_medium')
#             diff_abled_list = Differently_abled.objects.all().order_by('da_name')
#             dis_advantagedgrp_list = Disadvantaged_group.objects.all().order_by('dis_group_name')
#             schemes_list = Schemes.objects.all().order_by('scheme_name')
#             return render(request,'report_list.html',{'class_studying_list':class_studying_list,'academic_year_list':academic_year_list,'community_list':community_list,'religion_list':religion_list,'language_list':language_list,'nationality_list':nationality_list,'education_medium_list':education_medium_list,'diff_abled_list':diff_abled_list,'dis_advantagedgrp_list':dis_advantagedgrp_list,'schemes_list':schemes_list})
#         return render(request,'report_list.html',locals())

#     def post(self,request,**kwargs):
#         if request.user.account.user_category_id == 2 or request.user.account.user_category_id == 5:
#             blk1=Child_detail.objects.filter(block_id=request.user.account.associated_with).filter(academic_year_id=3).values('school').distinct()
#             school_list = School.objects.filter(block_id=request.user.account.associated_with).order_by('school_name')
#             category_list=School.objects.filter(block_id=request.user.account.associated_with).filter(category__id__in=['1','2','3','6','11','12','13'])
#             print blk1
#             # print school_list
#             print category_list
#             return render(request,'report_list.html',locals())

#         elif request.user.account.user_category_id == 3 or request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
#             block_list1 = Block.objects.filter(district_id=request.user.account.associated_with).order_by('block_name')
#             stud2=Child_detail.objects.filter(district_id=request.user.account.associated_with).filter(academic_year_id=3).values('block').annotate(bcount=Count('gender')).order_by('block')
#             stud3=Child_detail.objects.filter(district_id=request.user.account.associated_with).filter(academic_year_id=3).values('block').annotate(scount=Count('staff_id', distinct=True)).order_by('block')
#             stud4=School.objects.filter(district_id=request.user.account.associated_with).values('block').annotate(schcount=Count('school_code', distinct=True)).order_by('block')
#             return render(request,'report_list.html',locals())
#         elif request.user.account.user_category_id == 4 or request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17:
#             district_list = District.objects.all().order_by('district_name')
#             dist1=Child_detail.objects.filter(academic_year_id=3).values('district').annotate(bcount=Count('gender')).order_by('district')
#             dist2=Child_detail.objects.filter(academic_year_id=3).values('district').annotate(scount=Count('staff_id', distinct=True)).order_by('district')
#             dist3=School.objects.values('district').annotate(schcount=Count('school_code', distinct=True)).order_by('district')
#             return render(request,'report_list.html',locals())
#         else:
#             school_id = request.user.account.associated_with
#             community_list = Community.objects.all().order_by('community_name')
#             sub_caste_list = Sub_Castes.objects.all().order_by('caste_name')
#             religion_list = Religion.objects.all().order_by('religion_name')
#             language_list = Language.objects.all().order_by('language_name')
#             nationality_list = Nationality.objects.all().order_by('nationality')
#             education_medium_list = Education_medium.objects.all().order_by('education_medium')
#             diff_abled_list = Differently_abled.objects.all().order_by('da_name')
#             dis_advantagedgrp_list = Disadvantaged_group.objects.all().order_by('dis_group_name')
#             schemes_list = Schemes.objects.all().order_by('scheme_name')
#             cur1 = connection.cursor()
#             cur2 = connection.cursor()
#             cur3 = connection.cursor()
#             cur4 = connection.cursor()
#             cur5 = connection.cursor()
#             cur6 = connection.cursor()
#             cur7 = connection.cursor()
           
#             kwargs = {}
#             kwargs["school_id"] = eval(school_id)
#             student_detail_list = Child_detail.objects.filter(**kwargs)
#             if 'class_studying_id' in request.POST:
#                 kwargs['class_studying_id__in'] = request.POST.getlist("class_studying_id")
#             else:
#                 pass
#             if 'class_section' in request.POST:
#                 kwargs["class_section__in"] = request.POST.getlist("class_section") 
#             else:
#                 pass
#             if 'academic_year_id' in request.POST:
#                 kwargs["academic_year_id__in"] = request.POST.getlist("academic_year_id")
#             else:
#                 pass
#             if 'gender' in request.POST:
#                 kwargs["gender__in"] = request.POST.getlist("gender")
#             else:
#                 pass
#             if 'community_id' in request.POST:
#                 kwargs["community_id__in"] = request.POST.getlist("community_id")
#             else:
#                 pass
#             if 'religion_id' in request.POST:
#                 kwargs["religion_id__in"] =request.POST.getlist("religion_id")
#             else:
#                 pass
#             if 'mothertounge_id' in request.POST:
#                 kwargs["mothertounge_id__in"] =request.POST.getlist("mothertounge_id")
#             else:
#                 pass
#             if 'child_differently_abled' in request.POST:
#                 kwargs["child_differently_abled__in"] =request.POST.getlist("child_differently_abled")
#             else:
#                 pass
#             if 'child_disadvantaged_group' in request.POST:
#                 kwargs["child_disadvantaged_group__in"] =request.POST.getlist("child_disadvantaged_group")
#             else:
#                 pass
#             if 'nationality_id' in request.POST:
#                 kwargs["nationality_id__in"] =request.POST.getlist("nationality_id")
#             else:
#                 pass
#             if 'blood_group' in request.POST:
#                 kwargs["blood_group__in"] =request.POST.getlist("blood_group")
#             else:
#                 pass
#             if 'mother_occupation' in request.POST:
#                 kwargs["mother_occupation__in"] =request.POST.getlist("mother_occupation")
#             else:
#                 pass
#             if 'father_occupation' in request.POST:
#                 kwargs["father_occupation__in"] =request.POST.getlist("father_occupation")
#             else:
#                 pass
#             if 'attendance_status' in request.POST:
#                 kwargs["attendance_status__in"] =request.POST.getlist("attendance_status")
#             else:
#                 pass
#             if 'education_medium_id' in request.POST:
#                 kwargs["education_medium_id__in"] =request.POST.getlist("education_medium_id")
#             else:
#                 pass
#             if 'govt_schemes_status' in request.POST:
#                 kwargs["govt_schemes_status__in"] =request.POST.getlist("govt_schemes_status")
#             else:
#                 pass
#             if 'child_status' in request.POST:
#                 kwargs["child_status__in"] =request.POST.getlist("child_status")
#             else:
#                 pass
#             student_detail_list = Child_detail.objects.filter(**kwargs)
#             student_detail_count = student_detail_list.count()
#             paginator = Paginator(student_detail_list, 10)
#             page = request.GET.get('page')
#             try:
#                 page_obj = paginator.page(page)
#             except PageNotAnInteger:
#                 # If page is not an integer, deliver first page.
#                 page_obj = paginator.page(1)
#             except EmptyPage:
#                 # If page is out of range (e.g. 9999), deliver last page of results.
#                 page_obj = paginator.page(paginator.num_pages)
#             return render(request,'report_list.html',locals())
#             # return render_to_pdf('download_child_profile.html',locals(),'Child_Profile')
#         pagesize = 'A4'
#         title = 'Child Profile'
#         return render(request,'report_list.html',locals())