from hob_api.services import DBRouter

EBankRouter = DBRouter
EBankRouter.db_name = 'e_bank_db'
EBankRouter.route_app_labels = {'e_bank'}
