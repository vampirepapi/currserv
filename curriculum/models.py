from django.db import models

# Create your models here.
class Language(models.Model):
    LanguageId = models.AutoField(primary_key=True)  # It is an auto field.
    LanguageName = models.CharField(max_length=50, blank=True, null=True)
    LanguageNameInEnglish = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.LanguageName)