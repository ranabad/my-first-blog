from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('cv', views.CV, name='cv'),
    path('cv/Education', views.EducationCV, name='cvEducation'),
    path('cv/Skills', views.SkillsCV, name='cvSkills'),
    path('cv/Workshop', views.WorkshopsCV, name='cvWorkshop'),
    path('cv/Experience', views.ExperienceCV, name='cvExperience'),
    path('cv/<int:pk>/Education/edit/', views.EducationCVUpdatde, name='cv_Education_edit'),
    path('cv/<int:pk>/Education/remove/', views.EducationCVDlt, name='cv_Education_dlt'),
    path('cv/<int:pk>/Workshop/edit/', views.WorkshopsCVUpdatde, name='cv_Workshop_edit'),
    path('cv/<int:pk>/Workshop/remove/', views.WorkshopsCVDlt, name='cv_Workshop_dlt'),
    path('cv/<int:pk>/Skills/edit/', views.SkillsCVUpdatde, name='cv_Skills_edit'),
    path('cv/<int:pk>/Skills/remove/', views.SkillsCVDlt, name='cv_Skills_dlt'),
    path('cv/<int:pk>/Experience/edit/', views.ExperienceCVUpdatde, name='cv_Experience_edit'),
    path('cv/<int:pk>/Experience/remove/', views.ExperienceCVDlt, name='cv_Experience_dlt'),
     path("cv/", views.CV, name="contact"),
]
