# e-hub-releases

Canale **pubblico** dei metadati di rilascio per E-HUB.

NON contiene codice sorgente: il codice sorgente di E-HUB e' in un repo
privato separato (`eliaferrarii/e-hub`). Qui ci sono solo i metadati che
servono al meccanismo di "Controllo aggiornamenti" del prodotto.

## File

- **`version.json`** — fonte di verita' per "qual e' l'ultima release stable
  di E-HUB". I client on-prem leggono questo file via HTTPS anonima e
  confrontano con la propria `app.version` per sapere se c'e' una nuova
  versione disponibile.
- **`RELEASE_NOTES.md`** — note di rilascio leggibili agli admin. Linkato
  da `release_notes_url` in `version.json`.

## Come consumarlo dal client E-HUB

```bash
curl -s https://raw.githubusercontent.com/eliaferrarii/e-hub-releases/main/version.json
```

Risposta JSON:
```json
{
  "latest_version": "3.3.2",
  "image": "ghcr.io/eliaferrarii/e-hub",
  "image_tag": "3.3.2",
  "released_at": "2026-06-27T10:00:00Z",
  "release_notes_url": "https://github.com/.../RELEASE_NOTES.md#v332",
  "min_version_required": "3.0.0",
  "channel": "stable"
}
```

## Workflow di rilascio (lato Emironet)

1. Commit + push sul repo privato `eliaferrarii/e-hub`.
2. La CI builda e pubblica `ghcr.io/eliaferrarii/e-hub:latest` (e tag SHA).
3. Quando la versione e' pronta per la produzione (test interni superati,
   regressioni controllate): aggiornare `version.json` in questo repo con
   il nuovo `latest_version` + `image_tag` + entry in `RELEASE_NOTES.md`.
4. I client on-prem nel mondo vedono "Update available" e l'admin decide
   quando applicare dal menu "Aggiornamento" del prodotto.
