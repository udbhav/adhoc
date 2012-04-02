import json
from datetime import datetime
from random import choice

from django.http import HttpResponse, HttpResponseBadRequest

from advertising.models import Advertisement

def serve(request):
    if request.POST:
        try:
            slots = json.loads(request.POST['slots'])
        except KeyError:
            return HttpResponseBadRequest("Bad Request")

        ad_response = []

        for slot in slots:
            ads = Advertisement.objects.filter(position=slot).filter(active=True).filter(start_date__lte=datetime.now()).filter(end_date__gte=datetime.now())
            paid_ads = ads.filter(paid=True)

            if ads:
                if paid_ads:
                    ad = choice(paid_ads)
                else:
                    ad = choice(ads)

                ad_response.append({'slot': slot, 'code': ad.get_code()})
                ad.views += 1
                ad.save()
            else:
                ad_response.append({'slot': slot, 'code': ''})

        return HttpResponse(json.dumps(ad_response), mimetype="application/json")
    else:
        return HttpResponseBadRequest("Bad request")
