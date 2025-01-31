from repositories.manager_repository import ManagersRepository
from use_cases.colab.my_account.update_data.update_data_dto import UpdateDataDTO
from fastapi import Request, Response

class UpdateDataUseCase:
    manager_repository = ManagersRepository

    def __init__(self, manager_repository: ManagersRepository):
        self.manager_repository = manager_repository

    def execute(self, update_data_dto: UpdateDataDTO, response: Response, request: Request):
        manager_id = request.state.auth_payload["manager_id"]
        if not update_data_dto.name or not update_data_dto.email or not update_data_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Alteração não realizada, pois falta informações"}

        self.manager_repository.update_pwd(manager_id, update_data_dto.password)
        self.manager_repository.update_name(manager_id, update_data_dto.name)
        self.manager_repository.update_email(manager_id, update_data_dto.email)

        response.status_code = 202
        return{"status": "success", "message": "Atualização do cadastro realizado com sucesso"}