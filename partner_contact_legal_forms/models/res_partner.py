# Copyright © 2018 Matteo Bilotta (Link IT s.r.l.)
#
# GNU Affero General Public License v3.0

from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    legal_form_id = fields.Many2one('res.partner.form', string=_("Legal form"))

    @api.onchange
    def _onchange_name(self):
        if self.name and self.is_company:
            import pdb; pdb.set_trace()

            legal_form = self.env['res.partner.form'].guess_by_name(self.name, self.country_id)

    # @api.multi
    # @api.depends('is_company', 'name', 'parent_id.name',
    #              'type', 'company_name', 'legal_form')
    # def _compute_display_name(self):
    #     super()._compute_display_name()
    #
    # @api.multi
    # def name_get(self):
    #     #
    #     # The best thing could be to concatenate partner's
    #     #  name with legal form's acronym.
    #     # For example, something like...
    #     #
    #     #    [...]
    #     #
    #     #  for partner in self:
    #     #      name = partner.name
    #     #
    #     #      if partner.legal_form_id and \
    #     #         partner.legal_form_id.acronym:
    #     #          name += " %s" % partner.legal_form_id.acronym
    #     #
    #     #    [...]
    #     #
    #     # But, unfortunately, 'name_get' method on 'res.partner' model
    #     #  in Odoo's 'base' core module looks like s**t! :(
    #     # Rewriting 'name_get' method means breaking something,
    #     #  somewhere in someone's module for sure... So?
    #     #
    #     # TODO: Rewrite 'name_get' method or... ?
    #     #
