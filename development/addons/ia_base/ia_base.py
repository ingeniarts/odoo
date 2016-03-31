# -*- coding: utf-8 -*-

import logging
from openerp import models, api
import pdb

_logger = logging.getLogger(__name__)


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