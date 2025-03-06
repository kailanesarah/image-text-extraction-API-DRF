from django.urls import path
from . import views

urlpatterns = [
    path('extract_text/', views.ExtractTextImageView.as_view(), name="extract_text"),
    path('translate_text/', views.TranslateTextImageView.as_view(), name="translate_text"),
]
