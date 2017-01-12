from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Models, Trim, ModelsShown, Accessories, Location, Colours, Interiors, Engines, Gallery, Transmissions, Features, ExteriorColour, InteriorColour


class GalleryInline(admin.TabularInline):
    model = Gallery
#    list_display = ('name_en', 'base_price', 'freight_DPI')
    verbose_name = "Image"
    verbose_name_plural = "Gallery"
    readonly_fields = ('image_thumb',)


class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ('url', 'link', 'md5')

    def get_model_perms(self, request):
        return {}


class ModelsAdmin(admin.ModelAdmin):
    inlines = [
        GalleryInline,
    ]
    readonly_fields = ('image_thumb',)
    list_display = ('name_en', 'base_price', 'freight_DPI')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr'), 'year', ('subhead_en', 'subhead_fr'), ('disclaimer_en', 'disclaimer_fr')),
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),
        (_('Prices'), {
            'fields': ('base_price', 'freight_DPI'),
        }),
        (_('Special Offers & Promotions'), {
            'fields': (('line1_en', 'line1_fr'), ('line2_en', 'line2_fr'), 'percentage', 'price')
        }),
    )


class ExteriorColourGalleryInline(admin.StackedInline):
    model = ExteriorColour
    readonly_fields = ('image_thumb',)


class InteriorColourGalleryInline(admin.StackedInline):
    model = InteriorColour


class TrimAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'model', 'heading_en', 'engine', 'get_interiors')
    readonly_fields = ('image_thumb',)
    inlines = [ExteriorColourGalleryInline, InteriorColourGalleryInline]    
    filter_horizontal = ('interiors', 'features')    
    fieldsets = (
        (_('General'), {
            'fields': ('model', ('name_en', 'name_fr')),
        }),
        (_('Details'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),
        (_('Highlights'), {
            'fields': (('heading_en', 'heading_fr'), ('description_en', 'description_fr')),
        }),
        (_('Options'), {
            'fields': ('engine',),
        }),

        (_('Fuel'), {
            'fields': ('fuel_city', 'fuel_highway', 'fuel_combined',),
        }),

        (_('Colours'), {
            'fields': ('colour',),
        }),
        (_('Interiors'), {
            'fields': ('interiors',),
        }),
        (_('Transmissions'), {
            'fields': ('transmission', ),
        }),
        (_('Features'), {
            'fields': ( ('highlights_en', 'highlights_fr'),('features', )),
        }),
    )




class ModelsShownAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'trim', 'wheels_en', 'drivetrain')      
    filter_horizontal = ('location', 'accessory') 
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (_('General'), {
            'fields': ('vehicle', 'trim', 'wheels_en', 'wheels_fr', 'drivetrain', ('disclaimer_en', 'disclaimer_fr')),
        }),

        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),

        (_('Selected accessories'), {
            'fields': ('accessory',),
        }),
        (_('Locations'), {
            'fields': ('location',),
        }),
    )


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fr', 'base_price')

    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',), 'base_price'),
        }),
    )


class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'language'),
        }),
    )


class ColoursAdmin(admin.ModelAdmin):
    list_display = ('name', 'hexcode')
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'hexcode'),
        }),
    )


class InteriorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'link', 'get_trims')
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (_('General'), {
            'fields': ('name',)
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),
    )
'''
class InteriorsAdmin(admin.ModelAdmin):
    fields = (('url', 'image_thumb'))
    readonly_fields = ('image_thumb',)
'''


class EnginesAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'hp', 'torque', 'displacement', )
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',)),
        }),
        (_('Details'), {
            'fields': ('hp', 'torque', 'displacement', ('emissions_en', 'emissions_fr',), ('bore_and_stroke_en', 'bore_and_stroke_fr'), 'compression', 'driveByWire', 'ecoAssis', ('recommended_fuel_en', 'recommended_fuel_fr',)),
        }),
    )


class TransmissionsAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'abberviation', 'selected')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',)),
        }),
        (_('Details'), {
            'fields': ('abberviation', 'selected'),
        }),
    )


class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fr')
    fieldsets = (
        (_('General'), {
            'fields': ('name_en', 'name_fr')
        }),
    )


class InteriorColourAdmin(admin.ModelAdmin):
    list_display = ('colour', 'selected')
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'colour', 'selected')
        }),
    )


class ExteriorColourAdmin(admin.ModelAdmin):
    list_display = ('colour', 'selected')
    readonly_fields = ('image_thumb',)    
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'colour', 'selected')
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),        
    )


admin.site.register(Models, ModelsAdmin)
admin.site.register(Trim, TrimAdmin)
admin.site.register(ModelsShown, ModelsShownAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Location, LocationsAdmin)
admin.site.register(Colours, ColoursAdmin)
admin.site.register(Interiors, InteriorsAdmin)
admin.site.register(Engines, EnginesAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Transmissions, TransmissionsAdmin)
admin.site.register(Features, FeaturesAdmin)


