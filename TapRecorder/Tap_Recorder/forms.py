from django import forms
from .models import Tapes
from django.http import HttpResponseRedirect

class TapeForm(forms.ModelForm):

    class Meta:
        model = Tapes
        fields = ['title','music_by','singer','album','record_file']


    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # Customize the filename here
        filename = self.cleaned_data['record_file'].name
        new_filename = self.cleaned_data['title'] +'.'+ filename.split('.')[-1]
        instance.record_file.name = new_filename

        if commit:
            instance.save()
        pass




