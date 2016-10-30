from staticjinja import make_site
import glob
import os


def studio():
    images = glob.glob('media/studio*.jpg')
    images.sort()
    return {'images': images}


def images(template):
    folder = template.name.split('.')[0]
    images = os.listdir("media/{}".format(folder))
    images.sort()
    return {'images': images, 'folder': folder}


if __name__ == "__main__":
    site = make_site(contexts=[
        ('nina.html', images),
        ('frank.html', images),
        ('maike.html', images),
        ('studio.html', studio),
    ])
    site.render(use_reloader=True)
