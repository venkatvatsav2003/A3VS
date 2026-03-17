def build_auth_args(username, password):
    """
    Returns a list of nmap arguments for authentication.
    """
    if not username or not password:
        return []
    return ["--script-args", f"user={username},pass={password}"]
