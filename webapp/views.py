

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, request

from .models import *

import matplotlib.pyplot as plt;
import numpy as np
import numpy
from django.shortcuts import render, redirect
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

# Create your views here.
def adminlogin(request):
    return render(request, 'admin.html')


def adminloginaction(request):
    loginid=request.POST['aid']
    pwd=request.POST['pwd']
    print(loginid, pwd,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    if loginid=='admin' and pwd=="admin":
        request.session['adminid']='admin'
        return render(request, 'adminhome.html')
    else:
        err='Your Login Data is wrong !!' 
        return render(request, 'admin.html',{'msg':err})


def adminhome(request):
    return render(request, 'adminhome.html')


def adminlogout(request):
    return render(request, 'admin.html')

def user(request):
    return render(request, 'user.html', {'b':False})

def signup(request):
    return render(request, 'user.html', {'b':True})



def usignupaction(request):
    if request.method == 'POST':
        email = request.POST['mail']
        uid = request.POST['uid']

        d = students.objects.filter(loginid__exact=uid).count()
        if d > 0:
            return render(request, 'user.html', {'msg': "USer ID Already Registered"})
        else:

            pass_word = request.POST['pass_word']
            phone = request.POST['phone']
            city = request.POST['city']
            fname = request.POST['fname']
            lname = request.POST['lname']
            addr = request.POST['addr']
            state = request.POST['state']
            zip = request.POST['zip']
            gen = request.POST['gen']
            dept = request.POST['dept']
            
            
            d = students(fname=fname,lname=lname, email=email, loginid=uid, pass_word=pass_word, phone=phone, gender=gen, city=city, address=addr,state=state, zip=zip, department=dept)
            d.save()

            return render(request, 'user.html', {'msg': "Register Success, You can Login.."})

    else:
        return render(request, 'user.html')

def userloginaction(request):
    if request.method=='POST':
        uid=request.POST['mail']
        pass_word=request.POST['pass_word']
        d=students.objects.filter(loginid__exact=uid).filter(pass_word__exact=pass_word).count()
        
        if d>0:
            d=students.objects.filter(loginid__exact=uid)
            request.session['email']=d[0].email
            request.session['gender']=d[0].gender
            request.session['uid']=uid
            request.session['name']=d[0].fname+" "+d[0].lname
            return render(request, 'userhome.html',{'data': d[0]})

        else:
            return render(request, 'user.html',{'msg':"Login Fail"})

    else:
        return render(request, 'user.html')
            

def forgotpwd(request):
    if request.method == 'POST':
        email = request.POST["email"]
        d=students.objects.filter(email__exact=email).count()
        if d>0:
            d2=students.objects.filter(email__exact=email)
            uid='';pwd=''
            for d1 in d2:
                uid=d1.loginid
                pwd=d1.pass_word
            sub='Login Deatils'
            body='Hello..\n\nLogin Details:\n\nLogin ID:'+str(uid)+'\nPassword:'+str(pwd)
            from .EmailBot import sendEmail
            sendEmail(email, sub,body)
            return render(request, 'user.html',{'msg':'Check your Email, the User ID and Password sent to your email id !!'} )
        else:
            return render(request, 'user.html',{'msg':'Incorrect Email !!'} )


        
     
        
       
    else:       
        return render(request, 'forgotpwd.html')

def userlogout(request):
    try:
        del request.session['email']
    except:
        pass
    return render(request, 'user.html')


def userhome(request):
    if "uid" in request.session:
        uid=request.session["uid"]
        d=students.objects.filter(loginid__exact=uid)

       
        return render(request, 'userhome.html',{'data': d[0]})

    else:
        return redirect('userlogout')
    
def viewprofilepage(request):
    if "uid" in request.session:
        uid=request.session["uid"]
        d=students.objects.filter(loginid__exact=uid)
        return render(request, 'viewprofile.html',{'data': d[0]})

    else:
        return render(request, 'user.html')

    
def updateprofile(request):
    if request.method=='POST':
        uid=request.session["uid"]
        ph = request.POST['ph']
        city = request.POST['city']
        fname = request.POST['fname']
        lname = request.POST['lname']
        addr = request.POST['addr']
        state = request.POST['state']
        zip = request.POST['zip']
        
        students.objects.filter(loginid=uid).update(fname=fname, lname=lname, phone=ph, city=city, address=addr, state=state, zip=zip)
        d=students.objects.filter(loginid__exact=uid)
        return render(request, 'updateprofile.html',{'data': d[0], 'msg':'Profile Updated !!'})
    else:
        uid=request.session["uid"]
        d=students.objects.filter(loginid__exact=uid)
        return render(request, 'updateprofile.html',{'data': d[0]})



def addfaculty(request):
    if request.method == 'POST':
        if True:

            phone = request.POST['phone']
            fname = request.POST['fname']
            lname = request.POST['lname']
            addr = request.POST['addr']
            email = request.POST['mail']
            dept = request.POST['dept']
          
            d = faculty(fname=fname,lname=lname, email=email, phone=phone,address=addr, department=dept)
            d.save()
            d=faculty.objects.all()

            return render(request, 'viewfaculty.html', {'data':d, 'msg': "Faculty Added !! "})

    
def viewfaculty(request):
    d=faculty.objects.all()
    return render(request, 'viewfaculty.html',{'data':d})


def updatepwd(request):
    if request.method == 'POST':
        newpwd = request.POST["newpwd"] 
        old = request.POST['old']
        uid = request.session["uid"]
        d=students.objects.filter(loginid=uid).filter(pass_word=old).count()
        if d>0:
            students.objects.filter(loginid=uid).update(pass_word=newpwd)
        
        return render(request, 'updatepwd.html',{'msg':'Password Updated !!'} )
       
    else:       
        return render(request, 'updatepwd.html')

from django.db.models import Q

def pplsearch(request):
    if request.method == 'POST':
        fname = request.POST["fname"] 
        lname = request.POST['lname']
        dept = request.POST["dept"]
        d1=students.objects.filter(Q(fname__icontains=fname) | Q(lname__icontains=lname)| Q(department__icontains=dept))
        d2=faculty.objects.filter(Q(fname__icontains=fname) | Q(lname__icontains=lname)| Q(department__icontains=dept))
        
        return render(request, 'pplsearchres.html',{'data1':d1, 'data2':d2} )
       
    else:       
        return render(request, 'pplsearch.html')



def addbooks(request):
    return render(request, 'addbooks.html')

def addlib(request):
    if request.method == 'POST':
        title = request.POST["title"] 
        author = request.POST['author']
        ISBN = request.POST["ISBN"]
        location = request.POST["location"]
        d=library(title=title, author=author, ISBN=ISBN, location=location)
        d.save()
        
        return render(request, 'addbooks.html',{'msg':'Book Added !! '} )
       
    else:       
        pass

def addbook(request):
    if request.method == 'POST':
        title = request.POST["title"] 
        author = request.POST['author']
        ISBN = request.POST["ISBN"]
        bookstore = request.POST["bookstore"]
        cost = request.POST["cost"]
        d=books(title=title, author=author, ISBN=ISBN, bookstore=bookstore, cost=cost)
        d.save()
        
        return render(request, 'addbooks.html',{'msg':'Book Added !! '} )
       
    else:       
        pass
        


def booksearch(request):
    if request.method == 'POST':
        title = request.POST["title"] 
        author = request.POST['author']
        ISBN = request.POST["ISBN"]
        d1=library.objects.filter(Q(title__icontains=title) | Q(author__icontains=author)| Q(ISBN__icontains=ISBN))
        d2=books.objects.filter(Q(title__icontains=title) | Q(author__icontains=author)| Q(ISBN__icontains=ISBN))
        
        return render(request, 'booksearchres.html',{'data1':d1, 'data2':d2} )
       
    else:       
        return render(request, 'booksearch.html')

def purchasebooks(request):
    d=books.objects.all()
    l=[]
    sum=0
    for d1 in d:
        try:
            if request.POST[str(d1.id)]=='on':
                l.append(d1.id)
                sum=sum+d1.cost
        except:
            pass
    print(sum)
    if sum>200:
        ten_percent = sum * 0.1
        sum=sum-ten_percent
    return render(request, 'pay.html',{'amt':sum} )

def payment_u(request):
    if request.method=='POST':
        return render(request, 'userhome.html',{'msg':'Thank you for purchase !!', })
    else:
        pass

def roomreqstore(request):
    if request.method == 'POST':
        uid = request.session["uid"] 
        d=students.objects.filter(loginid=uid)
        d=d[0]
        dat_e = request.POST['dat_e']
        cost = request.POST["cost"]
        d2=room_request(fname=d.fname, lname=d.lname, email=d.email, phone=d.phone, loginid=uid, gender=d.gender, cost=cost, dat_e=dat_e)
        d2.save()
        
        
        return render(request, 'roomreqstore.html',{'msg':'Request published !! '} )
       
    else:       
        return render(request, 'roomreqstore.html' )
        


def searchroommate(request):
    if request.method == 'POST':
        uid = request.session["uid"] 
        dat_e = request.POST['dat_e']
        cost = request.POST["cost"]
        gen = request.POST["gen"]
        d2=room_request.objects.filter(dat_e__gte=dat_e).filter(cost__gte=cost).filter(gender=gen).exclude(loginid=uid)
        print(d2)
        return render(request, 'roomres.html',{'data':d2} )
       
    else:       
        pass


from .Dates import get
def mealplandef(request):
    if request.method == 'POST':
        plan = request.POST["plan"] 
        name = request.session["name"]
        loginid = request.session["uid"] 
        cost=600
        if plan=='monthly':
            cost=600
            dt1,dt2=get(30)
            d=mealplan(fname=name, loginid=loginid,plan='Monthly', fro_m=dt1, t_o=dt2,)
            d.save()

        else:
            cost=cost*6
            five_percent = cost * 0.05
            cost=cost-five_percent
            dt1,dt2=get(1800)
            d=mealplan(fname=name, loginid=loginid,plan='Sem', fro_m=dt1, t_o=dt2,)
            d.save()
        
        return render(request, 'pay.html',{'amt':cost} )
        
       
    else:
        loginid = request.session["uid"] 
        d=mealplan.objects.filter(loginid=loginid)
        
        return render(request, 'mealplan.html',{'data':d} )
               

def addevent(request):
    if request.method == 'POST':

        name = request.POST["name"]
        des = request.POST["des"]
        dat_e = request.POST["dat_e"]
      
        d=events(name=name, description=des, dat_e=dat_e)
        d.save()
        d=events.objects.filter()

        return render(request, 'addevents.html',{'data':d, 'msg':'Data Added !!'} )
      
    else:
        d=events.objects.filter()
        return render(request, 'addevents.html',{'data':d} )
               


def getevents(request):
    if request.method == 'POST':

        dt1 = request.POST["dt1"]
        dt2 = request.POST["dt2"]

        d = events.objects.filter(dat_e__range=[dt1, dt2])

        return render(request, 'getevents2.html',{'data':d, } )
      
    else:
        uid = request.session["uid"]
        d=bookevents.objects.filter(loginid=uid)
        
        return render(request, 'getevents.html', {'data':d} )
               

def bookeventsdef(request):
    if request.method == 'GET':

        id = request.GET["id"]
        uid = request.session["uid"]
        d=events.objects.filter(id=id)
        d=d[0]
        
        d = bookevents(eid=id, name=d.name, description=d.description, dat_e=d.dat_e, loginid=uid)
        d.save()


        return render(request, 'getevents.html',{'msg':'Event Selected !! ', } )
      
    else:
        
        pass
               




def bookbus(request):
    uid = request.session["uid"]
    d=busticket.objects.filter(loginid=uid)
    return render(request, 'bookbus.html', {'data':d})



def bookbusaction(request):
    if request.method == 'POST':

        
        st='';cost=0

        if 'id1' in request.POST:
            st=st+"Zone1 "
            cost=cost+2
            

        if 'id2' in request.POST:
        
            st=st+"Zone2 "
            cost=cost+4

        if 'id3' in request.POST:
        
            st=st+"Zone3 "
            cost=cost+6

        from .Dates import get
        dt1, dt2=get(1)

        uid = request.session["uid"]


        d=busticket(typ_e=st,cost=cost, dat_e=dt1, loginid=uid)
        d.save()
        return render(request, 'pay.html',{'amt':cost} )
      
    else:
        pass

def bookbusaction2(request):
    if request.method == 'POST':

        st='Bus card';cost=40

        from .Dates import get
        dt1, dt2=get(1)

        uid = request.session["uid"]

        d=busticket(typ_e=st,cost=cost, dat_e=dt1, loginid=uid)
        d.save()
        return render(request, 'pay.html',{'amt':cost} )
      
    else:
        pass



def regvoting(request):
    if request.method == 'POST':

        name = request.POST["name"]
        image = request.POST["image"]

        d = election(name=name, image=image, votes=0, votesp=0)
        d.save()

        d=election.objects.all()

        return render(request, 'regvoting.html',{'data':d,'msg':'Candidate Added !!' } )
      
    else:
        d=election.objects.all()

        return render(request, 'regvoting.html',{'data':d, } )


from django.db.models import F
def addvotes(request):
    if request.method == 'POST':

        id = request.POST["id"]
        election.objects.filter(id=id).update(votes=F('votes')+1)

        d=election.objects.all()
        tot=0
        ctot=0
        for d1 in d:
            tot=tot+d1.votes

        d=election.objects.filter(id=id)
        for d1 in d:
            ctot=ctot+d1.votes
        
        res=ctot/tot*100
             
        
        d = election.objects.filter(id=id).update(votesp=res)
        d=election.objects.all()
        return render(request, 'addvotes.html',{'data':d,'msg':'Thank you for voting !!' } )
      
    else:
        d=election.objects.all()

        return render(request, 'addvotes.html',{'data':d, } )
