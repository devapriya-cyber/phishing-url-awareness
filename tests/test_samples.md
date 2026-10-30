# Test Results

Python version used: 3.13.15  
Operating system: Windows  
Date: 29/10/2026

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | https://www.google.com/login | No listed warning signs | No warning signs found | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | Both warnings displayed | PASS |
| 3 | http://instagram.com@sample.invalid/login | @ symbol + HTTP | Both warnings displayed | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Warning displayed | PASS |
| 5 | https://xn--youtube.invalid/ | Punycode-style hostname | Warning displayed | PASS |
| 6 | http://[bad | Invalid URL message | Invalid URL message displayed | PASS |

## Notes

I learned how to identify common suspicious URL patterns using Python and handle malformed URL inputs safely.

I was surprised that a URL can contain multiple warning signs at the same time, and the program can identify and report them together.

