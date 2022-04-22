from django import forms
from django.core.mail import send_mail
from Online_Portfolio_and_Blog_With_CMS import settings
from .models import UserProfile, Contact, Resume, Skills, Project


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    phone = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Phone no. . .',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    gender = forms.ChoiceField(required=True,
                               choices=UserProfile.GENDER_CHOICES,
                               widget=forms.RadioSelect(
                                   attrs={"class": "uk-radio"
                                          }
                               )
                               )
    address = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your street address . . .',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    city = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'City . . ',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    zip = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Zip/ Postel code . . .',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    state = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your State . . .',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    country = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your Country . . . ',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    about = forms.CharField(required=False,
                            widget=forms.Textarea(
                                attrs={
                                    "class": "yb-input  uk-textarea uk-border-rounded",
                                    "rows": "5",
                                    "placeholder": "Write about your self . . ."
                                }
                            )
                            )
    introvideo = forms.CharField(required=False, label='Introduction Video',
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'Your introduction video link . . .',
                                            'class': 'uk-input uk-form-large uk-border-rounded',
                                            }))
    website = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Your website link . . . ',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    facebook = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Your facebook link . . .',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    instagram = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Your instagram link . . . ',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    twitter = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Your twitter link . . .',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    linkedin = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Your linkedin link . . . ',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    github = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Your github link . . .',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    youtube = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Your youtube link . . . ',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    whatsapp = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Your whatsapp link . . .',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))

    class Meta:
        model = UserProfile
        fields = ['phone', 'avatar', 'gender', 'address', 'city', 'zip', 'state', 'country', 'about', 'introvideo',
                  'website', 'thumbnail', 'cv', 'facebook', 'instagram', 'twitter', 'linkedin', 'github', 'youtube',
                  'whatsapp']


class EducationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': "uk-width-1-1 uk-form-custom uk-button "
                                                              "uk-button-default uk-border-rounded"})

    issueDate = forms.DateField(label='Start Date', required=True, widget=forms.NumberInput(
        attrs={'type': 'date',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    expirationDate = forms.DateField(label='End Date (or expected)', required=False, widget=forms.NumberInput(
        attrs={'type': 'date',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    name = forms.CharField(label='Degree', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ex: Bachelor of Computer Science',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    organization = forms.CharField(label='School', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'EX: Virtual University of Pakistan',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    description = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={"id": "message",
                                             "class": "yb-input uk-form-large uk-textarea uk-border-rounded",
                                             "rows": "6",
                                             "placeholder": "Write description here . . ."
                                             }
                                  )
                                  )

    class Meta:
        model = Resume
        fields = ['category', 'issueDate', 'expirationDate', 'name', 'organization', 'description']


class ExperienceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': "uk-width-1-1 uk-form-custom uk-button "
                                                              "uk-button-default uk-border-rounded"})

    issueDate = forms.DateField(label='Start Date', required=True, widget=forms.NumberInput(
        attrs={'type': 'date',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    expirationDate = forms.DateField(label='End Date (Leave it empty if you are currently working)', required=False,
                                     widget=forms.NumberInput(
                                         attrs={'type': 'date',
                                                'class': 'uk-input uk-form-large uk-border-rounded',
                                                }))
    name = forms.CharField(label='Title', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ex: Software Engineer',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    organization = forms.CharField(label='Company name', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ex: System Limited',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    description = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={"id": "message",
                                             "class": "yb-input uk-form-large uk-textarea uk-border-rounded",
                                             "rows": "6",
                                             "placeholder": "Write description here . . ."
                                             }
                                  )
                                  )

    class Meta:
        model = Resume
        fields = ['category', 'issueDate', 'expirationDate', 'name', 'organization', 'description']


class CertificationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': "uk-width-1-1 uk-form-custom uk-button "
                                                              "uk-button-default uk-border-rounded"})

    issueDate = forms.DateField(label='Issue Date', required=True, widget=forms.NumberInput(
        attrs={'type': 'date',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    expirationDate = forms.DateField(label='Expiration Date (Leave it empty if credential does not expire)',
                                     required=False, widget=forms.NumberInput(
            attrs={'type': 'date',
                   'class': 'uk-input uk-form-large uk-border-rounded',
                   }))
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ex: Python Programming Specialization',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    organization = forms.CharField(label='Issue organization', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ex: DigiSkills',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    description = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={"id": "message",
                                             "class": "yb-input uk-form-large uk-textarea uk-border-rounded",
                                             "rows": "6",
                                             "placeholder": "Write description here . . ."
                                             }
                                  )
                                  )

    class Meta:
        model = Resume
        fields = ['category', 'issueDate', 'expirationDate', 'name', 'organization', 'description']


class AwardsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': "uk-width-1-1 uk-form-custom uk-button "
                                                              "uk-button-default uk-border-rounded"})

    issueDate = forms.DateField(label='Issue date', required=True, widget=forms.NumberInput(
        attrs={'type': 'date',
               'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    name = forms.CharField(label='Title', required=True, widget=forms.TextInput(
        attrs={'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    organization = forms.CharField(label='Issuer', required=True, widget=forms.TextInput(
        attrs={'class': 'uk-input uk-form-large uk-border-rounded',
               }))
    description = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={
                                          "class": "yb-input uk-form-large uk-textarea uk-form-large uk-border-rounded",
                                          "rows": "6",
                                          "placeholder": "Write description here . . ."
                                      }
                                  )
                                  )

    class Meta:
        model = Resume
        fields = ['category', 'issueDate', 'name', 'organization', 'description']


class SkillsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': "uk-width-1-1 uk-form-custom uk-button "
                                                              "uk-button-default uk-border-rounded"})

    percentage = forms.CharField(required=True,
                                 widget=forms.NumberInput(
                                     attrs={'placeholder': 'EX: 75',
                                            'class': 'uk-input uk-form-large uk-border-rounded',
                                            }))
    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'EX: Docker',
                                       'class': 'uk-input uk-form-large uk-border-rounded',
                                       }))

    class Meta:
        model = Skills
        fields = ['category', 'percentage', 'title']


class KnowledgeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': "uk-width-1-1 uk-form-custom uk-button "
                                                              "uk-button-default uk-border-rounded"})

    percentage = forms.CharField(required=True,
                                 widget=forms.NumberInput(
                                     attrs={'placeholder': 'EX: 75',
                                            'class': 'uk-input uk-form-large uk-border-rounded',
                                            }))
    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'EX: Django Rest Framework',
                                       'class': 'uk-input uk-form-large uk-border-rounded',
                                       }))

    class Meta:
        model = Skills
        fields = ['category', 'percentage', 'title']


class LanguageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': "uk-width-1-1 uk-form-custom uk-button "
                                                              "uk-button-default uk-border-rounded"})

    percentage = forms.CharField(required=True,
                                 widget=forms.NumberInput(
                                     attrs={'placeholder': 'EX: 75',
                                            'class': 'uk-input uk-form-large uk-border-rounded',
                                            }))
    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'EX: English',
                                       'class': 'uk-input uk-form-large uk-border-rounded',
                                       }))

    class Meta:
        model = Skills
        fields = ['category', 'percentage', 'title']


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    category = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Category name. . .',
                                          'class': 'uk-input uk-form-large uk-border-rounded',
                                          }))
    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Project title . . .',
                                       'class': 'uk-input uk-form-large uk-border-rounded',
                                       }))
    link = forms.CharField(required=True,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Project link  . . .',
                                      'class': 'uk-input uk-form-large uk-border-rounded',
                                      }))

    class Meta:
        model = Project
        fields = ['category', 'title', 'web', 'mob', 'link']


class ContactForm(forms.ModelForm):
    message = forms.CharField(required=True,
                              widget=forms.Textarea(
                                  attrs={"id": "message",
                                         "class": "yb-input  uk-textarea uk-border-rounded",
                                         "rows": "7",
                                         "placeholder": "Your message here . . ."
                                         }
                              )
                              )
    phone = forms.DecimalField(required=True,
                               help_text="Please Enter Valid Phone Number!",
                               widget=forms.NumberInput(
                                   attrs={"class": "yb-input uk-input  uk-border-rounded",
                                          "id": "phone",
                                          "type": "tel",
                                          "placeholder": "Your phone here . . ."
                                          }
                               )
                               )
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(
                                 attrs={"class": "yb-input uk-input  uk-border-rounded",
                                        "id": "email",
                                        "placeholder": "Your email here . . ."
                                        }
                             )
                             )
    subject = forms.ChoiceField(required=True,
                                choices=Contact.SUBJECT,
                                widget=forms.RadioSelect(
                                    attrs={"class": "uk-radio"
                                           }
                                )
                                )

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        user_email = self.instance.user.email
        clean_email = self.cleaned_data['email']
        clean_phone = self.cleaned_data['phone']
        clean_subject = self.cleaned_data['subject']
        clean_message = self.cleaned_data['message']
        message = "Phone: " + str(clean_phone) + "\n" + "Email: " + clean_email + "\n" + "body: " + clean_message
        email_from = settings.EMAIL_HOST_USER
        email_to = [user_email]
        send_mail(clean_subject, message, email_from, email_to)

    class Meta:
        model = Contact
        fields = ['user', 'email', 'phone', 'subject', 'message']
