# from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm,MyPasswordResetForm,MySetPasswordForm
from django.contrib.auth import views as auth_view
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", views.home),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name="product-detail"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('add-to-cart/', views.add_to_cart,name='add-to-cart'),
    path('cart/', views.show_cart,name='showcart'),
    path('checkout/', views.checkout.as_view(),name='checkout'),
    path('search/',views.search,name='search'),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    # Login authentication paths
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html',), name='password_reset_complete'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
