from django.urls import path
from . import views

urlpatterns = [
    path('', views.ResumeListView.as_view(), name='resumesd'),
    path('<int:pk>/', views.ProfileDetail.as_view(), name='profile'),
    path('<int:pk>/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('education/add/', views.EducationCreate.as_view(), name='education-create'),
    path('education/<int:pk>/update/', views.EducationUpdateView.as_view(), name='education-update'),
    path('education/<int:pk>/delete/', views.EducationDelete.as_view(), name='education-delete'),
    path('experience/add/', views.ExperienceCreate.as_view(), name='experience-create'),
    path('experience/<int:pk>/update/', views.ExperienceUpdateView.as_view(), name='experience-update'),
    path('experience/<int:pk>/delete/', views.ExperienceDelete.as_view(), name='experience-delete'),
    path('certification/add/', views.CertificationCreate.as_view(), name='certification-create'),
    path('certification/<int:pk>/update/', views.CertificationUpdateView.as_view(), name='certification-update'),
    path('certification/<int:pk>/delete/', views.CertificationDelete.as_view(), name='certification-delete'),
    path('awards/add/', views.AwardsCreate.as_view(), name='awards-create'),
    path('awards/<int:pk>/update/', views.AwardsUpdateView.as_view(), name='awards-update'),
    path('awards/<int:pk>/delete/', views.AwardsDelete.as_view(), name='awards-delete'),
    path('skill/add/', views.SkillsCreate.as_view(), name='skill-create'),
    path('skill/<int:pk>/update/', views.SkillsUpdateView.as_view(), name='skill-update'),
    path('skill/<int:pk>/delete/', views.SkillsDelete.as_view(), name='skill-delete'),
    path('knowledge/add/', views.KnowledgeCreate.as_view(), name='knowledge-create'),
    path('knowledge/<int:pk>/update/', views.KnowledgeUpdateView.as_view(), name='knowledge-update'),
    path('knowledge/<int:pk>/delete/', views.KnowledgeDelete.as_view(), name='knowledge-delete'),
    path('language/add/', views.LanguageCreate.as_view(), name='language-create'),
    path('language/<int:pk>/update/', views.LanguageUpdateView.as_view(), name='language-update'),
    path('language/<int:pk>/delete/', views.LanguageDelete.as_view(), name='language-delete'),
    path('project/add/', views.ProjectCreate.as_view(), name='project-create'),
    path('project/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project-delete'),
    path('contact/', views.Contact.as_view(), name='contact'),
]