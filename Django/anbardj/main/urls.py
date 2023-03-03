import statistics
from django.conf import settings
from django.urls import path

from . import views

from django.conf.urls.static import static


urlpatterns = [  

    # Brand URLS
    path('/brand',views.brand,name='brand'),

    path('addbrand/',views.addbrand,name='addbrand'),

    path('silbrand/<int:id>',views.silbrand,name='silbrand'),

    path('silbrand/delete/<int:id>',views.delete,name='delete'),

    path('redaktebrand/<int:id>',views.redaktebrand,name='redaktebrand'),

    path('axtar/',views.axtar,name='axtar'),
    
    path('update/',views.edit,name='edit'),

    

    # Client URLS

    path('clients/',views.client,name='client'),

    path('clients/addclient/',views.addclient,name='addclient'),

    path('silclient/<int:id>',views.silclient,name='silclient'),

    path('silclient/deleteclient/<int:id>',views.deleteclient,name='deleteclient'),

    path('redakteclient/<int:id>',views.redakteclient,name='redakteclient'),

    path('axtar_client/',views.axtar_client,name='axtar_client'),
    
    path('updateclient/',views.editclient,name='editclient'),


    # Order URLS
    
    path('orders/',views.order,name='order'),

    path('orders/addorder/',views.addorder,name='addorder'),

    path('silorder/<int:id>',views.silorder,name='silorder'),

    path('silorder/deleteorder/<int:id>',views.deleteorder,name='deleteorder'),

    path('redakteorder/<int:id>',views.redakteorder,name='redakteorder'),
    
    path('updateorder/',views.editorder,name='editorder'),

    path('orders/tesdiqorder/',views.tesdiqorder,name='tesdiqorder'),

    path('legvetorder/<int:id>',views.legvetorder,name='legvetorder'),
    
    

    

    # Product URLS

    path('products/',views.product,name='product'),

    path('products/addproduct/',views.addproduct,name='addproduct'),

    path('silproduct/<int:id>',views.silproduct,name='silproduct'),

    path('silproduct/deleteproduct/<int:id>',views.deleteproduct,name='deleteproduct'),

    path('redakteproduct/<int:id>',views.redakteproduct,name='redakteproduct'),

    path('axtar_product/',views.axtar_product,name='axtar_product'),
    
    path('updateproduct/',views.editproduct,name='editproduct'),



    # Expenses URLS

    path('expenses/',views.expenses,name='expenses'),

    path('expenses/addexpenses/',views.addexpenses,name='addexpenses'),

    path('silexpenses/<int:id>',views.silexpenses,name='silexpenses'),

    path('silexpenses/deleteexpenses/<int:id>',views.deleteexpenses,name='deleteexpenses'),

    path('redakteexpenses/<int:id>',views.redakteexpenses,name='redakteexpenses'),
    
    path('updateexpenses/',views.editexpenses,name='editexpenses'),


    path('axtar_expenses/',views.axtar_expenses,name='axtar_expenses'),

    # Staff URLS

    path('staff/',views.staff,name='staff'),

    path('staff/addstaff/',views.addstaff,name='addstaff'),

    path('deleteconstaff/<int:id>',views.deleteconstaff,name='deleteconstaff'),

    path('deleteconstaff/deletestaff/<int:id>',views.deletestaff,name='deletestaff'),

    path('editstaff/<int:id>',views.editstaff,name='editstaff'),
    
    path('updatestaff/<int:id>',views.updatestaff,name='updatestaff'),


    # Senedler URLS

    path('senedler/<int:id>',views.senedler,name='senedler'),

    path('staff/senedler/addsenedler/',views.addsenedler,name='addsenedler'),

    path('silsenedler/deletesenedler/<int:id>',views.deletesenedler,name='deletesenedler'),


    # User URLS

    path('profile/',views.profile,name='profile'),
    
    path('profile/updateprofile/<int:id>',views.updateprofile,name='updateprofile'),

    

    path("register", views.register, name="register"),
    path("", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("home/", views.home, name="home")

    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)