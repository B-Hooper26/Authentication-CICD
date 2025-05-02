def authentication(username: str, password: str) -> bool:
    print(f"Authenticating: {username}, {password}")
    if not username or not password:
        raise ValueError("Username and Password must not be empty")
    return username == "Admin" and password == "Password123"