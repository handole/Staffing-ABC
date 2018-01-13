from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils import timezone

from markdown_deux import markdown
from django.utils.safestring import mark_safe

User = get_user_model()
# Create your models here.
class Applicant(models.Model):
	user = models.ForeignKey(User)
	username = models.CharField(max_length=50)
	email = models.CharField(max_length=100)

	def __str__(self):
		return self.username


class Resume(models.Model):
	GENDER_CHOICES = (
		('Male', 'MALE'),
		('Female', 'FEMALE'),
	)

	applicant = models.ForeignKey(Applicant, related_name='applicant')
	slug = models.SlugField(unique=True)
	first_name = models.CharField(max_length=50, db_index=True)
	last_name = models.CharField(max_length=50, db_index=True)
	photo = models.ImageField(upload_to='img/applicant/')
	birthday = models.DateField()
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	address = models.TextField()
	email = models.ForeignKey(Applicant, default=1)
	phone = models.CharField(max_length=15)
	graduates = models.TextField()
	experience = models.TextField()
	tag = models.CharField(max_length=255)

	def __str__(self):
		return u"%s %s" % (self.first_name, self.last_name)

	def get_absolute_url(self):
		return reverse('apps:detail_resume', kwargs={"slug": self.slug})

	def get_markdown_experience(self):
		experience = self.experience
		markdown_text = markdown(experience) 
		return mark_safe(markdown_text)

	def get_markdown_graduates(self):
		graduates = self.graduates
		markdown_text = markdown(graduates) 
		return mark_safe(markdown_text)


class Client(models.Model):
	user = models.ForeignKey(User)
	username = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	company = models.CharField(max_length=100)

	def __str__(self):
		return self.username

class Uploadresume(models.Model):
	applicant = models.ForeignKey(Applicant, related_name='applicantupload')
	resume = models.FileField(upload_to='resume')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.applicant


class Recruiter(models.Model):
	client = models.ForeignKey(Client, related_name='client')
	resume = models.ForeignKey(Resume, related_name='resume')
	from_upload = models.ForeignKey(Uploadresume, blank=True, related_name='fromupload')
	job_name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)
	job_description = models.TextField()

	def __str__(self):
		return self.job_name

	# def get_absolute_url(self):
	# 	return reverse('apps:recruiter_detail', args=[self.id, self.slug])


