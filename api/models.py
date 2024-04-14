from django.db import models
from django.contrib.auth.models import User


## Models


class Department(models.Model):
    short_name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=100)

    def __str__(self):
        return '%s: %s' % (self.short_name, self.long_name)

    def get_members(self):
        return Member.objects.filter(department=self)


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_department_name(self):
        return str(self.department)

    def get_tasks(self):
        return Task.objects.filter(member=self)
    
    def get_total_task_time(self):
        pass #### sum durations


class Team(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    coordinator = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_functions(self):
        return Function.objects.filter(team=self)


class Function(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    observations = models.TextField()
    members_needed_min = models.IntegerField()
    members_needed_max = models.IntegerField()
    vols_needed = models.IntegerField(default=0)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_tasks(self):
        return Task.objects.filter(function=self)

    def get_tasks_date(self, date):
        pass
    

class Building(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_spaces(self):
        return Space.objects.filter(building=self)


class Space(models.Model):
    name = models.CharField(max_length=30)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_building_name(self):
        return self.building.name

    def get_tasks(self):
        return Task.objects.filter(space=self)
    
    def get_tasks_date(self, date):
        pass


class Task(models.Model):
    date = models.DateField()
    hour_start = models.TimeField()
    hour_end = models.TimeField()
    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (str(self.function), str(self.date))
    
    def get_function_title(self):
        return str(self.function)
    
    def get_space_name(self):
        return str(self.space)
    
    def get_member_name(self):
        return str(self.member)


class Resource(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    #pickup = models.ForeignKey(Space, on_delete=models.CASCADE)
    #storage = models.ForeignKey(Space, on_delete=models.CASCADE)
    total_quantity = models.IntegerField()
    used_quantity = models.IntegerField(default=0)


class ResourceAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    stored = models.BooleanField(default=True)


class Activity(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    hour_start = models.TimeField()
    hour_end = models.TimeField()
    space = models.ForeignKey(Space, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_participants(self):
        participants = []
        registrations = ActivityRegistration.objects.filter(activity=self)

        for reg in registrations:
            participants.append(reg.participant)

        return participants


class Participant(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    internal_id = models.CharField(max_length=30)

    def get_act_registrations(self):
        return ActivityRegistration.objects.filter(participant=self)


class ActivityRegistration(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    pre_registered = models.BooleanField(default=False)
    showed_up = models.BooleanField(default=False)