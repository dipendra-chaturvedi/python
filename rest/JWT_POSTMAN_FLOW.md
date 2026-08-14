# JWT + Postman Automatic Token Flow

## 1. Login

First run:

```text
POST http://127.0.0.1:5000/login
```

Body → JSON:

```json
{
    "username": "admin",
    "password": "1234"
}
```

Server returns:

```json
{
    "message": "Login successful",
    "token": "eyJhbGciOi..."
}
```

---

## 2. Automatically Save Token in Postman

Open the `/login` request.

Go to:

```text
Scripts → Post-response
```

Add:

```javascript
const response = pm.response.json();

pm.globals.set(
    "json_web_token",
    response.token
);
```

This means:

```text
Login response
      ↓
response.token
      ↓
Postman saves it as
json_web_token
```

---

## 3. Use Token in Profile

Request:

```text
GET http://127.0.0.1:5000/profile
```

Go to:

```text
Authorization
→ Bearer Token
```

Instead of manually pasting the JWT, use:

```text
{{json_web_token}}
```

Postman automatically sends:

```text
Authorization: Bearer <JWT>
```

The Flask route uses:

```python
@token_required
```

to verify the JWT.

If valid:

```json
{
    "message": "Access granted",
    "username": "admin"
}
```

---

## 4. Use Same Token in Dashboard

Request:

```text
GET http://127.0.0.1:5000/dashboard
```

Authorization → Bearer Token:

```text
{{json_web_token}}
```

Again:

```python
@token_required
```

checks the token.

If valid:

```json
{
    "message": "Welcome to dashboard",
    "username": "admin"
}
```

---

# Complete Flow

```text
POST /login
     ↓
username + password
     ↓
JWT generated
     ↓
Post-response script
     ↓
Save token as:
json_web_token
     ↓
{{json_web_token}}
     ↓
     ├───────────────┐
     ↓               ↓
GET /profile    GET /dashboard
     ↓               ↓
@token_required   @token_required
     ↓               ↓
Verify JWT       Verify JWT
     ↓               ↓
200 OK           200 OK
```

## Important

Run `/login` first whenever you need a new token.

After that, Postman automatically uses:

```text
{{json_web_token}}
```

for `/profile` and `/dashboard`.

No manual copy/paste of the JWT is required.