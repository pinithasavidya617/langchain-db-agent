from fastapi import APIRouter
from starlette import status
from starlette.exceptions import HTTPException

from api_models import QueryRequest, QueryResponse
from db_agent import query_db_with_natural_language

router = APIRouter(prefix="/agent", tags=["DB Agent"])

@router.post(path="/", response_model=QueryResponse)
def query_db(request: QueryRequest) -> QueryResponse:
    try:
        thread_id = request.thread_id or "1"
        result = query_db_with_natural_language(request.query, thread_id=thread_id)
        return QueryResponse(query=request.query, result=result, thread_id=thread_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))