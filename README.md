# Hurry Asteroid

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

Schedule with something like:

```
0 6-22 * * *  hurryasteroid
```

This sets cron to run hourly during waking hours (6-10). No need running it when you're
asleep.

Also you shouldn't run this more frequently than hourly. Be kind.

## Future

- [ ] Faster
- [ ] Muting (if not conflict with above)
- [ ] Windows executable (depends how annoying to implement)

## FAQ

Q: What does it show?\
A: Posts and quoted posts. This is equivalent to the Only Posts feed.

Q: Images?\
A: No. And not likely in the future.

Q: How I do I remove a user?\
A: edit `~/.config/hurryasteroid/users.txt`

Q: Can I use this with a web server?\
A: Absolutely. But don't ask me how.
