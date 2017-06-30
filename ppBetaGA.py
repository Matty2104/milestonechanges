#!/usr/bin/python
"""Get name, bu_name, type of release (Public Beta or GA), and release date, save to local file"""
import datetime
import os
import requests


PP_API_BASE_URL = 'https://pp.engineering.redhat.com/pp/api/latest'


def _get_json(url):
    response = requests.get(url,
                            headers=dict(Accept='application/json'),
                            verify=False)
    return response.json()


class Release(object):
    """what info are we getting from Releases API"""
    def __init__(self, rel, beta=None):
        self.shortname = rel['shortname']
        self.name = rel['name']
        self.rel_id = rel['id']
        self.date = rel['ga_date']
        self.phase = rel['phase_display']
        self.beta = None
        self.rel_type = 'GA'

        if beta is not None:
            self.beta = True
            self.date = beta['ac_date_start']
            self.rel_type = beta['name']

    def __str__(self):
        return "%s (%s (%s))" % (self.name, self.date, self.rel_type)


def get_releases():
    """gettin greleases from PP API in to array"""
    all_rels = _get_json(
        '%s/releases/?active' % PP_API_BASE_URL)

    releases = []
    for rel in all_rels:
        releases.append(Release(rel))

        betas = _get_json('%s/releases/%s/schedule-tasks/?name=Public%%20Beta'\
                %(PP_API_BASE_URL, rel['id']))
        for beta in betas:
            releases.append(Release(rel, beta))

    return sorted(releases, key=lambda x: x.date)

# creates new path for comparison files
FILEPATH = r'/home/mvrchota/Documents/Assignments/Mark/170531/compare'
if not os.path.exists(FILEPATH):
    os.makedirs(FILEPATH)

# makes txt file where stores recieved data from PP
filename = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
f = open('%s/%s.txt' % (FILEPATH, filename), 'w+')
f.write("Welcome to PP BU Milestone comparison script v01\n")
f.write("Today we will try to create xls file next to this one\n")
f.write("So far, we have succeeded.\n")
f.write("Let's try to put there some info\n")
f.write("But just to be sure we are getting complete lists, ")
f.write("let,s see them here as well.\n\n")
# legend for release list
f.write('BU name -- GA/PB date -- Phase -- Rel ID\n')
for rel in get_releases():
    #TXT
    print "TXT - Inputting - %s" %rel
    f.write(rel.name)
    f.write(' - ')
    f.write(rel.rel_type)
    if rel.date is None:
        f.write(" - date not yet specified")
    else:
        f.write(' - release on ')
        f.write(str(rel.date))
    f.write(' - ')
    f.write(rel.phase)
    f.write(' - ID ')
    f.write(str(rel.rel_id))
    f.write("\n")
