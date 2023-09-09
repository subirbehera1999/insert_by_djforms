from django import forms

# functions
def check_for_s(value):
    if value[0]=="s":
        raise forms.ValidationError("name shouldn't start with s")
def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError("it should be  more than 5 character")




# classes
class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_s,check_for_len])
    Sid=forms.IntegerField()
    Semail=forms.EmailField(validators=[check_for_s])