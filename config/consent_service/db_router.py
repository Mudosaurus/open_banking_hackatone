from hob_api.services import DBRouter

ConsentRouter = DBRouter
ConsentRouter.db_name = 'consent_db'
ConsentRouter.route_app_labels = {'consent_service'}
