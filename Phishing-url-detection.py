url = input("Enter URL: ")

score = 0

if len(url) > 50:
    score += 1

if "https://" not in url:
    score += 1

if "@" in url or "-" in url:
    score += 1

if score >= 2:
    print("Phishing URL Detected")
else:
    print("Safe URL")

