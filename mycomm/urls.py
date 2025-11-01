
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('Register/',views.register.as_view(),name="register"),
    path('Login/',views.login.as_view(),name="login"),
    path('Products/',views.productview.as_view(),name="product"),
    path('Orders/',views.ordersview.as_view(),name="order"),
    path('Order/<int:Uid>/',views.UserBasedOrderview.as_view(),name="userbasedorder")
]







if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
