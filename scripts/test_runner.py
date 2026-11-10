import os
import subprocess
import sys

def main():
    test_dir = "/app/bobsgameweb/src/__tests__"
    files = sorted([f for f in os.listdir(test_dir) if f.endswith(".test.ts")])
    passed = 0
    failed = 0
    failed_files = []

    print(f"Discovered {len(files)} test suites in {test_dir}\n")

    for test_file in files:
        full_path = os.path.join(test_dir, test_file)
        cmd = ["npx", "tsx", f"src/__tests__/{test_file}"]
        res = subprocess.run(cmd, cwd="/app/bobsgameweb", capture_output=True, text=True)
        if res.returncode == 0:
            print(f" PASS: {test_file}")
            passed += 1
        else:
            print(f" FAIL: {test_file}")
            print(res.stdout)
            print(res.stderr)
            failed += 1
            failed_files.append(test_file)

    print(f"\n==========================================")
    print(f"Summary: {passed} passed, {failed} failed out of {len(files)} test suites.")
    if failed_files:
        print(f"Failed suites: {', '.join(failed_files)}")
        sys.exit(1)
    else:
        print("All test suites passed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
