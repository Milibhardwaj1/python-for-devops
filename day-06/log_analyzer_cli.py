import json
import argparse
class LogAnalyzer:
    

    def __init__(self, src_file, target_file, level):
        self.src_file = src_file
        self.target_file = target_file
        self.level = level

    def log_level_frequency(self):
        count = {"INFO": 0, "ERROR": 0, "WARNING": 0}
        try:
            with open(self.src_file,"r") as f:
                for line in f:
                    if "INFO" in line:
                        count["INFO"] += 1
                    elif "ERROR" in line:
                        count["ERROR"] += 1
                    elif "WARNING" in line:
                        count["WARNING"] += 1
                    else: 
                        pass
                print(count.items())
        except FileNotFoundError:
            print("File not found")
        
        if self.level:
            count = { self.level : count[self.level]}
        
        print("Log Summary: ")
        for k,v in count.items():
            print(k,v)
        
        self.write_json(count)
    def write_json(self, count):
        with open(self.target_file, "w") as f:
            json.dump(count, f, indent=4)
        print("Written successfully:", count)

def pass_cli_args():
    parser = argparse.ArgumentParser(description="Log Analyzer CLI Tool")
    parser.add_argument("--file", required=True, help = "Path to log file")
    parser.add_argument("--out", required=True, help = "Path to Output JSON File")
    parser.add_argument("--level", choices=["ERROR", "INFO", "WARNING"], help="Optional log level filter")
    return parser.parse_args()

if __name__ == "__main__":
    args = pass_cli_args()
    obj1 = LogAnalyzer(src_file=args.file, target_file=args.out, level=args.level)
    obj1.log_level_frequency()

