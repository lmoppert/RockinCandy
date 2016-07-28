from staticjinja import make_site
import glob


def studio():
    images = glob.glob('media/studio*.jpg')
    images.sort()
    return {'images': images}


def frank():
    return {'images': glob.glob('media/Frank*.jpg')}


def nina():
    return {'images': glob.glob('media/Nina*.jpg')}


if __name__ == "__main__":
    site = make_site(contexts=[
        ('nina.html', nina), ('frank.html', frank), ('studio.html', studio),
    ])
    site.render(use_reloader=True)
