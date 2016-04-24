from django import forms
from .models import Location
import json

region_choices = (('moscow', 'Moscow'),('london', 'London'))

sity_choices = (('moscow', 'Moscow'),('london', 'London'))

# region_choices = [region for region in Location.objects.only('region')]
# region_choices = Answer.objects.filter(id__in=[answer.id for answer in
#             answer_set.answers.all()])

class CommentForm(forms.Form):
	first_name = forms.CharField(max_length=100, required=True)
	last_name = forms.CharField(max_length=100, required=True)
	middle_name = forms.CharField(max_length=100, required=False)
	telephone = forms.CharField(max_length=100, required=False)
	email = forms.EmailField(max_length=100, required=False, widget=forms.EmailInput(attrs={'id': 'email-text'}))
	region = forms.CharField(required=False, widget=forms.Select(
		choices=region_choices, attrs={'id': 'id-region',})
	)

	sity = forms.CharField(required=False, widget=forms.Select(
		choices=sity_choices, attrs={'id': 'id-sity',})
	)

	def clean_first_name(self):
		first_name = self.cleaned_data.get('first_name')
		return first_name

	def clean_last_name(self):
		last_name = self.cleaned_data.get('last_name')
		return last_name

	def clean_middle_name(self):
		middle_name = self.cleaned_data.get('middle_name')
		return middle_name

	def clean_telephone(self):
		telephone = self.cleaned_data.get('telephone')
		return telephone

	def clean_email(self):
		email = self.cleaned_data.get('email')
		# email_base, provider = email.split("@")
		# domain, extension = provider.split('.')
		return email

	def clean_region(self):
		region = self.cleaned_data.get('region')
		return region

	def clean_sity(self):
		sity = self.cleaned_data.get('sity')
		return sity






# class CommentForm(forms.Form):
# 	fist_name = forms.CharField(max_length=100)
# 	last_name = forms.CharField(max_length=100)
# 	middle_name = forms.CharField(max_length=100, required=False)
# 	telephone = forms.CharField(max_length=100, required=False)
# 	email = forms.EmailField(max_length=100, required=False)
# 	region = forms.ChoiceField(required=False,)
# 	sity = forms.CharField(required=False,)
							

# def __init__(self, number, *args, **kwargs):
# 	super(CommentForm, self).__init__(*args, **kwargs)
# 	self.region_list = json.dumps([region for region in Location.objects.filter(id='select_region')])
# 	self.sity_list = json.dumps([sity for sity in Location.sity.objects.filter(id='select_sity')])

# 	self.widget_region = forms.ChoiceField(attrs={'class': 'select',
# 										'data-source': self.region_list,
# 										})
# 	self.widget_sity = forms.ChoiceField(attrs={'class': 'select',
# 										'data-source': self.sity_list,
# 										})

# 	self.fields['region'] = forms.ChoiceField(required=True, widget=self.widget_region,)
# 	self.fields['sity'] = forms.ChoiceField(required=True, widget=self.widget_sity,)