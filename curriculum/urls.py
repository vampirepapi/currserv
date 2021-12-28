from django.urls import include, path
from . import views

app_name = 'curriculum'
urlpatterns = [
    path('upsertlanguage/', views

    	.UpsertLanguage.as_view()),
    
    ]