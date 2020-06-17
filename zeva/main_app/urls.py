from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('', views.index, name='home'),
               path('aboutus',views.aboutus,name='aboutus'),
               path('clientdiaries',views.cdiary,name='aboutus'),
               path('FAQs',views.faqs,name='faqs'),
               path('cancelationpolicy',views.cp,name='cancelationpolicy'),
               path('termsandconditions',views.tnc,name='termsandconditions'),
               path('fullscreen/<str:id>',views.fs,name='fullscreen'),
               path('fullscreenclient/<str:id>',views.fsc,name='fullscreenclient'),
               path('display/<str:title>', views.display, name='display')]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

