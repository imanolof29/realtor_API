# realtor_API

Migrar la app
```
python manage.py makemigrations
python manage.py migrate
```

Crear super usuario
```
python manage.py createsuperuser
```

Acceder al panel de administrador de Django e iniciar sesion
```
'host':8000/admin/
```

## API URL

| Numero  | url  | Description  |
|:-:|:-:|:-:|
| 1  | /admin/  | Rutas del panel de administrados  |
| 2  | /auth/users  | Crear y listar usuarios (solo visible para el superusuario) |
| 3  | /api/realtor_seag  | Listado de realtors. Permite filtrar por zipcode y fechas de insercion  |
