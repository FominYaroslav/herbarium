from django.db import models

countries = (
    ("Slovensko", "Slovakia"),
    ("Cesko", "Czechia"),
    ("Rakusko", "Austria"),
    ("Polsko", "Poland"),
)


class Plant(models.Model):
    barcode = models.CharField(max_length=15, primary_key=True)
    taxon = models.CharField(max_length=30)
    locality = models.CharField(max_length=40)
    country = models.CharField(max_length=30, choices=countries, default=countries[0])
    year = models.IntegerField()
    legend_author = models.CharField(max_length=30, blank=True)
    collector = models.CharField(max_length=30, blank=True)
    scan = models.ImageField()

    def __str__(self):
        return self.taxon + ", barcode: " + self.barcode
