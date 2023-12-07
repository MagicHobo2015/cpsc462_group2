# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestHospitalAppointment(TransactionCase):

    def setUp(self):
        super(TestHospitalAppointment, self).setUp()
        self.patient = self.env['hospital.patient'].create({'name': 'Test Patient', 'age': 25, 'gender': 'male'})
        self.doctor = self.env['hospital.doctor'].create({'doctor_name': 'Test Doctor', 'age': 40, 'gender': 'female'})
        self.appointment = self.env['hospital.appointment'].create({
            'patient_id': self.patient.id,
            'doctor_id': self.doctor.id,
            'note': 'Test Appointment',
        })

    def test_create_appointment(self):
        # Check if appointment is created successfully
        self.assertEqual(self.appointment.state, 'draft')

    def test_confirm_appointment(self):
        # Confirm the appointment and check if the state changes
        self.appointment.action_confirm()
        self.assertEqual(self.appointment.state, 'confirm')

    def test_done_appointment(self):
        # Confirm and then mark the appointment as done
        self.appointment.action_confirm()
        self.appointment.action_done()
        self.assertEqual(self.appointment.state, 'done')

    def test_cancel_appointment(self):
        # Confirm and then cancel the appointment
        self.appointment.action_confirm()
        self.appointment.action_cancel()
        self.assertEqual(self.appointment.state, 'cancel')

    def test_unlink_appointment(self):
        # Try to delete an appointment in the 'done' state and check for ValidationError
        self.appointment.action_confirm()
        self.appointment.action_done()
        with self.assertRaises(ValidationError):
            self.appointment.unlink()
