from http.client import HTTPResponse
from django.shortcuts import render
from django.views import generic
from .models import Feedback
# Create your views here.
class FeedBackViews(generic.ListView):
    model = Feedback
    context_object_name = 'feedbacks'
    template_name = 'feedback_form.html'
    queryset = Feedback.objects.all()

    def post(self,request, *args, **kw):
        data = request.POST
        queryset=Feedback(name =data['name'],email=data['email'],phone=data['phone']
        ,subject_name = data['subject_name'],contents =data['contents'])
        queryset.save()
        queryset.clean_fields()
        return render(request,'feedback_success.html')
        

        

