from django.contrib import admin
from .models import profession , SocialLinks,AboutMe,Skills,Workingjourney,ServicesColor,Services,username

# Register your models here.

admin.site.register(username)
admin.site.register(profession)
admin.site.register(SocialLinks)
admin.site.register(AboutMe)
admin.site.register(Skills)
admin.site.register(Workingjourney)
admin.site.register(ServicesColor)
admin.site.register(Services)
