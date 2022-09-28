from django import forms

class TaskAdderForm(forms.Form):
    task_title = forms.CharField(label='Title', required=True, max_length=100)
    task_description = forms.CharField(label='Description', required=True)