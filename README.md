# Spark Log Analyzer
## 1 Introduction
Spark Log Analyzer is a tool for the analysis of large Apache log files using Spark. 
Inputs of the tool are a Spark execution context (such as 'local'), the location of the log file to analyze and a regex matching pattern that splits a single line in the logfile into its attributes.
This project is work in progress.

## 2 Example
The file example.py contains a script that analyzes a large public domain Apache log file from NASA.
  
```python
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
```

The output of this script contains various statistics:
CONTENT BYTE SIZE STATISTICS 
Total content size (bytes): 38464606624
Minimal content size (bytes): 0
Maximal content size (bytes): 6823936
Average content size per response (bytes): 20333 

