#!/usr/bin/env python

# Copyright 2011 Evan Driscoll  [driscoll@cs.wisc.edu]
#
# Licensed under the Apache License, Version 2.0 (the "License"); you
# may not use this file except in compliance with the License. A copy
# of the license is included with this distribution as "LICENSE.txt",
# or you may obtain a copy of the License from
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.



import sys
import subprocess
import tempfile
import shutil

placeholder="@"

def usage():
    print "Usage:", sys.argv[0], "FILE COMMAND ARGS..."
    print
    help = ("Runs COMMAND ARGS FILE, then puts the output in FILE. "
            + "Alternatively, use the @ character as an argument to "
            + "COMMAND, and FILE will take its place.")
    import textwrap
    print textwrap.fill(help)

def main():
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        usage()
        sys.exit(1)

    command = sys.argv[2:]
    filename = sys.argv[1]

    # Get the actual command to run
    if placeholder in command:
        command = [(arg, filename)[arg==placeholder]
                   for arg in command]
    else:
        command.append(filename)

    print "Running", command

    # Open a temporary file and run the command, redirecting output there
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        ret = subprocess.call(command, stdout=temp, stderr=temp)

        output_filename = temp.name


    # Replace the original file
    if ret == 0:
        backup = filename + ".orig"
        shutil.move(filename, backup)

        shutil.move(output_filename, filename)
    else:
        print "Subcommand returned", ret
        print "Leaving", filename, "unchanged; the output is stored in", output_filename

    sys.exit(ret)


if __name__ == "__main__":
    main()
    
