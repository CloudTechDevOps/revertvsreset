import time
import random

failure_threshold = 30   # like startupProbe failureThreshold
period_seconds = 5         # like startupProbe periodSeconds
restart_count = 0

def health_check():
    # Simulate failing startup (70% failure chance)
    return random.random() > 0.7

while True:
    failures = 0
    print(f"\n🚀 Starting container... (Restart count: {restart_count})")

    while failures < failure_threshold:
        time.sleep(period_seconds)
        if health_check():
            print("✅ Startup successful!")
            exit(0)
        else:
            failures += 1
            print(f"❌ Startup probe failed ({failures}/{failure_threshold})")

    restart_count += 1
    print("🔁 Restarting container...\n")
