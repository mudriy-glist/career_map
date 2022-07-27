from django.db import models

# Create your models here.
class Application(models.Model):

    choices = (('VN', 'Voodoo newstarter'),
                ('SSSE', 'Semi-skilled SE'),
                ('SSE', 'Skilled SE'),
                ('VTS', 'Voodoo Temple Supervisor')
    )
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    # email = models.EmailField(max_length=255)
    # job_role = models.CharField(max_length=64)
    # address = models.CharField(max_length=255)
    # city = models.CharField(max_length=50)
    # postcode = models.CharField(max_length=10)
    # date = models.DateField(auto_now_add=True)
    # cv_upload = models.FileField(upload_to=None, max_length=254)

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}",
            f"(Applied on {self.date})",
            f"(Position: {self.job_role})"
        )

