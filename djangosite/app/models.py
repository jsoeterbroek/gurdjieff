from django.db import models

class Rechtsgebied(models.Model):

    naam           = models.CharField(max_length=55)

    class Meta:
        verbose_name = "Rechtsgebied"
        verbose_name_plural = "Rechtsgebieden"

    def __str__(self):
        return self.naam

class Uitspraak(models.Model):

    #__tablename__ = "uitspraak"

    registered                  = models.CharField(max_length=25)
    description_identifier      = models.CharField(max_length=25)
    description_format          = models.CharField(max_length=25)
    description_accessrights    = models.CharField(max_length=25)
    description_modified        = models.CharField(max_length=255)
    description_publicatiedatum = models.CharField(max_length=255)
    description_language        = models.CharField(max_length=25)
    #description_rechtsgebied   TODO relationship with Rechtsgebied
    description_uitspraakdatum  = models.CharField(max_length=255)
    description_zaaknummer      = models.CharField(max_length=255)

