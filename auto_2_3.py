import os 





"""
reading the file named call_2
"""
call_2=open('call_2.txt','r')

old_list=call_2.readlines()
new_list=[]
print("old list:\n\n"+str(call_2.readlines())+"\n\n")




for x in range(len(old_list)):
     new_list.insert(x,old_list[x].replace('\n',''))
     



print("new list:\n\n"+str(new_list)+"\n\n")


call_2.close()





find_x=dir(os.path)
print("\n")
print("\n"+("->>"*10)+"\n")
the_env=os.path.exists(new_list[0])
dir_container=[]
html_page_cont="""

{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'css/css1.css'%}">
    <link rel="stylesheet" href="{% static 'css/css1.css'%}">
    <link rel="stylesheet" href="{% static 'css/css1.css'%}">
    <title>{% block tit %}home{% endblock%}</title>
</head>
<header>
    <div id="header_head">
        <div>
            <h1>logo</h1>
        </div>
        <div>
            <h3>menu area</h3>
        </div>
    </div>
    <div id="header_body">
    {% block header %}{% endblock%}
    </div>

</header>

<body>
    <section class="sec_1">{% block sec_1 %}{% endblock%}</section>
    <section class="sec_2">{% block sec_2 %}{% endblock%}</section>
    <section class="sec_3">{% block sec_3 %}{% endblock%}</section>
    <section class="sec_3">{% block sec_4 %}{% endblock%}</section>
    <script src="{% static 'js/js1.js'%}"></script>
    <script src="{% static 'js/js1.js'%}"></script>
    <script src="{% static 'js/js1.js'%}"></script>
</body>
<footer>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
</footer>

</html>




"""

child_call="""

{% extends "home.html" %}
<br>{% block tit%}{% endblock %}
<br>{% block header%}
<div class='cont_model_1'></div>

{% endblock %}
<br>{% block sec_1%}
<div class='cont_model_2'></div>
{% endblock %}
<br>{% block sec_2%}{% endblock %}
<br>{% block sec_3%}{% endblock %}
<br>{% block sec_4%}{% endblock %}
"""

L_cont="""
from django.urls import path, re_path
from django.contrib.auth import views as auth_model
from .views import *

app_name = ""

urlpatterns = [
      path('login',auth_model.LoginView.as_view(template_name="registration/login.html"),name='login'),
      path('logout',auth_model.LogoutView.as_view(template_name="registration/logout.html"),name='logout'),
      path('',Menu.as_view(),name='home'),
      ]

"""
model_cont="""

\n\n\n
class ModelName(models.Model):

      def __str__(self):
            pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'ModelName'
            verbose_name_plural = 'ModelNames'



"""


model_serializer_cont="""

\n\n\n
class ModelName(serializers.ModelSerializer):

      
      class Meta:
            model = Model_x
            fields = ('','','','','')



"""


model_adminModel_cont="""

\n\n
class ModelaAdmin(admin.ModelAdmin):pass
\n\n
"""


model_form_cont="""

\n\n\n
class ModelName_form(forms.ModelForm):

      
      class Meta:
            model = Model_x
            fields = ('','','','','')
            widget=\{gggppp\}



"""


views_cont="""
from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.views.generic.edit import *
#from django.views.generic import *
from django.urls import *
from django.contrib.auth.models import *
from django.contrib.auth import login
from .call_form import *
from django.shortcuts import *


class Menu(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super(Menu, self).get_context_data(**kwargs)
        print("this is home model model")
        context
        return context

"""
admin_cont="""

class Admin_x(admin.ModelAdmin):pass

admin.site.register(ModelName)\n\n\n

"""






pkg_install=["pipenv==2024.0.1",
     "django==5.0.6",
"django-widget-tweaks==1.5.0",
"django-jazzmin==3.0.0",
"requests==2.31.0",
"beautifulsoup4==4.12.2",
"lxml==4.9.3",
"html5==0.0.9",
"Pillow==10.1.0",
"mysql-connector-python==8.1.0",
"mysql-connector-repackaged==0.3.1",
"djangorestframework==3.15.2","Markdown==3.6","django-filter==24.2",
"django-createsuperuserwithpassword==2.0.0",
"django-rosetta==0.10.0",
"whitenoise==6.6.0","django-cors-headers==4.4.0",
"django-phonenumber-field==7.3.0",
"django-parler==2.3","django-countries==7.5.1","django-import-export==4.1.1","django-countries==7.6.1","stripe==10.3.0"



]


settings_act_1="""

STATIC_URL = 'static/'

STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
print(f"the static path{str(STATICFILES_DIRS)}")

#STATIC_ROOT=BASE_DIR / 'static'
#print(f"the static path{str(STATIC_ROOT)}")


MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static/media')
print(f"the Media root path{str(MEDIA_ROOT)}")


LOGIN_REDIRECT_URL='core:home'
LOGOUT_REDIRECT_URL='core:home'

"""
settings_act_2=""

dir_list=['html','static','media','local']
html_models=['add','view','update','view_item','model']
static_dir=['img','css','js']

if the_env:
      print("the target venv found")
      '''act_3=os.chdir(new_list[0]+'/Scripts')
      act_3=os.system("activate.bat")
      act_3=os.chdir("../..")'''
      
      
      '''dir_container=list(os.walk("/web"))
      for f in range(len(dir_container)):
            print(dir_container[f])
            t1,t2,t3=dir_container[f]
            print(f"dir_path:{t1},\ndir List:{t2},\nfile List:{t3}")
      '''
      
      
      
