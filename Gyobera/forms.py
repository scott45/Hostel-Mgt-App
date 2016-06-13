from django import forms
from Gyobera.models import List, Classification, UserProfile, Booking, Student, MobilePayment
from django.contrib.auth.models import User


class ClassificationForm(forms.ModelForm):
    class Meta:
        model = Classification
        fields = ('name', 'views', 'likes')


class BookForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('Book_No', 'Gender', 'Hostel', 'Room_Number', 'Room_capacity', 'Booked_by')


class MobilePaymentForm(forms.ModelForm):
    class Meta:
        model = MobilePayment
        fields = ('Booked_by', 'Hostel', 'Amount_deposited', 'Mobile_No', 'Pin_Number')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('Names', 'Sex', 'Age', 'Registration_Number', 'Course')


class ListForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Enter the title of the List.")
    Custodian = forms.CharField(max_length=25)
    description = forms.CharField()
    url = forms.URLField(max_length=200, help_text="Enter the URL of the List.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = List

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('classification',)
        # or specify the fields to include (i.e. not include the category field)
        # fields = ('title', 'url', 'views')


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your Names:"
        self.fields['contact_email'].label = "Your Email:"
        self.fields['content'].label = "Message:"


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('About_me', 'picture')
