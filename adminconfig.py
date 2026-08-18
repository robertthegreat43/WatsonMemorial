from admin import WatsonMemorialAdminSite


from django.contrib.admin.apps import AdminConfig

class EventsAdminConfig(AdminConfig):
        default_site = "admin.WatsonMemorialAdminSite"