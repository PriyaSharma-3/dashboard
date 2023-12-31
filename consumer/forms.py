from django import forms  
from consumer.models import Consumer

class DateTimeField(forms.DateTimeField):
    input_type = '%d-%m-%Y %H:%M:%S'


class ConsumerForm(forms.ModelForm):  
    class Meta:  
        model = Consumer  
        fields = "__all__"  

    widgets = {
            'Date_Time': DateTimeField(),
    } 