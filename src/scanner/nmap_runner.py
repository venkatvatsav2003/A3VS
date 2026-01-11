import subprocess

def run_nmap(command, on_output):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
        text=True
    )

    for line in process.stdout:
        on_output(line)

    process.wait()
