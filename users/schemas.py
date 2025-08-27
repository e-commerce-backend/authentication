from pydantic import Field,BaseModel,EmailStr, model_validator

from typing import Optional

class UserBase(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:EmailStr
    phone_number:str
    country:str
    address:str
    is_superuser:bool
        
    class Config:
        from_attributes=True


class UserSend(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    phone_number:str
    country:str
    address:str
    class Config:
        from_attributes=True
        


class UserCreate(BaseModel):
    first_name:str=Field(
        ...,
        max_length=40,
        min_length=2,
        description="Primer Nombre"

)
    last_name:str=Field(
        ...,
        max_length=40,
        min_length=2,
        description="Apellidos"

)


    password: str=Field(
        ...,
        min_length=8,
        
        description="La contraseña debe tener minimo 8 caracteres y contener un caracter especial"                
                        )
    
    email:EmailStr=Field(...)
    phone_number:str=Field(...,
                
                description="Numero telefonico",
                examples=["+34 900 457 678"]
        
    )

    country:str
    address: str


class UserSignIn(BaseModel):
    email:EmailStr=Field(...)
    password: str=Field(
        ...,
        min_length=8,
        
        description="La contraseña debe tener minimo 8 caracteres y contener un caracter especial"                
                        )
    
    

class UserUpdate(BaseModel):
    first_name:Optional[str]=Field(
        default=None,
        max_length=40,
        min_length=2,
        description="Primer Nombre"

)
    last_name:Optional[str]=Field(
        default=None,
        max_length=40,
        min_length=2,
        description="Apellidos"

)


    
    email:Optional[EmailStr]=None
    phone_number:Optional[str]=Field(
                default=None,
                description="Numero telefonico",
                examples=["+34 900 457 678"]
        
    )

    country:Optional[str]=None
    address: Optional[str]=None

class UpdatePassword(BaseModel):
    password: str=Field(
        ...,
        min_length=8,
        
        description="La contraseña debe tener minimo 8 caracteres y contener un caracter especial"                
                        )
    
    new_password:str=Field(
        ...,
        min_length=8,
        
        description="La contraseña debe tener minimo 8 caracteres , contener un caracter especial y ser diferente a la contraseña vieja "                
                        )
    
    @model_validator(mode="after")
    def password_validation(cls, values):
        if values.password==values.new_password:
            raise ValueError("La nueva contraseña debe ser diferente de la vieja")
        return values
    




class TokenRefreshResponse(BaseModel):
    access_token:str
    token_type:str
    user: UserBase


class TokenResponse(TokenRefreshResponse):
    refresh_token:str



class EmailRequest(BaseModel):
    email: str

class CodeRequest(BaseModel):
    code:int
    

class PasswordRequest(BaseModel):
    password:str