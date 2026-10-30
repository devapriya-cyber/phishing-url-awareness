
from urllib.parse import urlparse


def inspect_url(raw_url):
    candidate = raw_url.strip()

    if not candidate:
        return ["No URL entered."]

    if "://" not in candidate:
        candidate = "http://" + candidate

    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]

    warnings = []
    hostname = parsed.hostname or ""

    if parsed.scheme == "http":
        warnings.append("HTTP is used instead of HTTPS.")

    if hostname and all(part.isdigit() for part in hostname.split(".")):
        warnings.append("IP address used as hostname.")

    if "@" in candidate:
        warnings.append("@ symbol found in URL.")

    if len(hostname.split(".")) >= 6:
        warnings.append("Many hostname segments.")

    if hostname.startswith("xn--"):
        warnings.append("Punycode-style hostname.")

    return warnings


INFO_MESSAGES = (
    "No URL entered",
    "This text is not a valid URL format",
    "Could not identify",
    "No listed warning"
)


def has_warnings(findings):
    return bool(findings) and not findings[0].startswith(INFO_MESSAGES)


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)

        print("\nResult:")

        if findings:
            for item in findings:
                print("- " + item)
        else:
            print("- No listed warning signs found. This does NOT prove safety.")

        if has_warnings(findings):
            print(
                "\nREVIEW CAREFULLY: "
                + str(len(findings))
                + " warning sign(s) found."
            )

        print("\nNever enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
