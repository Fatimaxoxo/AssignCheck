                                      ##AssignCheck – A Smart Assignment Checker

Instantly validate, flag and compare every student submission — on time, on format, on point.

✨ Features:

✅ Validate file names – Ensures submissions follow your chosen naming pattern (e.g. `202314XXX.c`).

✅ Detect late submissions– Compares file timestamps with your deadline.

✅ Multi-format support – Works with `.txt`, `.c`, `.cpp`, `.pdf`, `.l`, `.y` out of the box.

✅ Similarity detection – Uses sequence matching to spot copy–paste across files.

✅ Automatic report generation – Produces a clear text report listing valid files, wrong names, late files and similarity percentages.

✅ Extensible & configurable – Easily adjust patterns, deadlines and file types for your own class or organisation.

🗂 Project Structure

checker.py # Main script
reports/ # Reports are saved here automatically
sample_submissions/ # (optional) Example folder with test files
README.md # This file

- How to Run:

1. Clone or Download -
```bash
git clone https://github.com/yourusername/assigncheck.git
cd assigncheck

2. Install Dependencies -
This script requires Python 3.7+ and the PyPDF2 library:
pip install PyPDF2

3. Run the Checker -
python checker.py
Now, you’ll be prompted for:
Submissions folder path (press Enter for current directory)
Submission deadline (format YYYY-MM-DD HH:MM:SS)

4. View the Report -
A new file like report_20240923_153000.txt appears in the reports/ folder and is also printed to the console.

📝_Sample Output:_

Enter submissions folder path (or press Enter for current directory): ./submissions
Enter submission deadline (YYYY-MM-DD HH:MM:SS): 2024-09-30 23:59:59
Scanning for submission files...

Valid Files:
   - 202314001.c
   - 202314002.pdf

Wrongly Named Files:
   - student3.txt

Late Submissions:
   - 202314002.pdf submitted at 2024-10-01 00:30:00 (after deadline!)

Similarities:
   - 202314001.c vs 202314002.pdf → 85.3% similar

Report saved to: reports/report_20240923_153000.txt

⚙️ Configuration Tips:

i. Change file naming pattern: edit the regex inside check_files() to fit your naming rules.
ii. Add more file types: update the list in get_files() and extract_text() to include new extensions.
iii. Change similarity threshold: adjust how you interpret the percentage returned by analyze_similarities().
iv. Report folder: by default reports are saved to a reports folder next to your submissions; change self.report_dir in the constructor to move it elsewhere.

🧠 Next Goal:
We plan to implement token-wise or fuzzy checking, which compares assignments based on individual words or code tokens rather than exact text, making the checker smarter at detecting similar logic even if variable names or formatting differ.

🤝 Contributing:
Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.
Feel free to fork the repository, improve the code, or add new features like:

i. Plagiarism thresholds
ii. CSV or PDF output reports
iii. Integration with an LMS

📄 License:
This project is open-source. You’re free to use and adapt it for your own courses or organisations under the terms of the MIT License (see LICENSE file if included).

👩‍🎓Contributors:
1. Tasmia Nasir
2. Afia Fahmida
3. Maria Sultana





