# Avilog is a simple logging interface to write to console or a file.
# It will support the following:
#   - Different log levels
#       - info  (least important)
#       - debug
#       - alert
#       - error (most important)


class avilog:

    LOG_INFO = 0
    LOG_DEBUG = 1
    LOG_ALERT = 2
    LOG_ERROR = 3

    def __init__(self, filepath=None, level=3):
        """
        Takes in the full filepath of the target log file. 
        If no file is given, logs will be written to console.
        Also takes in the level of logging.
        """
        self.optionsList = {
            "info": self.LOG_INFO,
            "debug": self.LOG_DEBUG,
            "alert": self.LOG_ALERT,
            "error": self.LOG_ERROR
        }
        self.logLevel = level

        # init the file and check if it exists. If not, create it.
        self.filepath = None

    def write(self, message):
        # If a filepath has been set, append to file,
        # otherwise write to console
        if (self.filepath):
            print "Filepath is not supported yet."
        else:
            print message

    def log(self, tag, message):
        level = self.optionsList[tag]
        if (level):
            if (self.logLevel <= level):
                msg = "%s: %s" % (tag, message)
                self.write(msg)
        else:
            msg = "Avilog Error: Invalid tag %s passed to avilog. Use only 'info', 'debug', 'alert', 'error' only." % tag
            self.write(msg)



