from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
import uuid

from datetime import datetime

from .models import Department, Member, Team, Function, Building, Space, Task, Activity, Participant, ActivityRegistration
from .serializers import UserSerializer, DepartmentSerializer, MemberSerializer, TeamSerializer, FunctionSerializer, BuildingSerializer, SpaceSerializer, TaskSerializer, ActivitySerializer, ParticipantSerializer

from .csv.departments import run_csv as RunCSVImportDepartments
from .csv.members import run_csv as RunCSVImportMembers
from .csv.teams import run_csv as RunCSVImportTeams
from .csv.functions import run_csv as RunCSVImportFunctions
from .csv.buildings import run_csv as RunCSVImportBuildings
from .csv.spaces import run_csv as RunCSVImportSpaces
from .csv.tasks import run_csv as RunCSVImportTasks
from .csv.activities import run_csv as RunCSVImportActivities
from .csv.participants import run_csv as RunCSVImportParticipants


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class DepartmentListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


class DepartmentRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    lookup_field = 'pk'


def DepartmentCSVImport(request):
    for dep in RunCSVImportDepartments():
        try:
            Department.objects.create(short_name=dep['short_name'], long_name=dep['long_name'])
        except:
            print("Import went wrong")

    return redirect('department_list')


class MemberListCreate(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


class MemberRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    lookup_field = 'pk'


def MembersCSVImport(request):
    for member in RunCSVImportMembers():
        try:
            department = Department.objects.filter(short_name=member['department_name'])[0]
        except:
            print('Could not find department')

        try:
            Member.objects.create(
                name=member['name'],
                email=member['email'],
                phone=member['phone'],
                department=department)
        except:
            print('Import went wrong')

    return redirect('member_list')


class TeamListCreate(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


def TeamsCSVImport(request):
    for team in RunCSVImportTeams():
        try:
            Team.objects.create(
                title=team['title'],
                description=team['description'],
                coordinator=Member.objects.filter(name=team['coordinator_name'])[0]
            )
        except:
            print('Import went wrong')

    return redirect('team_list')


class FunctionListCreate(generics.ListCreateAPIView):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


def FunctionsCSVImport(request):
    for function in RunCSVImportFunctions():
        try:
            Function.objects.create(
                title=function['title'],
                description=function['description'],
                members_needed_min=function['members_needed_min'],
                members_needed_max=function['members_needed_max'],
                vols_needed=function['vols_needed'],
                observations=function['obs'],
                #team=Team.objects.filter(pk=1)
            )
        except:
            print('Import went wrong')

    return redirect('function_list')


class BuildingListCreate(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


def BuildingsCSVImport(request):
    for building in RunCSVImportBuildings():
        try:
            Building.objects.create(name=building['name'])
        except:
            print('Import went wrong')

    return redirect('building_list')


class SpaceListCreate(generics.ListCreateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


def SpacesCSVImport(request):
    for space in RunCSVImportSpaces():
        try:
            building = Building.objects.filter(name=space['building_name'])[0]
            Space.objects.create(name=space['name'], building=building)
        except:
            print('Import went wrong')

    return redirect('space_list')


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


def TasksCSVImport(request):
    for task in RunCSVImportTasks():
        try:
            function = Function.objects.filter(title=task['function_title'])[0]
            space = Space.objects.filter(name=task['space_name'])[0]
            member = Member.objects.filter(name=task['member_name'])[0]

            date_num = int(task['date_num'])

            dates = {
                1: '15/04/2024',
                2: '16/04/2024',
                3: '17/04/2024',
                4: '18/04/2024',
                5: '19/04/2024'
            } # dates missing

            date = dates[date_num]

            Task.objects.create(date=datetime.strptime(date, '%d/%m/%Y').date(),
                hour_start=datetime.strptime(task['hour_start'], '%H:%M').time(),
                hour_end=datetime.strptime(task['hour_end'], '%H:%M').time(),
                function=function,
                space=space,
                member=member
            )
        except:
            print('Import went wrong')

    return redirect('task_list')


class ActivityListCreate(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


def ActivitiesCSVImport(request):
    for activity in RunCSVImportActivities():
        try:
            space = Space.objects.filter(name=activity['space_name'])[0]

            date_num = int(activity['date_num'])

            dates = {
                2: '15/04/2024',
                3: '16/04/2024',
                4: '17/04/2024',
                5: '18/04/2024',
                6: '19/04/2024'
            }

            date = dates[date_num]
            
            Activity.objects.create(
                title=activity['title'],
                date=datetime.strptime(date, '%d/%m/%Y').date(),
                hour_start=datetime.strptime(activity['hour_start'], '%H:%M').time(),
                hour_end=datetime.strptime(activity['hour_end'], '%H:%M').time(),
                space=space
            )
        except:
            print('Import went wrong')

    return redirect('activity_list')


class ParticipantListCreate(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


def ParticipantsRegister(request):
    name = request.POST['name'].strip()
    email = request.POST['email'].strip()
    internal_id = request.POST['internal_id'].strip()
    act_title = request.POST['act_title'].strip()

    try:            
        p = Participant.objects.create(
            name=name,
            email=email,
            internal_id=internal_id
        )

        act = Activity.objects.filter(title=act_title)[0]
        ActivityRegistration.objects.create(
            activity=act,
            participant=p,
            pre_registered=False,
            showed_up=True
        )   
        
    except:
        print('Register went wrong')

    return redirect('participant_list')


def ParticipantsCSVImport(request):
    for participant in RunCSVImportParticipants():
        try:            
            p = Participant.objects.create(
                name=participant['name'],
                email=participant['email'],
                internal_id=uuid.uuid4().hex[:7].upper() # unique id
            )
            
            for act_title in participant['activity_titles']:
                act = Activity.objects.filter(title=act_title)[0]
                ActivityRegistration.objects.create(
                    activity=act,
                    participant=p,
                    pre_registered=True,
                    showed_up=False
                )
            
        except:
            print('Import went wrong')

    return redirect('participant_list')