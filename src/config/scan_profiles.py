SCAN_PROFILES = {
    "Quick Scan": "-T4 -F --stats-every 5s",
    "Full Scan": "-Pn -p1-1000 -sV -O --stats-every 5s",
    "Service Discovery": "-sV -p- --stats-every 10s",
    "Vulnerability Scan": "-Pn -p1-1000 -sV --script vuln --stats-every 5s"
}
