# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'live-static', 'static-root')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),)    

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'live-static', 'media-root')