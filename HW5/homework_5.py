
import csv
import json
from pathlib import Path


def save_test_ids(test_ids):
    with open("tests.txt", "w", encoding="utf-8") as file:
        for test_id in test_ids:
            file.write(test_id + "\n")


def add_test_id(test_id):
    with open("tests.txt", "a", encoding="utf-8") as file:
        file.write(test_id + "\n")


def load_test_ids(filename):
    test_ids = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            test_id = line.strip()
            if test_id:
                test_ids.append(test_id)

    return test_ids


print("\n--- Task 1: Test IDs ---\n")

save_test_ids(["QA-1001", "QA-1002", "QA-1003"])
print("Initial IDs:", load_test_ids("tests.txt"))

add_test_id("QA-1004")
print("After adding QA-1004:", load_test_ids("tests.txt"))

save_test_ids([])
print("Empty list:", load_test_ids("tests.txt"))

save_test_ids(["QA-1001"])
add_test_id("QA-1002")
add_test_id("QA-1002")
print("Repeated ID:", load_test_ids("tests.txt"))

with open("tests.txt", "w", encoding="utf-8") as file:
    file.write(" QA-1001 \n\nQA-1002\n   \n QA-1003 \n")

print("Empty lines and spaces:", load_test_ids("tests.txt"))


def get_test_statistics(filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1
            total_duration_ms += int(row["duration_ms"])

            if row["status"] == "PASSED":
                passed += 1
            elif row["status"] == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms,
        "failed_ids": failed_ids
    }


print("\n--- Task 2: Test Statistics ---\n")

with open("results.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["test_id", "status", "duration_ms"])
    writer.writerow(["QA-1001", "PASSED", 120])
    writer.writerow(["QA-1002", "FAILED", 230])
    writer.writerow(["QA-1003", "PASSED", 150])

print("Results:", get_test_statistics("results.csv"))

with open("empty_results.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["test_id", "status", "duration_ms"])

print("Empty CSV:", get_test_statistics("empty_results.csv"))


def save_test_config(environment, base_url, timeout):
    config = {
        "environment": environment,
        "base_url": base_url,
        "timeout": timeout
    }

    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)


def load_test_config(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


print("\n--- Task 3: Test Configuration ---\n")

save_test_config("staging", "https://example.com", 30)
config = load_test_config("config.json")

print("Loaded config:", config)
print("Timeout type:", type(config["timeout"]))

assert type(config["timeout"]) == int
print("Timeout is int: True")

save_test_config("production", "https://shop.example.com", 60)
updated_config = load_test_config("config.json")

print("Updated config:", updated_config)

assert updated_config["environment"] == "production"
assert updated_config["timeout"] == 60

print("Old configuration replaced: True")


def build_run_report(project_name, csv_filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(csv_filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1
            total_duration_ms += int(row["duration_ms"])

            if row["status"] == "PASSED":
                passed += 1
            elif row["status"] == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])

    report_dir = Path("reports") / project_name
    report_dir.mkdir(parents=True, exist_ok=True)

    summary = {
        "project": project_name,
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms
    }

    with open(report_dir / "summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    with open(report_dir / "failed_tests.txt", "w", encoding="utf-8") as file:
        for test_id in failed_ids:
            file.write(test_id + "\n")

    return summary


print("\n--- Task 4: Build Run Report ---\n")

report = build_run_report("Shop", "results.csv")
print("Run report:", report)

report_dir = Path("reports") / "Shop"

print("Report directory exists:", report_dir.exists())
print("summary.json exists:", (report_dir / "summary.json").exists())
print("failed_tests.txt exists:", (report_dir / "failed_tests.txt").exists())

with open(report_dir / "summary.json", "r", encoding="utf-8") as file:
    print("Summary JSON:")
    print(json.dumps(json.load(file), indent=4))

with open(report_dir / "failed_tests.txt", "r", encoding="utf-8") as file:
    print("Failed test IDs:", file.read().strip().splitlines())

report_again = build_run_report("Shop", "results.csv")
print("Repeated run:", report_again)

with open("passed_results.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["test_id", "status", "duration_ms"])
    writer.writerow(["QA-2001", "PASSED", 100])

passed_report = build_run_report("PassedOnly", "passed_results.csv")
failed_file = Path("reports") / "PassedOnly" / "failed_tests.txt"

print("No failures report:", passed_report)
print(
    "Empty failed_tests.txt:",
    failed_file.exists() and failed_file.read_text(encoding="utf-8") == ""
)

print("\n--- All Tasks Completed ---")
