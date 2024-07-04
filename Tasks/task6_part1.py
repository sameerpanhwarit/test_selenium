from HelperMethods import Helper

def separate_sections(data):
    sections = {}
    current_section = []

    for line in data.split('\n'):
        line = line.strip()
        if line:
            current_section.append(line)
        else:
            if current_section:
                sections[current_section[0]] = current_section[1:]
                current_section = []

    if current_section:
        sections[current_section[0]] = current_section[1:]

    return sections


if __name__ == '__main__':
    helper = Helper()
    helper.driver.get('https://www.w3schools.com/python/python_intro.asp')
    sidebar = helper.getElementText('leftmenuinnerinner', 'id')
    allHeadings = separate_sections(sidebar)

    headingNo = 0
    for heading, subHeadings in allHeadings.items():
        headingNo = headingNo+1
        print(f'{headingNo}.{heading}: {subHeadings}')
        print("_"*100)