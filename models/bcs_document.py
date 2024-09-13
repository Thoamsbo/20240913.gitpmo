#from odoo import models, fields

from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.tools import format_amount, format_date, formatLang, groupby
from odoo.tools.float_utils import float_is_zero
from odoo.exceptions import UserError, ValidationError

class MyModel(models.Model):
    _name = 'bcs_document'
    
    item_number=fields.Char(string='编号')	
    state =fields.Char(string='状态')
    major_rev=fields.Char(string='版本')
    name = fields.Char(string='名称')    	
    classification=fields.Char(string='类型')
    description = fields.Text(string='描述')
	
	
    bcs_isrestricted = fields.Boolean(string='项目专属')
    has_change_pending = fields.Boolean(string='变更中')	
    has_files = fields.Boolean(string='附加文件')
	
    cn_productline = fields.Selection(
        string='生产线',
        selection=[
            ('icd', '芯片'),
            ('electronics', '电子'),
            ('auto', '汽配'),
            ('medical', '医材'),
            ('food', '食品'),
            ('nonstandard', '非标')
        ], default='icd', required=True)
		
    x_thomas = fields.Many2one(
        'x_thomastest0716', '关联Thomas',
        ondelete='cascade', required=False)

    # x_herbert = fields.One2many(
	# 'x_herberttest0715', 'x_doc2herbert', '关联herbert')

	
    #file显示的配置手法 filepropname,file namestring
    native_file=fields.Binary(string='文件')
    native_file_filename=fields.Char(string='文件')
    bcs_document_files = fields.One2many('bcs_document.files', 'bcs_document_id', '文件名')
    
    document2cad_id = fields.Many2one(
        'bcs_document', 'CAD',
        ondelete='cascade', required=False)
   # cn_document2cadship = fields.Many2one('bcs_document', related='document2cad_id', string='子阶工程图')
    cn_document2cadship = fields.One2many('bcs_document', 'document2cad_id', '关联工程图')
    
#    @api.model    
#    def create_with_existing(self, existing_record_id, other_values):
#        # 查询已存在的记录
#        existing_record = self.env['bcs_document_files.model'].browse(existing_record_id)
#        # 创建新行，将 existing_record 的ID设置到指定字段
#        new_record = self.create(dict(other_values, related_id=existing_record.id))
#        return new_record
    
    
class MyModel(models.Model):
    _name = 'bcs_document.files'
    
    bcs_document_id = fields.Many2one(
        'bcs_document', 'CAD',
        ondelete='cascade', required=False)
    file=fields.Binary(string='文件名')
    file_filename=fields.Char(string='文件名')
   



