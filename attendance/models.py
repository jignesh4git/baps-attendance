from django.db import models
from django.contrib.auth.models import User, Permission
# Create your models here.
class  attendance(models.Model):
	name = models.CharField(max_length=250)

class HaribhaktDetail(models.Model):
	HARIBHAKT = 'HB'
	SAMPARK = 'SK'
	SANCHALAK = 'MS'
	NIRIKSHAK = 'NI'
	NIRDESHAK = 'ND'
	BAPS_TYPE = (
			(HARIBHAKT,'Haribhakt'),
			(SAMPARK,'Sampark Karyakar'),
			(SANCHALAK,'Mandal Sanchalak'),
			(NIRIKSHAK,'Nirikshak'),
			(NIRDESHAK,'Nirdeshak'),
		)
	baps_type = models.CharField(max_length=255,choices=BAPS_TYPE,default=HARIBHAKT)
	name = models.CharField(max_length=250,blank=False)
	mobile_no = models.IntegerField(max_length=10,blank=True)
	address = models.CharField(max_length=250,blank=True)
	user = models.OneToOneField(User)
	def __str__(self):
		return '%s (%s)' % (self.name,self.baps_type)
     
class KaryakarGroup(models.Model):
	group_id = models.IntegerField(blank=False)
	karyakar = models.ForeignKey(HaribhaktDetail,related_name='karyakar',on_delete=models.CASCADE)
	haribhakt = models.ManyToManyField(HaribhaktDetail,related_name='haribhakt')
	karyakar_from = models.DateField(auto_created=True)
	karyakar_to = models.DateField(auto_created=True)
	user = models.OneToOneField(User)
	def __str__(self):
		return '%s (%s)' % (self.haribhakt,self.group_id)        