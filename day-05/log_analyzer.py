import json
class LogAnalyzer:

    def __init__(self, src_file, target_file):
        self.src_file = src_file
        self.target_file = target_file

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
        self.write_json(count)
    def write_json(self, count):
        with open(self.target_file, "w") as f:
            json.dump(count, f, indent=4)
        print("Written successfully:", count)

obj1 = LogAnalyzer("app.log", "output.json")
result = obj1.log_level_frequency()


