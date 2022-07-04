import uuid

from django.db.models import *


class users(Model):
    userId = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = CharField(max_length=100)
    nProblems = IntegerField


class problems(Model):
    problemId = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = CharField(max_length=1000)
    input = CharField(max_length=200)
    output = CharField(max_length=200)


class submissions(Model):
    problemId = ForeignKey(to=problems, on_delete=CASCADE)
    userId = ForeignKey(to=users, on_delete=CASCADE)
    time = DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    verdict = CharField(max_length=50)
