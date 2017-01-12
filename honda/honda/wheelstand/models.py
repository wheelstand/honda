from django.db import models
from django.utils.translation import ugettext_lazy as _
from colorfield.fields import ColorField
import choices
from django.core.files import File
import urllib
import os
from model_utils.fields import MonitorField
from .views import random_string


class Models(models.Model):
    name_en = models.CharField(max_length=255, help_text=_('English'), verbose_name="Name English")
    name_fr = models.CharField(max_length=255, help_text=_('French'), verbose_name="Name French", null=True, blank=True,)
    year = models.CharField(max_length=4, choices=choices.MODEL_YEAR_CHOICES)
    subhead_en = models.TextField(max_length=2550, help_text=_('English'), verbose_name="Subhead English", null=True, blank=True)
    subhead_fr = models.TextField(max_length=2550, help_text=_('French'), verbose_name="Subhead French", null=True, blank=True,)
    url = models.ImageField(upload_to='uploads/models/', blank=True, null=True, verbose_name=_('Hero Image'))
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name="OR Remote URL")
    disclaimer_en = models.TextField(max_length=500, null=True,
                                     blank=True, help_text=_('English'),
                                     verbose_name="Disclaimer English")
    disclaimer_fr = models.TextField(max_length=500, null=True, blank=True,
                                     help_text=_('French'), verbose_name="Disclaimer French")
    base_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    freight_DPI = models.DecimalField(max_digits=8, decimal_places=2,
                                      blank=True, null=True, verbose_name='Freight & DPI')
    special_offers = models.CharField(max_length=255)
    line1_en = models.CharField(max_length=255, blank=True,
                                null=True, help_text=_('English'), verbose_name="Line 1 English")
    line1_fr = models.CharField(max_length=255, blank=True,
                                null=True, help_text=_('French'), verbose_name="Line 1 French")
    line2_en = models.CharField(max_length=255, blank=True,
                                null=True, help_text=_('English'), verbose_name="Line 2 English")
    line2_fr = models.CharField(max_length=255, blank=True,
                                null=True, help_text=_('French'), verbose_name="Line 2 French")
    percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True,)
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)

    class Meta:
        verbose_name_plural = "Models"

    def __unicode__(self):
        return u"%s" % self.name_en

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(Models, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)
    image_thumb.allow_tags = True

    @property
    def name(self):
        return {
            'en': self.name_en,
            'fr': self.name_fr
        }

    @property
    def subhead(self):
        return {
            'en': self.subhead_en,
            'fr': self.subhead_fr
        }

    @property
    def disclaimer(self):
        return {
            'en': self.disclaimer_en,
            'fr': self.disclaimer_fr
        }

    @property
    def line1(self):
        return {
            'en': self.line1_en,
            'fr': self.line1_fr
        }

    @property
    def line2(self):
        return {
            'en': self.line2_en,
            'fr': self.line2_fr
        }


class Gallery(models.Model):
    image = models.ForeignKey(Models, blank=True, null=True, related_name='gallery')
    url = models.ImageField(upload_to='uploads/gallery/', null=True, blank=True, verbose_name=_('Image'))
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)

    class Meta:
        verbose_name_plural = "Galleries"

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(Gallery, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)
    image_thumb.allow_tags = True


class Transmissions(models.Model):
    name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
    name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), null=True, blank=True)    
    abberviation = models.CharField(max_length=255, verbose_name=_('Abbreviation'), null=True, blank=True)
    selected = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Transmissions"

    def __unicode__(self):
        return u"%s" % self.name_en

    @property
    def name(self):
        return {
            'en': self.name_en,
            'fr': self.name_fr
        }  
        

class Trim(models.Model):
    model = models.ForeignKey(Models, blank=True, null=True, related_name='trims')
    name_en = models.CharField(max_length=255, help_text=_('English'), verbose_name="Name English")
    name_fr = models.CharField(max_length=255, help_text=_('French'), verbose_name="Name French", null=True, blank=True)
    url = models.ImageField(upload_to='uploads/interiors/', null=True,  blank=True, verbose_name=_('Image'))
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)
    heading_en = models.CharField(max_length=255, help_text=_('English'), verbose_name="Heading English")
    heading_fr = models.CharField(max_length=255, help_text=_('French'), verbose_name="Heading French", null=True, blank=True)
    description_en = models.TextField(max_length=2000, help_text=_('English'), verbose_name="Description English")
    description_fr = models.TextField(max_length=2000, help_text=_('French'), verbose_name="Description French", null=True, blank=True)
