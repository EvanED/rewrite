#!/usr/bin/env python

import sys
import subprocess
import tempfile
import shutil

placeholder="@"

def main():
    command = sys.argv[2:]
    filename = sys.argv[1]

    # Get the actual command to run
    if placeholder in command:
        command = [arg if arg!=placeholder else filename
                   for arg in command]
        
        command = [(arg, filename)[arg!=placeholder]
                   for arg in command]
    else:
        command.append(placeholder)

    print "Running", command

    # Open a temporary file and run the command, redirecting output there
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        ret = subprocess.call(command, stdout=temp, stderr=temp)

        output_filename = temp.name


    # Replace the original file
    if ret == 0:
        backup = filename + ".orig"
        shutil.movefile(filename, backup)

        shutil.movefile(output_filename, filename)
    else:
        print "Subcommand returned", ret
        print "Leaving", filename, "unchanged; the output is stored in", output_filename

    sys.exit(ret)


if __name__ == "__main__":
    main()
    
