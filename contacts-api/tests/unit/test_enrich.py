import pytest
from app.services.enrich import gravatar_url, check_avatar_exists

@pytest.mark.asyncio
async def test_check_avatar_exists(monkeypatch):
    class DummyResp:
        status_code = 200
    async def fake_get(self, url):
        return DummyResp()
    import httpx
    monkeypatch.setattr(httpx.AsyncClient, "get", fake_get, raising=False)
    assert await check_avatar_exists("http://x") is True

def test_gravatar_url():
    url = gravatar_url("Test@Email.com")
    assert "gravatar.com/avatar/" in url
