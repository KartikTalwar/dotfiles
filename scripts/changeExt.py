import glob
import sys
import re
import os


def extender( old_extn, new_extn):
    """
    This script changes files with file type old_extn to have a new file type new_extn.
    """

    p = re.search("""['"]{0,1}\.{1}([a-zA-Z]+)['"]{0,1}""",old_extn)

    if not p:
        print "I think you put a wrong 'old extension' ending in. It must be only letters."
        sys.exit()

    old_extn = p.group(1)
    p        = re.search("""['"]{0,1}\.{1}([a-zA-Z]+)['"]{0,1}""",new_extn)

    if not p:
        print "I think you put a wrong 'new extension' ending in. It must be only letters."
        sys.exit()

    new_extn = p.group(1)    
    files    = glob.glob('*.'+old_extn)

    print "Found %d with extension .%s" % (len(files), old_extn)

    for file in files:
        name = re.search("""([^.]+)\.[^.]+""", file)
        name = name.group(1)
        os.rename(file, name+"."+new_extn)
        
    print "Done converting to .%s" % new_extn



if __name__ == '__main__':
    """
    first argument is the extensions you want to change, the second is
    what to change it to
    """
    
    if len(sys.argv) < 3:
        print "Wrong number of arguments. First arugment is which files to change, second is \
                what to change it to."
    else:
        extender( sys.argv[1], sys.argv[2] )
