# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fctie_alumno(models.Model):
    _name = 'fcties.alumno'
    _description = 'Alumno'
    name = fields.char(string="Nombre", required=True, help="Introduce el nombre del alumno")
    apellidos = fields.char(string="Apellidos", required=True, help="Introduce el apellido del alumno")
    fechanac = fields.date(string="Fecha de nacimiento", required=True)
    fechai = fields.Integer(string="Año inicial del curso académico", required=True)
    curso = fields.char(string="Curso académico", compute="_curso", required=True)
    correo = fields.char(string="correo electrónico")
    telefono = fields.integer(string="Teléfono")
    ciclo = fields.selection({('0', 'DAM'), ('1', 'DAW'), ('2', 'ASIR')}, string="Ciclo formativo", required=True)
    periodo = fields.selection({('0', 'abril'), ('1', 'septiembre')}, string="Periodo de prácticas", required=True)
    nota = fields.float(string="Nota media", required=True)
    notatxt = fields.char(string="Nota en formato texto", compute="_nota")
    empresa = fields.many2one("fcties.empresa", string="Empresa", required=True)

    @api.depends('nota', 'notatxt')
    def _nota(self):
        for r in self:
            if 5 <= r.nota < 7:
                r.notatxt = "Aprobado"
            elif 7 <= r.nota < 9:
                r.notatxt = "Notable"
            elif r.nota > 9:
                r.notatxt = "Sobresaliente"
        else:
            r.notatxt = "suspenso"

    @api.depends('fecha', 'curso')
    def _curso(self):
        for r in self:
            if len(str(r.fechai)) > 2:
                r.curso = str(r.fecha) + "/" + str(r.fechai + 1)[2:]
            else:
                r.curso = str(r.fechai) + "/" + str(r.fechai + 1)


class fcties_empresa(models.Model):
    _name = 'fcties.empresa'
    _description = 'Empresa'
    name = fields.Char(string="Nombre", required=True, help="Nombre de la empresa colaboradora")
    nombrecontacto = fields.Char(string="Nombre de la persona de contacto", required=True)
    apellidocontacto = fields.Char(string="Apellidos de la persona de contacto", required=True)
    telefonocontacto = fields.Char(string="Teléfono de la persona de contacto", required=True)
    correo = fields.Char(string="Correo electrónico", required=True)
    direccion = fields.Char(string="Dirección completa", required=True)
    alumno = fields.One2many("fcties.alumno", "empresa", string="Alumnos")
