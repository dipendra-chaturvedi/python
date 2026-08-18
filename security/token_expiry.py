# Password Reset Token Verificatio
# from datetime import datetime, timedelta, timezone

# created_at = datetime.now(timezone.utc)
# expires_at = created_at + timedelta(minutes=15)

# print("Created:", created_at)
# print("Expires:", expires_at)

# Token Expiry Verification
# from datetime import datetime, timedelta, timezone

# created_at = datetime.now(timezone.utc)
# expires_at = created_at + timedelta(seconds=10)

# print("Token created")
# print("Expires at:", expires_at)

# current_time = datetime.now(timezone.utc)

# if current_time < expires_at:
#     print("Token is valid")
# else:
#     print("Token expired")


# Token Expiry Verification
from datetime import datetime, timedelta, timezone
import time

expires_at = datetime.now(timezone.utc) + timedelta(seconds=5)

print("Token created")
print("Waiting...")

time.sleep(6)

current_time = datetime.now(timezone.utc)

if current_time < expires_at:
    print("Token is valid")
else:
    print("Token expired")