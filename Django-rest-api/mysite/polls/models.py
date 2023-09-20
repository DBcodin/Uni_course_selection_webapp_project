import datetime

from django.db import models
from django.utils import timezone





    
class UserModuleInfo(models.Model):
    User_name = models.CharField(max_length=100)
    User_age = models.IntegerField(default=0)
    User_course =models.CharField(max_length=100)
    User_current_part = models.CharField(max_length=100)
    User_Technical_skill = models.IntegerField(default=0)
    User_Communication_skill = models.IntegerField(default=0)
    User_Mathmatical_skill = models.IntegerField(default=0)
    User_Coding_skill = models.IntegerField(default=0)
    User_Project_manag_skill = models.IntegerField(default=0)
    User_Professional_dev_skill = models.IntegerField(default=0)
    User_student_id = models.CharField(max_length=100,default="N/a")
    User_student_password = models.CharField(max_length=100,default="N/a")
    def __str__(self): #This allows the model to return the user name of each entry when objects.all() is called in the shell
        return self.User_name  

class ModuleInfo(models.Model):
    Module_Code = models.CharField(max_length=100)
    Module_Part = models.CharField(max_length=200)
    Module_Semester = models.IntegerField(default=0)
    Module_name = models.CharField(max_length=200)
    Module_Manditory = models.BooleanField(default=False)
    Module_Technical_skill = models.IntegerField(default=0)
    Module_Communication_skill = models.IntegerField(default=0)
    Module_Mathmatical_skill = models.IntegerField(default=0)
    Module_Coding_skill = models.IntegerField(default=0)
    Module_Project_manag_skill = models.IntegerField(default=0)
    Module_Professional_dev_skill = models.IntegerField(default=0)
    Module_Completed_by_user = models.BooleanField(default=False)
    Test = models.CharField(max_length=100, default= "hello")
    def __str__(self):
        return self.Module_Code   

class ModuleLinking(models.Model):
    Link_Module_code = models.CharField(max_length=100, default="Empty")
    Followed_by = models.CharField(max_length=100)
    Precursed_by = models.CharField(max_length=100)
    def __str__(self):
        return self.Link_Module_code 