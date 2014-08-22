# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc - Avanced Open Source Consulting
#    Copyright (C) 2011 - 2013 Avanzosc <http://www.avanzosc.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
import time
from osv import osv
from osv import fields
from tools.translate import _

class sample_rank(osv.osv):

    _name = 'sample.rank'
    _description = 'Sample Rank'
   
    _columns = {'name':fields.char('Description', size=250, required=True),
                'product_id': fields.many2one('product.product', 'Product'),
                'category_id': fields.many2one('product.category', 'Category'),
                'sample_rank_lines_ids':fields.one2many('sample.rank.line','sample_rank_id','Sample Rank Lines'),
                }

sample_rank()