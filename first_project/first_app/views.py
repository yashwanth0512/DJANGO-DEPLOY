from django.shortcuts import render
from django.http import HttpResponse
# 'request' name is convention. It can be some other name too.
def index(request) :    
   my_dict = { 'message' : "This is an injected content"}
   return render(request,'index.html',context=my_dict)



# Create your views here.
