import os
import difflib
from datetime import datetime
import re
from pathlib import Path
import PyPDF2

class AssignmentChecker:
    def __init__(self, directory_path, deadline_str):
        self.directory = directory_path
        self.deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M:%S")
        self.files = []
        self.report_dir = os.path.join(os.path.dirname(self.directory), "reports")
        os.makedirs(self.report_dir, exist_ok=True)

    def get_files(self):
        self.files = [f for f in os.listdir(self.directory) if f.lower().endswith((".txt", ".c", ".cpp", ".pdf", ".l", ".y"))]
        return self.files

    def extract_text(self, filepath):
        ext = Path(filepath).suffix.lower()
        try:
            if ext in [".txt", ".c", ".cpp", ".l", ".y"]:
                with open(filepath, "r", errors="ignore") as f:
                    return f.read()
            elif ext == ".pdf":
                text = ""
                with open(filepath, "rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        text += page.extract_text() or ""
                return text
            else:
                return ""
        except:
            return ""

    def check_files(self):
        valid_files = []
        wrong_files = []
        late_files = []

        pattern = re.compile(r'^202314\d{3}\.(txt|c|cpp|pdf|l|y)$')

        for f in self.files:
            filepath = os.path.join(self.directory, f)
            submit_time = datetime.fromtimestamp(os.path.getmtime(filepath))

            if pattern.match(f):
                valid_files.append(f)
                if submit_time > self.deadline:
                    late_files.append(f)
                    print(f" LATE SUBMISSION: {f} submitted at {submit_time.strftime('%Y-%m-%d %H:%M:%S')} (after deadline!)")
            else:
                wrong_files.append(f)

        return valid_files, wrong_files, late_files

    def analyze_similarities(self, files):
        similarities = []
       
        ext_groups = {}
        for f in files:
            ext = Path(f).suffix.lower()
            ext_groups.setdefault(ext, []).append(f)

        
        for ext, group in ext_groups.items():
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    text1 = self.extract_text(os.path.join(self.directory, group[i]))
                    text2 = self.extract_text(os.path.join(self.directory, group[j]))
                    ratio = difflib.SequenceMatcher(None, text1, text2).ratio() * 100
                    similarities.append((group[i], group[j], round(ratio, 2)))
        return similarities

    def generate_report(self, valid_files, wrong_files, similarities, late_files):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(self.report_dir, f"report_{timestamp}.txt")

        with open(report_path, "w", encoding="utf-8") as report:
            report.write(" Assignment Report\n\n\n")

            report.write(" Valid Files:\n")
            for f in valid_files:
                report.write(f"   - {f}\n")
            print("\n Valid Files:")
            for f in valid_files:
                print(f"   - {f}")

            report.write("\n Wrongly Named Files:\n")
            if wrong_files:
                for f in wrong_files:
                    report.write(f"   - {f}\n")
                print("\n Wrongly Named Files:")
                for f in wrong_files:
                    print(f"   - {f}")
            else:
                report.write("   None\n")
                print("\n Wrongly Named Files: None")

            report.write("\n Late Submissions:\n")
            if late_files:
                for f in late_files:
                    report.write(f"   - {f}\n")
                print("\n Late Submissions:")
                for f in late_files:
                    print(f"   - {f}")
            else:
                report.write("   None\n")
                print("\n Late Submissions: None")

            report.write("\n Similarities:\n")
            print("\n Similarities:")
            if similarities:
                for f1, f2, ratio in similarities:
                    report.write(f"   - {f1} vs {f2} → {ratio}% similar\n")
                    print(f"   - {f1} vs {f2} → {ratio}% similar")
            else:
                report.write("   None\n")
                print("   None")

        print(f"\n Report saved to: {report_path}")


if __name__ == "__main__":
    directory = input("Enter submissions folder path (or press Enter for current directory): ").strip()
    if not directory:
        directory = os.getcwd()

    deadline_str = input("Enter submission deadline (YYYY-MM-DD HH:MM:SS): ").strip()

    checker = AssignmentChecker(directory, deadline_str)
    print(" Scanning for submission files...")
    checker.get_files()
    valid_files, wrong_files, late_files = checker.check_files()
    print(f"\nScanning complete. Found {len(valid_files)} valid files.\n")

    similarities = checker.analyze_similarities(valid_files)
    checker.generate_report(valid_files, wrong_files, similarities, late_files)
