from django.contrib import admin
from .models import *
# Register your models here.

class CategoryInline(admin.TabularInline):
    '''Tabular Inline View for '''
    model = HomeItem
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category','id')
admin.site.register(Category , CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('kinds', 'name', 'id')
admin.site.register(Item , ItemAdmin)

    
class HomeItemAdmin(admin.ModelAdmin):
    list_display = ('pid','name','kind_status','price','model','id')
    fieldsets    = (('Main' ,{'fields': ['pid','name','kind','original', 'price']}),
                        ('off' ,{'fields':[('brand','color','date','image'),('details')]
                    }),
                    )
    list_filter  = ['kind_status' , 'price']
admin.site.register(HomeItem ,HomeItemAdmin)


class LaptopItemAdmin(admin.ModelAdmin):
    list_display = ('kind_status','brand','price','made', 'id')
    fieldsets    = (('Main' ,{'fields': ['kind_status','brand','made', 'price']}),
                        ('off' ,{'fields':[('number', 'dateadd')]
                    }),
                    )
    list_filter  = ['kind_status' , 'price']
admin.site.register(LaptopItem ,LaptopItemAdmin)


class LaptopAdmin(admin.ModelAdmin):
    list_display = ('pid', 'name','model','os_statuse','size_status','id')
    fieldsets    = (('Main' ,{'fields': ['pid','model','os_statuse','size_status']}),
                        ('off' ,{'fields':[('color','original','touchlcd', 'opaquelcd', 'details', 'image'),
                        ('graphic', 'ram', 'cputype', 'hdd')]
                    }),
                    )
    list_filter  = ['size_status' , 'model']
admin.site.register(Laptop ,LaptopAdmin)


class MobileItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'os_status','brand','price', 'model','made', 'id')
    fieldsets    = (('Main' ,{'fields': ['name', 'os_status','brand','made', 'model','price']}),
                        ('off' ,{'fields':[('number', 'dateadd')]
                    }),
                    )
    list_filter  = ['brand' , 'price']
admin.site.register(MobileItem ,MobileItemAdmin)


class MobileAdmin(admin.ModelAdmin):
    list_display = ('pid', 'name','memory','camera','id')
    fieldsets    = (('Main' ,{'fields': ['pid', 'name','memory','camera']}),
                        ('off' ,{'fields':[('color','original','touchlcd', 'lcd', 'details', 'image'),
                        ('cpu', 'ram', 'sizelcd')]
                    }),
                    )
    list_filter  = ['name']
admin.site.register(Mobile ,MobileAdmin)

