from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
class TestHospitalDoctor(TransactionCase):

    def setUp(self):
        super(TestHospitalDoctor, self).setUp()
        self.doctor_data = {
            'doctor_name': 'Dr. John Doe',
            'age': 35,
            'gender': 'male',
            'note': 'Experienced doctor',
            'active': True,
        }

    def test_create_doctor(self):
        doctor = self.env['hospital.doctor'].create(self.doctor_data)
        self.assertEqual(doctor.doctor_name, 'Dr. John Doe')
        self.assertEqual(doctor.age, 35)
        self.assertEqual(doctor.gender, 'male')
        self.assertEqual(doctor.note, 'Experienced doctor')
        self.assertTrue(doctor.active)

    def test_copy_doctor(self):
        original_doctor = self.env['hospital.doctor'].create(self.doctor_data)
        copied_doctor = original_doctor.copy()
        self.assertEqual(copied_doctor.doctor_name, 'Dr. John Doe (Copy)')
        self.assertEqual(copied_doctor.note, 'Copied Record')

    def test_invalid_age(self):
        with self.assertRaises(ValidationError):
            # Trying to create a doctor with an invalid age (negative value)
            invalid_doctor_data = self.doctor_data.copy()
            invalid_doctor_data['age'] = -5
            self.env['hospital.doctor'].create(invalid_doctor_data)
