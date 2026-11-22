# Projeto Álbum

Aplicação para cadastrar e consultar álbuns, com frontend React + Vite e API backend Django.

## Estrutura

- `frontend/`: aplicação React, componentes, estilos e recursos estáticos.
- `backend/`: projeto Django, app `albuns`, migrations e API.
- `backend/requirements.txt`: dependências Python.

## Executar o backend

```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

O backend usa SQLite localmente. O banco é criado pelas migrations e não é versionado.

Para configurar o ambiente, copie `backend/.env.example` para `backend/.env` e exporte as variáveis no ambiente antes de iniciar o Django. `DJANGO_SECRET_KEY` deve ser substituída por uma chave exclusiva e segura fora do desenvolvimento local. `DJANGO_DEBUG` deve ser `false` em produção.

## Executar o frontend

Em outro terminal:

```bash
cd frontend
npm install
npm run dev
```

Por padrão, o frontend consome `http://127.0.0.1:8000`. Para apontar para outra URL, copie `frontend/.env.example` para `frontend/.env` e ajuste `VITE_API_BASE_URL`.

## Verificações

```bash
# Frontend
cd frontend
npm run build
npm run lint

# Backend
cd ../backend
python manage.py check
python manage.py test
```
