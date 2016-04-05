# -*- coding: utf-8 -*-

import logging
from openerp import models, api
import pdb

_logger = logging.getLogger(__name__)

class IAModelData(models.Model):
    _inherit = "ir.model.data"

    @api.model
    def set_noupdate(self, external_id, new_noupdate_value):
        record_ids = self.search([('name', '=', external_id)])
        record_ids.write({'noupdate': new_noupdate_value})

class IALang(models.Model):
    _inherit = "res.lang"

    @api.model
    def create(self, vals):
        if 'code' in vals:
            lang_records = self.search([('code', '=', vals['code'])])
            if len(lang_records) == 0:
                return super(IALang, self).create(vals)
            else:
                return self


class IAPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        _logger.info("Setting partner data...")
        overriden_id = vals.get('overriden_id', False)
        if overriden_id:
            # this is an inheritance
            del vals['overriden_id']
            super(IAPartner, self.browse(overriden_id)).write(vals)
            return self
        return super(IAPartner, self).create(vals)


class IACompany(models.Model):
    _inherit = "res.company"

    @api.model
    def create(self, vals):
        _logger.info("Setting company data...")
        overriden_id = vals.get('overriden_id', False)
        if overriden_id:
            # this is an inheritance
            del vals['overriden_id']
            super(IACompany, self.browse(overriden_id)).write(vals)
            return self
        return super(IACompany, self).create(vals)
