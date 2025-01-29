from repositories.pessoa_fisica_repository import PessoaFisicasRepository
from fastapi import Request, Response

class getPessoaFisicaName:
    def __init__(self, pessoa_fisica_repository: PessoaFisicasRepository) -> None:
        self.pessoa_fisica_repository = pessoa_fisica_repository

    def execute(self, response: Response, request:Request):
        pessoa_fisica_id = request.state.auth_payload["pessoa_fisica_id"]
        pessoa_fisica_name = self.pessoa_fisica_repository.get_name(pessoa_fisica_id)

        return {"status":"success", "pessoa_fisica_name":pessoa_fisica_name}