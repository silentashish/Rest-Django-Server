from django.contrib import admin

from . import models


admin.site.register(models.UserProfile)
admin.site.register(models.ProfilesFeedItem)
admin.site.register(models.ImageUploadField)
admin.site.register(models.CommentField)
admin.site.register(models.ImageField)
admin.site.register(models.TokenFiled)
