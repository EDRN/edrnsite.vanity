# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from plone.app.testing import PloneSandboxLayer, IntegrationTesting, FunctionalTesting, PLONE_FIXTURE

class EDRNSiteVanityLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    def setUpZope(self, app, configurationContext):
        import edrnsite.vanity
        self.loadZCML(package=edrnsite.vanity)
    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'edrnsite.vanity:default')

    
EDRN_SITE_VANITY = EDRNSiteVanityLayer()
EDRN_SITE_VANITY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDRN_SITE_VANITY,),
    name='EDRNSiteVanityLayer:Integration'
)
EDRN_SITE_VANITY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDRN_SITE_VANITY,),
    name='EDRNSiteVanityLayer:Functional'
)
