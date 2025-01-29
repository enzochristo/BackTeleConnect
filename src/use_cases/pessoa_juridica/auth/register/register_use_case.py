from repositories.pessoa_juridica_repository import PessoaJuridicasRepository
from use_cases.pessoa_juridica.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.pessoa_juridica import PessoaJuridica

class RegisterUseCase:
    pessoa_juridica_repository = PessoaJuridicasRepository

    def __init__(self, pessoa_juridica_repository: PessoaJuridicasRepository):
        self.pessoa_juridica_repository = pessoa_juridica_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        if not register_dto.name or not register_dto.email or not register_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        pessoa_juridica = PessoaJuridica(**register_dto.model_dump())

        self.pessoa_juridica_repository.save(pessoa_juridica)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro da empresa salvo com sucesso"}