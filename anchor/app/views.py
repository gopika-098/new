from django.shortcuts import render,redirect
from django.http import  HttpResponse
from.models import Anchor_registration
from.models import user_registration
from.models import log_in
from.models import ufeed
from.models import booking
from.models import payment
from.models import *
from.models import anchor_gallery
from.models import PasswordReset
from.models import amountdetails
from django.contrib import messages
from django.utils.crypto import get_random_string
from  django.core.mail import send_mail
import razorpay
# Create your views here.


def index(re):
    return render(re,'index.html')

def about(re):
    return render(re,'about.html')

def contact(re):
    return render(re,'contact.html')

def jobs(re):
    return render(re,'jobs.html')

def job_details(re):
    return render(re,'job-details.html')

def property(re):
    return render(re,'property-details.html')

def terms(re):
    return render(re,'terms.html')

def user_index(re):
    return render(re,'index1.html')

# def anchors(re):
#     d=Anchor_registration.objects.all()
#     return render(re,'anchor.html',{'r':d})

def artist(re):
    return render(re,'artist.html')

def electrician(re):
    return render(re,'Photographers.html')

def profil(re):
    if 'u_id' in re.session:
        z=re.session['u_id']
        d=user_registration.objects.filter(username=z)
        return render(re,'user_profile.html',{'r':d})
    else:
        return HttpResponse('your not registered')

def logout(re):
    if 'id' in re.session:
        re.session.flush()
        return render(re, 'index1.html')
    else:
        return render(re,'index.html')




def anchor_register(re):
    if re.method=='POST':
        a=re.POST['first_name']
        b=re.POST['last_name']
        c=re.POST['address']
        d=re.POST['phone_no']
        e=re.POST['email']
        f=re.POST['gender']
        g=re.POST['location']
        # j=re.FILES['pro_pic']
        h=re.POST['username']
        i=re.POST['password']
        k=re.FILES['profil']
        # l=re.FILES['biodata']
        d1 = Anchor_registration.objects.filter(username=h)
        d2 = Anchor_registration.objects.filter(email=e)
        if list(d1) == []:
            if list(d2) == []:
                x=Anchor_registration.objects.create(first_name=a,last_name=b,address=c,phone_no=d,email=e,gender=f,location=g,profile=k,username=h,action='pending')
                x.save()
                y=log_in.objects.create(username=h,password=i,status=1)
                y.save()
            else:
                return HttpResponse("<script>alert('email already exists');window.location='emp_reg'</script>")
        else:
            return HttpResponse("<script>alert('username already exists');window.location='emp_reg'</script>")

        return HttpResponse("<script>alert('Registered Successfully');window.location='login'</script>")
    else:
        return render(re,'anchor_reg.html')


def user_reg(re):
    if re.method == 'POST':
        a = re.POST['n1']
        b = re.POST['n2']
        c = re.POST['n3']
        d = re.POST['n4']
        e = re.POST['n5']
        f = re.POST['n6']
        g = re.POST['n7']
        # k= re.FILES['n8']
        d1 = user_registration.objects.filter(username=f)
        d2 = user_registration.objects.filter(email=c)
        if list(d1) == []:
            if list(d2) == []:
                x = user_registration.objects.create(name=a, address=b, email=c, location=d,phone_no=e, username=f,password=g)
                x.save()
                y = log_in.objects.create(username=f, password=g, status=2)
                y.save()
            else:
                return HttpResponse("<script>alert('email already exists');window.location='user_reg'</script>")
        else:
            return HttpResponse("<script>alert('username already exists');window.location='user_reg'</script>")

        return HttpResponse("<script>alert('Registered Successfully');window.location='login'</script>")
    else:
        return render(re, "user-reg.html")
    #     x = user_registration.objects.create(name=a, address=b, email=c, location=d,phone_no=e, username=f,password=g,photo=k)
    #     x.save()
    #     y = log_in.objects.create(username=f, password=g, status=2)
    #     y.save()
    #     return render(re,'login.html')
    # else:
    #     return render(re, "user_registration.html")

