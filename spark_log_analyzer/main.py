""" Spark Log Analyzer.

Main module for Spark Log Analytics, a package for analyzing large Apache logfiles with Spark.

This project is work in progress.

"""

from pyspark import SparkContext, SparkConf
import os.path
#from pattern_matcher import PatternMatcher


class LogAnalyzer:


    def __init__(self, log_file=None, line_matcher=None, context="local"):
        """ Assigns instance variables and initializes a new LogAnalyzer instance

        Args:
            log_file (str): Path to the logfile that will be analyzed
            line_matcher (PatternMatcher): Object that parses single lines of logs and returns a structured dict
            context (str): Master / cluster URL to connect to. Defaults to "local".

        Returns:
            None
        """
        self._context = context
        self._line_matcher = line_matcher

        # make sure path if valid before assignment
        if not os.path.isfile(log_file):
            raise ValueError("Invalid path to logfile")
        self._log_file = log_file

        self._spark_setup()
        pass


    def __del__(self):
        """ Destructor that performs final tasks, including closing the spark context

        Args:
            -
        Returns:
             None
        """
        self.close()


    def _spark_setup(self):
        """ Initialize the Spark context

        Args:
            -
        Returns:
            None
        """

        # create spark context with logfiles
        conf = SparkConf().setAppName("LogAnalyzer").setMaster(self._context)
        self._sc = SparkContext(conf=conf)
        log_lines = self._sc.textFile(self._log_file)

        # parse logs using the supplied patternmatcher
        self._logs = log_lines.map(self._line_matcher.match).cache()



    def content_size_stats(self, no_printout = False):
        log_content_sizes = self._logs.map(lambda x: x['response_bytes']).cache()

        total_content_size = log_content_sizes.reduce(lambda a, b: a + b)
        min_content_size = log_content_sizes.min()
        max_content_size = log_content_sizes.max()
        avg_content_size = log_content_sizes.mean()

        if not no_printout:
            print("\n*** CONTENT BYTE SIZE STATISTICS ***")
            print("Total content size (bytes): %d" %total_content_size)
            print("Minimal content size (bytes): %d" %min_content_size)
            print("Maximal content size (bytes): %d" %max_content_size)
            print("Average content size per response (bytes): %d \n" %avg_content_size)
        return {
            'total_content_size': total_content_size,
            'min_content_size': min_content_size,
            'max_content_size': max_content_size,
            'avg_content_size': avg_content_size
        }


    def close(self):
        """ Close down the spark context

        Args:
            -
        Returns:
            None
        """
        self._sc.stop()

