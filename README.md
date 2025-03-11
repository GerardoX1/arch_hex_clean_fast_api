# arch_hex_clean_fast_api
mi version de clean

## Organizacion de carpetas
myproject/
├── main.py
├── app/
│   ├── domain/
│   │   ├── models/
│   │   │   └── user.py
│   │   └── services/
│   │       └── user_service.py
│   ├── application/
│   │   ├── use_cases/
│   │   │   └── create_user.py
│   │   ├── dto/
│   │   │   └── user_dto.py
│   │   └── interfaces/
│   │       └── user_repository.py
│   ├── adapters/
│   │   ├── api/
│   │   │   ├── controllers/
│   │   │   │   └── user_controller.py
│   │   │   └── routers/
│   │   │       └── user_router.py
│   │   ├── database/
│   │   │   └── user_repository_impl.py
│   │   └── orm_models/
│   │       └── user_orm.py
│   └── core/
│       └── config.py
└── tests/
    ├── unit/
    ├── integration/
    └── acceptance/

