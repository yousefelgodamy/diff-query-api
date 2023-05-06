import logging
import json



class LambdaAbstractHandler:

    def handle(self, event: dict, context: object):
        logger = logging.getLogger()
        logger.log(level=1, msg=f"EVENT: {json.dumps(event)}")
        logger.log(level=1, msg=f"CONTEXT: {json.dumps(context)}")
        self._handle(event=event, context=context)

    def _handle(self, event: dict, context: object):
        pass