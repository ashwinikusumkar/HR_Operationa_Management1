'''
UserName : makku
Email-Id : makku@gmail.com
Password : makku123
'''

from django.contrib import admin
from .models import State
from .models import City
from .models import Add_Jobs
from .models import HR_Registration
from .models import Manager_Registration
from .models import Interviewer_Registration

admin.site.register(State)
admin.site.register(City)
admin.site.register(Add_Jobs)
admin.site.register(HR_Registration)
admin.site.register(Manager_Registration)
admin.site.register(Interviewer_Registration)

