from hob_api.services import DBRouter


class EBankRouter(DBRouter):
    route_app_labels = {'e_bank'}
    db_name = 'e_bank_db'
