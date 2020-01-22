from django import forms
from .models import HomeItem

kind_choice = [
    ('home', 'home'),
    ('mobile', 'mobile'),
    ('laptop', 'laptop'),
]

class AdditemForm(forms.Form):
    pid = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class":"form-control col-md-10 btn-primary m-2","id":"addpid","placeholder":" pid (10 char)",
        })
    )

    kind = forms.ChoiceField(widget=forms.Select(attrs={
        "class":"form-control col-md-10 btn-primary m-2","id":"addkind",
        }), choices=kind_choice
    )

    brand = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-10 btn-primary m-2","id":"addbrand"
        }), required=False
    )

    name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-10 btn-primary m-2","id":"addname"
        })
    )

    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class":"form-control col-md-10 btn-primary m-2","id":"addprice"
        }))

    date = forms.DateField(widget=forms.SelectDateWidget(attrs={
        "class":"form-control col-md-10 btn-primary","id":"adddate"
        })
    )

    color = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-10 btn-primary m-2","id":"addcolor"
        }), required=False
    )

    original = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        "class":"form-control col-md-10 btn-primary m-2 novalidate","id":"addoriginal"
        }), required=False
    )

    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class":"form-control col-md-10 btn-primary m-2","id":"addimage"
        }), required=False
    )

    details = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control col-md-10 btn-primary m-2","id":"adddetails"
        }), required=False
    )

    
    class Meta:
        model = HomeItem
        fields = ['pid','kind','brand','name','price','date','color','original','image','details']
