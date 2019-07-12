from django import forms

from .models import Complaint,Compuser


class ComplaintForm(forms.ModelForm):
	class Meta:
		model = Complaint
		fields = ('name', 'designation', 'user', 'office_address', 'Crime','description', 'proof' )
class SignupForm(forms.ModelForm):
	class Meta:
		model = Compuser
		fields = ('first_name', 'last_name' ,'username','address', 'identity_card_type', 'identity_card_no', 'email' ,'password' )