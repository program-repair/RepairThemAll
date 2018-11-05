import os
import sys
import datetime
import time

from runner.Runner import Runner


def get_terminal_size():
    env = os.environ

    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
        except:
            return
        return cr

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

    ### Use get(key[, default]) instead of a try/catch
    # try:
    #    cr = (env['LINES'], env['COLUMNS'])
    # except:
    #    cr = (25, 80)
    return int(cr[1]), int(cr[0]) - 1


def clean_terminal():
    (width, height) = get_terminal_size()

    for i in range(1, height + 1):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


class BashRenderer(object):
    def __init__(self, runner):
        """
        :param runner:
        :type runner: Runner
        """
        self.runner = runner

        (width, height) = get_terminal_size()
        for i in range(1, height + 1):
            print("")
        pass

    def get_errored_tasks(self):
        output = []
        for task in self.runner.finished:
            if task.status == "ERROR":
                output += [task]
        return output

    def get_patched_tasks(self):
        output = []
        for task in self.runner.finished:
            if task.status == "PATCHED":
                output += [task]
        return output

    def render(self):
        (width, height) = get_terminal_size()
        clean_terminal()

        output = ""

        output += "%d Running, %d Waiting, %d Finished, %d Patched, %d Error\n" % (len(self.runner.running), len(self.runner.waiting), len(self.runner.finished), len(self.get_patched_tasks()), len(self.get_errored_tasks()))

        output += "Running: \n"
        line_number = 1
        for task in self.runner.running:
            starting_date = task.starting_date
            if starting_date is None:
                starting_date = time.time()
            execution_time = datetime.timedelta(seconds=int(time.time() - starting_date))
            output += "%d. %s %s %s %s\n" % (line_number, task.tool.name, task.bug, task.status, execution_time)
            line_number += 1

        output_length = len(output.split("\n"))
        if output_length < height:
            for i in range(1, height - output_length):
                output += "\n"
        elif output_length > height:
            output_lines = output.split("\n")

            output_tmp = ""
            for i in range(0, height - 1):
                output_tmp += output_lines[i] + "\n"
            output_tmp += "All data is not displayed due to small terminal size"
            output = output_tmp
        print(output)

    def render_final_result(self):
        (width, height) = get_terminal_size()
        clean_terminal()

        output = ""

        output += "%d Finished, %d Patched, %d Error\n\n" % (len(self.runner.finished), len(self.get_patched_tasks()), len(self.get_errored_tasks()))

        output += "Patched bug: \n"
        patch_number = 1
        for task in self.get_patched_tasks():
            output += "%d. %s %s\n" % (patch_number, task.tool.name, task.bug)
            patch_number += 1
        output_length = len(output.split("\n"))
        if output_length < height:
            for i in range(1, height - output_length):
                output += "\n"
        print(output)
