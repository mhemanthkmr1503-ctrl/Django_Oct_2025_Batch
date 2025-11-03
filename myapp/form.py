from django import forms
from .models import Attendance


class LoginForm(forms.Form):
    email_id = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['name', 'student_id', 'course']

    def clean_name(self):
        name = self.cleaned_data['name']
        if(len(name) < 3):
            print(len(name))
            raise forms.ValidationError("Name must be at least 3 characters.")
        return name
    
    def clean_student_id(self):
        student_id = self.cleaned_data['student_id']
        if(len(str(student_id)) != 6):
            print(len(str(student_id)))
            print(len(str(student_id)))
            raise forms.ValidationError("Student_id must be 6 characters.")
        return student_id
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        student_id = cleaned_data.get('student_id')

        if "spam" in name.lower():
            raise forms.ValidationError("No SPAM word present in your Name")
