# mp3.vinyl

Website for **mp3.vinyl** — independent curated online record store, KL & Penang.

Loads the full White Noise Records catalog (6,200+ in-stock records) with search and category filters. Built as a retro Mac OS desktop experience.

---

## What's in this folder

```
index.html              — the website shell (HTML + CSS + JS)
catalog.json            — the product catalog (loaded async on page load)
mp3_vinyl_logo.jpeg     — your logo
fetch_whitenoise.py     — script to refresh catalog.json with latest stock
README.md               — this file
```

All files must live in the same folder on GitHub for the site to work.

---

## Deploy on GitHub Pages

1. Go to [github.com/new](https://github.com/new), create a public repo (any name)
2. Click **"uploading an existing file"**, drag in all files, commit
3. **Settings → Pages → Source: Deploy from a branch → main → / (root) → Save**
4. Wait ~1 minute, your site is at `https://YOUR_USERNAME.github.io/REPO_NAME/`

---

## Refreshing the catalog (do this weekly)

White Noise's stock changes constantly. To pull the latest:

1. Open VS Code terminal in your project folder
2. Run: `python fetch_whitenoise.py`
3. Wait ~2 minutes — it downloads the catalog as `whitenoise_all.json`
4. Send `whitenoise_all.json` to Claude and ask for an updated `catalog.json`
5. Commit the new `catalog.json` to GitHub. Site updates in ~30 seconds.

---

## Editing the site

Everything visual lives in `index.html`. Edit on GitHub directly:
1. Click `index.html` → pencil icon (✏️)
2. Edit, scroll down, **Commit changes**
3. Site updates in ~30 seconds

Common edits:
- **Email:** search for `mailto:` and update
- **Instagram handle:** search for `instagram.com/mp3.vinyl`
- **Xiaohongshu link:** search for `xhslink`
- **Logo:** replace `mp3_vinyl_logo.jpeg` (keep same filename)

---

## Site behavior

- **Loads instantly** — site shell appears, then catalog streams in
- **Search** filters live across all records (artist + title)
- **Category filters** narrow by Hip-Hop / R&B / Indie / Jazz / City Pop / Electronic / Pre-orders
- **Pagination** shows 24 records per page (◀ ▶ in the toolbar)
- **Quicklook** opens a modal when you click any record
- **Cart button + every record** opens your IG DMs

All transactions happen in DMs — site is pure discovery + listing.

---

## Custom domain (optional)

Buy a domain (e.g. `mp3vinyl.com`), then in repo:
**Settings → Pages → Custom domain → enter your domain → set DNS records at your registrar.** Free SSL included.

---

Made with ♥ for mp3.vinyl