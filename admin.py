from django.contrib import admin
from .models import library,student,notes,stud_select,staff_select,staff_Ret

# Register your models here.
admin.site.register(library)
admin.site.register(student)
admin.site.register(notes)
admin.site.register(staff_select)
admin.site.register(stud_select)
admin.site.register(staff_Ret)