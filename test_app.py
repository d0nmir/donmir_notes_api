import json
import os
import sys
import urllib.error
import urllib.request

BASE_URL = f"http://localhost:{os.environ.get('PORT', '8080')}"

EXPECTED_NOTES = [
    {"id": 1, "title": "First note"},
    {"id": 2, "title": "Second note"},
]


def get(path):
    """Return (status, body). HTTP errors such as 404 are returned, not raised."""
    try:
        with urllib.request.urlopen(BASE_URL + path, timeout=2) as resp:
            return resp.status, resp.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        return err.code, err.read().decode("utf-8")


def test_root():
    status, body = get("/")
    assert status == 200, f"expected 200, got {status}"
    assert "Notes API" in body, f"unexpected body: {body!r}"


def test_healthz():
    status, body = get("/healthz")
    assert status == 200, f"expected 200, got {status}"
    assert body == "OK", f"expected 'OK', got {body!r}"


def test_notes():
    status, body = get("/notes")
    assert status == 200, f"expected 200, got {status}"
    assert json.loads(body) == EXPECTED_NOTES, f"unexpected JSON: {body!r}"


def test_unknown_path_is_404():
    status, _ = get("/no-such-path")
    assert status == 404, f"expected 404, got {status}"


def run_tests():
    tests = [test_root, test_healthz, test_notes, test_unknown_path_is_404]
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as err:
            print(f"{test.__name__} failed: {err}", file=sys.stderr)

    print(f"TESTS: {passed}/{len(tests)}")
    if passed != len(tests):
        sys.exit(1)


if __name__ == "__main__":
    run_tests()