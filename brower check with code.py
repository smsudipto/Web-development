import subprocess
import re

def get_browser_connections():
    browsers = [
        "chrome",
        "firefox",
        "brave",
        "opera",
        "microsoft-edge",
        "msedge"
    ]

    print("Gathering active browser connections...\n")
    print(f"{'Browser':<18} | {'PID':<8} | {'Local IP':<18} | {'Local Port':<10} | {'Destination IP':<18} | {'Destination Port'}")
    print("-" * 110)

    try:
        # PID -> Process Name
        ps_output = subprocess.check_output(
            ["ps", "-eo", "pid,comm"],
            text=True
        )

        pid_to_name = {}

        for line in ps_output.splitlines()[1:]:
            parts = line.strip().split(None, 1)
            if len(parts) == 2:
                pid_to_name[parts[0]] = parts[1].lower()

        # Network connections
        ss_output = subprocess.check_output(
            ["ss", "-tanp"],
            text=True,
            stderr=subprocess.DEVNULL
        )

        found = False

        for line in ss_output.splitlines():

            if "ESTAB" not in line:
                continue

            parts = line.split()

            # Find PID
            pid_match = re.search(r'pid=(\d+)', line)
            if not pid_match:
                continue

            pid = pid_match.group(1)
            process_name = pid_to_name.get(pid, "")

            if not any(browser in process_name for browser in browsers):
                continue

            # Local Address:Port and Destination Address:Port
            addresses = re.findall(r'(\S+:\d+)', line)

            if len(addresses) < 2:
                continue

            local_addr = addresses[0]
            remote_addr = addresses[1]

            local_ip, local_port = local_addr.rsplit(":", 1)
            destination_ip, destination_port = remote_addr.rsplit(":", 1)

            print(
                f"{process_name:<18} | "
                f"{pid:<8} | "
                f"{local_ip:<18} | "
                f"{local_port:<10} | "
                f"{destination_ip:<18} | "
                f"{destination_port}"
            )

            found = True

        if not found:
            print("No active browser connections found.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    get_browser_connections()
    input("\nPress Enter to exit...")