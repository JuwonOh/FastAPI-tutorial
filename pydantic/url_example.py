from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError


class User(BaseModel):
    email: EmailStr
    website: HttpUrl


if __name__ == "__main__":
    print(User(email="jdoe@example.com", website="https://www.example.com"))

# pydantic.error_wrappers.ValidationError: 1 validation error for User
# email value is not a valid email address (type=value_error.email)
