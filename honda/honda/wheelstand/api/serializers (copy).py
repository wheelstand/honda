from rest_framework import serializers
from ..models import Models, Trim, ModelsShown, Accessories, Location, Colours, Interiors, Engines, Gallery, Transmissions, Features, InteriorColour, ExteriorColour


class TransmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmissions
        fields = ('id', 'name', 'abberviation', 'selected')


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmissions
        fields = ('id', 'name',)


class ColoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colours
        fields = '__all__'


class InteriorsSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Interiors
        fields = ('id', 'name', 'url', 'path', 'link')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }

    def get_url_url(self, obj):
        return obj.url.url


class EnginesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engines
        fields = ('id', 'name', 'twoLiter', 'onePointFiveLiter', 'hp', 'torque', 'displacement', 'emissionsRating', 'boreAndStroke', 'compression', 'driveByWire', 'ecoAssis', 'recommendedFueld')





class InteriorsImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Interiors
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }

    def get_url_url(self, obj):
        return obj.url.url


class ExteriorColourSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = ExteriorColour
        fields = ('id', 'colour', 'path', 'selected')


    def get_url_url(self, obj):
        return obj.url.url


class ExteriorColourImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = ExteriorColour
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }

    def get_url_url(self, obj):
        return obj.url.url
        

class InteriorColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteriorColour
        fields = ('id', 'colour', 'selected')



class TrimNSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')    
    engine = EnginesSerializer(read_only=True)
    colour = ColoursSerializer(read_only=True)
    interiors = InteriorsSerializer(read_only=True, many=True)
#    model = ModelsSerializer(read_only=True)
    transmission = TransmissionsSerializer(read_only=True, many=True)  
    features = FeaturesSerializer(read_only=True, many=True)
    exteriorColours = ExteriorColourSerializer(read_only=True, many=True)  
    interiorColours = InteriorColourSerializer(read_only=True, many=True)



    class Meta:
        model = Trim
#        fields = ('id', 'model', 'name', 'url', 'link', 'heading', 'description', 'features', 'engine', 'colour', 'interiors', 'transmission_type', 'price', 'fuel_city', 'fuel_highway', 'fuel_combined')
#        fields = ('id', 'name',  'base_price', 'engine', 'transmission', 'features', 'highlights', 'exteriorColours', 'interiorColours', 'url', 'path', 'link', 'heading', 'description',  'colour', 'interiors',  'model', 'fuel_city', 'fuel_highway', 'fuel_combined')

        fields = ('id', 'name',  'base_price', 'engine', 'transmission', 'features', 'highlights', 'exteriorColours', 'interiorColours', 'url', 'path', 'link', 'heading', 'description',  'colour', 'interiors', 'fuel_city', 'fuel_highway', 'fuel_combined')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }        
        depth = 1

    def get_url_url(self, obj):
        return obj.url.url


class GallerySerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

#    vehicle = ModelsSerializer(read_only=True)

    class Meta:
        model = Gallery
        fields = ('id', 'url', 'path')

    def get_url_url(self, obj):
        return obj.url.url


class ModelsSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')
    trims = TrimNSerializer(many=True)
    gallery = GallerySerializer(many=True)

    class Meta:
        model = Models
#        fields = ('id', 'gallery', 'path', 'trims')
        fields = ('id', 'trims', 'name', 'year', 'subhead', 'url', 'path', 'link', 'disclaimer', 'base_price', 'freight_DPI', 'special_offers', 'line1', 'line2', 'percentage', 'price', 'gallery',)        
#        fields = '__all__'
        depth = 1

    def get_url_url(self, obj):
        return obj.url.url




class ModelsImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Models
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }

    def get_url_url(self, obj):
        return obj.url.url





class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = ('id', 'name', 'base_price')
        depth = 1










class TrimSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')    
    engine = EnginesSerializer(read_only=True)
    colour = ColoursSerializer(read_only=True)
    interiors = InteriorsSerializer(read_only=True, many=True)
#    model = ModelsSerializer(read_only=True)
    transmission = TransmissionsSerializer(read_only=True)
    features = FeaturesSerializer(read_only=True, many=True)
    exteriorColours = ExteriorColourSerializer(read_only=True, many=True)  
    interiorColours = InteriorColourSerializer(read_only=True, many=True)



    class Meta:
        model = Trim
#        fields = ('id', 'model', 'name', 'url', 'link', 'heading', 'description', 'features', 'engine', 'colour', 'interiors', 'transmission_type', 'price', 'fuel_city', 'fuel_highway', 'fuel_combined')

        fields = ('id', 'name',  'base_price', 'engine', 'transmission', 'features', 'highlights', 'exteriorColours', 'interiorColours', 'url', 'path', 'link', 'heading', 'description',  'colour', 'interiors',  'fuel_city', 'fuel_highway', 'fuel_combined')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }        
#        depth = 1

    def get_url_url(self, obj):
        return obj.url.url


class TrimImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Trim
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }

    def get_url_url(self, obj):
        return obj.url.url


class ModelsShownSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')    
    location = LocationSerializer(read_only=True, many=True)
    vehicle = ModelsSerializer(read_only=True)
    trim = TrimSerializer(read_only=True)
    accessory = AccessoriesSerializer(read_only=True, many=True)

    class Meta:
        model = ModelsShown
        fields = ('id', 'vehicle', 'trim', 'url', 'path', 'link', 'disclaimer', 'wheels', 'drivetrain', 'accessory', 'price_override', 'location')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }        
#        depth = 1

    def get_url_url(self, obj):
        return obj.url.url


class ModelsShownImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = ModelsShown
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }

    def get_url_url(self, obj):
        return obj.url.url

        

class GalleryImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Gallery
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }

    def get_url_url(self, obj):
        return obj.url.url













