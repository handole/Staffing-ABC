from django.contrib import admin
from . models import Applicant, Resume, Client, Recruiter, Uploadresume

# Register your models here.
class ApplicantAdmin(admin.ModelAdmin):
	list_display = ['username', 'email']
	list_filter = ['username']
	list_per_page = 10
admin.site.register(Applicant, ApplicantAdmin)

class ResumeAdmin(admin.ModelAdmin):
	list_display = ['applicant', 'first_name', 'last_name', 'birthday', 'gender', 'address', 'email', 'phone', 'tag']
	list_filter = ('tag',)
	search_fields = ['tag']
	prepopulated_fields = {'slug': ('applicant',)}
	list_per_page = 5
admin.site.register(Resume, ResumeAdmin)

class ClientAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'company']
	list_filter = ['username']
	list_per_page = 10
admin.site.register(Client, ClientAdmin)

class RecruiterAdmin(admin.ModelAdmin):
	list_display = ['client', 'resume', 'job_name', 'job_description']
	list_filter = ['job_name']
	prepopulated_fields = {'slug':('job_name',)}
	list_per_page = 10
admin.site.register(Recruiter, RecruiterAdmin)

class UploadAdmin(admin.ModelAdmin):
	list_display = ['applicant', 'resume']
	list_filter = ['applicant']
admin.site.register(Uploadresume, UploadAdmin)
