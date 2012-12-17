This package provides vanity pages for members of the Early Detection Research
Network (EDRN).

To demonstrate the code, we'll classes in a series of functional tests.  And
to do so, we'll need a test browser::

    >>> app = layer['app']
    >>> from plone.testing.z2 import Browser
    >>> from plone.app.testing import SITE_OWNER_NAME, SITE_OWNER_PASSWORD
    >>> browser = Browser(app)
    >>> browser.handleErrors = False
    >>> browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD))
    >>> portal = layer['portal']    
    >>> portalURL = portal.absolute_url()

Here we go.


Bespoke Page
============

A bespoke page is a place for members to show off their stuff, customize their
personal attributes, etc.  For now, they can be added anywhere::

    >>> browser.open(portalURL)
    >>> l = browser.getLink(id='edrnsite-vanity-bespokepage')
    >>> l.url.endswith('++add++edrnsite.vanity.bespokepage')
    >>> True
    >>> l.click()
    >>> browser.getControl(name='form.widgets.title').value = u'John Yaya'
    >>> browser.getControl(name='form.widgets.description').value = u"I'm the boss."
    >>> browser.getControl(name='form.buttons.save').click()
