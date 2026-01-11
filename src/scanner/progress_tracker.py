def estimate_progress(line: str) -> int:
    line = line.lower()

    if "starting nmap" in line:
        return 5
    if "discovered open port" in line:
        return 40
    if "nse:" in line:
        return 70
    if "nmap done" in line:
        return 100

    return -1
