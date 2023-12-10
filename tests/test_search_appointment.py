from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestSearchAppointmentWizard(TransactionCase):

    def setUp(self):
        super(TestSearchAppointmentWizard, self).setUp()
        self.patient = self.env['hospital.patient'].create({'name': 'Test Patient', 'age': 25, 'gender': 'male'})
        self.wizard = self.env['search.appointment.wizard'].create({'patient_id': self.patient.id})

    def test_action_search_appointment_m1(self):
        action_result = self.wizard.action_search_appointment_m1()
        self.assertEqual(action_result['res_model'], 'hospital.appointment')
        self.assertEqual(action_result['view_mode'], 'tree,form')
        self.assertEqual(action_result['domain'], [('patient_id', '=', self.patient.id)])
        self.assertEqual(action_result['target'], 'current')

