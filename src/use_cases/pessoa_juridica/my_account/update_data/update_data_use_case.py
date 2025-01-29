from repositories.pessoa_juridica_repository import PessoaJuridicasRepository
from use_cases.pessoa_juridica.my_account.update_data.update_data_dto import UpdateDataDTO
from fastapi import Request, Response

class UpdateDataUseCase:
    pessoa_juridica_repository = PessoaJuridicasRepository

    def __init__(self, pessoa_juridica_repository: PessoaJuridicasRepository):
        self.pessoa_juridica_repository = pessoa_juridica_repository

    def execute(self, update_data_dto: UpdateDataDTO, response: Response, request: Request):
        pessoa_juridica_id = request.state.auth_payload["pessoa_juridica_id"]
        if not update_data_dto.name or not update_data_dto.email or not update_data_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Alteração não realizada, pois falta informações"}

        self.pessoa_juridica_repository.update_pwd(pessoa_juridica_id, update_data_dto.password)
        self.pessoa_juridica_repository.update_name(pessoa_juridica_id, update_data_dto.name)
        self.pessoa_juridica_repository.update_email(pessoa_juridica_id, update_data_dto.email)

        response.status_code = 202
        return{"status": "success", "message": "Atualização do cadastro realizado com sucesso"}