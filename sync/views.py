
from django.http import HttpResponse
from django.shortcuts import render
from models import Run, Step, Value

__author__ = 'kenneth'


def index(request):
    runs = Run.objects.all()
    ir_step = []
    ir_value = []
    ic_step = []
    ic_value = []
    for r in runs:
        steps = Step.objects.filter(run_id=r.run_id)
        for s in steps:
            ir_step.append(s)
            ic_step.append(ir_step)
            ir_step = []
        values = Value.objects.filter(run_id=r.run_id)
        for v in values:
            ir_value.append(v)
            ic_value.append(ir_value)
            ir_value = []

    return render(request, 'index.html', {'step': ic_step, 'value': ic_value})