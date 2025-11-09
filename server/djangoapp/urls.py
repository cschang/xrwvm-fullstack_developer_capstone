# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path(route='register', view=views.registration, name='registration'),
    # path for login
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),
        path(route='get_cars', view=views.get_cars, name ='getcars'),
    # path for dealer reviews view
    path(route='get_dealers', view=views.get_dealerships, name ='getDealerships'),
     path('get_dealers/<str:dealer_name>/', views.get_dealerships, name='single_dealership'),
     path('dealer/<str:dealer_id>/', views.get_dealer_details, name='single_dealership'),
     path('reviews/dealer/<str:dealer_id>/', views.get_dealer_reviews, name='single_dealership'),
    # path for add a review view
    path('add_review/', views.add_review, name='add_review'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
