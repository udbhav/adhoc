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
    paid = models.BooleanField()
    active = models.BooleanField(editable=False, default=True)
    paid_views = models.IntegerField(blank=True, default=0)
    views = models.IntegerField(editable=False, default=0)

    def __unicode__(self):
        return self.title

    def get_code(self):
        if self.code:
            html = self.code
        else:
            html = '<a href="%s"><img src="%s" alt="%s" /></a>' % (self.url, self.image.url, self.title)

        return html

    def save(self, *args, **kwargs):
        if self.paid_views < self.views and self.paid:
            self.active = False

        super(Advertisement, self).save(*args, **kwargs)

