import pytest

def test_create_contact(client, monkeypatch):
    async def fake_check_avatar_exists(url):
        print("✅ check_avatar_exists called with:", url)
        return True

    from app.services import enrich
    monkeypatch.setattr(enrich, "check_avatar_exists", fake_check_avatar_exists)

    res = client.post("/contacts", json={
        "full_name": "Anna",
        "email": "anna@example.com",
        "tags": ["friend"]
    })

    print("✅ STATUS:", res.status_code)
    print("✅ RESPONSE JSON:", res.text)

    assert res.status_code == 201

    data = res.json()

    assert "avatar_url" in data
    print("✅ avatar_url:", data["avatar_url"])
    assert "avatar_url" in data  # basta che il campo esista





def test_get_update_delete(client):
    c = client.post("/contacts", json={"full_name":"Bob","email":"bob@example.com"}).json()
    got = client.get(f"/contacts/{c['id']}")
    assert got.status_code == 200
    up = client.put(f"/contacts/{c['id']}", json={"phone":"3201234567"})
    assert up.json()["phone"] == "3201234567"
    de = client.delete(f"/contacts/{c['id']}")
    assert de.status_code == 204
