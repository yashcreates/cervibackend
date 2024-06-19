
from django.urls import path
from admin import views   # Import views module

urlpatterns = [
    path('register', views.RegisterView),  # Assuming 'register_view' is your function-based view
    path('get-data', views.GetDataView),
    path('verify-doctor', views.VerifyDoctor),
    path('disable-user', views.DisableUserView),
    path('enable-user', views.EnableUserView),
    path('add-model', views.AddModelView),
    path('set-active-model', views.SetActiveModelView),
]
