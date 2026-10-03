import os
import urllib.request
import sys

def run_tests():
    port = os.environ.get('PORT', '8080')
    base_url = f"http://localhost:{port}"
    passed = 0
    total = 3

    # Test 1: GET /
    try:
        req = urllib.request.urlopen(f"{base_url}/", timeout=2)
        if req.status == 200:
            passed += 1
    except Exception as e:
        print(f"Test 1 failed: {e}", file=sys.stderr)

    # Test 2: GET /healthz
    try:
        req = urllib.request.urlopen(f"{base_url}/healthz", timeout=2)
        if req.status == 200 and req.read().decode('utf-8') == "OK":
            passed += 1
    except Exception as e:
        print(f"Test 2 failed: {e}", file=sys.stderr)

    # Test 3: GET /notes
    try:
        req = urllib.request.urlopen(f"{base_url}/notes", timeout=2)
        if req.status == 200:
            passed += 1
    except Exception as e:
        print(f"Test 3 failed: {e}", file=sys.stderr)

    print(f"TESTS: {passed}/{total}")

    if passed != total:
        sys.exit(1)

if __name__ == '__main__':
    run_tests()