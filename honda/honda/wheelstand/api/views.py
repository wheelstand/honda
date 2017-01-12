from ..models import Models, Trim, ModelsShown, Accessories, Location, Colours, Interiors, Engines, Gallery, Transmissions, Features, InteriorColour, ExteriorColour
from rest_framework import viewsets
from serializers import ModelsSerializer, TrimSerializer, ModelsShownSerializer, AccessoriesSerializer, LocationSerializer, ColoursSerializer, InteriorsSerializer, EnginesSerializer, InteriorsImageSerializer, TrimImageSerializer, GalleryImageSerializer, ModelsImageSerializer, GallerySerializer, TransmissionsSerializer, FeaturesSerializer, InteriorColourSerializer, ExteriorColourSerializer, ExteriorColourImageSerializer, ModelsShownImageSerializer
from drf_multiple_model.views import MultipleModelAPIView


class ModelsViewSet(viewsets.ModelViewSet):
    queryset = Models.objects.all()
    serializer_class = ModelsSerializer


class TrimViewSet(viewsets.ModelViewSet):
    queryset = Trim.objects.all()
    serializer_class = TrimSerializer


class ModelsShownViewSet(viewsets.ModelViewSet):
    queryset = ModelsShown.objects.all()
    serializer_class = ModelsShownSerializer


class AccessoriesViewSet(viewsets.ModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ColoursViewSet(viewsets.ModelViewSet):
    queryset = Colours.objects.all()
    serializer_class = ColoursSerializer


class InteriorsViewSet(viewsets.ModelViewSet):
    queryset = Interiors.objects.all()
    serializer_class = InteriorsSerializer


class EnginesViewSet(viewsets.ModelViewSet):
    queryset = Engines.objects.all()
    serializer_class = EnginesSerializer


class TransmissionsViewSet(viewsets.ModelViewSet):
    queryset = Transmissions.objects.all()
    serializer_class = TransmissionsSerializer


class FeaturesViewSet(viewsets.ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer



class InteriorColourViewSet(viewsets.ModelViewSet):
    queryset = InteriorColour.objects.all()
    serializer_class = InteriorColourSerializer


class ExteriorColourViewSet(viewsets.ModelViewSet):
    queryset = ExteriorColour.objects.all()
    serializer_class = ExteriorColourSerializer








class AllAPIView(MultipleModelAPIView):
    objectify = True
    queryList = [
        (Models.objects.all(), ModelsSerializer),
        (Trim.objects.all(), TrimSerializer),
        (ModelsShown.objects.all(), ModelsShownSerializer),
        (Accessories.objects.all(), AccessoriesSerializer),
        (Location.objects.all(), LocationSerializer),
        (Colours.objects.all(), ColoursSerializer),
        (Interiors.objects.all(), InteriorsSerializer),
        (Engines.objects.all(), EnginesSerializer),
        (Gallery.objects.all(), GallerySerializer),
        (Transmissions.objects.all(), TransmissionsSerializer),
        (Features.objects.all(), FeaturesSerializer),        
        (ExteriorColour.objects.all(), ExteriorColourSerializer),
        (InteriorColour.objects.all(), InteriorColourSerializer),
    ]


class AllAPIImagesView(MultipleModelAPIView):
    flat = True
    add_model_type = False

    queryList = [
        (Interiors.objects.all(), InteriorsImageSerializer),
        (Trim.objects.all(), TrimImageSerializer),
        (Gallery.objects.all(), GalleryImageSerializer),
        (Models.objects.all(), ModelsImageSerializer),
        (ExteriorColour.objects.all(), ExteriorColourImageSerializer),
        (ModelsShown.objects.all(), ModelsShownImageSerializer),
    ]
