from repositories.pessoa_fisica_repository import PessoaFisicasRepository
from use_cases.pessoa_fisica.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.pessoa_fisica import PessoaFisica

class RegisterUseCase:
    pessoa_fisica_repository = PessoaFisicasRepository

    def __init__(self, pessoa_fisica_repository: PessoaFisicasRepository):
        self.pessoa_fisica_repository = pessoa_fisica_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        if not register_dto.name or not register_dto.email or not register_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        pessoa_fisica = PessoaFisica(**register_dto.model_dump())

        self.pessoa_fisica_repository.save(pessoa_fisica)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro do avaliador com sucesso"}