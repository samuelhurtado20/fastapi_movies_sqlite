import json
import os
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from middlewares.jwt_manager import validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        auth: HTTPAuthorizationCredentials | None = await super().__call__(request)
        data = validate_token(auth.credentials)
        print(data.body.decode())
        result = json.loads(data.body.decode())
        print(result.get("message"))
        if result.get("message"):
            raise HTTPException(status_code=401, detail="Invalid crendentials")
