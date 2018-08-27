# Copyright © 2018 Matteo Bilotta (Link IT s.r.l.)
#
# GNU Affero General Public License v3.0

import re

from odoo import _, api, fields, models

JOIN_PATTERN = '(?:\.\s?)?'


class ResPartnerForm(models.Model):
    _name = 'res.partner.form'
    _description = "Legal form"
    _order = 'sequence, name, id'

    @classmethod
    def _get_pattern(cls, acronym):
        pattern = '(.*?)\s'

        for char in acronym:
            pattern += '%s%s' % (char, JOIN_PATTERN)

        return pattern

    @classmethod
    def _get_regex(cls, acronym):
        pattern = cls._get_pattern(acronym)
        regex = re.compile(pattern, re.IGNORECASE)

        return regex

    active = fields.Boolean(string=_("Active"), default=True)
    sequence = fields.Integer(string=_("Sequence"), index=True, default=10)

    name = fields.Char(string=_("Name"), index=True, required=True)
    acronym = fields.Char(string=_("Acronym"))

    # TODO: Should we add a new model 'res.partner.form.category'?

    country_id = fields.Many2one('res.country',
                                 string=_("Country"),
                                 required=True)

    @api.multi
    @api.depends('name', 'acronym')
    def _compute_display_name(self):
        for form in self:
            display_name = form.name

            if form.acronym:
                display_name += " (%s)" % form.acronym

            form.display_name = display_name

    @api.model
    def guess_by_name(self, name, country=None):
        domain = [('acronym', '!=', False)]

        if country:
            domain.append(('country_id', '=', country.id))

        legal_forms = self.search(domain)

        for form in legal_forms:
            regex = self._get_regex(form.acronym)
            result = regex.match(name)

            if result:
                return form, result.group(1)

        return False, name
