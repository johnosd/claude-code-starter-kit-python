# /test

Run the test suite and report only failures with actionable suggestions.

## Steps

1. Run the tests with JSON reporting:
   ```
   pytest --json-report --json-report-file=test-results.json
   ```
   If `pytest-json-report` is not installed, install it first: `pip install pytest-json-report`

2. Read `test-results.json` and parse the results.

3. **Report only failures.** Do not list passing tests. For each failed test, include:
   - **Test name:** full nodeid (e.g. `tests/test_books.py::test_get_book_not_found`)
   - **Error:** the concise error message and relevant traceback lines
   - **Suggestion:** a concrete fix — point to the likely cause and what to change

4. **Final summary** at the end:
   - Total tests: X passed, Y failed
   - Coverage percentage if available in the report (field `coverage`)
   - If all tests passed, say so clearly and skip the failure section

## Output format

```
## Test Failures

### 1. tests/path/test_file.py::test_function_name
**Error:** AssertionError: expected 404, got 200
**Traceback:** `response.status_code == 404` (line 42)
**Suggestion:** The endpoint is not raising HTTPException for missing resources. Add a 404 guard in the route handler before returning the response.

---

## Summary
- Passed: 8
- Failed: 1
- Coverage: 87%
```

If there are no failures, output only:
```
All X tests passed. Coverage: Y%
```
