from django.db import models

class Advertisement(models.Model):
    POSITION_CHOICES = (
        ('1', '728 Leaderboard'),
        ('2', 'Sidebar Ad 1'),
        ('3', 'Sidebar Ad 2'),
        )

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ads', blank=True, null=True)
    url = models.CharField(max_length=255, blank=True)
    code = models.TextField(blank=True)
    position = models.CharField(max_length=1, choices=POSITION_CHOICES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __unicode__(self):
        return self.title
