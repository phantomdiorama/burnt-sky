# Hurry Asteroid

> "Don't they know it's the end of the world?"

Hurry Asteroid is a minimal Bluesky viewer in a static webpage. 

It uses Python and RSS.

It is a *work-in-progress*

## Requirements

- [Requests](https://docs.python-requests.org/en/latest/index.html)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Feed Parser](https://feedparser.readthedocs.io/)
- [Dominate](https://github.com/Knio/dominate/)

## Install

Run `install.sh`

## Use

Add user feed with:

```
hurryasteroid https://bsky.app/profile/exampleuser.bsky.social
```

Build page with:

```
hurryasteroid
```

Schedule with cron:

```
0 * * * *  ~/.local/bin/hurryasteroid
```

Note: You probably shouldn't run this more frequently than hourly
