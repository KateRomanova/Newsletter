from django.urls import path
from mail.apps import MailConfig
from mail.views import home, NewsletterDeleteView
from mail.views import NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterUpdateView

app_name = MailConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('newsletter/', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter/create', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/<int:pk>/update', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter/<int:pk>/delete/', NewsletterDeleteView.as_view(), name='newsletter_delete'),
]

# from django.urls import reverse_lazy, reverse
