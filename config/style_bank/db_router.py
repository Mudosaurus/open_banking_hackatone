from hob_api.services import DBRouter

StyleBankRouter = DBRouter
StyleBankRouter.db_name = 'style_bank_db'
StyleBankRouter.route_app_labels = {'style_bank'}
