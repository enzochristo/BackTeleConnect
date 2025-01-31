from fastapi import APIRouter, Depends, Response
from use_cases.pessoa_juridica.logout.logout_use_case import LogoutPessoaJuridicaUseCase
from middlewares.validate_pessoa_juridica_auth_token import validate_pessoa_juridica_auth_token
router = APIRouter()


logout_pessoa_juridica_use_case = LogoutPessoaJuridicaUseCase()


@router.post("/pessoa-juridica/logout", dependencies=[Depends(validate_pessoa_juridica_auth_token)])
def logout_pessoa_juridica(response: Response):
    return logout_pessoa_juridica_use_case.execute(response)