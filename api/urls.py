from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('user/registo', views.CreateUserView.as_view(), name="register"),
    path('token', TokenObtainPairView.as_view(), name="get_token"),
    path('token/refresh', TokenRefreshView.as_view(), name="refresh"),
    path('api-auth', include('rest_framework.urls')),

    path('departamentos', views.DepartmentListCreate.as_view(), name='department_list'),
    path('departamentos/<int:pk>', views.DepartmentRetrieveUpdateDelete.as_view(), name='department_rud'),
    path('departamentos/importar', views.DepartmentCSVImport, name='department_import'),

    path('membros', views.MemberListCreate.as_view(), name='member_list'),
    path('membros/<int:pk>', views.MemberRetrieveUpdateDelete.as_view(), name='member_rud'),
    path('membros/importar', views.MembersCSVImport, name='member_import'),

    path('equipas', views.TeamListCreate.as_view()),

    path('funcoes', views.FunctionListCreate.as_view(), name='function_list'),
    path('funcoes/importar', views.FunctionsCSVImport, name='function_import'),

    path('edificios', views.BuildingListCreate.as_view(), name='building_list'),
    path('edificios/importar', views.BuildingsCSVImport, name='building_import'),

    path('espacos', views.SpaceListCreate.as_view(), name='space_list'),
    path('espacos/importar', views.SpacesCSVImport, name='space_import'),

    path('tarefas', views.TaskListCreate.as_view(), name='task_list'),
    path('tarefas/importar', views.TasksCSVImport, name='task_import'),

    path('atividades', views.ActivityListCreate.as_view(), name='activity_list'),
    path('atividades/importar', views.ActivitiesCSVImport, name='activity_import'),

    path('participantes', views.ParticipantListCreate.as_view(), name='participant_list'),
    path('participantes/importar', views.ParticipantsCSVImport, name='participant_import'),
]