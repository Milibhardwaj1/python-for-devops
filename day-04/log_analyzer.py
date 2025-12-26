import json
src_file = "app.log"
target_file = "out.json"

def log_level_frequency():
    count = {"INFO": 0, "ERROR": 0, "WARNING": 0}
    try:
        with open(src_file,"r") as f:
            for line in f:
                if "INFO" in line:
                    count["INFO"] += 1
                if "ERROR" in line:
                    count["ERROR"] += 1
                if "WARNING" in line:
                    count["WARNING"] += 1
            print(count.items())
        with open(target_file, "w") as f:
            json.dump(count, f, indent=4)
        print("Written successfully:", count)
    except FileNotFoundError:
        print("File not found")

log_level_frequency()


