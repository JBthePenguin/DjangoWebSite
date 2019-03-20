"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'DjangoWebSite.dashboard.CustomIndexDashboard'
"""
from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        self.site_name = get_admin_site_name(context)
        # append an models list for "websiteapp"
        self.children.append(modules.ModelList(
            _('Web site'),
            column=1,
            collapsible=False,
            models=(
                'websiteapp.models.Page', 'websiteapp.models.FooterItem',
                'websiteapp.models.SocialLink', 'websiteapp.models.CardButton',
                'websiteapp.models.AlertMessage',
                'websiteapp.models.FormPlaceHolder'),
        ))
        # append an models list for "aboutapp"
        self.children.append(modules.ModelList(
            _('About'),
            column=2,
            collapsible=False,
            models=('websiteapp.aboutapp.*',),
        ))
        # append an models list for "portfolioapp"
        self.children.append(modules.ModelList(
            _('Portfolio'),
            column=2,
            collapsible=False,
            models=('websiteapp.portfolioapp.*',),
        ))
        # append an models list for "blogapp"
        self.children.append(modules.ModelList(
            _('Blog'),
            column=2,
            collapsible=False,
            models=(
                'websiteapp.blogapp.models.BlogCategory',
                'websiteapp.blogapp.models.Post',
                'websiteapp.blogapp.models.Comment',),
        ))
        # append an models list for "contactapp"
        self.children.append(modules.ModelList(
            _('Contact'),
            column=2,
            collapsible=False,
            models=('websiteapp.contactapp.*',),
        ))
        # append an models list for "Administration"
        self.children.append(modules.ModelList(
            _('Auth'),
            column=3,
            collapsible=False,
            models=('django.contrib.*',),
        ))
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Media'),
            column=3,
            collapsible=False,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))
