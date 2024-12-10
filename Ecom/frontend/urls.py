from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Product list view
    path('products/', views.product_list_view, name='product_list'),
    
    # Brand list view
    path('brands/', views.brand_list_view, name='brand_list'),
    
    # Category list view
    path('categories/', views.category_list_view, name='category_list'),
    
    # Order list view
    path('orders/', views.order_list_view, name='order_list'),
    
    # Coupon list view
    path('coupons/', views.coupon_list_view, name='coupon_list'),
    
    # Report list view
    path('reports/', views.report_list_view, name='report_list'),
    
    # Settings view (fixed typo)
    path('settings/', views.setting_view, name='settings'),
     
     path('checkout/', views.checkout, name='checkout'),

    # Password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
     path('products/delete/<int:product_id>/', views.delete_product_view, name='delete_product'),
]


