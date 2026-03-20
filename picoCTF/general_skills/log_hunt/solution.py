import re

def solve():
    file_path = 'server.log'
    
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            
        # 1. Extract fragments and their timestamps
        # We use a dictionary to automatically handle duplicates
        # Key: Timestamp, Value: Flag Fragment
        found_data = {}
        
        for line in lines:
            if "FLAGPART" in line:
                # Extract timestamp [YYYY-MM-DD HH:MM:SS]
                timestamp = line[1:20]
                # Extract the piece after the colon
                piece = line.split("FLAGPART: ")[1].strip()
                found_data[timestamp] = piece
        
        # 2. Sort by timestamp (keys) to ensure the flag is in order
        sorted_timestamps = sorted(found_data.keys())
        
        # 3. Join the fragments
        full_flag = "".join([found_data[t] for t in sorted_timestamps])
        
        print("-" * 30)
        print(f"Final Flag: {full_flag}")
        print("-" * 30)

    except FileNotFoundError:
        print(f"Error: {file_path} not found. Ensure the log file is in this folder.")

if __name__ == "__main__":
    solve()