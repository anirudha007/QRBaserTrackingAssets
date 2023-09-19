from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('datatable/', views.InformationTable),
    path('submitotp/', views.dataregister, name="SubmitOtp"),
    path('submit_QR_request/', views.GenQrCode, name="submitQrRequest"),
    path('main_qr_view/', views.mainview, name="HelpView"),
    # path('customer/', views.customer),
    path('register/', views.RegisterPage, name="register"), 
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('code/<str:pk_test>/', views.Landing_apge, name="Landing_apge"),

]