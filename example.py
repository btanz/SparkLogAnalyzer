""" Example for Spark Log Analyzer.

This example illustrates the use of Spark Log Analyzer using a large public-domain Apache logfile from NASA,
available at
http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html
("NASA_access_log_Jul95")

The example expects the file at the location defined in FILE_LOC in the local filesystem. On initialization, this
file is converted to an RDD and distributed.

"""
import spark_log_analyzer as sla

# 1) Configure script variables
# the regex pattern that splits single lines of logs into individual components
LINE_MATCHER = '^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+)'
# the location of the log file
FILE_LOC = '../LogData/NASA_access_log_Jul95'
# the execution context
CONTEXT = 'local'

# 2) Initialize the matching pattern and the log analyzer
line_matcher = sla.PatternMatcher(LINE_MATCHER, False)
logAnalyze = sla.LogAnalyzer(FILE_LOC, line_matcher, CONTEXT)

# 3) Perform computations
logAnalyze.content_size_stats()

# 4) Close the log analyzer
logAnalyze.close()
