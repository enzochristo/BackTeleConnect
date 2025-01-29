from repositories.pessoa_fisica_repository import PessoaFisicasRepository
from fastapi import FastAPI, Request, Response
from use_cases.pessoa_fisica.auth.send_pwd_recovery_email.send_pwd_recovery_email_use_case import SendPwdRecoveryEmailUseCase
from use_cases.pessoa_fisica.auth.send_pwd_recovery_email.send_pwd_recovery_email_dto import SendPwdRecoveryEmailDTO
from fastapi import APIRouter

router = APIRouter()

pessoa_fisicas_repository = PessoaFisicasRepository()
send_pwd_recovery_email_use_case = SendPwdRecoveryEmailUseCase(pessoa_fisicas_repository)

@router.post("/pessoa/fisica/auth/pwd/recovery/email")
def send_pwd_recovery_email(send_pwd_recovery_email_dto: SendPwdRecoveryEmailDTO, response: Response, request: Request):
    return send_pwd_recovery_email_use_case.execute(send_pwd_recovery_email_dto, response, request)
    