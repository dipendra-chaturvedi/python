import secrets

reset_token = secrets.token_urlsafe(32)

reset_link = f"https://example.com/reset-password?token={reset_token}"

print(reset_link)


# User clicks "Forgot Password"
#         ↓
# Server creates a secure random token
#         ↓
# Token is stored with the user + expiry time
#         ↓
# Email contains:
# https://site.com/reset-password?token=ABC123...
#         ↓
# User opens link
#         ↓
# Server checks:
# Is token valid?
# Is it expired?
#         ↓
# Yes → allow new password
# No  → reject
#         ↓
# After password change → delete/invalidate token