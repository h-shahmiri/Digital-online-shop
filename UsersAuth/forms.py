from django import forms

class AddressForm(forms.Form):

    state = (('Tehran','tehran'),
            ('Soon','soon'))

    city = (('Tehran','tehran'),
            ('Baharestan','baharestan'),
            ('Shemiranat','shemiranat'),
            ('Robat Karim','robat karim'),
            ('Firozkouh','firozkouh'),
            ('Varamin','varamin'),
            ('Eslamshahr','eslamshahr'),
            ('Rey','rey'),
            ('Pishya','pishya'),
            ('Ghods','ghods'),
            ('Malard','Malard'),
            ('Shahriar','shahriar'),
            ('Damavand','damavand'))

    post_code = forms.IntegerField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-8 ml-3 text-white bg-info text-right","id":"reglname","placeholder":"کد پستی"
    }))
    state = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={
        "class":"form-control col-md-8 ml-5 text-dark bg-info text-right","id":"regname"
    }), choices=state)
    city  = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={
        "class":"form-control col-md-8 ml-5 text-dark bg-info text-right","id":"regname"
    }), choices=city)
    address = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-8 ml-3 text-white bg-info text-right","id":"regname","placeholder":"آدرس"
    }))



class ProfileForm(forms.Form):

    phone_numb = forms.IntegerField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-8 text-white bg-info text-right","id":"reglname","placeholder":"شماره تلفن بدون صفر"
    }))
    national_code = forms.IntegerField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-8 ml-2 text-white bg-info text-right","id":"reglname","placeholder":"کد ملی"
    }))
    # xxxxx = forms.IntegerField(widget=forms.TextInput(attrs={
    #     "class":"form-control col-md-8 ml-4 text-white bg-info text-right","id":"reglname","placeholder":"کد پستی"
    # }))



class RegisterForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-12 ml-2 text-right", "id":"firstname", "placeholder":"نام"
    }))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-12 ml-2  text-right", "id":"lastname", "placeholder":"فامیل"
    }))
    # username = forms.CharField(widget=forms.TextInput(attrs={
    #     "class":"form-control col-md-8 ml-5 bg-info", "id":"reglname", "placeholder":"Username"
    # }))
    email    = forms.EmailField(widget=forms.TextInput(attrs={
        "class":"form-control col-md-12 ml-2", "id":"regemail", "placeholder":"Email@gmail.com"
    }))

    def email_valid(self):
        emails = self.cleaned_data['email']
        if "gmail.com" not in emails:
            raise forms.ValidationError("Pls use @gmail.com")
        return emails

    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    #     "class":"form-control col-md-8 ml-5 bg-info","id":"regpass", "placeholder":"password"
    # }))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    #     "class":"form-control col-md-8 ml-5 bg-info","id":"regpass2", "placeholder":"password"
    # }))

    # def pass_valid(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #     if password1 != password2:
    #         raise forms.ValidationError("Passwords is not match")
    #     return password1
