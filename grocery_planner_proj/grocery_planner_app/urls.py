from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('',views.index ),
    
    # Register/logout/login
    path("register/", views.register),
    path("logout/", views.logout),
    path("success/", views.success),
    path("login/", views.login),
    
    # Discussion Board
    path('process_message/', views.post_mess),
    path('add_comment/<int:id>/', views.post_comment),
    path('user_profile/<int:id>/', views.profile),
    path('like/<int:id>/', views.add_like),
    path('delete/<int:id>/', views.destroy),
    path('edit/<int:id>/', views.edit_page),
    path('process_edit/<int:id>/', views.process_edit),

    # Profile
    path('my_profile/', views.my_profile),
    path('update_user_info/<int:id>', views.update_profile),

    # Grocery List
    path('add_item/', views.add_item),
    path('view_add_item/<int:id>/<int:recipe_id>/', views.view_add_item),
    path('remove/<int:id>/', views.remove_item), 
    path('grocery_list/', views.grocery_list),
    
    # Meal Plan
    path('meal_plan/', views.meal_plan),
    path('add_to_meal_plan/', views.add_to_meal_plan),
    path('remove_meal_plan/<int:id>', views.remove_plan),
    
    # Recipes
    path('view_recipe/<int:id>/', views.view_recipe),
    path('add_recipe/', views.add_recipe),
    path('create_recipe/', views.create_recipe),
    path('update_recipe/<int:id>/', views.update_recipe),
    path('render_edit_recipe/<int:id>/', views.render_edit_recipe),
    path('process_add_recipe/', views.process_add_recipe),

    # Ingredients
    path('add_ingredient/<int:id>', views.add_ingredient),
    path('remove_ingredient/<int:id>/', views.remove_ingredient),
    
]
