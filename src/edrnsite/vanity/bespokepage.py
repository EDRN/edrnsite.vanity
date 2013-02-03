# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''Bespoke page.'''

from zope import schema
from plone.directives import form
from edrnsite.vanity import MESSAGE_FACTORY as _
from five import grok
from plone.namedfile.field import NamedImage

class IBespokePage(form.Schema):
    '''A bespoke page.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of the person for whom this bespoke page exists.'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A short summary of the person.'),
        required=False,
    )
    photograph = NamedImage(
        title=_(u'Photograph'),
        description=_(u'A picture of this person.'),
        required=False,
    )
    

class View(grok.View):
    '''View for a bespoke page.'''
    grok.context(IBespokePage)
    grok.require('zope2.View')
