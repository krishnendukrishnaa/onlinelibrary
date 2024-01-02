from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from onlib import models
from onlib.models import library,student,notes,staff_select,stud_select,staff_Ret
from django.http import HttpResponse
from datetime import datetime,date




# Create your views here.
def index(request):
    return render(request,"index.html")

def log(request):
    return render(request,"login.html")

def lib(request):
    return render(request,"admin.html")

def staff(request):
    return render(request,"staff.html")

def stud(request):
    return render(request,"stud.html")

def addbook(request):
    return render(request,"addb.html")

def viewbook(request):
    data = notes.objects.all()
    print(data)
    return render(request,"viewb.html",{'data':data})
   

def studview(request):
    data = library.objects.all()
    return render(request,"studview.html",{'data':data})


def staffview(request):   
    data = library.objects.all()
    return render(request,"viewstaff.html",{'data':data})


def issue_staffs(request):   
    issuedBooks = staff_select.objects.all()   
    return render(request, "issue.html", {'issuedBooks':issuedBooks})
    


def issue_studs(request):
    issuedBook = stud_select.objects.all()   
    return render(request, "ret.html", {'issuedBook':issuedBook})

def nonret(request):
    return render(request,"nonret.html")  

def books(request):
    data = notes.objects.all()
    return render(request,"books.html",{'data':data})

def staff_book(request):
    data = notes.objects.all()
    return render(request,"staff_book.html",{'data':data})


def staff_book_pg(request):
    data = notes.objects.all()
    return render(request,"staff_book_pg.html",{'data':data})


def view_profile_staff(request):
    if request.user:
        user= request.user
        data = library.objects.filter(User=user).values()
    
    return render(request,"view_profile_stf.html",{'data':data})


def stud_book(request):
    data = notes.objects.all()
    return render(request,"stud_book.html",{'data':data})


def stud_book_pg(request):
    data = notes.objects.all()
    return render(request,"stud_book_pg.html",{'data':data})


def view_prfl_stud(request):
    if request.user:
        user= request.user
        data = student.objects.filter(User=user).values()    
    return render(request,"view_prfl_stud.html",{'data':data})

def admin_view_approved_staff(request):
    data = library.objects.all().filter(status=1).values()
    return render(request,"viewstaff.html",{'data':data})

def admin_view_pending_staff(request):   
    data = library.objects.all().filter(status=0).values()
    return render(request,"view_staff_pending.html",{'data':data})

def admin_staff_approve(request,reg_id):
    reg = library.objects.get(id=reg_id)
    reg.status=1
    reg.save()
    return redirect('admin_view_approved_staff')

def admin_reject_staff(request,r_id):
    teacher = library.objects.get(id=r_id)
    teacher.delete()
    return redirect('admin_view_pending_staff')

#admin view staff issued Books
def issue_staffs(request):   
    issuedBooks = staff_select.objects.all()   
    return render(request, "admin_issue_staff.html", {'issuedBooks':issuedBooks})
    

#admin view stud issued Books
def issue_studs(request):
    issuedBook = stud_select.objects.all()   
    return render(request, "admin_issue_stud.html", {'issuedBook':issuedBook})



def admin_view_approved_stud(request):
    data = student.objects.all().filter(status=1).values()
    return render(request,"studview.html",{'data':data})

def admin_view_pending_stud(request):   
    data = student.objects.all().filter(status=0).values()
    return render(request,"view_stud_pending.html",{'data':data})

def admin_stud_approve(request,regi_id):
    regi = student.objects.get(id=regi_id)
    regi.status=1
    regi.save()
    return redirect('admin_view_approved_stud')

def admin_reject_stud(request,c_id):
    child = student.objects.get(id=c_id)
    child.delete()
    return redirect('admin_view_pending_stud')



def issue_staff_delete(request,b_id):
    add = staff_select.objects.get(id=b_id)
    add.delete()
    return redirect('staff_issued_bk')


def stud_issued_bk(request):
    issuedBook = stud_select.objects.all()   
    return render(request, "stud_issued_bk.html", {'issuedBook':issuedBook})


def issue_stud_delete(request,b_id):
    add = stud_select.objects.get(id=b_id)
    add.delete()
    return redirect('stud_issued_bk')

def admin_ret_staff(request,u_id):
    Data = staff_select.objects.get(id=u_id)
    return render(request,"admin_return_staff.html",{'Data':Data})

def admin_ret_stud(request,u_id):
    Data = stud_select.objects.get(id=u_id)
    return render(request,"admin_return_stud.html",{'Data':Data})



    
    




def addstaff(request):
    if request.method == "POST":
        SName=request.POST['stname']        
        user_name=request.POST['stuname']
        Password1=request.POST['stpass']
        Password2=request.POST['conpass']
        Stemail=request.POST['stemail']
        StPhone=request.POST['stphone']
        role = 'staff'
        status = 0

        if Password1==Password2:
            if User.objects.filter(username=user_name).exists():
                return redirect('staff')
            elif User.objects.filter(email=Stemail).exists():
                return redirect('staff')
            
            else:
                user = User.objects.create_user(username=user_name, email=Stemail, password=Password1)
                user.save()
                print(user)
                staff = models.library(User=user, SName=SName, StPhone=StPhone, role=role, status=status)
                staff.save()
                print(staff)
        else:
            return redirect('staff')
        
        return redirect('log')
    
    else:
        return render(request,'staff.html')

        



