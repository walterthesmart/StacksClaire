import subprocess
import os

def run_cmd(cmd):
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def get_contracts():
    # List files in contracts directory from reference-main
    try:
        output = subprocess.check_output("git ls-tree -r reference-main --name-only", shell=True).decode('utf-8')
        files = [f for f in output.splitlines() if f.startswith("contracts/") and f.endswith(".clar")]
        return files
    except:
        return []

contracts = get_contracts()
print(f"Found {len(contracts)} contracts in reference-main.")

for i, contract_path in enumerate(contracts):
    filename = os.path.basename(contract_path)
    name = filename.replace(".clar", "")
    branch_name = f"feature/{name}"
    
    print(f"[{i+1}/{len(contracts)}] Processing {name}...")
    
    # Create branch from b372d50 (Clean state)
    run_cmd(f"git checkout -b {branch_name} b372d50")
    
    # Checkout specific file from reference-main
    # Note: We must ensure directory exists
    os.makedirs("contracts", exist_ok=True) # locally
    
    # We use git checkout to grabbing the blob from reference-main and placing it in worktree
    ret = subprocess.call(f"git checkout reference-main -- \"{contract_path}\"", shell=True, stderr=subprocess.DEVNULL)
    
    if ret == 0:
        # Also try to get the test file if it exists
        test_path = f"tests/{name}.test.ts"
        subprocess.call(f"git checkout reference-main -- \"{test_path}\"", shell=True, stderr=subprocess.DEVNULL)
        
        run_cmd("git add .")
        run_cmd(f"git commit -m \"Add {name}\"")
        run_cmd(f"git push -f origin {branch_name}")
    else:
        print(f"Failed to verify {contract_path}")

run_cmd("git checkout main")
print("All branches reconstructed and pushed.")
