from django.shortcuts import render
from django.utils.decorators import method_decorator 
from django.contrib.auth.decorators import login_required
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
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FeedBackViews, self).dispatch(*args, **kwargs)
        

        