def addstud(request):
    if request.method == "POST":
        SDName=request.POST['sdname']
        print(SDName)
        SDUName=request.POST['studuname']
        SDPassword=request.POST['sdpass']
        CPassword=request.POST['sdconpass']
        SDemail=request.POST['studemail']
        SDPhone=request.POST['stdphone']
        role = 'student'
        status = 0

        if SDPassword==CPassword:
            if User.objects.filter(username=SDUName).exists():
                return redirect('stud')
            elif User.objects.filter(email=SDemail).exists():
                return redirect('stud')
            else:
                user = User.objects.create_user(username=SDUName,email=SDemail,password=SDPassword)
                user.save()
                print(user)
                student = models.student(User=user,SDName=SDName,SDPhone=SDPhone, role=role, status=status)
                student.save()
                print(student)
        else:
            return redirect('stud')
        
        return redirect('log')
    
    else:
        return render(request,'stud.html')
        

    
def logs(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            users = User.objects.filter(username=username).values()
            for i in users:
                id = i['id']

            if library.objects.filter(User=id).exists():
                st = library.objects.filter(User=id).values()

                for i in st:
                    role = i['role']
                    status = i['status']

                user = authenticate(request, username=username, password=password)
                if user is not None and role == 'staff' and status == '1':
                    auth_login(request, user)
                    return redirect('staff_book')

            elif student.objects.filter(User=id).exists():
                st = student.objects.filter(User=id).values()

                for i in st:
                    role = i['role']
                    status = i['status']

                user = authenticate(request, username=username, password=password)
                if user is not None and role == 'student' and status == '1':
                    auth_login(request, user)
                    return redirect('stud_book')
            
            elif username == 'library' and password == '9876':
                return redirect('lib')

        # Invalid credentials or other cases
        return HttpResponse("Invalid credentials or other message")

    else:
        return render(request, 'login.html')




def book_add(request):
    if request.user:
        user=request.user
        if request.method == "POST" and request.FILES:
            BookNo=request.POST['bookno']
            Image=request.FILES['image']
            BookName=request.POST['bname']
            Category=request.POST['bcat']
            Author=request.POST['author']
            Publisher=request.POST['pub']
            Return=request.POST['return']
            Fine=request.POST['fine']
            add=notes(User=user,BookNo=BookNo,Image=Image,BookName=BookName,Category=Category,Author=Author,Publisher=Publisher,Return=Return,Fine=Fine)
            add.save()       
            return redirect("viewbook")
               
    return render(request,"addb.html")
    

def editbook(request,b_id):
    Data = notes.objects.get(id=b_id)
    return render(request,'bedit.html',{'Data':Data})


def book_update(request,b_id):
    if request.method=="POST":
        add=notes.objects.get(id=b_id)
        add.BookNo=request.POST['bookno']
        add.Image=request.FILES['image']
        add.BookName=request.POST['bname']
        add.Category=request.POST['bcat']
        add.Author=request.POST['author']
        add.Publisher=request.POST['pub']
        add.Return=request.POST['return']
        add.Fine=request.POST['fine']
        add.save()
        return redirect("viewbook")
    

def book_delete(request,b_id):
    add = notes.objects.get(id=b_id)
    add.delete()
    return redirect('viewbook')


def edit_staff(request,s_id):
    Data = library.objects.get(id=s_id)
    return render(request,'edit_staff.html',{'Data':Data})

def staff_update(request,s_id):
    if request.method=="POST":
        add=library.objects.get(id=s_id)
        add.SName=request.POST['stname']
        add.user_name=request.POST['stuname']
        add.Password1=request.POST['stpass']
        add.Password2=request.POST['conpass']
        add.Stemail=request.POST['stemail']
        add.StPhone=request.POST['stphone']
        add.save()
        return redirect("view_profile_staff")
    
def edit_stud(request,s_id):
    Data = student.objects.get(id=s_id)
    return render(request,'edit_stud.html',{'Data':Data})


def stud_update(request,s_id):
    if request.method=="POST":
        add=student.objects.get(id=s_id)
        add.SDName=request.POST['sdname']
        add.SDUName=request.POST['studuname']
        add.SDPassword=request.POST['sdpass']
        add.CPassword=request.POST['sdconpass']
        add.SDemail=request.POST['studemail']
        add.SDPhone=request.POST['stdphone']
        add.save()
        return redirect("view_prfl_stud")
    

def select_staff(request, bk_id):

    # Check if the user is authenticated
    if request.user.is_authenticated:
        #import datetime
        

        x = datetime.now()
        #x=str(x)
        print(x) 
        # Get the library instance for the current user
        library_instance, created = library.objects.get_or_create(User=request.user)

        # Get the book data
        # data = get_object_or_404(notes, id=bk_id)
        data=notes.objects.filter(id=bk_id).values()
        #print(data)
        for i in data:
          
            Bookname=i['BookName']
            Bookno=i['BookNo']
            id=i['id']
            user_id=i['User_id']
            image=i['Image']
            Date=x
            category=i['Category']
            author=i['Author']
            Publisher=i['Publisher']
            Return=i['Return']
            fine=i['Fine']
            status=i['status']
            
            #print(i['Fine'])

    
        
        # Create a new staff_select instance
        staff_selection = staff_select(
            Date=Date,
            BookName=Bookname,       
            User=user_id,
            book=id,
            BookNo=Bookno,
            Image=image,
            Category=category,
            Author=author,
            Publisher=Publisher,
            Return=Return,
            Fine=fine,
            status=status
        )
        print(staff_selection)

        # Save the instance
        staff_selection.save()
        

        # Redirect to the view_staff page
        return redirect("staff_issued_bk")
    else:
        # Handle the case where the user is not authenticated
        # You might want to redirect the user to a login page or do something else
        return HttpResponse("Unauthorized access")



def staff_issued_bk(request):
    #if User.objects.filter(username=username).exists():
    # if request.user:
    #     user= request.user
    #     print(user)
    #     for i in user:
    #         Username=i['username']
    #         print(i['username'])
    #     issuedBooks = staff_select.objects.filter(User=user).all()    
    # return render(request,"staff_issued_bk.html")
    issuedBooks = staff_select.objects.filter()     
    return render(request, "staff_issued_bk.html", {'issuedBooks':issuedBooks})


def select_stud(request,bk_id):
    if request.user.is_authenticated:
       # import datetime

        #x= datetime.datetime.now()
        x = date.today()
        #z=x.strftime("%D")

        # Get the library instance for the current user
        library_instance, created = student.objects.get_or_create(User=request.user)

        # Get the book data
        # data = get_object_or_404(notes, id=bk_id)
        data=notes.objects.filter(id=bk_id).values()
        print(data)
        for i in data:
            BookName=i['BookName']
            BookNo=i['BookNo']
            id=i['id']
            User_id=i['User_id']
            Image=i['Image']
            Date1=x
            Category=i['Category']
            Author=i['Author']
            Publisher=i['Publisher']
            Return=i['Return']
            Fine=i['Fine']
            status=i['status']
            
            print(Date1)

    
        
        # Create a new stud_select instance
        stud_selection = stud_select(
            BookName=BookName, 
            BookNo=BookNo,      
            User=User_id,
            book=id,           
            Image=Image,
            Date1=Date1,
            Category=Category,
            Author=Author,
            Publisher=Publisher,
            Return=Return,
            Fine=Fine,
            status=status
        )
        print(stud_selection)

        # Save the instance
        stud_selection.save()
        

        # Redirect to the view_staff page
        return redirect("stud_issued_bk")
    else:
        # Handle the case where the user is not authenticated
        # You might want to redirect the user to a login page or do something else
        return HttpResponse("Unauthorized access")



def ret_staff(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        user = request.user  # Use the authenticated user

        if request.method == "POST":
            print("POST")
            # Retrieve values from the POST request
            user_id = request.POST.get('ret_user_id')
            book = request.POST.get('ret_id')
            BookName = request.POST.get('ret_name')
            BookNo = request.POST.get('ret_id_no')
            Date = request.POST.get('ret_issue_date')
            RetDate = request.POST.get('ret_Ret_date')
            Fine = request.POST.get('ret_ret_fine')

            # Ensure all required fields are not empty
            if user_id and book and BookName and BookNo and Date and RetDate and Fine:
                try:
                    # Parse the date strings into datetime objects
                    Date = datetime.strptime(Date, '%b. %d, %Y').date()
                    RetDate = datetime.strptime(RetDate, '%b. %d, %Y').date()

                    # Create a staff_Ret instance and save it to the database
                    add = staff_Ret(
                        user=user,
                        book=book,
                        BookName=BookName,
                        BookNo=BookNo,
                        Date=Date,
                        RetDate=RetDate,
                        Fine=Fine
                    )
                    add.save()
                    return redirect("issue_staffs")  # Redirect to the specified URL after successful submission
                except Exception as e:
                    print(f"Error saving to database: {e}")
                    # Handle the error or log it
                    return HttpResponse("Error saving to database.")
            else:
                # Handle the case where required fields are empty
                return HttpResponse("Error: All required fields must be filled.")
        else:
            # Handle cases where the request method is not POST
            return HttpResponse("Invalid request method")
    else:
        # Handle cases where the user is not authenticated
        return HttpResponse("Unauthorized access")


        #Clothes Online Store with Payment
    #Hospital Management System using Django
    #Healthcare Management System 
    #Django project on the grocery store.
    #online gift store.










    





