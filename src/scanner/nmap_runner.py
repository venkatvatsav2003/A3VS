import subprocess
from utils.logger import logger

def run_nmap(args: list, on_output):
    """
    Runs nmap command securely and streams output to on_output callback.
    'args' should be a list of command line arguments (e.g., ['nmap', '-F', '127.0.0.1']).
    """
    try:
        logger.info(f"Starting scan with arguments: {args}")

        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
...

        if process.stdout:
            for line in iter(process.stdout.readline, ""):
                on_output(line)
        
        process.wait()
        
        if process.returncode != 0:
            logger.error(f"Nmap process finished with return code {process.returncode}")
        else:
            logger.info("Nmap scan completed successfully.")
            
    except FileNotFoundError:
        logger.error("Nmap not found. Please ensure it is installed and in your PATH.")
        on_output("Error: Nmap not found.\n")
    except Exception as e:
        logger.exception(f"An unexpected error occurred during nmap execution: {e}")
        on_output(f"Error: {str(e)}\n")
