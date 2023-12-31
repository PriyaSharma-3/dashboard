"""TPWODL_Dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from consumer import views as con
from login import views as log
# from network import views as net

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from consumer import views as con
from login import views as log
# from network import views as net

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index', land.index),
    # path('landbase', land.Landbase),
    path('show', con.show),
    path('index', con.index),
    path('consumer', con.consumer),
    # path('show_NewAccountNumber', con.show_NewAccountNumber),
    # path('show_Username', con.show_Username),
    # path('show_FeederName', con.show_FeederName),
    path('login', log.login),
    path('consumer_edit/<int:Id>', con.consumer_edit),  
    path('update/<int:Id>', con.update),  
    path('consumer_delete/<int:Id>', con.consumer_delete),
    path('consumer_view/<int:Id>', con.consumer_view),
    path('consumer_map/<int:Id>', con.consumer_map),
    path('consumer_excel', con.consumer_excel),
    path('excel_download', con.excel_download),
    path('logout', con.logout),
    path('ajax_calls/show/', con.autocompleteModel),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
