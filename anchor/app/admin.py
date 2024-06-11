from django.contrib import admin

# Register your models here.
from.models import log_in
admin.site.register(log_in)
from.models import Anchor_registration
admin.site.register(Anchor_registration)
from.models import user_registration
admin.site.register(user_registration)
from.models import ufeed
admin.site.register(ufeed)
from.models import PasswordReset
admin.site.register(PasswordReset)
from.models import booking
admin.site.register(booking)
from.models import amountdetails
admin.site.register(amountdetails)
from.models import anchor_gallery
admin.site.register(anchor_gallery)

