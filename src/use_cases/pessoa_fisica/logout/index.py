from fastapi import APIRouter, Depends, Response
from use_cases.pessoa_fisica.logout.logout_use_case import LogoutPessoaFisicaUseCase
from middlewares.validate_pessoa_fisica_auth_token import validate_pessoa_fisica_auth_token

router = APIRouter()
logout_pessoa_fisica_use_case = LogoutPessoaFisicaUseCase()

@router.post("/pessoa/fisica/logout", dependencies=[Depends(validate_pessoa_fisica_auth_token)])
def logout(response: Response):
    return logout_pessoa_fisica_use_case.execute(response)
