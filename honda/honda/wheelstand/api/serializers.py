from rest_framework import serializers
from ..models import Models, Trim, ModelsShown, Accessories, Location, Colours, Interiors, Engines, Gallery, \
	Transmission, Features, InteriorColour, ExteriorColour


class TransmissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transmission
		fields = (
		'id', 'name', 'abberviation', 'MSRP', 'fuel_economy', 'selected', 'colour_name', 'colour_name2', 'colour_name3')


class FeaturesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transmission
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
		if obj.url == '':
			pass
		else:
			return obj.url.url


# def get_url_url(self, obj):
#        return obj.url.url


class EnginesSerializer(serializers.ModelSerializer):
	transmission_engines = TransmissionSerializer(read_only=True, many=True)

	class Meta:
		model = Engines
		fields = (
		'id', 'name', 'twoLiter', 'onePointFiveLiter', 'horsepower', 'torque', 'displacement', 'emissionsRating',
		'boreAndStroke', 'compression', 'driveByWire', 'ecoAssis', 'recommendedFueld', 'transmission_engines')
		depth = 1


class InteriorsImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = Interiors
		fields = ('url', 'path', 'filesize')
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

	def get_alternate_md5(self, obj):
		return str(obj.url.size)


class InteriorColourSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')

	class Meta:
		model = InteriorColour
		fields = ('id', 'name', 'url', 'path', 'selected', 'transmission')

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url


class ExteriorColourSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	interior_colour = InteriorColourSerializer(read_only=True, many=True)

	class Meta:
		model = ExteriorColour
		fields = ('id', 'name', 'url', 'colour', 'path', 'selected', 'interior_colour')

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url


# def get_url_url(self, obj):
#        return obj.url.url


class ExteriorColourImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = ExteriorColour
		fields = ('url', 'path', 'filesize')
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

	def get_alternate_md5(self, obj):
		return str(obj.url.size)


class InteriorColourImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = ExteriorColour
		fields = ('url', 'path', 'filesize')
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

	def get_alternate_md5(self, obj):
		return str(obj.url.size)


class TrimNSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	engine = EnginesSerializer(read_only=True)
	colour = ColoursSerializer(read_only=True)
	interiors = InteriorsSerializer(read_only=True, many=True)
	#    model = ModelsSerializer(read_only=True)
	transmissions = TransmissionSerializer(read_only=True, many=True)
	#    features = FeaturesSerializer(read_only=True, many=True)
	exteriorColours = ExteriorColourSerializer(read_only=True, many=True)
	interiorColours = InteriorColourSerializer(read_only=True, many=True)
	base_price = serializers.SerializerMethodField()

	class Meta:
		model = Trim
		#        fields = ('id', 'model', 'name', 'url', 'link', 'heading', 'description', 'features', 'engine', 'colour', 'interiors', 'transmission_type', 'price', 'fuel_city', 'fuel_highway', 'fuel_combined')
		#        fields = ('id', 'name',  'base_price', 'engine', 'transmission', 'features', 'highlights', 'exteriorColours', 'interiorColours', 'url', 'path', 'link', 'heasding', 'description',  'colour', 'interiors',  'model', 'fuel_city', 'fuel_highway', 'fuel_combined', 'colour')

		fields = (
		'id', 'name', 'order', 'base_price', 'engine', 'transmissions', 'features', 'highlights', 'exteriorColours',
		'interiorColours', 'url', 'path', 'link', 'heading', 'description', 'colour', 'interiors')
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}
		depth = 1

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

			#    def get_url_url(self, obj):
			#        return obj.url.url

	def get_base_price(self, obj):
		if obj.base_price is None:
			return ''
		else:
			return str(obj.base_price)


class GallerySerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')

	#    vehicle = ModelsSerializer(read_only=True)

	class Meta:
		model = Gallery
		fields = ('id', 'url', 'path')

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url


# def get_url_url(self, obj):
#        return obj.url.url


class ModelsSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	trims = TrimNSerializer(many=True)
	gallery = GallerySerializer(many=True)
	percentage = serializers.SerializerMethodField()
	price = serializers.SerializerMethodField()

	class Meta:
		model = Models
		#        fields = ('id', 'gallery', 'path', 'trims')
		fields = (
		'id', 'trims', 'name', 'year', 'subhead', 'url', 'path', 'link', 'disclaimer', 'base_price', 'freight_DPI',
		'special_offers', 'line1', 'line2', 'line3', 'line4', 'line5', 'line6', 'line7', 'line8', 'line9', 'line9_city',
		'line10', 'line10_city', 'line11', 'line11_city', 'line12', 'line12_city', 'line13', 'line13_city', 'line14',
		'line14_city', 'line15', 'line15_city', 'line16', 'line16_city', 'percentage', 'price', 'gallery',
		'overview_image_text')
		#        fields = '__all__'
		depth = 1

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

			#    def get_url_url(self, obj):
			#        return obj.url.url

	def get_percentage(self, obj):
		if obj.percentage is None:
			return ''
		else:
			return str(obj.percentage)

	def get_price(self, obj):
		if obj.price is None:
			return ''
		else:
			return str(obj.price)


class ModelsImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = Models
		fields = ('url', 'path', 'filesize')
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

			#    def get_url_url(self, obj):
			#        return obj.url.url

	def get_alternate_md5(self, obj):
		return str(obj.url.size)


class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ('name', 'language', 'description')


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
	transmissions = TransmissionSerializer(read_only=True, many=True)
	#    features = FeaturesSerializer(read_only=True, many=True)
	exteriorColours = ExteriorColourSerializer(read_only=True, many=True)
	interiorColours = InteriorColourSerializer(read_only=True, many=True)
	base_price = serializers.SerializerMethodField()

	class Meta:
		model = Trim
		#        fields = ('id', 'model', 'name', 'url', 'link', 'heading', 'description', 'features', 'engine', 'colour', 'interiors', 'transmission_type', 'price', 'fuel_city', 'fuel_highway', 'fuel_combined')

		fields = (
		'id', 'name', 'order', 'base_price', 'engine', 'transmissions', 'features', 'highlights', 'exteriorColours',
		'interiorColours', 'url', 'path', 'link', 'heading', 'description', 'colour', 'interiors')
		extra_kwargs = {
			'url': {
				'required': False,
			},
			'base_price': {
				'required': False,
			}
		}
		depth = 1

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

			#    def get_url_url(self, obj):
			#        return obj.url.url

	def get_base_price(self, obj):
		if obj.base_price is None:
			return ''
		else:
			return str(obj.base_price)


class TrimImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = Trim
		fields = ('url', 'path', 'filesize')
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

	def get_alternate_md5(self, obj):
		return str(obj.url.size)


class ModelsShownSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	location = LocationSerializer(read_only=True, many=True)
	vehicle = ModelsSerializer(read_only=True)
	trim = TrimSerializer(read_only=True)
	accessory = AccessoriesSerializer(read_only=True, many=True)
	price_override = serializers.SerializerMethodField()

	class Meta:
		model = ModelsShown
		fields = ('id', 'vehicle', 'trim', 'url', 'path', 'link', 'disclaimer', 'wheels', 'drivetrain', 'accessory',
		          'price_override', 'location', 'fuel_city', 'fuel_highway', 'fuel_combined', 'transmissions',
		          'transimissionAbbreviation', 'horsepower_override')
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}

	# depth = 1

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

			#    def get_url_url(self, obj):
			#        return obj.url.url

	def get_price_override(self, obj):
		if obj.price_override is None:
			return ''
		else:
			return str(obj.price_override)


class ModelsShownImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = ModelsShown
		fields = ('url', 'path', 'filesize')
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

	def get_alternate_md5(self, obj):
		if obj.url == '':
			pass
		else:
			return str(obj.url.size)


class GalleryImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = Gallery
		fields = ('url', 'path', 'filesize')
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

	def get_alternate_md5(self, obj):
		return str(obj.url.size)













