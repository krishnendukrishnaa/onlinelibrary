"""
URL configuration for onlinelibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from onlib import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name="index"),
    path("log",views.log,name="log"),
    path("lib",views.lib,name="lib"),
    path("staff",views.staff,name="staff"),
    path("stud",views.stud,name="stud"),
    path("addbook",views.addbook,name="addbook"),
    path("viewbook",views.viewbook,name="viewbook"),
    path("studview",views.studview,name="studview"),
    path("staffview",views.staffview,name="staffview"),
    path("issue_staffs",views.issue_staffs,name="issue_staffs"),
    path("issue_studs",views.issue_studs,name="issue_studs"),
    path("nonret",views.nonret,name="nonret"),
    path("addstaff",views.addstaff,name="addstaff"),
    path("addstud",views.addstud,name="addstud"),
    path("books",views.books,name="books"),
    path("logs",views.logs,name="logs"),
    path("book_add",views.book_add,name="book_add"),
    path("editbook/<int:b_id>",views.editbook,name="editbook"),
    path("book_update/<int:b_id>",views.book_update,name="book_update"),
    path("book_delete/<int:b_id>",views.book_delete,name="book_delete"),
    path("staff_book",views.staff_book,name="staff_book"),
    path("staff_book_pg",views.staff_book_pg,name="staff_book_pg"),
    path("view_profile_staff",views.view_profile_staff,name="view_profile_staff"),
    path("stud_book",views.stud_book,name="stud_book"),
    path("stud_book_pg",views.stud_book_pg,name="stud_book_pg"),
    path("view_prfl_stud",views.view_prfl_stud,name="view_prfl_stud"),
    path("edit_staff/<int:s_id>",views.edit_staff,name="edit_staff"),
    path("staff_update/<int:s_id>",views.staff_update,name="staff_update"),
    path("edit_stud/<int:s_id>",views.edit_stud,name="edit_stud"),
    path("stud_update/<int:s_id>",views.stud_update,name="stud_update"),
    path("admin_view_approved_staff",views.admin_view_approved_staff,name="admin_view_approved_staff"),
    path("admin_view_pending_staff",views.admin_view_pending_staff,name="admin_view_pending_staff"),
    path("admin_staff_approve/<int:reg_id>",views.admin_staff_approve,name="admin_staff_approve"),
    path("admin_reject_staff/<int:r_id>",views.admin_reject_staff,name="admin_reject_staff"),
    path("admin_view_approved_stud",views.admin_view_approved_stud,name="admin_view_approved_stud"),
    path("admin_view_pending_stud",views.admin_view_pending_stud,name="admin_view_pending_stud"),
    path("admin_stud_approve/<int:regi_id>",views.admin_stud_approve,name="admin_stud_approve"),
    path("admin_reject_stud/<int:c_id>",views.admin_reject_stud,name="admin_reject_stud"),
    path("select_staff/<int:bk_id>",views.select_staff,name="select_staff"),
    path("select_stud/<int:bk_id>",views.select_stud,name="select_stud"),
    path("staff_issued_bk",views.staff_issued_bk,name="staff_issued_bk"),
    path("issue_staff_delete/<int:b_id>",views.issue_staff_delete,name="issue_staff_delete"),
    path("stud_issued_bk",views.stud_issued_bk,name="stud_issued_bk"),    
    path("issue_stud_delete/<int:b_id>",views.issue_stud_delete,name="issue_stud_delete"),
    path("admin_ret_staff/<int:u_id>",views.admin_ret_staff,name="admin_ret_staff"),
    path("admin_ret_stud/<int:u_id>",views.admin_ret_stud,name="admin_ret_stud"),
    path("ret_staff",views.ret_staff,name="ret_staff"),
    
   
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
