import argparse
import re
import sys


def parse_logs(file_path):
    # Regex to match timestamp, level, and message
    log_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s\[(ERROR|FATAL|MEMORY_LEAK|STACKTRACE)\]\s(.*)")
    findings = []

    try:
        with open(file_path, "r") as f:
            for line_num, line in enumerate(f, start=1):
                match = log_pattern.match(line.strip())
                if match:
                    timestamp, level, message = match.groups()
                    findings.append({
                        "line": line_num,
                        "timestamp": timestamp,
                        "level": level,
                        "message": message
                    })
    except FileNotFoundError:
        print(f"[ERROR] Could not find file: {file_path}")
        sys.exit(1)

    return findings


def generate_report(findings):
	print("\n=== ASML INTEGRATION LOG TRIAGE REPORT ===")
	print(f"Total Critical Events Found: {len(findings)}\n")
	print("| Line | Timestamp | Severity | Details |")
	print("|---|---|---|---|")
	
	for f in findings:
		print(f"| {f['line']} | {f['timestamp']} | **{f['level']}** | {f['message']} |")
	print("===========================================\n")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="ASML Automated System Log Parser") 
	parser.add_argument("--file", required=True, help="Path to log file")
	args = parser.parse_args()

	results = parse_logs(args.file)
	generate_report(results)

