from django.urls import path
from .views import classify_toxic, classify_insult, classify_hate

urlpatterns = [
    path("toxic", classify_toxic),
    path("insult", classify_insult),
    path("hate", classify_hate),
]
