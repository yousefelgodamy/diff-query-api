from diff_query_api.diff_query_models import EventTypeEnum, DiffQueryCallModelRequest, DiffQueryCallModelResponse, \
    DiffQueryGetDiffRequest, DiffQueryGetDiffResponse
import diff_match_patch
import logging
import openai
import json
import os

class DiffQueryExecutor:
    
    def __init__(self) -> None:
        self.logger = logging.getLogger()
        self.dmp = diff_match_patch.diff_match_patch()
        super().__init__()

    def _log(self, event: str, event_type: EventTypeEnum) -> None:
        self.logger.log(level=1, msg=f"{str(event_type)}: {json.dumps(event)}")

    def get_diff(self, request: DiffQueryGetDiffRequest) -> str:
        self._log(event=request.json(), event_type=EventTypeEnum.REQUEST)
        diff = self.dmp.diff_main(text1=request.primaryText, text2=request.secondaryText)
        self.dmp.diff_cleanupSemantic(diffs=diff)

        response = DiffQueryGetDiffResponse(textDiff=list(diff)).json()
        self._log(event=response, event_type=EventTypeEnum.RESPONSE)
        return response

    def call_model(self, request: DiffQueryCallModelRequest) -> str:
        self._log(event=request.json(), event_type=EventTypeEnum.REQUEST)

        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=str.join(DiffQueryCallModelRequest.textDiff, DiffQueryCallModelRequest.query),
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        self._log(event=response, event_type=EventTypeEnum.RESPONSE)

        return response
    