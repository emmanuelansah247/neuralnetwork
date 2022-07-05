from socket import fromshare
from django import forms
from .models import *


class TrainAppForm(forms.ModelForm):
    class Meta:
        model = TrainApp
        fields = (
            "epochs",
            "hiddennodes",
        )
    

class TrainImageForm(forms.ModelForm):
    class Meta:
        model = TrainImage
        fields = (
            'image',
        )

    def customSave(self):        
        lv = self.save(commit=False)
        lv.save("hello")
        # return lv.image.name
        return lv.pk
        