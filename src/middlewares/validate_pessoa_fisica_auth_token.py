import os
import jwt
from fastapi import Request, Response, HTTPException

def validade_pessoa_fisica_auth_token(request: Request, response: Response):
    token = request.cookies.get("pessoa_fisica_auth_token")
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    try:
        payload = jwt.decode(token.split(" ")[1], os.getenv("PF_JWT_SECRET"), algorithms=["HS256"])
        pessoa_fisica_id = payload.get("id")
        pessoa_fisica_email = payload.get("email")

        request.state.auth_payload = {"pessoa_fisica_id": pessoa_fisica_id, "pessoa_fisica_email": pessoa_fisica_email}

    except jwt.PyJWTError:
        response.delete_cookie("pessoa_fisica_auth_token")

        raise HTTPException(status_code=401, detail="Invalid JWT token")
    
    return True