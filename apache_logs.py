"""Kör programmet genom att skriva en giltig logfil efter programmet
      Tex : python apache_logs.py access_log"""
import sys

def log_output(line):
    split_line = line.split()
    return {"remote_host" : split_line[0],
            "date" : split_line[4],
            "apache_status" : split_line[8],
            "site" : split_line[-1]
    }

def final_report(logfile):
    for line in logfile:
        log_file_parsed = log_output(line)
        print(log_file_parsed)

if not len(sys.argv) > 1:
    print(__doc__)
    sys.exit(1)
log_file_input = sys.argv[1]

try:
    log_file = open(log_file_input, 'r')
except IOError:
    print("Du måste ange en giltig fil som input!")
    print(__doc__)
    sys.exit(1)
log_file_report = final_report(log_file)
#print(log_file_report)
log_file.close()
