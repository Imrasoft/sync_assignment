from django.test import TestCase
from models import Run

__author__ = 'kenneth'


class TestRun(TestCase):
    def test_add_runs(self):
        run_count = Run.objects.count()
        added_runs = Run.add_runs()
        self.assertEquals(Run.objects.count(), run_count + added_runs)

    def test_run_exists(self):
        class R(object):
            def __init__(self, id=None, flow=None, contact=None, responded=None, path=None, values=None):

                self.id = id
                self.flow = flow
                self.contact = contact
                self.responded = responded
                self.path = path
                self.values = values

                #created_on = models.DatetimeField()
                #modified_on = models.DatetimeField()
                #exited_on = models.DatetimeField()
                #exit_type = SimpleField()

        rapidpro_mock_run = R(id='001A', flow='Axx', contact='Allan', path=None, values=None)
        self.assertEquals(Run.group_exists(rapidpro_mock_run), False)
        Run.objects.create(id='001A', flow='Axx', contact='Allan', path=None, values=None)
        self.assertEquals(Run.group_exists(rapidpro_mock_run), True)

