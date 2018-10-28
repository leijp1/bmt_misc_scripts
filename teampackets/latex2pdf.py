import csv
import re
import sys
from collections import OrderedDict

DEFINITION_REGEX = re.compile(r'^\\newcommand{([^{}]*)}{.*}\s*(%.*)?$')

# These must be consecutive integers
NONE_SECTION = -1
SETUP_SECTION = 0
DEFINITIONS_SECTION = 1
CONTENT_SECTION = 2
ENDPAGE_SECTION = 3
CLEANUP_SECTION = 4

SECTION_DICT = {
    '%----------------SETUP----------------': SETUP_SECTION,
    '%-------------DEFINITIONS-------------': DEFINITIONS_SECTION,
    '%---------------CONTENT---------------': CONTENT_SECTION,
    '%---------------ENDPAGE---------------': ENDPAGE_SECTION,
    '%---------------CLEANUP---------------': CLEANUP_SECTION,
}

class FormatException(Exception):
    """
    Exception raised when the input .tex file is badly formatted.
    """
    def __init__(self, line, msg):
        Exception.__init__(self)
        self.line = line
        self.msg = msg

class BadDataException(Exception):
    """
    Exception raised when one of the dictionaries is badly formatted.
    """
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

def readCommands(csvFile):
    """
    Read the new commands from csvFile, and return them as an OrderedDict, with
    the first row of the file as keys.
    """
    csvin = csv.reader(csvFile)
    keys = next(csvin)
    return [OrderedDict((k, v) for k, v in zip(keys, line)) for line in csvin]

def getSubstitution(value):
    """
    Returns the value to be substituted into a definition line.
    """
    value = str(value)
    value = value.replace('\\', r'\textbackslash ')
    value = value.replace(r'\textbackslash  ', r'\textbackslash\ ')
    value = value.replace('~', r'\textasciitilde ')
    value = value.replace(r'\textasciitilde  ', r'\textasciitilde\ ')
    value = value.replace('^', r'\textasciicircum ')
    value = value.replace(r'\textasciicircum  ', r'\textasciicircum\ ')
    for s in '&%$#_{}':
        value = value.replace(s, '\\' + s)
    value = value.replace('\n', r'\\')
    return value

def getDefinitionLine(line, isFirstTeam, definitions):
    """
    Returns the definition line to be added to a team, or a tuple containing
    only the definition if it is not specified in the dictionary definitions,
    or None if the line from the file is badly formatted.
    """
    if line[0] == '%':
        return ''
    regexString = DEFINITION_REGEX.search(line)
    if regexString is None:
        return None
    # TODO: other errors (like bad definition, etc.)
    if isFirstTeam:
        command = 'newcommand'
    else:
        command = 'renewcommand'
    definition = regexString.group(1)
    if definition not in definitions:
        return (definition,)
    substitution = getSubstitution(definitions.pop(definition))
    return '\{0}{{{1}}}{{{2}}}\n'.format(command, definition, substitution)

def getTeam(inLines, isFirstTeam, isLastTeam, definitions):
    """
    Returns the next team, as a string, to be written to the output file.
    """
    prevSection = NONE_SECTION
    output = ''
    definitions = definitions.copy()
    missing = []
    for line in inLines:
        line = line.replace('\r\n', '\n').replace('\n', '')
        curSection = SECTION_DICT.get(line, prevSection)
        if curSection == prevSection:
            if (curSection == CONTENT_SECTION) or \
               (curSection == SETUP_SECTION and isFirstTeam) or \
               (curSection == ENDPAGE_SECTION and not isLastTeam) or \
               (curSection == CLEANUP_SECTION and isLastTeam):
               output += line + '\n'
            elif curSection == DEFINITIONS_SECTION:
                definition = getDefinitionLine(line, isFirstTeam, definitions)
                if isinstance(definition, tuple):
                    missing += [definition[0]]
                else:
                    output += definition
        else:
            prevSection = curSection
            if curSection != SETUP_SECTION:
                output += '\n'
    errorList = ['Error: Bad dictionary']
    if len(missing) > 0:
        errorList += ['    Not in dictionary: ' + ', '.join(missing)]
    # if len(definitions) > 0:
    #     errorList += ['    Not in template file: ' + ', '.join(definitions)]
    if len(errorList) > 1:
        raise BadDataException('\n'.join(errorList))
    return output

def testInLines(inLines):
    """
    Reads the input .tex file to see if it is formatted correctly, or raises
    a FormatException otherwise.
    """
    prevSection = NONE_SECTION
    for i, line in enumerate(inLines):
        line = line.replace('\r\n', '\n').replace('\n', '')
        curSection = SECTION_DICT.get(line, prevSection)
        if curSection == NONE_SECTION:
            raise FormatException(i + 1, 'Must start with setup section')
        elif curSection == prevSection:
            if curSection == DEFINITIONS_SECTION and \
                getDefinitionLine(line, True, {}) is None:
                raise FormatException(i + 1, 'Badly formatted definition')
        else:
            if curSection != prevSection + 1:
                raise FormatException(i + 1, 'Missing section')
            prevSection = curSection

def main():
    args = sys.argv
    if len(args) < 4:
        print('Error: must pass .csv file name, input file name, and output '
            'file name')
        return
    elif len(args) > 4:
        print('Error: too many arguments')
        return
    try:
        with open(args[1], 'r') as csvFile:
            teams = readCommands(csvFile)
    except IOError:
        print("Error: can't open command file: " + args[1])
        return
    try:
        with open(args[2], 'r') as inputFile:
            inLines = [line for line in inputFile]
    except IOError:
        print("Error: can't open input file: " + args[2])
        return
    try:
        testInLines(inLines)
    except FormatException as e:
        print('{0}: {1}'.format(e.line, e.msg))
        return
    teamOutput = []
    try:
        for i, team in enumerate(teams):
            teamOutput += [getTeam(inLines, i == 0, i == len(teams) - 1, team)]
    except BadDataException as e:
        print(e.msg)
        return
    with open(args[3], 'w') as outFile:
        outFile.write('\n'.join(teamOutput))

if __name__ == '__main__':
    main()
