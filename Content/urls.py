from django.conf.urls   import url
from django.urls        import path
from .import views
from .views import ItemViewset
from django.views.generic import TemplateView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('itemlist' , ItemViewset)

urlpatterns = [
    # path('additem'  , views.Additem , name='additem'),
    url(r'^$' ,        TemplateView.as_view(template_name = 'index.html'), name = 'home'),
    path('mobilecat' , views.MobileCat.as_view()  , name='mobilecat'),
    path('laptopcat' , views.LaptopCat.as_view()  , name='laptopcat'),
    path('homecat'   , views.HomeCat.as_view()    , name='homecat'),
    path('itemview'	   , views.ListUser.as_view()),
    path('itemlistview', views.ListApiUser.as_view()),
]

urlpatterns += router.urls