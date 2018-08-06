from django.contrib import admin

from .models import Contact, Partner, EventStatusSet, PartnerStatusSet, ProductSet, Request, Storage, Transaction

admin.site.register(Contact)
admin.site.register(Transaction)
admin.site.register(Storage)
admin.site.register(Request)
admin.site.register(ProductSet)
admin.site.register(Partner)
admin.site.register(PartnerStatusSet)
admin.site.register(EventStatusSet)
