# Todo API

API para gestionar tareas con Django REST Framework y JWT. Permite a los usuarios autenticarse, crear, listar, buscar, filtrar y marcar tareas como completadas.

---

## 🔹 Levantar el proyecto localmente (sin Docker)

Sigue estos pasos para levantar la API localmente:

### 1️⃣ Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

### 2️⃣ Crear y activar un entorno virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar migraciones

```bash
python manage.py migrate
```

### 5️⃣ Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Levantar el servidor

```bash
python manage.py runserver
```

El servidor quedará corriendo en:

```
http://localhost:8000/
```

---

## 🔹 Levantar el proyecto con Docker

### 1️⃣ Construir la imagen

```bash
docker build -t todo-api .
```

### 2️⃣ Correr el contenedor

```bash
docker run -p 8000:8000 todo-api
```

El servidor quedará corriendo en:

```
http://localhost:8000/
```

> Nota: El Dockerfile usa Gunicorn como servidor WSGI.

---

## 🔹 Base URL

```
http://localhost:8000/api/v1/
```

---

## 🔹 Endpoints de Autenticación

Se utiliza **Djoser** + **JWT** para autenticación.

### 1️⃣ Registrar usuario

```
POST /users/
```

**Body (JSON)**:

```json
{
  "username": "tomas",
  "password": "12345678",
  "email": "tomas@example.com"
}
```

**Respuesta**: 201 Created

---

### 2️⃣ Login y obtener token JWT

```
POST /jwt/create/
```

**Body (JSON)**:

```json
{
  "username": "tomas",
  "password": "12345678"
}
```

**Respuesta**:

```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJh...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJh..."
}
```

**Nota**: Guardá el token `access` para usarlo en la autorización de tareas.

---

## 🔹 Headers para endpoints protegidos

```
Authorization: Bearer <ACCESS_TOKEN>
Content-Type: application/json
```

---

## 🔹 Endpoints de Tareas

Todos los endpoints requieren **JWT**.

### 1️⃣ Listar todas las tareas

```
GET /tasks/
```

Opcional: agregar query params para buscar y filtrar:

- Buscar por contenido (title o description): `?search=leche`
- Filtrar por fecha: `?created_at=2025-10-05`
- Filtrar completadas: `?completed=true`
- Ordenar: `?ordering=-created_at`

**Ejemplo combinado**:

```
GET /tasks/?search=leche&created_at=2025-10-05&completed=false&ordering=-created_at
```

---

### 2️⃣ Crear tarea

```
POST /tasks/
```

**Body (JSON)**:

```json
{
  "title": "Comprar leche",
  "description": "Ir al supermercado",
  "completed": false
}
```

**Respuesta**: 201 Created

---

### 3️⃣ Obtener tarea específica

```
GET /tasks/<id>/
```

**Ejemplo**:

```
GET /tasks/3/
```

---

### 4️⃣ Actualizar tarea

```
PUT /tasks/<id>/
```

**Body (JSON)**:

```json
{
  "title": "Comprar leche y pan",
  "description": "Ir al supermercado",
  "completed": true
}
```

---

### 5️⃣ Eliminar tarea

```
DELETE /tasks/<id>/
```

