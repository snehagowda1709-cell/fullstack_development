from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import home  # <-- important! This must match the folder structure.

urlpatterns = [
    path('', home, name='home'),  # <-- exact empty path (homepage)
    path('admin/', admin.site.urls),

    # JWT auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # All your other API endpoints...
    path('api/account/', include('accounts.urls')),
    path('api/academics/', include('academics.urls')),
    path('api/assignment/', include('assignment.urls')),
    path('api/org/', include('org.urls')),
    path('api/student/', include('student.urls')),
]
