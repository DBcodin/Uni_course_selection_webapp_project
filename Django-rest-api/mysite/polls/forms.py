"""from django.forms import ModelForm

from django import forms

from polls import UserModuleInfo

class UploadForm(ModelForm):
    User_name = forms.CharField()
    User_age = forms.IntegerField()
    User_course =forms.CharField()
    User_current_part = forms.CharField()
    User_Technical_skill = forms.IntegerField()
    User_Communication_skill = forms.IntegerField()
    User_Mathmatical_skill = forms.IntegerField()
    User_Coding_skill = forms.IntegerField()
    User_Project_manag_skill = forms.IntegerField()
    User_Professional_dev_skill = forms.IntegerField()
    User_student_id = forms.CharField()
    User_student_password = forms.CharField()
    class Meta:
        model = UserModuleInfo
        fields = ['User_name','User_age','User_course','User_current_part','User_Technical_skill','User_Communication_skill',' User_Mathmatical_skill',' User_Coding_skill','User_Project_manag_skill','User_Professional_dev_skill',' User_student_id','User_student_password']"""