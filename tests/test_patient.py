from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestHospitalPatient(TransactionCase):

    def setUp(self):
        super(TestHospitalPatient, self).setUp()
        self.patient = self.env['hospital.patient'].create({'name': 'John Doe'})

    def test_create_patient(self):
        self.assertEqual(self.patient.name, 'John Doe')
        self.assertEqual(self.patient.state, 'draft')

    def test_confirm_patient(self):
        self.patient.action_confirm()
        self.assertEqual(self.patient.state, 'confirm')

    def test_done_patient(self):
        self.patient.action_done()
        self.assertEqual(self.patient.state, 'done')

    def test_draft_patient(self):
        self.patient.action_draft()
        self.assertEqual(self.patient.state, 'draft')

    def test_cancel_patient(self):
        self.patient.action_cancel()
        self.assertEqual(self.patient.state, 'cancel')

    def test_create_patient_with_duplicate_name(self):
        with self.assertRaises(ValidationError):
            self.env['hospital.patient'].create({'name': 'John Doe'})

    def test_create_patient_with_zero_age(self):
        with self.assertRaises(ValidationError):
            self.env['hospital.patient'].create({'name': 'Jane Doe', 'age': 0})

    def test_open_appointments(self):
        action = self.patient.action_open_appointments()
        self.assertEqual(action['type'], 'ir.actions.act_window')
        self.assertEqual(action['res_model'], 'hospital.appointment')
        self.assertEqual(action['domain'], [('patient_id', '=', self.patient.id)])
        self.assertEqual(action['context'], {'default_patient_id': self.patient.id})
        self.assertEqual(action['view_mode'], 'tree,form')
        self.assertEqual(action['target'], 'current')
