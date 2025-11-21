# Obsidian Cloud API

To start with, this service will be entirely API driven.

#### 1. Register an email address to start using the service

Start with a request to the registration endpoint:

```json
POST /api/v1/register
{
  "email": "valid@email.com",
}
```

This will:

1. Check for an existing user
   1. If exists, error back pointing to login
2. Check for an existing registration request
   1. If exists, error back that one is already in progress
3. If checks pass, send an email with a code
   1. Reply back with a different code and instructions

```json
HTTP 200
{
  "response_code": "123ABC",
  "message": "Look for a code in your email. POST a JSON with a 'response_code' property set to the value returned here, a property set to 'email' with the email you used, and a property set to `email_code` set to the code that was emailed",
}
```

Once the email code shows up, both codes are sent to the verfiy nedpoint:

```json
POST /api/v1/verify
{
  "email": "existing@email.com",
  "response_code": "123ABC",
  "email_code": "ABC123",
}
```

This will:

1. Verify that the 2 codes match and are not expired
   1. If not, allow 2 more attempts before blocking the email address for a bit
2. If checks pass, respond back with an API key and an expiration time

```json
HTTP 200
{
  "api_key_": "A1B2C3",
  "expires_in": "8 hours",
  "message": "This is your account administration key. See API docs for details."
}
```

This API key is an account admin key and can be regenerated using the login endpoint:

```json
POST /api/v1/login
{
  "email": "existing@email.com",
}
```

This will email a code and repond like the `register` endpoint above. that can be sent to the same endpoint:

```json
POST /api/v1/login
{
  "email": "existing@email.com",
  "response_code": "123ABC",
  "email_code": "ABC123",
}
```

... which will repond back with a temporary API key. 