from django.shortcuts import render
from django.views import View
import pytesseract
from PIL import Image

# Create your views here.

#class based view for home page
class Home(View):
    #if get request return homepage
    def get(self, request):         
        return render(request,'index.html')

    #if post request the return home with data
    def post(self,request):
        context={}
        #fetch all uploaded files
        files=request.FILES.getlist('myfiles')

        #if 1 or more file are uploaded
        if (len(files)>0):
            filedatalist=[]
            for f in files:
                im_pic = Image.open(f)
                #find name and text from image
                filedatalist.append({
                    'file_text':pytesseract.image_to_string(im_pic),
                    'file_name':f.name
                })
                #print(pytesseract.image_to_string(im_pic))
                #print(f.name)
            context['file_data']=filedatalist
        return render(request,'index.html',context=context)