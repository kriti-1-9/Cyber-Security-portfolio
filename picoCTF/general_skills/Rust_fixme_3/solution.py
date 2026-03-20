import subprocess

def run_binary():
    try:
        result = subprocess.run(
            ["cargo", "run"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except Exception as e:
        print(f"Error running binary: {e}")

if __name__ == "__main__":
    run_binary()