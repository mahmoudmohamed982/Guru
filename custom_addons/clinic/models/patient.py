from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError


class ClinicPatient(models.Model):
    _name = "patient.one"
    _description = "Clinic Patient"

    # =========================
    # Fields
    # =========================

    name = fields.Char(
        string="Patient Name",
        required=True
    )

    patient_code = fields.Char(
        string="Patient Code",
    )

    doctor_id = fields.Many2one(
        "clinic.doctor",
        string="Primary Doctor"
    )
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string="Gender"
    )

    date_of_birth = fields.Date(
        string="Date of Birth"
    )

    age = fields.Integer(
        string="Age",
        compute="_compute_age",
        store=True
    )

    blood_type = fields.Selection(
        [
            ('a+', 'A+'), ('a-', 'A-'),
            ('b+', 'B+'), ('b-', 'B-'),
            ('ab+', 'AB+'), ('ab-', 'AB-'),
            ('o+', 'O+'), ('o-', 'O-')
        ],
        string="Blood Type"
    )

    height = fields.Float(
        string="Height (cm)"
    )

    weight = fields.Float(
        string="Weight (kg)"
    )

    allergies = fields.Text(
        string="Allergies"
    )

    chronic_diseases = fields.Text(
        string="Chronic Diseases"
    )

    room_number = fields.Integer(
        string="Room Number"
    )

    is_active_patient = fields.Boolean(
        string="Active Patient",
        default=True
    )






    # =========================
    # SQL Constraints
    # =========================

    _sql_constraints = [
        (
            'unique_patient_code',
            'unique(patient_code)',
            'Patient code must be unique!'
        )
    ]

    # =========================
    # Compute Methods
    # =========================

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                dob = rec.date_of_birth
                rec.age = today.year - dob.year - (
                    (today.month, today.day) < (dob.month, dob.day)
                )
            else:
                rec.age = 0

    @api.model_create_multi
    def create(self, vals):
        records = super(ClinicPatient,self).create(vals)
        print('create')
        return records

    def _search(self, domain, offset=0, limit=None, order=None):
        print("Custom Search Running")
        return super()._search(domain, offset=offset, limit=limit, order=order)


