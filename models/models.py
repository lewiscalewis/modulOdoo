# -*- coding: utf-8 -*-

from odoo import models, fields, api

#este es el modelo para alumno con sus campos
class fcties_alumno(models.Model):
    _name = 'fcties.alumno'
    _description = 'Alumno'
    name = fields.Char(string="Nombre", required=True, help="Nombre del alumno")
    apellidos = fields.Char(string="Apellidos", required=True, help="Apellidos del alumno")
    fechanac = fields.Date(string="Fecha de nacimiento", required=True)
    fechai = fields.Integer(string="Año inicial del curso académico", required=True)
    curso = fields.Char(string="Curso académico", compute="_curso", required=True)
    correo = fields.Char(string="Correo electrónico")
    telefono = fields.Char(string="Teléfono")
    ciclo = fields.Selection([('0', 'DAM'), ('1', 'DAW'), ('2', 'ASIR')], string="Ciclo formativo", required=True)
    periodo = fields.Selection([('0', 'abril'), ('1', 'septiembre')], string="Periodo de prácticas", required=True)
    nota = fields.Float(string="Nota media", required=True)
    notatxt = fields.Char(string="Nota en formato texto", compute="_nota")
    empresa = fields.Many2one("fcties.empresa", string="Empresa", required=True)

#campos calculados
    @api.depends('fechai', 'curso')
    def _curso(self):
        for r in self:
            if len(str(r.fechai)) > 3:
                r.curso = str(r.fechai) + "/" + str(r.fechai + 1)[2:]
            else:
                r.curso = str(r.fechai) + "/" + str(r.fechai + 1)

    @api.depends('nota', 'notatxt')
    def _nota(self):
        for r in self:
            if r.nota >= 5 and r.nota < 7:
                r.notatxt = "Aprobado"
            elif r.nota >= 7 and r.nota < 9:
                r.notatxt = "Notable"
            elif r.nota >= 9:
                r.notatxt = "Sobresaliente"
            else:
                r.notatxt = "Suspenso"

#este es el modelo para empresa con sus campos
class fcties_empresa(models.Model):
    _name = 'fcties.empresa'
    _description = 'Empresa'
    name = fields.Char(string="Nombre", required=True, help="Nombre de la empresa colaboradora")
    nombrecontacto = fields.Char(string="Nombre de la persona de contacto", required=True)
    apellidoscontacto = fields.Char(string="Apellidos de la persona de contacto", required=True)
    telefonocontacto = fields.Integer(string="Teléfono de contacto", required=True)
    correo = fields.Char(string="Correo electrónico", required=True)
    direccion = fields.Char(string="Dirección completa", required=True)
    alumno = fields.One2many("fcties.alumno", "empresa", string="Alumnos")
