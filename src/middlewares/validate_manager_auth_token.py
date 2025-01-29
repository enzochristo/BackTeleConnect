import os
import jwt
from fastapi import Request, Response, HTTPException

def validade_manager_auth_token(request: Request, response: Response):
    token = request.cookies.get("manager_auth_token")
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    try:
        payload = jwt.decode(token.split(" ")[1], os.getenv("MANAGER_JWT_SECRET"), algorithms=["HS256"])
        manager_id = payload.get("id")
        manager_email = payload.get("email")
        manager_cpf = payload.get("cpf")

        request.state.auth_payload = {"manager_id": manager_id, "manager_email": manager_email, "manager_cpf": manager_cpf}

    except jwt.PyJWTError:
        response.delete_cookie("manager_auth_token")

        raise HTTPException(status_code=401, detail="Invalid JWT token")
    
    return True