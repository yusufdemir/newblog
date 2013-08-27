import PIL
from celery import task
from NewBlog import settings
from PIL import Image
from django.core.mail import send_mail

@task
def resize_post_image(post):
    """
    Resize given posts image
    """

    if not post.image:
        return True
    image_path = "/photo/%s" % post.image

    image = Image.open(image_path)
    # ImageOps compatible mode
    if image.mode not in ("L", "RGB"):
        image = image.convert("RGB")

    size=(200,200)
    image = image.resize(size, PIL.Image.ANTIALIAS)
    image.save(image_path)
    return True


@task
def sendUserActivationMail(userid):
    if userid:
        message = """ / """
        send_mail('Subject here', message, 'from@example.com',
    ['to@example.com'], fail_silently=False)