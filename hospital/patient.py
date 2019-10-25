from odoo import models,fields,api
class Hospital(models.Model):
    _name="hospital.patient"
    _description="Hospital managment"
    # _inherit=['mail.thread','mail.activity.mixin']
    _rec_name="patient_name"
    patient_name=fields.Char(string='Name')
    patient_age=fields.Integer(string='Age')
    notes=fields.Text(string="Notes")
    image=fields.Binary(string="Image")
    name_sec=fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True,
                         default=lambda self:('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_sec', ('New')) == ('New'):
            vals['name_sec'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')

        result = super(Hospital, self).create(vals)
        return result
