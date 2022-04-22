import os
from django.conf import settings
from django.core.mail import send_mail
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Subscribe, Post
from django import forms


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': "uk-width-1-1 uk-form-custom uk-button "
                                                              "uk-button-default uk-border-rounded"})

    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={"id": "message",
                                       "class": "yb-input  uk-textarea uk-border-rounded",
                                       "placeholder": "Write title here . . ."
                                       }
                            )
                            )

    content = SummernoteTextField()
    meta_description = forms.CharField(required=True,
                                       widget=forms.Textarea(
                                           attrs={"id": "message",
                                                  "class": "yb-input  uk-textarea uk-border-rounded",
                                                  "rows": "6",
                                                  "placeholder": "Write meta description here . . ."
                                                  }
                                       )
                                       )
    status = forms.ChoiceField(required=True,
                               choices=Post.STATUS,
                               widget=forms.RadioSelect(
                                   attrs={"class": "uk-radio"
                                          }
                               )
                               )

    class Meta:
        model = Post
        widgets = {
            'content': SummernoteWidget(),
        }
        fields = ('title', 'cover', 'category', 'tags', 'content', 'meta_description', 'status')


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={"id": "i_comment", "class": "uk-textarea uk-border-rounded", "rows": "5",
               "placeholder": "Write Your Comments Here . . ."}))
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "uk-input uk-border-rounded", "id": "i_name", "type": "text", "placeholder": "Your Name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "uk-input uk-border-rounded", "id": "i_name", "type": "email", "placeholder": "Your Email"}))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')


class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "uk-input ",
               "type": "email",
               "placeholder": "Your Email"
               }
    )
    )

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        clean_email = self.cleaned_data['email']
        # message =  "Email:" + clean_email + "body: " + clean_message
        subject = "subscribed arshan aslam blog"
        message = "body: you have successfully subscribed with this email " + clean_email
        email_from = settings.EMAIL_HOST_USER
        email_to = [clean_email]
        send_mail(subject, message, email_from, email_to)

    class Meta:
        model = Subscribe
        fields = 'email',
