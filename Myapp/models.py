from django.db import models


class Person(models.Model):

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100, blank=True)
	telephone = models.CharField(max_length=100, blank=True)
	email = models.EmailField(max_length=100, blank=True)

	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

 
class Location (models.Model):
	person = models.ForeignKey(Person,blank=True, null=True)
	region = models.CharField(max_length=50, blank=True)
	sity = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return '%s, %s' % (self.region,self.sity)


class Comment(models.Model):
	person = models.ManyToManyField(Person)
	text = models.TextField(max_length=1000)
	
	def __unicode__(self):
		return unicode(self.id)

