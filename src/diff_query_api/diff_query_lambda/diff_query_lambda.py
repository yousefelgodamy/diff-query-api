from diff_query_api.abstract_lambda_handler import LambdaAbstractHandler
from diff_query_api.diff_query_lambda.diff_query_lambda_models import DiffQueryRequest, DiffQueryResponse

class DiffQueryLambda(LambdaAbstractHandler):
    def _handle(self, event: dict, context: object) -> str:
        '''
        :param event: Lambda event that will be typed to DiffQueryRequest
        :param context: Lambda context object
        :returns: JSON typed to DiffQueryResponse
        '''
        validated_event = DiffQueryRequest.parse_obj(event)


        
