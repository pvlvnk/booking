from api.views import ListDatesViewSet, ParkingSpaceViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

appname = 'api'
router = DefaultRouter()

router.register(r'spaces', ParkingSpaceViewSet)
router.register(r'spaces/(?P<parkingspace_slug>[-\w]+)/vacant_dates',
                ListDatesViewSet, basename='vacant_dates')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
