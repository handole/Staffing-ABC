import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from . models import Applicant, Resume, Recruiter, Client, Uploadresume
from . forms import ResumeForm, RecruiterForm, ApplicantForm, ClientForm, UploadForm

from django.views.generic import View, DetailView
from django.contrib.auth import get_user_model
from django.utils.timezone import now

from django.template.loader import render_to_string
import weasyprint

# export to pdf
def resume_pdf(request, resume_id):
	resume = get_object_or_404(Resume, id=resume_id)
	html = render_to_string('resume/pdf.html', {'resume':resume})
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename=\"resume_{}.pdf"'.format(resume.id)
	weasyprint.HTML(string=html).write_pdf(response, 
		stylesheets=[weasyprint.CSS(
			settings.STATIC_ROOT + 'css/pdf.css')])
	return response


# Create your views here.
def index(request):
	pass
	return render(request, 'index.html', {})
	
# for Applicant
@login_required
def add_applicant(request):
	if not request.user.is_active or not request.user.is_superuser:
		raise Http404
	form = ApplicantForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('/list_applicant')

	context = {
		'form':form,
	}

	return render(request, 'form/form_applicant.html', context)

@login_required
def list_applicant(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	applicant = Applicant.objects.all()
	return render(request, 'list_applicant.html', {'applicant':applicant})

@login_required
def detail_applicant(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Applicant)
	return render(request, 'detail_applicant.html', {})

@login_required
def delete_applicant(request, username=None):
	if not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Applicant, username=username)
	instance.delete()
	return redirect('/list_applicant')


# for client
@login_required
def add_client(request):
	if not request.user.is_staff:
		raise Http404
	form = ClientForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('/list_client')

	context = {
		'form':form,
	}

	return render(request, 'form/form_client.html', context)

@login_required
def list_client(request):
	if not request.user.is_active or not request.user.is_superuser:
		raise Http404
	client = Client.objects.all()
	return render(request, 'list_client.html', {'client':client})

@login_required
def detail_client(request, slug=None):
	if not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Client)
	return render(request, 'detail_client.html', {})


@login_required
def delete_client(request, username=None):
	if not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Client, username=username)
	instance.delete()
	return redirect('/list_client')


# for Resume 
@login_required
def create_resume(request):
	if not request.user.is_active or not request.user.is_superuser:
		raise Http404	
	form = ResumeForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('/list_resume')

	context = {
		'form':form,
	}

	return render(request, 'form/form_resume.html', context)

@login_required
def list_resume(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	resume = Resume.objects.all()
	return render(request, 'list_resume.html', {'resume':resume})

@login_required
def detail_resume(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Resume, slug=slug)

	context = {
		'instance':instance,
	}

	return render(request, 'detail_resume.html', context)


@login_required
def delete_resume(request, email=None):
	if not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Resume, email=email)
	instance.delete()
	return redirect('/list_resume')

# upload resume
@login_required
def upload_resume(request):
	if not requets.user.is_active or request.user.is_superuser:
		raise Http404
	form = UploadForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('/list_upload')

	return render(request, 'form/form_upload.html', {'form':form})

@login_required
def list_upload(request):
	upload = Uploadresume.objects.all()
	return render(request, 'list_upload.html', {'upload':upload})


@login_required
def detail_upload(request, slug=None):
	instance = get_object_or_404(Recruiter, slug=slug)
	return render(request, 'detail_upload.html', {'instance':instance})


@login_required
def delete_upload(request, applicant=None):
	if not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Uploadresume, applicant=applicant)
	instance.delete()
	return redirect('/list_upload')


# for Recruiter
@login_required
def create_recruiter(request):
	if not request.user.is_staff:
		raise Http404
	form = RecruiterForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('/detail_recruiter')

	context = {
		'form':form,
	}

	return render(request, 'form/form_recruiter.html', context)

@login_required
def list_recruiter(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404	
	recruiter = Recruiter.objects.all()
	return render(request, 'list_recruiter.html', {'recruiter':recruiter})

@login_required
def detail_recruiter(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Recruiter, slug=slug)
	return render(request, 'detail_recruiter.html', {})

@login_required
def update_recruiter(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Applicant)
	form = RecruiterForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('/list_recruiter')

	context = {
		'title': instance.title,
		'instance': instance,
		'form': form,
	}
	return render(request, 'form/form_recruiter.html', context)

@login_required
def delete_recruiter(request, slug=None):
	if not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Recruiter, slug=slug)
	instance.delete()
	return redirect('/list_recruiter')
