# Castlecraft Auth

Frappe App for Castlecraft Authorization.

It requires Authorization Server with following features:

- Capability to generate `id_token` signed using JWKS
- `/.well-known/jwks` endpoint which returns set of public keys.

After installation of this app, request to frappe app can be made using `id_token` jwt signed using jwks.

## Usage Diagram

![Usage Diagram](diagrams/diagram.png)

## Installation

Note: Works on version 13 onwards.

```shell
bench get-app castlecraft_auth https://gitlab.com/castlecraft/castlecraft_auth.git
bench --site <site-name> install-app castlecraft_auth
```

## Configuration

Make following changes in `site_config.json` or `common_site_config.json` as per your setup:

```json
{
 ...
 "castlecraft_allowed_aud": ["client_id_or_allowed_aud_claim"],
 "castlecraft_auth_introspect_bearer": 1,
 "castlecraft_auth_jwt": 0,
 "castlecraft_client_id": "client_id_or_allowed_aud_claim",
 "castlecraft_client_secret": "client_secret",
 "castlecraft_create_user_on_auth": 1,
 "castlecraft_introspect_token_key": "access_token",
 "castlecraft_introspect_url": "https://accounts.example.com/oauth2/introspection",
 "castlecraft_jwks_url": "https://accounts.example.com/.well-known/jwks",
 "castlecraft_userinfo_url": "https://accounts.example.com/oauth2/profile"
}
```

- `castlecraft_allowed_aud`: Array of allowed audience claim in `id_token`. Generally `client_id`
- `castlecraft_auth_introspect_bearer`: When set to `1`, .
- `castlecraft_auth_jwt`: When set to `1`, .
- `castlecraft_client_id`: Registered `client_id`.
- `castlecraft_client_secret`: Registered `client_secret`.
- `castlecraft_create_user_on_auth`: When set to `1`, user with no roles will be created if not found in system.
- `castlecraft_introspect_token_key`: Key used to pass token to introspection endpoint. Defaults to `token`. Example request will have `token=abc123`.
- `castlecraft_introspect_url`: Token introspection url.
- `castlecraft_jwks_url`: JWKS Url to verify `id_token` signature (asymmetric).
- `castlecraft_userinfo_url`: User info url.

## License

Copyright 2021 Castlecraft Ecommerce Pvt. Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
