# Burnt Sky

A minimal Bluesky viewer in a static web page.

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
burntsky https://bsky.app/profile/exampleuser.bsky.social
```

Build page in current directory with:

```
burntsky
```

Schedule with something like:

```
0 6-22 * * *  burntsky
```

This sets cron to run hourly during waking hours (6-10). No need running it when you're
asleep.

Also you shouldn't run this more frequently than hourly. Be kind.

## Future

- [ ] Faster
- [ ] Muting (if not conflict with above)
- [ ] Windows executable (depends how annoying to implement)

## FAQ

Q: What is displayed?\
A: Posts and quoted posts (labelled with a 🅠). This is equivalent to the Only Posts feed.

Q: Images?\
A: No. And not likely in the future.

Q: I get an error when adding @coolexample.user?\
A: They may be limiting their visibility. Can you
view the account when not logged in? If not, it won't
visible in Burnt Sky either.

Q: How I do I remove a user?\
A: edit `~/.config/burntsky/users.txt`

Q: Can I use this with a web server?\
A: Absolutely. But don't ask me how.
