# AgriSource — Streamlit Stakeholder Demo

This project runs the **latest AgriSource intelligent-dispatch HTML demo** inside
Streamlit **without redesigning or editing the original HTML**. It includes
guest checkout, customer sign-in, separate retailer and branch accounts,
inventory and sales views, driver matching, shared-route dispatch, and the
existing demonstration workflows.

## Files

- `app.py` — Streamlit wrapper and optional server-side access-password gate.
- `agrisource_demo.html` — **unchanged** source HTML, including embedded
  product images, CSS and JavaScript.
- `requirements.txt` — Streamlit dependency (modern `st.iframe` API).
- `.streamlit/config.toml` — shell theme and minimal chrome.
- `.streamlit/secrets.toml.example` — example password configuration; **not**
  a live password.
- `run_local.bat`, `run_local.sh` — local launch helpers.

## Launch locally

Install Python 3.10+; open a terminal in this folder, then:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Or run `run_local.bat` on Windows.
Streamlit opens a local address such as `http://localhost:8501`.

## Deploy privately on Streamlit Community Cloud

1. Create a **private** GitHub repository. Upload the project files, **including
   the `.streamlit` folder**, but never upload real `secrets.toml` values.
2. Sign in at https://share.streamlit.io/ and connect the GitHub account.
3. Deploy from the repository using **`app.py` as the entrypoint**.
4. Set the app's **sharing/access setting to private** and explicitly invite
   the intended retailer or investor viewers by email. Check the actual
   privacy setting before sending the link.
5. Optionally add a second access gate: in **App settings > Secrets**, set:

   ```toml
   AGRISOURCE_ACCESS_PASSWORD = "a-long-unique-password-you-choose"
   ```

6. Share the generated Streamlit URL with permitted viewers.

**If this secret isn't configured, the optional password screen is disabled.**
For sensitive presentations, **configure both private-app sharing and a
separate access password** rather than relying on obscurity of the URL.

## What stays the same

- Approved desktop/mobile HTML layout, brand colours, product imagery, pages
  and customer experience.
- All existing interactions within the standalone HTML (catalogue, search,
  guest ordering, accounts, inventory verification, payment simulation,
  dispatch routing and driver job offers).
- The HTML file is unchanged, byte-for-byte.

## Important limitations

- **This is a hosted demonstration, not a shared multi-user backend.**
  Retailer logins, orders, vehicle availability and payments are simulated.
  Browser data is stored in browser `localStorage`, so changes do *not*
  synchronize among viewers, browsers or devices.
- **This does not conceal client-side IP.** After admission, visitors can
  inspect HTML and JavaScript delivered to their browser. Keep proprietary
  algorithms on the server in a future production architecture.
- This password gate is an optional additional layer, not strong account
  management or per-user authorization. Prefer private Streamlit invites.
- Don't distribute the original HTML file or commit the repository publicly
  if source disclosure is a concern.
- Demo payments do not process money. Driver matches, routes, capacities,
  delivery quotes and retailer records are illustrative.

## Troubleshooting

- If `st.iframe` is missing, upgrade Streamlit using `pip install -U streamlit`
  (version 1.57 or later is expected).
- If GitHub seems unable to find `app.py`, ensure you deploy from the
  repository root.
- If visitors can reach the app without a password, confirm that the
  `AGRISOURCE_ACCESS_PASSWORD` secret was saved, and that the app was
  redeployed or restarted.
- A normal browser reload retains the demo's local sample state. Reset demo
  data from inside the AgriSource UI when you want to restart a walkthrough.

Official references:
- https://docs.streamlit.io/develop/api-reference/text/st.iframe
- https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app
- https://docs.streamlit.io/develop/concepts/configuration/secrets-management
