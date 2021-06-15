from django.views.generic import FormView,TemplateView
from .models import Classes
# from .forms import ContatoForms
# from django.urls import reverse_lazy
# from django.contrib import messages


class IndexView (TemplateView):
    template_name='index.html'
    # form_class=ContatoForms
    # success_url=reverse_lazy('index')
    
    def get_context_data(self,**kwargs):
        context=super(IndexView,self).get_context_data(**kwargs)
        context['Classes']=Classes.objects.all()
        return context

    # def form_valid(self, form,*args,**kwargs) :
    #     form.send_email()
    #     messages.success(self.request,'Email Enviado com sucesso')
    #     return super(IndexView,self).form_valid(form,*args,**kwargs)

    # def form_invalid(self, form,*args,**kwargs):
    #     messages.error(self.request,'Erro ao Enviar o Email')
    #     return super(IndexView,self).form_invalid(form,*args,**kwargs)


