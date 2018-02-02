
def platform_image_upload(instance, filename):
    ext = filename.split('.')[-1]
    return '{}.{}'.format(instance.slug, ext)
