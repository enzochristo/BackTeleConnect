from repositories.manager_repository import ManagersRepository
from fastapi import Request, Response

class getManagerName:
    def __init__(self, manager_repository: ManagersRepository) -> None:
        self.manager_repository = manager_repository

    def execute(self, response: Response, request:Request):
        manager_id = request.state.auth_payload["manager_id"]
        manager_name = self.manager_repository.get_name(manager_id)

        return {"status":"success", "manager_name":manager_name}