from hob_api.services import DBRouter


class ConsentRouter(DBRouter):
    route_app_labels = {'consent_service'}
    db_name = 'consent_db'
