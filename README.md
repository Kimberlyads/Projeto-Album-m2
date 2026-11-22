Para instalação do projeto realize os seguintes comandos no terminal:
Para todas o django
cd albuns
pip install django django-cors-headers 
python manage.py migrate 
python manage.py createsuperuser (cria o super usuário com user, email e senha)
python manage.py runserver 

Em um segundo terminal para rodar o frontend
cd frontend 
npm install
npm run dev 
