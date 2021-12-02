from .models import DealershipListing
  

for item in DealershipListing.objects.all():
    id = item.color
    intColor = item.ids
    color = item.intcolor
    item.ids = id
    item.intcolor = intColor
    item.color = color
    item.save()