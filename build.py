from staticjinja import make_site
import glob


def frank():
    return {'images': glob.glob('media/Frank*.jpg')}


def nina():
    return {'images': glob.glob('media/Nina*.jpg')}


if __name__ == "__main__":
    site = make_site(contexts=[('nina.html', nina), ('frank.html', frank), ])
    site.render(use_reloader=True)
