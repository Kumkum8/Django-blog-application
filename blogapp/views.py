from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Post,Profile
from django .contrib import messages

# Create your views here.
def index(request):
    post= Post.objects.all()
    context={'posts':post}
    return render(request,template_name="index.html",context=context)

def post(request):
    return render(request,template_name="post.html")


def post_blog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('Description')
        try:
            img = request.FILES['image']
        except KeyError:
            img = None  # or handle the missing image in a way that makes sense for your application
        blog = Post(title=title, content=desc, author=request.user, image=img)   
        blog.save()       
        messages.success(request, 'Post has been submitted successfully')
        return redirect('post_blog')
    return render(request, template_name='post.html')





  


def register(request):
    return render(request,template_name="register.html")

#For user login


def loginpage(request):
    return render(request,template_name="loginpage.html")


def loginuser(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user )
        
        return render(request,template_name="index.html")
    
        # Redirect to a success page.
        
    else:
        # Return an 'invalid login' error message.
        pair={"msg":"Invalid username or password"}
        return render(request,template_name="index.html",context=pair)
    
#for create new account
    
def createuser(request):
    return render(request,template_name="register.html")



def create(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    
    
        
    user=User.objects.create_user(username,email,password)
    user.save()
    pair={"msg":"Your account is created successfully!"}
    return render(request,template_name="loginpage.html",context=pair)


#for disppearing login form after user logged in




#logout function
def logoutuser(request):
    logout(request)
    return render(request,template_name='index.html')
    # Redirect to a success page.


#blogs

def blog1(request):
    return render(request,template_name="blog1.html")


def blog2(request):
    return render(request,template_name="blog2.html")  

#blog detail display
def blog_detail(request,id):
    post=Post.objects.get(id=id)
    context={'post': post}
    return render (request,'blog_detail.html',context)

def deletepost(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    messages.success(request,'Your post has been deleted')
    return render(request,'index.html')
    


def editpost(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('Description')
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.save()
        messages.success(request,'Your post has been edited successfully!')
        return render(request,'index.html')

    return render(request, 'editpost.html', {'post': post})


#user profile
def profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get_or_create(user=request.user)[0]
        return render(request, 'profile.html', {'profile': profile})
    else:
        # Redirect the user to the login page if they are not authenticated
        return redirect('login')  


def edit_profile_photo(request):
    if request.method == 'POST':
        profile = request.user.profile
        if 'image' in request.FILES:
            profile.image = request.FILES['image']
            profile.save()
            return redirect('profile')  # Redirect to the profile view or another appropriate page
    return render(request, 'edit_profile.html')


def delete_profile_photo(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.image.delete()
        profile.save()
        return redirect('profile')  # Redirect to the profile view or another appropriate page
    return render(request, 'delete_profile.html')

