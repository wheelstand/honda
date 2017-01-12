from django.conf.urls import url, include
from rest_framework import routers
from wheelstand.api import views

router = routers.DefaultRouter()
router.register(r'model', views.ModelsViewSet)
router.register(r'trim', views.TrimViewSet)
router.register(r'modelsshown', views.ModelsShownViewSet)
router.register(r'accessories', views.AccessoriesViewSet)
router.register(r'location', views.LocationViewSet)
router.register(r'colours', views.ColoursViewSet)
router.register(r'interiors', views.InteriorsViewSet)
router.register(r'engines', views.EnginesViewSet)
router.register(r'gallery', views.GalleryViewSet)
router.register(r'transmissions', views.TransmissionsViewSet)
router.register(r'features', views.FeaturesViewSet)
router.register(r'interiorcolour', views.InteriorColourViewSet)
router.register(r'exteriorcolour', views.ExteriorColourViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url('^allapi/$', views.AllAPIView.as_view()),
    url('^allapiimages/$', views.AllAPIImagesView.as_view()),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]