import re
import logging

def estimate_progress(line: str) -> int:
    """
    Estimates the progress percentage based on nmap output line.
    Returns -1 if no progress update can be derived.
    """
    line = line.lower()

    # Look for exact percentage output by Nmap --stats-every
    match = re.search(r'about (\d+\.\d+)% done', line)
    if match:
        return int(float(match.group(1)))

    if "starting nmap" in line:
        return 1
    if "discovered open port" in line:
        # Avoid overriding exact percentages with vague progress
        return -1
    if "nse:" in line:
        return -1 # NSE takes a while, hard to estimate
    if "nmap done" in line:
        return 100

    return -1