else:
      print("the venv NOT found.....building one")
      
      act_1=os.system("python -m venv "+new_list[0])
      print("Done")
act_3=os.chdir(new_list[0]+'/Scripts')
act_3=os.system("activate.bat")
act_3=os.system("pip3 install --upgrade pip")
for install_x in range(len(pkg_install)):act_3=os.system("pip3 install "+pkg_install[install_x])
#act_3=os.chdir("../..")
act_6=os.system("pip3 install django")
act_6=os.system("django-admin startproject "+new_list[1])
#act_5=os.chdir('new_list[0]/Scripts')
print("\n\nchanging the first LVL\n\n")

act_7=os.chdir(new_list[1])

act_7_1=open(new_list[1]+'/settings.py','a+')

act_7_1.write("from pathlib import Path".replace("from pathlib import Path","""from pathlib import Path\nimport os"""))

print("\nACTION DONE\n")

act_7_1.write("'django.contrib.staticfiles',".replace("'django.contrib.staticfiles',","\n#'django.contrib.staticfiles','APP_NAME','widget_tweaks','stripe','phonenumber_field','import_export','django_countries','rest_framework','corsheaders' "))

#print("\nACTION DONE\n")
#act_7_1.write("'DIRS': []".replace("'DIRS': []","'DIRS': ['html']"))

print("\nACTION DONE\n")
act_7_1.write("STATIC_URL = 'static/'".replace("STATIC_URL = 'static/'",settings_act_1))





act_7_1.close()


#act_7=os.chdir("..")
print("\n\ndir changed\n\n")

act_8=os.system("python manage.py startapp "+new_list[2])
#act_7_1=os.chdir(new_list[2])





act_8=os.system("nul>"+new_list[2]+"/L.py")
act_8_1=open(new_list[2]+"/L.py",'+w')
act_8_1.write(L_cont)
act_8_1.close()


act_8_1=open(new_list[2]+"/models.py",'+w')
act_8_1.write("from django.db import models")
for m in range(5):
 act_8_1.write(f"""
               
               \n\n\n
class ModelName{m}(models.Model):

      def __str__(self):
            pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'ModelName{m}'
            verbose_name_plural = 'ModelNames{m}'



               
               """)
act_8_1.close()

act_8_1=open(new_list[2]+"/admin.py",'+w')
act_8_1.write("from django.contrib import admin\n\nfrom .models import *")
for m in range(5):
 act_8_1.write(f"""

class Admin_x{m}(admin.ModelAdmin):pass

admin.site.register(ModelName{m})\n\n\n

 """)
act_8_1.close()

act_8_1=open(new_list[2]+"/views.py",'+w')
act_8_1.write(views_cont)
act_8_1.close()


act_8=os.system("nul>"+new_list[2]+"/Act_1.py")
act_8=os.system("nul>"+new_list[2]+"/call_form.py")
form_w=open(new_list[2]+"/call_form.py",'w+')
form_w.write("from django import forms\nfrom .models import *\n")
for m in range(5):
 form_w.write(f"""

\n\n\n
class ModelName_form{m}(forms.ModelForm):

      
      class Meta:
            model = ModelName{m}
            fields = ()
            



""")
form_w.close()


act_8=os.system("nul>"+new_list[2]+"/Act_2.py")
act_8=os.system("nul>"+new_list[2]+"/serializers.py")
ser_w=open(new_list[2]+"/serializer.py",'w+')
ser_w.write("from rest_framework import serializers\n\nform .models import *\n\n\n")
for s in range(5):
 ser_w.write(f"""

\n\n\n
class ModelName_ser{s}(serializers.ModelSerializer):

      
      class Meta:
            model = ModelName{s}
            fields = ('','','','','')



""")
ser_w.close()
act_8=os.system("nul>"+new_list[2]+"/Act_3.py")
for f1 in range(len(dir_list)):
      os.mkdir(dir_list[f1])
      print(dir_list[f1])
      if f1 == 0:
            print("contents of "+dir_list[f1])
            
            act_9=os.chdir("html")
            act_9=os.system("nul>home.html")
            act_9h=open("home.html","w+")
            act_9h.write(html_page_cont)
            act_9h.close()
            act_9=os.mkdir("admin")
            act_9=os.system("nul>admin/base.html")
            act_9=os.mkdir("registration")
            act_9=os.system("nul>registration/reg.html")
            act_9=os.system("nul>registration/login.html")
            act_9=os.system("nul>registration/logout.html")
            for d in range(5):
                  print("dir_"+str(d+1))
                  act_10=os.mkdir("dir_"+str(d+1))
                  for f in range(len(html_models)):
                        act_11=os.system("nul>dir_"+str(d+1)+"\\"+html_models[f]+".html")
                        act_11x=open("dir_"+str(d+1)+"\\"+html_models[f]+".html","w+")
                        act_11x.write(child_call)
                        act_11x.close()
            act_12=os.chdir("..")
      else:pass
      if f1 == 1:
            print("contents of "+dir_list[f1])
            act_13=os.chdir("static")
            for s in range(len(static_dir)):
                  act_14=os.mkdir(static_dir[s])
                  for f in range(3):
                        act_15=os.system("nul>"+static_dir[s]+"/css"+str(1+f)+".css")
                  if s == 2:
                   for f in range(3):
                        act_15=os.system("nul>"+static_dir[s]+"/js"+str(1+f)+".js")
            
      else:pass
      

act_16=os.chdir("..")
act_16=os.system("python3 manage.py runserver")
                  

print("\n"+("->>"*10)+"\n")
print("\n")
