import re
import sys
import os

# List of 13 Colonies Special Event stations, plus WM3PEN and GB13COL
colonies_callsigns = {
    "K2A", "K2B", "K2C", "K2D", "K2E", "K2F", "K2G", "K2H", "K2I", "K2J", "K2K", "K2L", "K2M",
    "WM3PEN", "GB13COL"
}

def file_exists(filepath):
    return os.path.isfile(filepath)

def extract_field(line, field_name):
    pattern = fr"<{field_name}:\d+>([^<]+)"
    match = re.search(pattern, line)
    return match.group(1).strip() if match else None

def filter_adif(input_file, output_file):
    recordsProcessed = 0
    recordsFound = 0
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        qso_record = "" 
        for line in infile:
            qso_record += line.strip() + "\n"
            if "<eor>" in line:
                call = extract_field(qso_record, "Call")
                if call and call.upper() in colonies_callsigns:
                    outfile.write(qso_record)
                    recordsFound = recordsFound + 1
                qso_record = ""
                recordsProcessed = recordsProcessed + 1
    print("Searched " + str(recordsProcessed) + " calls")
    print("Found " + str(recordsFound) + " matching callsign of 13 Colonies event stations")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filter_colonies.py <input.adi> <output.adi>")
        print("")
        print("Author: Jason Johnson <k3jsj@arrl.net>")
        print("")
        print("AI DISCLAIMER")
        print("Portions of this program were generated using AI.")
        print("")
        print("DISCLAIMER")
        disclaimer = """\
This software is provided "as is", without warranty of any kind, express or implied. In no event shall the authors or contributors be held liable for any damages arising from the use of this software, including but not limited to data loss, system failure, or inaccuracies.

Use this software at your own risk. It is intended for educational and hobbyist purposes only. The authors make no representations regarding suitability for any specific application. All responsibility for the use and performance of this software lies solely with the user.

This software may reference third-party systems or events (such as the 13 Colonies Special Event) which are not affiliated with or endorsed by the developers. Callsigns and event data are used for illustrative and filtering purposes only.
"""
        print(disclaimer)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if (file_exists(input_file)):
        filter_adif(input_file, output_file)
        print(f"Filtered 13 Colonies QSOs saved to {output_file}")
    else:
        print(f"Error:  input file does not exist or cannot be read")
        
