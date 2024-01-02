"""HealthCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path(r'^jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('', include('Users.urls')),
    path('Feedback/', include('Feedback.urls')),
    path('Contact/', include('Contact.urls')),
    path('Category/', include('Category.urls')),
    path('Product/', include('Product.urls')),
    path('Order/',include("Order.urls")),
    path('Cart/',include("Cart.urls")),
    path('Designer/',include("Designer.urls"))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)