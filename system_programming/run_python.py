import subprocess

result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print("Output:", result.stdout.strip())