from django.conf import settings
from django.db import models
from temba_client.v2 import TembaClient

__author__ = 'kenneth'

class Run(models.Model):
    run_id = models.IntegerField(default=0)
    responded = models.BooleanField(default=False)
    created_on = models.DateTimeField(null=True)
    modified_on = models.DateTimeField(null=True)

    @classmethod
    def get_run(cls):
        client = TembaClient(settings.HOST, settings.KEY)
        runs = client.get_runs().all()
        initial_runs = 0
        for run in runs:
            if not cls.run_exists(run):
                cls.objects.create(id=run.id, responded=run.responded,
                                   created_on=run.created_on, modified_on=run.modified_on)

                k= Run.objects.get(run_id=run.run_id)
                Value.get_values(values=run.values, run_id=k)
                Step.get_steps(path=run.path, run_id=k)
                initial_runs += 1

        return initial_runs

    @classmethod
    def run_exists(cls, run):
        return cls.objects.filter(run_id=run.run_id).exists()

    def __unicode__(self):
        return self.run_id



class Contact(models.Model):
    uuid = models.CharField(max_length=16)
    name = models.CharField(max_length=100, null=True)
    urn = models.CharField(max_length=100, null=True)

    @classmethod
    def get_contact(cls):
        client = TembaClient(settings.HOST, settings.KEY)
        contacts = client.get_contacts().all()
        for contact in contacts:
            cls.objects.create(uuid=contact.uuid, name=contact.name, urn=contact.urn)


class Step(models.Model):
    node = models.CharField(max_length=100)
    time = models.DateTimeField()
    run_id = models.ForeignKey(Run, null=True)

    @classmethod
    def get_step(cls, path, runid):
        for paths in path:
            cls.objects.create(node=paths.node, time=paths.time, run_id=runid)

    def __str__(self):
        return self.node


class Value(models.Model):
    value = models.CharField(max_length=20)
    run_id = models.ForeignKey(Run, null=True)

    @classmethod
    def get_values(cls, values, runid):
        for val in values:
            cls.objects.create(value=val, run_id=runid)

    def __str__(self):
        return self.value

class Flow(models.Model):
    uuid = models.CharField(max_length=16)
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    complete_runs = models.IntegerField(default=0)
    interrupted_runs = models.IntegerField(default=0)
    expired_runs = models.IntegerField(default=0)
    run_id = models.ForeignKey(Run, null=True)

    @classmethod
    def get_flow(cls):
        client = TembaClient(settings.HOST, settings.KEY)
        flows = client.get_flows().all()
        for flow in flows:
            cls.objects.create(uuid=flow.uuid, name=flow.name, created_on=flow.created_on,
                               complete_runs=flow.runs.completed, interrupted_runs=flow.runs.interrupted,
                               expired_runs=flow.runs.expired)



