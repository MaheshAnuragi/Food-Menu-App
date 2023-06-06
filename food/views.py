from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import Itemform
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context ={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)
    # return HttpResponse(template.render(context,request))
    # return HttpResponse(item_list)

# it simmiliar to index func but for reducing the complexity of func we are using inbuilt class of Django
@method_decorator(login_required,name='dispatch')
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'
    
# it simmiliar to Detail func but for reducing the complexity of func we are using inbuilt class of Django
class DetailClassView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'

# Below class based view for create an item

class CreateItemClassView(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_img'] #here we are not adding user-name bcz user-name is auto when user will login
    template_name = 'food/item-form.html'

    # for this will create a func
    def form_valid(self, form):
        form.instance.user_name =  self.request.user
        return super().form_valid(form)
    
    


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    print(item)
    context = {
        'item':item,
    }
    return render(request,'food/detail.html',context)
    # return HttpResponse("This is Id Number: %s" % item_id)

@login_required
def create_item(request):
    form = Itemform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form})

def update_item(request,item_id):
    item = Item.objects.get(id=item_id)
    form = Itemform(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/item-delete.html',{'item':item})