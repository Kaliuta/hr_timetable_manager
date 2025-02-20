# -*- coding: utf-8 -*-

from odoo import fields, models


class Worktime(models.Model):
    _name = 'timetable.worktime'
    _description = 'Timetable Worktime'

    employee_id = fields.Many2one(comodel_name='hr.employee')
    period = fields.Date()
    d1 = fields.Float(string="1")
    d2 = fields.Float(string="2")
    d3 = fields.Float(string="3")
    d4 = fields.Float(string="4")
    d5 = fields.Float(string="5")
    d6 = fields.Float(string="6")
    d7 = fields.Float(string="7")
    d8 = fields.Float(string="8")
    d9 = fields.Float(string="9")
    d10 = fields.Float(string="10")
    d11 = fields.Float(string="11")
    d12 = fields.Float(string="12")
    d13 = fields.Float(string="13")
    d14 = fields.Float(string="14")
    d15 = fields.Float(string="15")
    d16 = fields.Float(string="16")
    d17 = fields.Float(string="17")
    d18 = fields.Float(string="18")
    d19 = fields.Float(string="19")
    d20 = fields.Float(string="20")
    d21 = fields.Float(string="21")
    d22 = fields.Float(string="22")
    d23 = fields.Float(string="23")
    d24 = fields.Float(string="24")
    d25 = fields.Float(string="25")
    d26 = fields.Float(string="26")
    d27 = fields.Float(string="27")
    d28 = fields.Float(string="28")
    d29 = fields.Float(string="29")
    d30 = fields.Float(string="30")
    d31 = fields.Float(string="31")

    schedule_d1 = fields.Selection(related='employee_id.schedule_id.d1')
    schedule_d2 = fields.Selection(related='employee_id.schedule_id.d2')
    schedule_d3 = fields.Selection(related='employee_id.schedule_id.d3')
    schedule_d4 = fields.Selection(related='employee_id.schedule_id.d4')
    schedule_d5 = fields.Selection(related='employee_id.schedule_id.d5')
    schedule_d6 = fields.Selection(related='employee_id.schedule_id.d6')
    schedule_d7 = fields.Selection(related='employee_id.schedule_id.d7')
    schedule_d8 = fields.Selection(related='employee_id.schedule_id.d8')
    schedule_d9 = fields.Selection(related='employee_id.schedule_id.d9')
    schedule_d10 = fields.Selection(related='employee_id.schedule_id.d10')
    schedule_d11 = fields.Selection(related='employee_id.schedule_id.d11')
    schedule_d12 = fields.Selection(related='employee_id.schedule_id.d12')
    schedule_d13 = fields.Selection(related='employee_id.schedule_id.d13')
    schedule_d14 = fields.Selection(related='employee_id.schedule_id.d14')
    schedule_d15 = fields.Selection(related='employee_id.schedule_id.d15')
    schedule_d16 = fields.Selection(related='employee_id.schedule_id.d16')
    schedule_d17 = fields.Selection(related='employee_id.schedule_id.d17')
    schedule_d18 = fields.Selection(related='employee_id.schedule_id.d18')
    schedule_d19 = fields.Selection(related='employee_id.schedule_id.d19')
    schedule_d20 = fields.Selection(related='employee_id.schedule_id.d20')
    schedule_d21 = fields.Selection(related='employee_id.schedule_id.d21')
    schedule_d22 = fields.Selection(related='employee_id.schedule_id.d22')
    schedule_d23 = fields.Selection(related='employee_id.schedule_id.d23')
    schedule_d24 = fields.Selection(related='employee_id.schedule_id.d24')
    schedule_d25 = fields.Selection(related='employee_id.schedule_id.d25')
    schedule_d26 = fields.Selection(related='employee_id.schedule_id.d26')
    schedule_d27 = fields.Selection(related='employee_id.schedule_id.d27')
    schedule_d28 = fields.Selection(related='employee_id.schedule_id.d28')
    schedule_d29 = fields.Selection(related='employee_id.schedule_id.d29')
    schedule_d30 = fields.Selection(related='employee_id.schedule_id.d30')
    schedule_d31 = fields.Selection(related='employee_id.schedule_id.d31')