def profile1(re):
    if 'a_id' in re.session:
        return redirect(ad_view_employe)
    else:
        return render(re,'index_login.html')


def profile2(re):
    if'u_id' in re.session:
        y=re.session['u_id']
        d=user_registration.objects.filter(username=y)
        return render(re,'index1.html',{'r':d})
    else:
        return render(re,'index_login.html')


def profile3(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        d=Anchor_registration.objects.filter(username=z)
        return render(re,'anchor_profilevieww.html',{'r':d})
    else:
        return render(re,'index_login.html')


def loginn(re):
    if re.method=='POST':
        u=re.POST['n1']
        p=re.POST['n2']
        try:
            d=log_in.objects.get(username=u)
            print('hi')
            if d.password==p:
                if d.status=='0':
                    re.session['a_id']=u
                    return redirect(profile1)
                elif d.status=='1':
                    x = Anchor_registration.objects.get(username=u)
                    if x.action=='confirm':
                        re.session['e_id']=u
                        return redirect(profile4)
                    else:
                        return render(re, 'index_login.html', {'message1': 'login failed,request is processing...'})
                    # else:
                    # messages.info(re,'wait')
                    # return HttpResponse("wait")
                    # return redirect(profile4)
                elif d.status=='2':
                    re.session['u_id']=u
                    return redirect(profile2)
            else:
                return HttpResponse("<script>alert('incorrect username');window.location='login'</script>")
        except Exception:
            return HttpResponse("<script>alert('incorrect password');window.location='login'</script>")
    else:
         return render(re,'index_login.html')


def gallery(re):
        return render(re, 'gallery.html')

from django.shortcuts import render


def dash(re):
    return render(re,'admin.html')

def login_dash(re):
    return render(re,"login-admin.html")

def register_dash(re):
    return render(re,"register-admin.html")

def calender(re):
    return render(re,'calendar.html')

def admin(re):
    return render(re,'admin.html')

def tables(re):
    return render(re,"tables.html")

def interior(re):
    d=Anchor_registration.objects.all()
    return render(re,'services1.html',{'r':d})


def userdtls(re):
    d=user_registration.objects.all()
    return render(re,'userdetails.html',{'r':d})

def anchordtls(re):
    d=Anchor_registration.objects.all()
    return render(re,'anchordetails.html',{'r':d})
# def reject(re):
#     if re.method == 'POST':
#         a= re.POST['n1']
#         b=re.POST['action']
#         print(b)
#         if b== 'reject':
#             d=Anchor_registration.objects.filter(name=a)
#             d.delete()
#             return render(re,'admin.html')
#         elif b== 'accept':
#             d=Anchor_registration.objects.filter(name=a)
#             d.update(action='conform',status='1')
#             d1=Anchor_registration.objects.all()
#
#             return render(re,'admin.html',{'r':d1})
#         else:
#             return HttpResponse("error")


def anchors(request):    # userpage accepted books
    if request.method == "GET":
         # s = request.POST['n1']
        data = Anchor_registration.objects.filter(action="Confirm")
        return render(request,'anchor.html',{'r':data})
    else:
        return render(request,'anchor.html')

# Create your views here.

def feedback(request):     #  User feedback
    if 'u_id' in request.session:
        y=request.session['u_id']
        g=user_registration.objects.filter(username=y)
        if request.method == "POST":
            a = request.POST['n1']
            d = request.POST['n4']
            b = request.POST['n2']
            c = request.POST['n3']
            x = ufeed.objects.create(username=a,anchorname=d,email=b,feed=c)
            y=Anchor_registration.objects.filter(username=a)
            # c = entry.objects.all()
            # c.update(select='avaliable')
            return HttpResponse("<script>alert('Thanks for your feedback');window.location='feed'</script>")
        return render(request,'feedba.html',{'r1':g})
        # else:
        #     return render(request,'feedba.html')


def mainfeed(re):
    d = ufeed.objects.all()
    return render(re,'userfeedback.html',{'r': d})

def anchorfeed(re):
    d = afeed.objects.all()
    return render(re,'anchorfeedback.html',{'r': d})

def afeedback(request):     #  User feedback
    if request.method == "POST":
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        data = afeed.objects.create(wname=a,bname=b,feed=c)
        data.save()
        # c = entry.objects.all()
        # c.update(select='avaliable')
        return HttpResponse("<script>alert('Thanks for your feedback');window.location='feed'</script>")
    else:
        return render(request,'anchor_profilevieww.html')

def anchoraccept(re):
    if re.method == "POST":
        r = re.POST['n1']
        d = Anchor_registration.objects.filter(id=r)
        d.update(action="confirm")
        d1=log_in.objects.filter(username=r)
        d1.update(action="confirm")
        return HttpResponse("<script>alert('Accepted');window.location='ad_request'</script>")
    else:
        return HttpResponse(re,'ad_request.html')

def autnew(re):  #author request
    if re.method == "GET":
        data=Anchor_registration.objects.all()
        return render(re,'ad_request.html',{'r':data})
    else:
        return render(re,'ad_request.html')

def anchorreject(re):
    if re.method=="POST":
        r = re.POST['n1']
        d = Anchor_registration.objects.filter(id=r)
        d.delete()
        return HttpResponse("<script>alert('rejected');window.location='ad_request'</script>")
    else:
        return render(re,'ad_request.html')

# def book_anchor(re):
#     if 'u_id' in re.session:
#         z = re.session['u_id']
#         if re.method=='POST':
#             a=re.POST['NAME']
#             b=re.POST['PHONE']
#             c=re.POST['ADDRESS']
#             d=re.POST['EMAIL']
#             # e=re.POST['DATE']
#             f=re.POST['ANCHOR']
#             x=booking.objects.create(NAME=a,PHONE=b,ADDRESS=c,EMAIL=d,ANCHOR=f)
#             return HttpResponse('payment')
#         # else:
#         return render(re,'book_anchor.html')





def amanageview(re):
    d = Anchor_registration.objects.all()
    return render(re, 'anchordetailsview.html', {'r': d})

def profile4(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        d=Anchor_registration.objects.filter(username=z)
        return render(re,'anchor_profilevieww.html',{'r':d})
    else:
        return HttpResponse("<script>alert('your registration is not yet completed');windows.location='login' </script>")

def pro_anchor(re):
    return render(re,'anchor_profilevieww.html')


def anchor_view(re):
    if re.method=='POST':
        return redirect(profile4)



def profile5(re):
    if 'e_id' in re.session:
        z = re.session['e_id']
        d = Anchor_registration.objects.filter(username=z)
        return render(re,'anchor_profileedit.html',{'r':d})
    return redirect(anchor_edit)


def anchor_edit(re):
    if 'e_id' in re.session:
        z = re.session['e_id']
        g =Anchor_registration.objects.filter(username=z)
        if re.method=='POST':
            a =re.POST['name']
            w= re.POST['last_name']
            # b = re.POST['address']
            c = re.POST['email']
            d = re.POST['phone_no']
            e = re.POST['gender']
            # f = re.POST['account_number']
            # g = re.POST['experience']
            # h = re.POST['previous_work']
            i = re.POST['location']
            # j = re.POST['username']
            y=Anchor_registration.objects.filter(username=z)
            print(y)
            y.update(username=z,first_name=a,last_name=w,email=c,phone_no=d,gender=e,location=i)
            return HttpResponse("<script>alert('updated');window.location='editpro'</script>")
        else:
            return render(re,'anchor_profileedit.html')




# def ser(re):
#     return render(re,'services1.html')
# def userpro(re):
#     d=user_registration.objects.all()
#     return render(re,'user-profil.html',{'r':d})

# user profile view
def profile6(re):
    if 'u_id' in re.session:
        z=re.session['u_id']
        d=user_registration.objects.filter(username=z)
        return render(re,'user-profil.html',{'r':d})
    else:
        return render(re,'index_login.html')

def user_view(re):
    if re.method=='POST':
        return redirect(profile6)


# def forgot_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         try:
#             user = reg.objects.get(email=email)
#         except:
#             messages.info(request, "Email id not registered")
#             return redirect(forgot_password)
#         # Generate and save a unique token
#         token = get_random_string(length=4)
#         PasswordReset.objects.create(user=user, token=token)
#
#         # Send email with reset link
#         reset_link = f'http://127.0.0.1:8000/reset/{token}'
#
#         try:
#             send_mail('Reset Your Passwor\d', f'Click the link to reset your password: {reset_link}',
#                       'settings.EMAIL_HOST_USER', [email], fail_silently=False)
#             return render(request, 'emailsent.html')
#         except:
#             messages.info(request, "Network connection failed")
#             return redirect(forgot_password)
#
#     return render(request, 'password_reset_sent.html')



def ad_view_employe(re):
    d=Anchor_registration.objects.filter(action='confirm')
    return render(re,'ad_view_anchor.html',{'r':d})

def remove(re):
    if re.method=='POST':
        z=re.POST['uname']
        d=Anchor_registration.objects.filter(username=z)
        x=log_in.objects.filter(username=z)
        x.delete()
        d.delete()
        return redirect(ad_view_employe)

def accept_request(re,d):
    Anchor_registration.objects.filter(pk=d).update(status=1)
    return redirect(ad_request)



def ad_request(request):
    d=Anchor_registration.objects.filter(action='pending')
    return render(request,'ad_request.html',{'r':d})

def work(re,user):
    d = Anchor_registration.objects.filter(username=user)
    return render(re, 'work_view.html', {'r': d})

def chng_pwd(re):
    if re.method=='POST':
        u=re.POST['n1']
        o=re.POST['n2']
        p=re.POST['n3']
        c=re.POST['n4']
        try:
            b=log_in.objects.filter(username=u)
            if o!=p & p==c:
                b.update(password=c)
                return render(re,'index_login.html')
        except Exception:
            return HttpResponse('please write another password')
    else:
        return render(re,'change_password.html')


def book(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        d=booking.objects.filter(employee_name=z,action='pending')
        return render(re,'book_req.html',{'r':d})
def book_accept(re):
    if re.method == "POST":
        if 'e_id' in re.session:
            r = re.POST['n1']
            d = booking.objects.filter(id=r)
            print(d)
            d.update(action="Confirm")
            return HttpResponse("<script>alert('Accepted');window.location='book'</script>")
    else:
        return render(re, 'emp_req.html')

def book_reject(request):      # rejecting book
    if request.method == "POST":
        r = request.POST['n1']
        d = Anchor_registration.objects.filter(id=r)
        d.delete()
        return HttpResponse("<script>alert('Rejected');window.location='booking_list'</script>")
    else:
        return render(request, 'book_req.html')

def booking_list(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        x=booking.objects.filter(ANCHOR=z,action='confirm')
        return render(re,'bookings.html',{'r':x})

def searchh(request):     #searching author
    if request.method == "POST":
        s = request.POST['n1']
        data = Anchor_registration.objects.filter(location=s)
        if list(data) == []:
            return HttpResponse("<script>alert('Author does not Exists');window.location='photographer'</script>")
        else:
            return render(request,'searchauth.html',{'s':data})
    else:
        return HttpResponse("<script>alert('No results found');window.location='photographer'</script>")

def viewuser(re):
    d = user_registration.objects.all()
    return render(re, 'ad_view_user.html', {'r': d})
def delete_user(re):
    if re.method=='POST':
        z=re.POST['uname']
        d=user_registration.objects.filter(username=z)
        x=log_in.objects.filter(username=z)
        x.delete()
        d.delete()
        return redirect(viewuser)




def profile(re):
    return render(re,'profile.html')


# def forgot_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         try:
#             user = user_registration.objects.get(email=email)
#         except:
#             messages.info(request,"Email id not registered")
#             return redirect(forgot_password)
#         # Generate and save a unique token
#         token = get_random_string(length=4)
#         PasswordReset.objects.create(user=user, token=token)
#
#         # Send email with reset link
#         reset_link = f'http://127.0.0.1:8000/reset/{token}'
#         try:
#             send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
#             # return render(request, 'emailsent.html')
#         except:
#             messages.info(request,"Network connection failed")
#             return redirect(forgot_password)
#
#     return render(request, 'forget.html')

def an_profil(re,user): #anchor profile view
    d=Anchor_registration.objects.filter(username=user)
    x=anchor_gallery.objects.filter(username=user)
    y = amountdetails.objects.filter(username=user)
    print(y)
    return render(re,'audition.html',{'r':d,'r2':y,'r1':x})
def gall(re):
    d=anchor_gallery.objects.all()
    return render(re, 'audition.html', {'r1': d})


def location(request):     #search location
    if request.method == "POST":
        s = request.POST['n1']
        r = Anchor_registration.objects.filter(location=s)
        print(r)
        return render(request, 'search_result.html',{'d1': r})
    else:
        return HttpResponse("failed")


    #     if list(r) == []:
    #         return HttpResponse("<script>alert('Anchor does not Exists');window.location='12'</script>")
    #     else:
    #         return render(request,'location.html',{'s':r})
    #
    # else:
    #     return HttpResponse("<script>alert('No results found');window.location='12'</script>")
def reg(re):
    return render(re,'index-reg.html')

def user_inbox(re):
    if 'u_id' in re.session:
        y=re.session ['u_id']
        d=booking.objects.filter(name=y,action='Confirm')
        if list (d) == []:
            return HttpResponse("<script>alert('Message is empty');window.location='index1'</script>")
        else:
            return HttpResponse("<script> alert ('Your booking is confirmed. Make your payment') ; window.location='payment' </script>")
    else:
        return HttpResponse("<script>alert('No results found');window.location='index1'</script>")



def audition(re):
    return render(re,'anchor_reg.html')


def view_feedback(re):
    d=ufeed.objects.all()
    return render(re,'ad_view_feedback.html',{'r':d})
def feed_delete(re):
    if re.method=='POST':
        z=re.POST['uname']
        d=ufeed.objects.filter(username=z)
        x=log_in.objects.filter(username=z)
        x.delete()
        d.delete()
        return redirect(view_feedback)

def reviewlist(re):
    if 'u_id' in re.session:
        y=re.session ['u_id']
        d=ufeed.objects.filter(username=y)
        return render(re,'reviewlist.html',{'r':d})



# def forgot_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         try:
#             user = user_registration.objects.get(email=email)
#         except:
#             messages.info(request,"Email id not registered")
#             return redirect(forgot_password)
#         # Generate and save a unique token
#         token = get_random_string(length=4)
#         PasswordReset.objects.create(user=user, token=token)
#
#         # Send email with reset link
#         reset_link = f'http://127.0.0.1:8000/reset/{token}'
#         try:
#             send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
#             # return render(request, 'emailsent.html')
#         except:
#             messages.info(request,"Network connection failed")
#             return redirect(forgot_password)
#
#     return render(request, 'forget.html')

# def reset_password(request, token):
#     # Verify token and reset the password
#     print(token)
#     password_reset = PasswordReset.objects.get(token=token)
#     # usr = reg.objects.get(id=password_reset.user_id)
#     if request.method == 'POST':
#         new_password = request.POST.get('newpassword')
#         repeat_password = request.POST.get('cpassword')
#         if repeat_password == new_password:
#             a = password_reset.user.username
#             log_in.objects.filter(username=a).update(password=new_password)
#             # password_reset.user.set_password(new_password)
#             # password_reset.user.save()
#             # password_reset.delete()
#             return redirect(loginn)
#     return render(request, 'reset.html',{'token':token})


#user-change password
def chpass(request):
    if request.method=='POST':
        x=request.POST['n']
        y=request.POST['n1']
        z=request.POST['n2']
        d=log_in.objects.filter(username=x)
        d.update(password=z)
        return render(request,'index_login.html')
    else:
        return render(request,'change_password.html')


#user alert box
def user_inbox(re):
    if 'u_id' in re.session:
        y=re.session ['u_id']
        d=booking.objects.filter(name=y,action='Confirm')
        if list (d) == []:
            return HttpResponse("<script>alert('Message is empty');window.location='index1'</script>")
        else:
            return HttpResponse("<script> alert ('Your booking is confirmed. Make your payment') ; window.location='pay' </script>")
    else:
        return HttpResponse("<script>alert('No results found');window.location='index1'</script>")



def request_us(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        d=booking.objects.filter(ANCHOR=z,ACTION='pending')
        return render(re,'request-user.html',{'r':d})
    else:
        return HttpResponse('FGHJ')


def useraccept(re):
    if re.method == "POST":
        r = re.POST['n1']
        d = booking.objects.filter(id=r)
        d.update(ACTION="confirm")
        d1=log_in.objects.filter(username=r)
        d1.update(action="confirm")
        return HttpResponse("<script>alert('Accepted');window.location='request_user'</script>")
    else:
        return HttpResponse(re,'request-user.html')




def userreject(re):
    if re.method=="POST":
        r = re.POST['n1']
        d = booking.objects.filter(id=r)
        d.delete()
        return HttpResponse("<script>alert('rejected');window.location='request_user'</script>")
    else:
        return render(re,'request-user.html')





def book_anchor(re,user):
    if 'u_id' in re.session:
        z = re.session['u_id']
        g=user_registration.objects.filter(username=z)
        d=Anchor_registration.objects.filter(username=user)
        y=amountdetails.objects.filter(username=user)
        if re.method=='POST':
            a=re.POST['NAME']
            b= re.POST['PHONE']
            c= re.POST['ADDRESS']
            e= re.POST['DATE']
            d= re.POST['EMAIL']
            f=re.POST['AMOUNT']
            # g=re.POST['ANCHOR']
            x=booking.objects.create(username=z , name=a,PHONE=b,ADDRESS=c,DATE=e,EMAIL=d,ANCHOR=user,amount=f,ACTION='pending', payment='pending')
            return HttpResponse("<script>alert('booking is processing.confirmation will be updated');window.location='../index1'</script>")
        return render(re, 'book_anchorr.html',{'r':d,'r1':g,'r2':y})



def user_inbox(re):
    if 'u_id' in re.session:
        y=re.session['u_id']
        d=booking.objects.filter(username=y,ACTION='confirm')
        if list (d) ==[]:
            return HttpResponse("<script>alert('message is empty');window.location='index1'</script>")
        else:
            return HttpResponse("<script> alert ('your booking is confirmed. Make your payment'); window.location='booking_list'</script>")
    else:
        return HttpResponse("<script>alert('No result found');window.location='index1'</script>")



def confirm_us(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        x=booking.objects.filter(ANCHOR=z,ACTION='confirm')
        return render(re,'confirm-user.html',{'r':x})



def emp_profeed(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        d=ufeed.objects.filter(anchorname=z)
        return render(re,'anchor_profeed.html',{'r':d})
    else:
        return render(re,'index_login.html')






def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        try:
            user = user_registration.objects.get(email=email)
            print(user)
        except:
            messages.info(request,"Email id not registered")
            print("not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user_registration=user, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            # return render(request, 'emailsent.html')
            print("sended")
        except:
            print("error")
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'forget.html')

def reset_password(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    # usr = user_registration.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            a = password_reset.user_registration.username
            log_in.objects.filter(username=a).update(password=new_password)
            # PasswordReset.user.password=new_password
            # password_reset.delete()
            return redirect(loginn)
    return render(request, 'reset.html',{'token':token})


def user_message(req):
    if req.method=='POST':
        nm=req.POST['name']
        email=req.POST['email']
        sub=req.POST['subject']
        msg=req.POST['message']
        send_mail(f'{sub} from user {req.user.email}', f'{msg}','settings.EMAIL_HOST_USER', [email], fail_silently=False)

    return render(req,'user_message.html')

def hello(re):
    if 'u_id' in re.session:
        z = re.session['u_id']
        d = booking.objects.filter(username=z)
        return render(re, 'payment1.html', {'r': d})
    else:
        return render(re, 'index1.html')

# def paymentt(request):
#     if request.method == 'POST':
#             x = request.POST['b1']
#             y = request.POST['b2']
#             z = request.POST['b3']
#             a = request.POST['b4']
#             c = request.POST['b6']
#             e = request.POST['b7']
#             request.session['p_name'] = a
#             request.session['l_name'] = y
#             d = payment.objects.filter(username=x,PHONE=y,ADDRESS=z,EMAIL=a,ANCHOR=c,payment=e,status='confirm')
#             if list(d) ==[]:
#                 url='viewapp'
#                 msg='''<script>alert('payment not allowed.. your in processing')
#                 window.location='%s'</script>'''%(url)
#                 return HttpResponse(msg)
#             else:
#                 data=payment.objects.filter(test=z,name=y)
#                 for i in data:
#                     k=i.amount
#                 return render(request,'payment.html',{'r':d,'r1':k})
#     else:
#         return render(request, 'payment.html')



def anchor_photo(re):
    if 'e_id' in re.session:
        z = re.session['e_id']
        if re.method=='POST':
            a=re.FILES['b1']
            b=re.FILES['b2']
            c=re.FILES['b3']
            d=re.FILES['b4']
            e=re.FILES['b5']
            x=anchor_gallery.objects.create(photo=a,photo2=b,photo3=c,photo4=d,photo5=e,username=z)
            x.save()
    return render(re,'ad_gallery.html')



# def Ad_gallery(re):
#     if 'e_id' in re.session:
#         z=re.session['e_id']
#         d=anchor_gallery.objects.filter(username=z)
#         return render(re,'ad_gallery.html',{'r':d})
#     else:
#         return render(re,'login.html')

#payment


def payment1(request):
    if request.method == 'POST':
            a = request.POST['b2']
            y = request.POST['b4']
            b = request.POST['b3']
            request.session['p_name'] = a
            request.session['l_name'] = y
            # d = Booking.objects.filter(username=x,name=a,hotel_name=y,status='confirm')
            d = booking.objects.filter(username=a,ANCHOR=y, ACTION='confirm',payment='pending')
            if list(d) ==[]:
                url='booking_list'
                msg='''<script>alert('payment not allowed.. your in processing')
                window.location='%s'</script>'''%(url)
                return HttpResponse(msg)
            else:
                data=amountdetails.objects.get(username=y)
                print(data)

                k = data.advance
                # data.advance
                return render(request, 'payment.html', {'r': d,'r1':k})
    else:
        return render(request, 'payment.html')


#user-paying payment
def pay(request, id):
        amount = (id)*100
        request.session['price']=id
        order_currency = 'INR'
        client = razorpay.Client(
            auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
        # cursor = connection.cursor()
        # cursor.execute(
        #     "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(
        #         id) + "' ")

        # payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        return render(request, "pay.html",{'r':amount})


def success(re):
    if 'u_id' in re.session:
        z = re.session['u_id']
        d= booking.objects.filter(username=z)
        e_name = re.session['l_name']
        # a = request.session['u_na']
        # b = request.session['h_name']
        # c = request.session['price']
        # d=booking.objects.get(name=a,username=b)
        # x=d.email
        print(d)
        # y = d.room_category
        # d1=payment.objects.create(name=a,username=b,price=c,EMAIL=x,ANCHOR=y)
        # d1.save()
        # d2 = Booking.objects.get(name=a,hotel_name=b)
        # y=d2.username
        # # d3=adpay.objects.create(username=y,price=10,hotel_name=b)
        # d3 = adpay.objects.create(username=y, hotel_name=b)
        # d3.save()
        d4=booking.objects.filter(username=z,ANCHOR=e_name)
        d4.update(payment='paid')
        return HttpResponse("<script>alert('Your payment succeeded');window.location='booking_list'</script>")
        # return render(request, 'user.html'


#userbooking
def bookinglist(re):
    if 'u_id' in re.session:
        y=re.session ['u_id']
        d=booking.objects.filter(username=y,ACTION='confirm')
        return render(re,'user_booking.html',{'r':d})

def remove_review(request):
    print('hii')
    if request.method == "POST":
        r = request.POST['n1']
        print(r)
        d = ufeed.objects.filter(feed=r)
        print(d)
        d.delete()
        return HttpResponse("<script>alert('review deleted');window.location='index1'</script>")
    else:
        return HttpResponse('not okay')


def booking_accept(re):
    if re.method == "POST":
        r = re.POST['n1']
        d = booking.objects.filter(id=r)
        d.update(action="confirm")
        d1=log_in.objects.filter(username=r)
        d1.update(action="confirm")
        return HttpResponse("<script>alert('Accepted');window.location='accept_booking'</script>")
    else:
        return HttpResponse(re,'request-user.html')

def your_cancelledbooking(re):
    if 'u_id' in re.session:
        y=re.session ['u_id']
        d=booking.objects.filter(name=y,action='cancelled')
        return render(re,'cancelled_booking.html',{'r1':d})
    else:
        return HttpResponse('NO BOOKING')


def cancel(re):
    if re.method=='POST':
        x=re.POST['n2']
        d=booking.objects.filter(EMAIL=x,payment='pending')
        if list(d) == []:
            return HttpResponse("<script>alert('not allowed.. no refund after payment');window.location='index1 '</script>")
        else:
            print(d)
            # return render(re, 'employee_reviews.html', {'r': d})
            d.update(ACTION="cancelled")
            return HttpResponse("<script>alert('your booking is cancelled');window.location='index1 '</script>")
    else:
        return HttpResponse("error")


def view_gallery(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        d=anchor_gallery.objects.filter(username=z)
        return render(re,'view_gallery.html',{'r':d})
    else:
        return render(re,'index_login.html')


def gallery_user(re,user):
    g=anchor_gallery.objects.filter(username=user)
    return render(re,'gallery1.html',{'r':g})

def amountdtls(re):
    if 'e_id' in re.session:
        z = re.session['e_id']
        if re.method=='POST':
            x = re.POST['advance_amount']
            y = re.POST['fixed_amount']
            b = amountdetails.objects.create(fixedamount=y,advance=x,username=z)
            b.save()
    return render(re,'anchor_amount.html')
        # else:
        #     return render(re, 'anchor_profilevieww.html')


def locationfilter(re):
    if 'u_id' in re.session:
        x=re.session['u_id']
        z=Anchor_registration.objects.filter(action='confirm')
        s = set()
        print(s)
        for i in z:
            s.add(i.location)
        l = list(s)
        return render(re,'services1.html',{'r':z})
    else:
        return render(re,'services1.html')


def search(request):     #searching author
    if request.method == "POST":
        r = request.POST['n1']
        d = Anchor_registration.objects.filter(location=r)
        if list (d) == []:
            print(d)
            return HttpResponse("<script>alert('Not found check another location');window.location='12'</script>")
        else:
            return render(request,'search_result.html',{'r':d})
    else:
        return HttpResponse("<script>alert('No results found');window.location='12'</script>")

def up_user1(request):
    if request.method == 'POST':
        u = request.POST['n1']
        data = user_registration.objects.filter(username=u)
        return render(request, 'userprofileupdate.html', {'r': data})
    else:
        return redirect(profil)


def user_update2(re):
    if 'u_id' in re.session:
        z= re.session['u_id']
        v= user_registration.objects.filter(username=z)
        a = re.POST['n1']
        b = re.POST['n2']
        c = re.POST['n3']
        d = re.POST['n4']
        u = re.POST['n5']
        s=user_registration.objects.filter(username=z)
        r=s.update(name=a,address=b,phone_no=c,email=d,location=u)
        return HttpResponse("<script> alert ('Details updated') ; window.location='up_user1' </script>")
    else:
        return HttpResponse("NOT UPDATED")



# def forget_pwd(re):
#     if re.method=='POST':
#         u=re.POST['uname']
#         p=re.POST['pwd']
#         c=re.POST['con_pwd']
#         try:
#             b = log_in.objects.filter(username=u)
#             if p==c:
#                 b.update(password=c)
#                 return render(re,'login.html')
#             else:
#                 return HttpResponse("<script>alert('Password is incorrect');windows.location='index1' </script>")
#         except Exception:
#             return HttpResponse("<script>alert('please write another password');windows.location='index1' </script>")
#     else:
#         return render(re,'forget_pwd.html')








