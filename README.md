# upyurts.info

Static site for UP Yurts, hosted on Cloudflare Pages (free).

- Edit page content in `build.py`, then run `python3 build.py` to regenerate the HTML. Terms of Sale text lives in `terms.html.part`.
- Styles: `public/assets/style.css` (colors and fonts follow the old Wix theme: navy #232941, teal #2A5651, Barlow + Nunito Sans).
- `_redirects` maps the old Wix addresses (/features-2, /shop, /product-page/...) to the new pages.
- Images in `public/img/` are 1400 px web copies; originals are in Google Drive: 01 UP Yurts & Clean Air Yurts / Project Photos / metal roof (1). Web copies and videos also in .../Website/images.
- Cloudflare: deployed as a Worker with static assets (`wrangler.jsonc`). Build command blank, deploy command `npx wrangler deploy`. Only the `public/` folder is published.

Open items:
- `ORDER_URL` in build.py points to the ACH Debit Authorization Jotform, which still asks for a Wix order number. Replace with the order form once it's set up.
