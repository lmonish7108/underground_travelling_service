from django.contrib import admin
from accounts import models as act_models

admin.site.register(act_models.UserProfile)
admin.site.register(act_models.MetroCard)
admin.site.register(act_models.SocialProfile)
admin.site.register(act_models.GoogleRequest)
