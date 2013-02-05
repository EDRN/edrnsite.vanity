# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''Bespoke page.'''

from Acquisition import aq_inner
from edrnsite.vanity import MESSAGE_FACTORY as _
from five import grok
from plone.directives import form
from plone.namedfile.field import NamedImage
from zope import schema
from zope.component import getMultiAdapter

class IBespokePage(form.Schema):
    '''A bespoke page.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u"Enter your name, as you'd like it to appear."),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'Type up a short summary. You might include research interests, personal background, funny quirks, etc.'),
        required=False,
    )
    photograph = NamedImage(
        title=_(u'Photograph'),
        description=_(u'Upload a photograph of yourself. Please, keep it tasteful.'),
        required=False,
    )
    

class View(grok.View):
    '''View for a bespoke page.'''
    grok.context(IBespokePage)
    grok.require('zope2.View')
    def isMine(self):
        context = aq_inner(self.context)
        state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        if state.anonymous():
            return False
        userID = state.member().getUser().getId()
        pageOwnerID = context.getOwner().getId()
        if userID != pageOwnerID:
            return False
        contextState = getMultiAdapter((context, self.request), name=u'plone_context_state')
        return contextState.is_editable()
    def _getWorkflowState(self):
        context = aq_inner(self.context)
        contextState = getMultiAdapter((context, self.request), name=u'plone_context_state')
        return contextState.workflow_state()
    def isPublic(self):
        return self._getWorkflowState() in ('public', 'visible')
    def isPrivate(self):
        return self._getWorkflowState() == 'private'
    def _getCanonicalURL(self):
        context = aq_inner(self.context)
        contextState = getMultiAdapter((context, self.request), name=u'plone_context_state')
        return contextState.canonical_object_url()
    def editURL(self):
        return self._getCanonicalURL() + '/edit'
    def publishURL(self):
        return self._getCanonicalURL() + '/content_status_modify?workflow_action=show'
    def privateURL(self):
        return self._getCanonicalURL() + '/content_status_modify?workflow_action=hide'
