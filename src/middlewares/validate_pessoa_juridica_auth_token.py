import os
import jwt
from fastapi import Request, Response, HTTPException

def validate_pessoa_juridica_auth_token(request: Request, response: Response):
    token = request.cookies.get("pessoa_juridica_auth_token")
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    try:
        payload = jwt.decode(token.split(" ")[1], os.getenv("PJ_JWT_SECRET"), algorithms=["HS256"])
        pessoa_juridica_id = payload.get("id")
        pessoa_juridica_cnpj = payload.get("cnpj")  # Extração do CNPJ do payload

        # # Verificação do CNPJ (exemplo de verificação simples)
        # if not pessoa_juridica_cnpj or len(pessoa_juridica_cnpj) != 14:
        #     raise HTTPException(status_code=401, detail="Invalid CNPJ in JWT token")

        request.state.auth_payload = {
            "pessoa_juridica_id": pessoa_juridica_id,
            "pessoa_juridica_cnpj": pessoa_juridica_cnpj
        }
        print("Auth Payload recebido:", request.state.auth_payload)

    except jwt.PyJWTError:
        response.delete_cookie("pessoa_juridica_auth_token")
        raise HTTPException(status_code=401, detail="Invalid JWT token")
    
    return True
