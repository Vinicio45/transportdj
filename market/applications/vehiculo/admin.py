from django.contrib import admin

# Register your models here.
from .models import Transport
from .models import Marca
from .models import Empresa
from .models import Flete
from .models import Heavy_machinery
from .models import Rent
from .models import Sale

admin.site.register(Transport)
admin.site.register(Marca)
admin.site.register(Empresa)
admin.site.register(Flete)
admin.site.register(Heavy_machinery)
admin.site.register(Rent)
admin.site.register(Sale)
