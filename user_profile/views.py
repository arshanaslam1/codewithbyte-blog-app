from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView

from accounts.models import User
from user_profile.forms import UserProfileForm, ContactForm, SkillsForm, EducationForm, ExperienceForm, \
    CertificationForm, AwardsForm, ProjectForm
from user_profile.models import UserProfile, Project, Skills, Resume


class ProfileDetail(DetailView):
    model = UserProfile
    template_name = 'user_profile/resume.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        slug = self.kwargs["pk"]
        user = get_object_or_404(User, pk=slug)
        context['obj_user'] = user
        education = user.resume.filter(category='Education')
        context['education'] = education
        experience = user.resume.filter(category='Experience')
        context['experience'] = experience
        certification = user.resume.filter(category='Certification')
        context['certification'] = certification
        skills = user.skills.filter(category='Skills')
        context['skills'] = skills
        knowledge = user.skills.filter(category='Knowledge')
        context['knowledge'] = knowledge
        language = user.skills.filter(category='Language')
        context['language'] = language
        awards = user.resume.filter(category='Awards')
        context['awards'] = awards
        articles = user.posts.published().approved().filter().order_by('-created_on')[:4]
        context['articles'] = articles

        context['contact_form'] = ContactForm()
        return context


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile/profile_update.html'
    success_message = 'You have update profile successfully'

    def form_valid(self, form):
        if self.request.user == form.instance.user_id:
            form.save()
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user.id == profile.user_id:
            return True
        return False


class EducationCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = EducationForm
    template_name = 'user_profile/education-create.html'
    success_message = 'You have add education successfully.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def page_title(self):
        page_title = "Add education"
        return page_title


class EducationUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Resume
    form_class = EducationForm
    template_name = 'user_profile/education-create.html'
    success_message = 'You have update education successfully'

    def form_valid(self, form):
        if self.request.user == form.instance.user:
            form.save()
        return super().form_valid(form)

    def test_func(self):
        resume = self.get_object()
        if self.request.user == resume.user:
            return True
        return False

    def page_title(self):
        page_title = "Update education"
        return page_title


class EducationDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resume
    template_name = 'user_profile/delete.html'
    success_message = 'You have delete education successfully'

    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        resume = self.get_object()
        if self.request.user == resume.user:
            return True
        return False

    def page_title(self):
        page_title = "Delete education"
        return page_title

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.id})


class ExperienceCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ExperienceForm
    template_name = 'user_profile/experience-create.html'
    success_message = 'You have add experience successfully.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def page_title(self):
        page_title = "Add experience"
        return page_title



class ExperienceUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Resume
    form_class = ExperienceForm
    template_name = 'user_profile/experience-create.html'
    success_message = 'You have update experience successfully'

    def form_valid(self, form):
        if self.request.user == form.instance.user:
            form.save()
        return super().form_valid(form)

    def test_func(self):
        resume = self.get_object()
        if self.request.user == resume.user:
            return True
        return False

    def page_title(self):
        page_title = "Update experience"
        return page_title


class ExperienceDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resume
    template_name = 'user_profile/delete.html'
    success_message = 'You have delete experience successfully'

    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        resume = self.get_object()
        if self.request.user == resume.user:
            return True
        return False

    def page_title(self):
        page_title = "Delete experience"
        return page_title

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.id})

class CertificationCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CertificationForm
    template_name = 'user_profile/certification-create.html'
    success_message = 'You have add certification successfully.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def page_title(self):
        page_title = "Add certification"
        return page_title


class CertificationUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Resume
    form_class = CertificationForm
    template_name = 'user_profile/certification-create.html'
    success_message = 'You have update certification successfully'

    def form_valid(self, form):
        if self.request.user == form.instance.user:
            form.save()
        return super().form_valid(form)

    def test_func(self):
        resume = self.get_object()
        if self.request.user == resume.user:
            return True
        return False

    def page_title(self):
        page_title = "Update certification"
        return page_title


class CertificationDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resume
    template_name = 'user_profile/delete.html'
    success_message = 'You have delete certification successfully'

    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        resume = self.get_object()
        if self.request.user == resume.user:
            return True
        return False

    def page_title(self):
        page_title = "Delete Certification"
        return page_title

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.id})


class AwardsCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = AwardsForm
    template_name = 'user_profile/awards-create.html'
    success_message = 'You have add awards successfully.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def page_title(self):
        page_title = "Add Award"
        return page_title


class AwardsUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Resume
    form_class = AwardsForm
    template_name = 'user_profile/awards-create.html'
    success_message = 'You have update awards successfully'

    def form_valid(self, form):
        if self.request.user == form.instance.user:
            form.save()
        return super().form_valid(form)

    def test_func(self):
        resume = self.get_object()
        if self.request.user == resume.user:
            return True
        return False

    def page_title(self):
        page_title = "Update Award"
        return page_title


class AwardsDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resume
    template_name = 'user_profile/delete.html'
    success_message = 'You have update awards successfully'

    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        resume = self.get_object()
        if self.request.user == resume.user:
            return True
        return False

    def page_title(self):
        page_title = "Awards"
        return page_title

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.id})

# Create your views here.
class SkillsCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = SkillsForm
    template_name = 'user_profile/skill-create.html'
    success_message = 'You have add skill successfully.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def page_title(self):
        page_title = "Add skill"
        return page_title


class SkillsUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Skills
    form_class = SkillsForm
    template_name = 'user_profile/skill-create.html'
    success_message = 'You have update skill successfully'

    def form_valid(self, form):
        if self.request.user == form.instance.user_id:
            form.save()
        return super().form_valid(form)

    def test_func(self):
        skills = self.get_object()
        if self.request.user == skills.user:
            return True
        return False

    def page_title(self):
        page_title = "Update skill"
        return page_title



class SkillsDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Skills
    template_name = 'user_profile/delete.html'
    success_message = 'You have delete skill successfully'

    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        skills = self.get_object()
        if self.request.user == skills.user:
            return True
        return False

    def page_title(self):
        page_title = "Delete Skill"
        return page_title

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.id})

# Create your views here.
class KnowledgeCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = SkillsForm
    template_name = 'user_profile/skill-create.html'
    success_message = 'You have add skill successfully.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def page_title(self):
        page_title = "Add knowledge"
        return page_title


class KnowledgeUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Skills
    form_class = SkillsForm
    template_name = 'user_profile/skill-create.html'
    success_message = 'You have update successfully'

    def form_valid(self, form):
        if self.request.user == form.instance.user_id:
            form.save()
        return super().form_valid(form)

    def test_func(self):
        skills = self.get_object()
        if self.request.user == skills.user:
            return True
        return False

    def page_title(self):
        page_title = "Update knowledge"
        return page_title


class KnowledgeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Skills
    template_name = 'user_profile/delete.html'
    success_message = 'You have delete successfully'

    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        skills = self.get_object()
        if self.request.user == skills.user:
            return True
        return False

    def page_title(self):
        page_title = "Delete knowledge"
        return page_title

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.id})


class LanguageCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = SkillsForm
    template_name = 'user_profile/skill-create.html'
    success_message = 'You have add language successfully.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def page_title(self):
        page_title = "Add language"
        return page_title

class LanguageUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Skills
    form_class = SkillsForm
    template_name = 'user_profile/skill-create.html'
    success_message = 'You have update language successfully'

    def form_valid(self, form):
        if self.request.user == form.instance.user_id:
            form.save()
        return super().form_valid(form)

    def test_func(self):
        skills = self.get_object()
        if self.request.user == skills.user:
            return True
        return False

    def page_title(self):
        page_title = "Update language"
        return page_title


class LanguageDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Skills
    template_name ='user_profile/delete.html'
    success_message = 'You have delete language successfully'

    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        skills = self.get_object()
        if self.request.user == skills.user:
            return True
        return False

    def page_title(self):
        page_title = "Delete language"
        return page_title

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.id})


# Create your views here.
class ProjectCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ProjectForm
    template_name = 'user_profile/portfolio-create.html'
    success_message = 'You have add project successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def page_title(self):
        page_title = "Add project"
        return page_title



class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'user_profile/portfolio-create.html'
    success_message = 'You have update project successfully'

    def form_valid(self, form):
        if self.request.user == form.instance.user_id:
            form.save()
        return super().form_valid(form)

    def test_func(self):
        portfolio = self.get_object()
        if self.request.user == portfolio.user:
            return True
        return False

    def page_title(self):
        page_title = "Update project"
        return page_title


class ProjectDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'user_profile/delete.html'
    success_message = 'You have delete project successfully'

    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        portfolio = self.get_object()
        if self.request.user == portfolio.user:
            return True
        return False

    def page_title(self):
        page_title = "Delete project"
        return page_title

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.id})


class JsonableResponseMixin:
    """
    Mixin to add JSON support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        super().form_invalid(form)
        data = {
            'status': "False",
            'error': form.errors
        }
        # return JsonResponse(form.errors, status=400)
        return JsonResponse(data)

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        super().form_valid(form)
        form.send_email()
        data = {
            'status': "True",
            'message': self.success_message,
            'response': "response"
        }
        return JsonResponse(data, status=200)


class ResumeListView(TemplateView):

    template_name = 'user_profile/resume1.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeListView, self).get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context




# Handle Post data from Contact Form
class Contact(JsonableResponseMixin, CreateView):
    form_class = ContactForm
    success_url = "resume"
    template_name = ""
    success_message = "Your message has been successfully sent. I will contact you very soon."