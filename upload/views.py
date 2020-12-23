from django.shortcuts import render
from .models import Doc
from django.views.generic import TemplateView
from django.http import HttpResponse,JsonResponse


# Create your views here.
class index(TemplateView):
    template_name = 'upload/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] =Doc.objects.all() 
        return context
    
# This is just to upload image in database.
# if user hits this api he will be returns with appropriate false response
def file_upload_view(request):
    if request.method == "POST":
        my_file = request.FILES.get('file')
        Doc.objects.create(upload = my_file)
        return HttpResponse('')
    return JsonResponse({'post':'false'})

def view_image(request,image_id):
    img=Doc.objects.get(pk=image_id)
    return render(request,"upload/image_disp.html",{"image":img})

