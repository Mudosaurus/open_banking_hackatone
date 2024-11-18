from hob_api.services import DBRouter


class StyleBankRouter(DBRouter):
    route_app_labels = {'style_bank'}
    db_name = 'style_bank_db'
