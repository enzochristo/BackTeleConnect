from repositories.pessoa_juridica_repository import PessoaJuridicasRepository
from fastapi import Request, Response

class getPessoaJuridicaName:
    def __init__(self, pessoa_juridica_repository: PessoaJuridicasRepository) -> None:
        self.pessoa_juridica_repository = pessoa_juridica_repository

    def execute(self, response: Response, request:Request):
        pessoa_juridica_id = request.state.auth_payload["pessoa_juridica_id"]
        pessoa_juridica_name = self.pessoa_juridica_repository.get_name(pessoa_juridica_id)

        return {"status":"success", "pessoa_juridica_name":pessoa_juridica_name}