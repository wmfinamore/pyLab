from string import Template


def start_response(resp="text/html"):
    return('Content-type: '+ resp + '\n\n')


def include_header(the_title):
    with open('template/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))


def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href"' + the_links[key] + '">"' + key + '</a>$nbsp;$nbp,$nbsp,$nbsp;
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))