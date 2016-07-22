from charms.reactive import when, when_not, set_state

from charmhelpers.fetch import apt_install
from charmhelpers.fetch import apt_update

@when_not('ctdb-charm.installed')
def install_ctdb_charm():
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #

    packages = [
        'ctdb',
        'samba',
    ]
    apt_update()
    apt_install(packages)

    set_state('ctdb-charm.installed')
