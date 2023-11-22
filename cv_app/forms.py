# cv_app/forms.py

from django import forms
from .models import Education, Experience

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'graduation_year', 'diploma']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'start_year', 'end_year', 'responsibilities', 'reference_letter']
