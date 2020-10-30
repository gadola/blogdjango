from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Post, Comment
from django.views.generic.edit  import UpdateView
from django.views.generic  import ListView,DetailView,DeleteView
from .forms import CommentForms, PostForm, PostUpdateForm
from django.http import HttpResponseRedirect,HttpResponse
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from rest_framework import status,viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import PostSerializer , UserSerializer
from django.contrib.auth.models import User
from .permissions import IsAuthorOrReadOnly
# Create your views here.


class PostListView(ListView):
    queryset      = Post.objects.all().order_by("-created")
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 6 # tách ra 2 bài viết mỗi trang 

def search(request):
    query = request.GET['query']
    queryset = Post.objects.filter(title__icontains=query)
    return render(request,'blog/index.html', {'posts':queryset})

class Index(View):
    def get(self,request):
        posts = Post.objects.all().order_by('-created')
        paginator  = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/index.html', {'posts':posts, 'page_obj':page_obj})

    #add post
    def post(self,request):
        post = Post.objects.all().order_by('-created')
        form = PostForm()
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES,author = request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)
        return render(request,'blog/index.html',{'post':post,'form':form})

    
class PostDetailView(View):
    def get(self,request,pk):
        post =  get_object_or_404(Post,pk=pk)
        form = CommentForms()
        return render(request, 'blog/detail.html', {"post":post, "form":form})
    
    #add comment
    def post(self,request,pk):
        post =  get_object_or_404(Post,pk=pk)
        form = CommentForms()
        if request.method =="POST" :
            form = CommentForms(request.POST , author=request.user, post=post)
            if form.is_valid():
                form.save() #data saved
                return HttpResponseRedirect(request.path) # create a new form, data = null
        return render(request, 'blog/detail.html', {"post":post, "form":form})

def deletePost(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if post.author == request.user:
        post.delete()
    else:
        return HttpResponse("k the xoa")
    return redirect('index')
        
def updatePost(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method =='POST':
        if post.author == request.user:
            data=request.POST
            Post.objects.filter(pk=pk).update(title=data['title'],text=data['text'],image=request.FILES['image'])
            return redirect('post_detail', pk=pk)
    return render(request, 'blog/update.html', {"post":post})


class PostUpdate(UpdateView):
    model = Post
    fields = ['title','text','image']
    success_url ="/"
   
def about(request):
    return render(request,'blog/about.html')
def contact(request):
    return render(request,'blog/contact.html')

def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,author = request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'blog/add_post.html',{'form':form})


class PostList(APIView):

    def get(self, request, format = None):
        post =  Post.objects.all()
        serializer = PostSerializer(post, many = True)
        return Response(serializer.data)


    def post(self, request, format = None):
        serializer = PostSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Post = self.get_object(pk)
        serializer = PostSerializer(Post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Post = self.get_object(pk)
        serializer = PostSerializer(Post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Post = self.get_object(pk)
        Post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(author = self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
