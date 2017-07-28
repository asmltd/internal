import logging
import inspect
from django.conf.urls import patterns, url, include
from django.conf import settings
from rest_framework import routers
from rest_framework.viewsets import ViewSet


def module_import(name):
    """
    If you need to import a module on the fly, this helper function assists
    you.  So say you want to import something like spam.eggs.are.cool, this
    will sort out the full import.
    """
    mod = __import__(name, globals(), locals(), [], -1)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

logger = logging.getLogger('debug.logger')
logger.debug('Initializing API views...')

router = routers.DefaultRouter()
router.include_format_suffixes = True

# urlpatterns = patterns('',
#     url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
# )
urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]


def extract_api_url(module_obj, installed_app):
    if module_obj.base_url is None:
        return installed_app[installed_app.index('.')+1:].replace('.', '/') + '/' + module_obj.base_name
    else:
        return installed_app.split('.')[-1] + module_obj.base_url + module_obj.base_name


for app in settings.INSTALLED_APPS:
    try:
        module = module_import('%s.api' % app)
        logger.debug('Importing %s.api...' % app)

        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and ViewSet in obj.__bases__:
                logger.debug('name = %s' % name)
                api_url = extract_api_url(obj, app)
                try:
                    router.register(api_url, obj, base_name=obj.base_name if obj.base_name != '' else api_url)
                    logger.debug('Registering: api_url=%s, obj=%s, base_name=%s' % (api_url, obj, obj.base_name))
                except Exception, ex:
                    logger.error(ex)

    except ImportError, e:
        logger.debug('Import failed for %s.api... %s' % (app, e))

        pass

urlpatterns += url(r'^', include(router.urls)),

