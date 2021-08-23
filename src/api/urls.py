from django.urls import path

from .views import TodoCompletedList, TodoListCreate, TodoRetrieveUpdateDestroy, TodoComplete, signup, login


urlpatterns = [
    # Todos:
    path('todos/', TodoListCreate.as_view()),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete/', TodoComplete.as_view()),
    path('todos/completed/', TodoCompletedList.as_view()),
    
    # Auth:
    path('signup/', signup),
    path('login/', login),
]
