from django import forms
from .models import Location
region_choices = Location.objects.values_list('id','region').order_by().distinct()
print region_choices
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
		choices=[], attrs={'id': 'id-sity',})
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

