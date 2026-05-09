from odoo import models, fields

class ClinicDoctor(models.Model):
    _name = "clinic.doctor"
    _description = "Clinic Doctor"

    name = fields.Char(required=True)
    specialization = fields.Char()

    patient_ids = fields.One2many(
        "patient.one",
        "doctor_id",
        string="Patients"
    )
