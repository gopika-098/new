"""
URL configuration for service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index',views.index),
    path('about',views.about),
    path('terms',views.terms),
    path('jobs',views.jobs),
    path('job_details',views.job_details),
    path('property-details.html',views.property),
    path('emp_reg',views.anchor_register),
    path('user_reg',views.user_reg),
    path('login',views.loginn),
    path('index1',views.user_index),
    path('12',views.interior),
    path('stage anchoring', views.artist),
    path('wedding', views.electrician),
    path('usproo',views.profil),
    path('contact',views.contact),
    path('gallery',views.gallery),
    path('profile1',views.profile1),
    path('profile2',views.profile2),
    path('profile3',views.profile3),
    path('logout',views.logout),
    # path('12',views.interior),
    path('userpro',views.profile6),
    path('13',views.user_view),
    path('about.html/<user>',views.work),
    path('book/<user>',views.book_anchor),
    path('profile',views.profile),
    path('forgot',views.forgot_password,name="forgot"),
    path('anpro/<user>',views.an_profil),
    path('search',views.location),
    path('user_inbox',views.user_inbox),
    path('feedback',views.audition),
    # path('user_inbox',views.user_inbox),
    # path('pay',views.paymentt),
    path('booking_confirm',views.hello),
    path('user_feed',views.reviewlist),
    path('booking_list',views.bookinglist),
    path('remove_review',views.remove_review),
    path('accept_booking',views.booking_accept),
    path('cancelled_booking',views.your_cancelledbooking),
    path('paycancel',views.cancel),
    path('gallery1/<user>',views.gallery_user),
    path('payment',views.payment1),
    path('success',views.success),
    path('search1',views.search),
    path('location',views.locationfilter),
    path('up_user1',views.up_user1),
    path('us_update2',views.user_update2),
    # path('forget_pwd',views.forget_pwd),




# Admin Dashboard------------------------------------------------------

    path('dash',views.dash),
    path('login-dash',views.login_dash),
    path("register-dash",views.register_dash),
    path("calender",views.calender),
    #path("reject",views.admin),
    path("tables",views.tables),
    path("udash",views.userdtls),
    path("anchordash",views.anchordtls),
    # path('reject1',views.reject),
    path('userfeedback',views.mainfeed),
    path('',views.afeedback),
    # path('dashanchor',views.dash_anchor),
    path('accept/<int:d>',views.accept_request),
    path('change',views.chng_pwd),
    path('chpassword',views.chpass),
    path('pay/<int:id>',views.pay),



#anchor dash

    path('dashanchor',views.profile4),
    path('pro_view',views.pro_anchor),
    path('editpro',views.profile5),
    path('anchoredit',views.anchor_edit),
    path('ad_view_employe',views.ad_view_employe),
    path('ad_request',views.ad_request),
    path('view_user',views.viewuser),
    path('delete_user',views.delete_user),
    path('ad_view_feedback',views.view_feedback),
    path('acceptuser',views.useraccept),
    path('request_user',views.request_us),
    path('rejectuser',views.userreject),
    path('confirm',views.confirm_us),
    path('add_gallery',views.anchor_photo),
    path('view_gallery',views.view_gallery),
    path('amountdetails',views.amountdtls),
    path('delete1',views.remove),
    path('feed_delete',views.feed_delete),



# feedback

    path('feed',views.feedback), #mainpage................................
    path('emp_profeed',views.emp_profeed),
    path('acceptanchor',views.anchoraccept),
    path('rejectanchor',views.anchorreject),
    path('amanage',views.amanageview),


#forgot password


    path('forgot',views.forgot_password,name="forgot"),
    path('reset/<token>',views.reset_password,name='reset_password'),



]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)