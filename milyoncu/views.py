from django.shortcuts import render,get_object_or_404 ,redirect, reverse
from django.views.generic import ListView, DetailView, FormView, DeleteView
from .models import Product, Category , Cart
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from milyoncu.forms import ProductForm,AddCart
from django.template.defaultfilters import slugify


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class IndexView(ListView):
    template_name = "index.html"
    queryset = Product.objects.order_by('?')[0:4]


class SweatbandsView(IndexView):
    template_name = "sweatbands.html"
    queryset = Product.objects.all().filter(category_id='1')


class HeadbandsView(IndexView):
    template_name = "headbands.html"
    queryset = Product.objects.all().filter(category_id='2')


class BandanasView(IndexView):
    template_name = "bandanas.html"
    queryset = Product.objects.all().filter(category_id='3')


class BalloonsView(IndexView):
    template_name = "balloons.html"
    queryset = Product.objects.all().filter(category_id='4')


class TableCoversView(IndexView):
    template_name = "tablecovers.html"
    queryset = Product.objects.all().filter(category_id='5')


class CoastersView(IndexView):
    template_name = "coasters.html"
    queryset = Product.objects.all().filter(category_id='6')


class CartView(ListView):
    template_name = "cart.html"

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class AllProducts(IndexView):
    template_name = "allproducts.html"
    queryset = Product.objects.all()


class Delete(DeleteView):
    model = Cart

    def get(self, request, *args, **kwargs):
        obj = Cart.objects.get(user_id=self.request.user.id, id=self.kwargs.get('id'))
        obj.delete()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('milyoncu:cart')




class Preview(DetailView, FormView):
    template_name = "preview.html"
    form_class = AddCart

    def form_valid(self, form):
        cart = form.save(commit=False)
        cart.quantity = form.cleaned_data['quantity']
        cart.user = self.request.user
        cart.product = self.get_object()
        cart.save()
        return super(DetailView, self).form_valid(form)

    def get_success_url(self,  **kwargs):
           return reverse_lazy('milyoncu:cart')

    def get_object(self):
        """Returns the BlogPost instance that the view displays"""
        return get_object_or_404(Product, slug=self.kwargs.get("slug"))


def post_new(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.POST['name']
            post.description = request.POST['description']
            post.price = request.POST['price']
            post.size = request.POST['size']
            post.category.id = request.POST['category']
            post.logo = request.FILES['logo']
            post.save()
            return redirect('milyoncu:preview', slug= slugify(post.name))
    else:
        return render(request, 'edit.html', {'form': form})


def totalPrice(request):
    user = request.user
    if user.is_authenticated:
        list = Cart.objects.filter(user=user)
        total= 0
        for c in list:
            total += c.quantity*c.product.price
        return { "cartTotal":total, "totalAmount": list.count()}
    return {}