#    features_en = models.TextField(max_length=2000, help_text=_('English'), verbose_name="Features English")
#    features_fr = models.TextField(max_length=2000, help_text=_('French'), verbose_name="Features French", null=True, blank=True)
    engine = models.ForeignKey('Engines', blank=True, null=True)
    colour = models.ForeignKey('Colours', blank=True, null=True)
    interiors = models.ManyToManyField('Interiors', blank=True, )
#    transmission_type = models.CharField(max_length=4, choices=choices.TRANSMISSIONS)
    base_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fuel_city = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fuel_highway = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fuel_combined = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    transmission = models.ManyToManyField('Transmissions', blank=True)
    features = models.ManyToManyField('Features', blank=True, )
    highlights_en = models.CharField(max_length=2000, help_text=_('English'), verbose_name="Highlights English", null=True, blank=True,)
    highlights_fr = models.CharField(max_length=2000, help_text=_('French'), verbose_name="Highlights French", null=True, blank=True,)


    class Meta:
        verbose_name_plural = "Trims"

    def __unicode__(self):
        return u"%s" % self.name_en

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(Trim, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)
    image_thumb.allow_tags = True


    def get_interiors(self):
        return ",".join([str(p) for p in self.interiors.all()])    

    @property
    def name(self):
        return {
            'en': self.name_en,
            'fr': self.name_fr
        }

    @property
    def heading(self):
        return {
            'en': self.heading_en,
            'fr': self.heading_fr
        }

    @property
    def description(self):
        return {
            'en': self.description_en,
            'fr': self.description_fr
        }

    @property
    def highlights(self):
        return {
            'en': self.highlights_en,
            'fr': self.highlights_fr
        }



class ModelsShown(models.Model):
    vehicle = models.ForeignKey(Models, blank=True, null=True)
    trim = models.ForeignKey('Trim', blank=True, null=True)
    wheels_en = models.CharField(max_length=255, help_text=_('English'), null=True, blank=True)
    wheels_fr = models.CharField(max_length=255, help_text=_('French'), null=True, blank=True)
    drivetrain = models.CharField(max_length=4, choices=choices.DRIVETRAINS, null=True, blank=True)
    accessory = models.ManyToManyField('Accessories', blank=True)
    price_override = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    location = models.ManyToManyField('Location', blank=True)
    disclaimer_en = models.TextField(max_length=500, null=True,
                                     blank=True, help_text=_('English'),
                                     verbose_name="Disclaimer English")
    disclaimer_fr = models.TextField(max_length=500, null=True, blank=True,
                                     help_text=_('French'), verbose_name="Disclaimer French")
    url = models.ImageField(upload_to='uploads/modelsshown/', null=True,  blank=True, verbose_name=_('Image'))
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)

    class Meta:
        verbose_name_plural = "Models Shown"

    def __unicode__(self):
        return u"%s" % self.trim

    @property
    def wheels(self):
        return {
            'en': self.wheels_en,
            'fr': self.wheels_fr
        }

    @property
    def disclaimer(self):
        return {
            'en': self.disclaimer_en,
            'fr': self.disclaimer_fr
        }

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(ModelsShown, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)
    image_thumb.allow_tags = True











class Accessories(models.Model):
    name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
    name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), null=True, blank=True)
    base_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Accessories"

    def __unicode__(self):
        return u"%s" % self.name_en

    @property
    def name(self):
        return {
            'en': self.name_en,
            'fr': self.name_fr
        }        


class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'), help_text=_('English'))
    language = models.CharField(max_length=4, choices=choices.LANGUAGE_CHOICES, default='EN')

    class Meta:
        verbose_name_plural = "Locations"

    def __unicode__(self):
        return u"%s" % self.name


