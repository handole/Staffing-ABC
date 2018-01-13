from django.forms import ModelForm
from django import forms
from pagedown.widgets import PagedownWidget
from django.utils.text import slugify
from . models import Applicant, Client, Resume, Recruiter, Uploadresume

# form for Applicant
class ApplicantForm(ModelForm):
	
	class Meta:
		model = Applicant
		fields = [
			'user',
			'username',
			'email',
		]


# form for Client
class ClientForm(ModelForm):
	
	class Meta:
		model = Client
		fields = [
			'user',
			'username',
			'email',
			'company',			
		]

# form for Resume
YEARS= [x for x in range(1950,2021)]

class ResumeForm(ModelForm):
	experience = forms.CharField(
		widget=forms.Textarea(), max_length=4000)
	birthday = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
	class Meta:
		model = Resume
		fields = [			
			'applicant', 
			'first_name', 
			'last_name',
			'photo', 
			'birthday', 
			'gender',
			'address',
			'email',
			'phone',
			'graduates',
			'experience', 
			'tag',
		]


# form for Recruiter
class RecruiterForm(ModelForm):
	#job_description = forms.CharField(widget=PagedownWidget(show_preview=False))
	class Meta:
		model = Recruiter
		fields = [
			'client',
			'resume',
			'from_upload',
			'job_name',
			'job_description',
		]

class UploadForm(ModelForm):
	class Meta:
		model = Uploadresume
		fields = [
			'applicant',
			'resume',
		]