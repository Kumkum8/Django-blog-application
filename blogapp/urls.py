from django.urls import path
from .import views

urlpatterns=[
path("",views.index,name="index"),

path("post_blog",views.post_blog,name="post_blog"),
path("post",views.post,name="post"),

path("register",views.register,name="register"),
#login form 
path("login",views.login,name="login"),
path("loginuser",views.loginuser,name="loginuser"),
path("loginpage",views.loginpage,name="loginpage"),
#create new account
path("createuser",views.createuser,name="createuser"),
path("create",views.create,name="create"),
path("logoutuser",views.logoutuser,name="logoutuser"),
#blogs
path("blog1",views.blog1,name="blog1"),
path("blog2",views.blog2,name="blog2"),
path("blog_detail/<int:id>",views.blog_detail,name="blog_detail"),
path("deletepost/<int:id>",views.deletepost,name="deletepost"),
path("editpost/<int:id>",views.editpost,name="editpost"),
path("profile",views.profile,name="profile"),
path("edit_profile_photo",views.edit_profile_photo,name="edit_profile_photo"),
path("delete_profile_photo",views.delete_profile_photo,name="delete_profile_photo"),

]