class Colours(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'), help_text=_('English'))
    hexcode = ColorField(default='#FFFFFF')

    class Meta:
        verbose_name_plural = "Colours"

    def __unicode__(self):
        return u"%s" % self.name


class Interiors(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    url = models.ImageField(upload_to='uploads/interiors/', null=True, blank=True, verbose_name=_('Image'))
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)

    class Meta:
        verbose_name_plural = "Interiors"

    def __unicode__(self):
        return u"%s" % self.name

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(Interiors, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)
    image_thumb.allow_tags = True

    def get_trims(self):
        return ",".join([str(p) for p in self.trim_set.all()])


class Engines(models.Model):
    name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
    name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), null=True, blank=True)
#    name = models.CharField(max_length=255, null=True, blank=True,)
    hp = models.CharField(max_length=255, null=True, blank=True,)
    torque = models.CharField(max_length=255, null=True, blank=True,)
    displacement = models.CharField(max_length=255, null=True, blank=True,)
    emissions_en = models.CharField(max_length=255, help_text=_('English'), verbose_name=_('Emissions English'), null=True, blank=True)
    emissions_fr = models.CharField(max_length=255, help_text=_('French'), verbose_name=_('Emissions French'), null=True, blank=True)
    bore_and_stroke_en = models.CharField(max_length=255, help_text=_('English'),
                                          verbose_name=_('Bore and Stroke English'), null=True, blank=True)
    bore_and_stroke_fr = models.CharField(max_length=255, help_text=_('French'),
                                          verbose_name=_('Bore and Stroke French'), null=True, blank=True)
    compression = models.CharField(max_length=255, null=True, blank=True)
    driveByWire = models.BooleanField(max_length=255, verbose_name=_('Drive-by-Wire Throttle System'))
    ecoAssis = models.BooleanField(max_length=255)
    recommended_fuel_en = models.CharField(max_length=255, help_text=_('English'),
                                           verbose_name=_('Recommended fuel English'), null=True, blank=True)
    recommended_fuel_fr = models.CharField(max_length=255, help_text=_('French'),
                                           verbose_name=_('Recommended fuel French'), null=True, blank=True)
    twoLiter = models.BooleanField(default=False)
    onePointFiveLiter = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = "Engines"

    def __unicode__(self):
        return u"%s" % self.name_en

    @property
    def name(self):
        return {
            'en': self.name_en,
            'fr': self.name_fr
        }   

    @property
    def emissionsRating(self):
        return {
            'en': self.emissions_en,
            'fr': self.emissions_fr
        }   

    @property
    def boreAndStroke(self):
        return {
            'en': self.bore_and_stroke_en,
            'fr': self.bore_and_stroke_fr
        }           

    @property
    def recommendedFueld(self):
        return {
            'en': self.recommended_fuel_en,
            'fr': self.recommended_fuel_fr
        }   



 
class Features(models.Model):
    name_en = models.CharField(max_length=255, verbose_name=_('Features English'))
    name_fr = models.CharField(max_length=255, verbose_name=_('Features French'))


    class Meta:
        verbose_name_plural = "Features"

    def __unicode__(self):
        return u"%s" % self.name_en

    @property
    def name(self):
        return {
            'en': self.name_en,
            'fr': self.name_fr
        }  


class ExteriorColour(models.Model):
    name = models.CharField(max_length=255, default='')      
    trim_exterior_colour = models.ForeignKey('Trim', blank=True, null=True, related_name='exteriorColours')
    colour = ColorField(default='#FFFFFF') 
    selected = models.BooleanField(default=True)
    url = models.ImageField(upload_to='uploads/trim_exterior_colour/', null=True, blank=True, verbose_name=_('Image'),)
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)

    class Meta:
        verbose_name_plural = "Exterior Colour"

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(ExteriorColour, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)
    image_thumb.allow_tags = True

    def __unicode__(self):
        return u"%s" % self.name

    def related_trim(self, obj):
        return obj.trim_exterior_colour.colour
#    related_trim.short_description = 'Trim'

 
class InteriorColour(models.Model):
    name = models.CharField(max_length=255, default='')    
    trim_interior_colour = models.ForeignKey('Trim', blank=True, null=True, related_name='interiorColours')
    colour = ColorField(default='#FFFFFF') 
    selected = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Interior Colour"


    def __unicode__(self):
        return u"%s" % self.colour



























