# encoding: utf-8
# Copyright 2013 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowCore import WorkflowException

def installMemberPagesFolder(portal):
    if 'member-pages' not in portal.keys():
        folder = portal[portal.invokeFactory('Folder', 'member-pages')]
        folder.setTitle(u'Member Pages')
        folder.setDescription(u'Personal pages of EDRN members.')
        folder.reindexObject()
    else:
        folder = portal['member-pages']
    wfTool = getToolByName(portal, 'portal_workflow')
    state = wfTool.getInfoFor(folder, 'review_state')
    if state != 'published':
        try:
            wfTool.doActionFor(folder, 'publish')
        except WorkflowException:
            # Fsck if I know why
            pass
    localRoles = folder.get_local_roles()
    found = False
    for principal, roles in localRoles:
        if principal == 'AuthenticatedUsers':
            if u'Contributor' in roles:
                found = True
                break
    if not found:
        folder.manage_setLocalRoles('AuthenticatedUsers', ['Contributor'])


def setupImportSteps(context):
    if context.readDataFile('edrnsite.vanity.marker.txt') is None: return
    portal = context.getSite()
    installMemberPagesFolder(portal)
