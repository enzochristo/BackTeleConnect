from repositories.pessoa_fisica_repository import PessoaFisicasRepository
from use_cases.pessoa_fisica.my_account.update_data.update_data_dto import UpdateDataDTO
from fastapi import Request, Response

class UpdateDataUseCase:
    pessoa_fisica_repository = PessoaFisicasRepository

    def __init__(self, pessoa_fisica_repository: PessoaFisicasRepository):
        self.pessoa_fisica_repository = pessoa_fisica_repository

    def execute(self, update_data_dto: UpdateDataDTO, response: Response, request: Request):
        pessoa_fisica_id = request.state.auth_payload["pessoa_fisica_id"]
        if not update_data_dto.name or not update_data_dto.email or not update_data_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Alteração não realizada, pois falta informações"}

        self.pessoa_fisica_repository.update_pwd(pessoa_fisica_id, update_data_dto.password)
        self.pessoa_fisica_repository.update_name(pessoa_fisica_id, update_data_dto.name)
        self.pessoa_fisica_repository.update_email(pessoa_fisica_id, update_data_dto.email)

        response.status_code = 202
        return{"status": "success", "message": "Atualização do cadastro realizado com sucesso"}