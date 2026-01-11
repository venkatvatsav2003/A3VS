def build_auth_args(username, password):
    if not username or not password:
        return ""
    return f"--script-args user={username},pass={password}"
