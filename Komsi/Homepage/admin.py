from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import referencemedia
from .models import HalliTyomaa
from .models import Rengashalli
from .models import Rivitaloremontti
from .models import Lumiesteidenasennus
from .models import Ravitalonsahko
from .models import Uudisrakentaminen
from .models import Hietaniemenkadulta
from .models import Item


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(referencemedia)
admin.site.register(HalliTyomaa)
admin.site.register(Rengashalli)
admin.site.register(Rivitaloremontti)
admin.site.register(Lumiesteidenasennus)
admin.site.register(Ravitalonsahko)
admin.site.register(Uudisrakentaminen)
admin.site.register(Hietaniemenkadulta)
admin.site.register(Item, MyModelAdmin)
# Register your models here.
