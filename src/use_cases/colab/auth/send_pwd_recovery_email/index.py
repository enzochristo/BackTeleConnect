from repositories.manager_repository import ManagersRepository
from fastapi import FastAPI, Request, Response
from use_cases.colab.auth.send_pwd_recovery_email.send_pwd_recovery_email_use_case import SendPwdRecoveryEmailUseCase
from use_cases.colab.auth.send_pwd_recovery_email.send_pwd_recovery_email_dto import SendPwdRecoveryEmailDTO
from fastapi import APIRouter

router = APIRouter()

managers_repository = ManagersRepository()
send_pwd_recovery_email_use_case = SendPwdRecoveryEmailUseCase(managers_repository)

@router.post("/manager/auth/pwd/recovery/email")
def send_pwd_recovery_email(send_pwd_recovery_email_dto: SendPwdRecoveryEmailDTO, response: Response, request: Request):
    return send_pwd_recovery_email_use_case.execute(send_pwd_recovery_email_dto, response, request)
    