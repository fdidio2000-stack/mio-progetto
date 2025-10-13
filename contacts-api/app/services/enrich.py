import hashlib
import httpx

def gravatar_url(email: str, size: int = 200) -> str:
    h = hashlib.md5(email.strip().lower().encode()).hexdigest()
    return f"https://www.gravatar.com/avatar/{h}?s={size}&d=identicon"

async def check_avatar_exists(url: str) -> bool:
    async with httpx.AsyncClient(timeout=3.0) as client:
        r = await client.get(url)
        return r.status_code == 200
