from tkinter.font import names

from django.urls import path
from .views import home_page, contact_page, success, SinglePageView, called_page, uncalled_page, recalled_page, \
    rejected_page, complete_page, LoginPageView, success_logout, LogoutPageView

urlpatterns = [
    path('', home_page, name='home'),
    path('called/', called_page, name='called'),
    path('uncalled/', uncalled_page, name='uncalled'),
    path('recalled/', recalled_page, name='recalled'),
    path('rejected/', rejected_page, name='rejected'),
    path('complete/', complete_page, name='complete'),
    path('form/', contact_page, name='contact'),
    path('success/', success, name='success'),
    path('success-logout/', success_logout, name='success_logout'),
    path('leed/<slug:slug>/', SinglePageView, name='single'),
    path('login/', LoginPageView, name='login'),
    path('logout/', LogoutPageView, name="logout")
]
