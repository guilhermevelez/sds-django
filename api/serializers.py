from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Department, Member, Team, Function, Building, Space, Task, Activity, Participant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class DepartmentSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'short_name', 'long_name', 'members']

    def get_members(self, department):
        return [{
            'id': m.id,
            'name': str(m),
            'email': m.email
        } for m in department.get_members()]


class MemberSerializer(serializers.ModelSerializer):
    department_obj = serializers.SerializerMethodField(read_only=True)
    tasks = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'phone', 'department', 'department_obj', 'admin', 'tasks']
        extra_kwargs = {'department': {'write_only': True}}
    
    def get_department_obj(self, member):
        return {
            'id': member.department.id,
            'name': member.get_department_name()
        }
    
    def get_tasks(self, member):
        return [{
            'id': t.id,
            'title': t.get_function_title(),
            'date': t.date
        } for t in member.get_tasks()]
    

class TeamSerializer(serializers.ModelSerializer):
    coordinator_obj = serializers.SerializerMethodField(read_only=True)
    tasks = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'title', 'description', 'coordinator', 'coordinator_obj', 'tasks']
        extra_kwargs = {'coordinator': {'write_only': True}}
    
    def get_coordinator_obj(self, team):
        return {
            'id': team.coordinator.id,
            'name': str(team.coordinator)
        }
    
    def get_tasks(self, team):
        tasks = []
        for f in team.get_functions():
            for t in f.get_tasks():
                tasks.append({
                    'id': t.id,
                    'title': f.title,
                    'date': t.date,
                    'space': t.space
                })

        return tasks


class FunctionSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Function
        fields = [
            'id',
            'title',
            'description',
            'members_needed_min',
            'members_needed_max',
            'vols_needed',
            'observations',
            'tasks']
    
    def get_tasks(self, function):
        return [{
            'id': t.id,
            'date': t.date,
            'space': str(t.space)
        } for t in function.get_tasks()]


class BuildingSerializer(serializers.ModelSerializer):
    spaces = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Building
        fields = ['id', 'name', 'spaces']
    
    def get_spaces(self, building):
        return [{
            'id': s.id,
            'name': str(s)
        } for s in building.get_spaces()]
    

class SpaceSerializer(serializers.ModelSerializer):
    building_obj = serializers.SerializerMethodField(read_only=True)
    tasks = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Space
        fields = ['id', 'name', 'building', 'building_obj', 'tasks']
        extra_kwargs = {'building': {'write_only': True}}
    
    def get_building_obj(self, space):
        return {
            'id': space.building.id,
            'name': space.get_building_name()
        }
    
    def get_tasks(self, space):
        return [{
            'id': t.id,
            'title': t.get_function_title(),
            'date': t.date ## Horario tb
        } for t in space.get_tasks()]


class TaskSerializer(serializers.ModelSerializer):
    function_obj = serializers.SerializerMethodField(read_only=True)
    space_obj = serializers.SerializerMethodField(read_only=True)
    member_obj = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'date', 'hour_start', 'hour_end', 'function', 'function_obj', 'space', 'space_obj', 'member', 'member_obj']
        extra_kwargs = {'function': {'write_only': True}, 'space': {'write_only': True}, 'member': {'write_only': True}}
    
    def get_function_obj(self, task):
        return {
            'id': task.function.id,
            'title': task.get_function_title()
        }
    
    def get_space_obj(self, task):
        return {
            'id': task.space.id,
            'name': task.get_space_name()
        }
    
    def get_member_obj(self, task):
        return {
            'id': task.member.id,
            'name': str(task.member)
        }


class ActivitySerializer(serializers.ModelSerializer):
    space_obj = serializers.SerializerMethodField(read_only=True)
    participants = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'title', 'date', 'hour_start', 'hour_end', 'space', 'space_obj', 'participants']
        extra_kwargs = {'space': {'write_only': True}}
    
    def get_space_obj(self, act):
        return {
            'id': act.space.id,
            'name': str(act.space)
        }
    
    def get_participants(self, act):
        return [{
            'id': p.id,
            'name': p.name,
            'internal_id': p.internal_id
        } for p in act.get_participants()]
    

class ParticipantSerializer(serializers.ModelSerializer):
    activities = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Participant
        fields = ['id', 'name', 'email', 'internal_id', 'activities']
    
    def get_activities(self, participant):
        return [{
            'id': act.id,
            'title': act.title,
            'date': act.date,
            'hour_start': act.hour_start,
            'hour_end': act.hour_end
        } for act in participant.get_activities()]