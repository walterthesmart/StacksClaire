import webbrowser
import time

repo_url = "https://github.com/walterthesmart/All-contracts-repository"
branches = [
    "feature/achievement-badge",
    "feature/auth-registry",
    "feature/backup-wallet",
    "feature/billboard",
    "feature/config-store",
    "feature/data-registry",
    "feature/event-logger",
    "feature/flash-loan-record",
    "feature/fungible-token",
    "feature/hello-world",
    "feature/kv-store",
    "feature/liquidity-pool",
    "feature/math-utils",
    "feature/message-board",
    "feature/multisig-helper",
    "feature/name-service",
    "feature/non-fungible-token",
    "feature/permission-manager",
    "feature/proposal-submission",
    "feature/registry-controller",
    "feature/reputation-system",
    "feature/simple-counter",
    "feature/sip-009-trait",
    "feature/sip-010-trait",
    "feature/stacking-logger",
    "feature/status-tracker",
    "feature/string-utils",
    "feature/timestamp-logger",
    "feature/tip-jar",
    "feature/user-profile",
    "feature/version-control",
    "feature/voting-poll"
]

print(f"Found {len(branches)} branches.")
print("I will open the Pull Request creation pages in your default browser.")
print("To avoid overwhelming your browser, I'll open them in batches of 5.")

for i in range(0, len(branches), 5):
    batch = branches[i:i+5]
    print(f"\nReady to open PRs for:")
    for b in batch:
        print(f" - {b}")
    
    input("Press Enter to open these 5 tabs (or Ctrl+C to stop)...")
    
    for branch in batch:
        # compare main...branch (or whatever the default base is, usually main)
        url = f"{repo_url}/compare/main...{branch}?expand=1"
        print(f"Opening {url}...")
        webbrowser.open(url)
        time.sleep(0.5) 

print("\nAll done!")
