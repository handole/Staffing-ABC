from django.conf.urls import url
from django.contrib import admin
from easy_pdf.views import PDFTemplateView
from . import views


urlpatterns = [
	url(r'^demo/$', views.DemoPDFView.as_view()),
	url(r'^list_client/$', views.list_client, name='list_client'),
	url(r'^list_recruiter/$', views.list_recruiter, name='list_recruiter'),
	url(r'^list_applicant/$', views.list_applicant, name='list_applicant'),
	url(r'^list_resume/$', views.list_resume, name='list_resume'),
	url(r'^list_upload/$', views.list_upload, name='list_upload'),

	url(r'^add_client/$', views.add_client, name='add_client'),
	url(r'^create_recruiter/$', views.create_recruiter, name='create_recruiter'),
	url(r'^add_applicant/$', views.add_applicant, name='add_applicant'),
	url(r'^upload_resume/$', views.upload_resume, name='upload_resume'),
	url(r'^create_resume/$', views.create_resume, name='create_resume'),
	
	url(r'^(?P<slug>[\w-]+)/$', views.detail_resume, name='detail_resume'),
	url(r'^list_resume/(?P<resume_id>\d+)/pdf/$', views.admin_order_pdf, name='admin_order_pdf'),

	url(r'^list_client/(?P<username>[\w-]+)/delete_client/$', views.delete_client, name='delete_client'),
	url(r'^list_applicant/(?P<username>[\w-]+)/delete_applicant/$', views.delete_applicant, name='delete_applicant'),
	url(r'^list_resume/(?P<applicant>[\w-]+)/delete_resume/$', views.delete_resume, name='delete_resume'),
	url(r'^list_recruiter/(?P<client>[\w-]+)/delete_recruiter/$', views.delete_recruiter, name='delete_recruiter'),
	url(r'^list_recruiter/(?P<client>[\w-]+)/update_recruiter/$', views.update_recruiter, name='update_recruiter'),		
	
	# url(r'^/recruiter/(?P<slug>[­\w]+)/$', views.list_recruiter, name='list_recruiter'),
	# url(r'^(?P<tag_slug>[­\w]+)/$', views.car_list, name='car_list_by_tag'),
	# url(r'^(?P<id>\d+)/(?P<slug>[­\w]+)/$', views.car_detail, name='car_detail'),
]