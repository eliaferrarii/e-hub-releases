# E-HUB Release Notes

Note di rilascio leggibili. Le voci sono ordinate dalla piu' recente alla piu' vecchia.

---

## v3.3.2 — 2026-06-27

- Fix Caddyfile in modalita' internal: il sito di default usa `localhost` invece di catch-all `:443`. Risolve `SEC_E_ILLEGAL_MESSAGE` su Windows / schannel durante l'handshake TLS quando il container e' in modalita' prod (Caddy attivo) senza dominio configurato.
- Fix CSS per gli input dentro i modal (cambio password, novita' versione): adesso usano padding e focus blu coerenti col resto della dashboard.

## v3.3.0 — 2026-06-27

- Nuovo step **Codice licenza** nell'onboarding di primo avvio. Per provare il prodotto si puo' inserire `demo` e l'istanza parte con piano demo (tutti i moduli abilitati, nessun limite).

## v3.2.x — 2026-06-27 (mini-plan dominio embedded)

- **Caddy embedded** nel container: reverse proxy + TLS automatico su porte 80/443.
- Modalita' TLS supportate: `internal` (CA self-signed Caddy), `acme` (Let's Encrypt), `custom` (cert dell'admin).
- Menu admin **Rete & Dominio** sotto la sezione Sistema per gestire dominio + TLS senza riavviare.
- Dev locale: tutti i comportamenti restano invariati se si avvia il container con `EHUB_DISABLE_CADDY=true`.

## v3.0.0 — 2026-06-27

- Prima release del nuovo prodotto **E-HUB** (rinominato e riarchitettato da DocuAI). Il client e' un peer puro: non gestisce piu' altri tenant, niente menu Multi-Tenant, niente Docker socket richiesto.
- Forkato da DocuAI v2.121.0 come punto di partenza pulito. Il vecchio repo resta in produzione invariato.

---

## Politica di rilascio

- I tag `:latest` su `ghcr.io/eliaferrarii/e-hub` sono auto-pubblicati ad ogni push.
- Il file `version.json` di questo repo viene aggiornato SOLO quando una versione e' marcata **stable**. I client E-HUB leggono quel file per il controllo aggiornamenti.
- Per provare versioni di sviluppo, gli admin Emironet possono pinnare manualmente tag specifici (es. `ghcr.io/eliaferrarii/e-hub:3.4.0-rc1`); non saranno mai mostrate come "Update available" agli utenti.
