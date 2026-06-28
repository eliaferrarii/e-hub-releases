# E-HUB Release Notes

Note di rilascio leggibili. Le voci sono ordinate dalla piu' recente alla piu' vecchia.

---

## v3.6.4 — 2026-06-28

- Risolto: con la licenza in scadenza l'avviso in cima copriva il contenuto dei menu di sistema (Aggiornamento, Scripts, Rete) lasciando la pagina vuota.

## v3.6.3 — 2026-06-27

- Nel menu Licenza il campo Utenti mostra ora il valore attuale rispetto al massimo consentito dalla licenza (es. `7 / 10`).

## v3.6.2 — 2026-06-27

- Il dominio del cliente viene riconosciuto automaticamente in fase di provisioning e mostrato nella scheda licenza, senza richiederlo a mano.

## v3.6.1 — 2026-06-27

- I menu di sistema (Dashboard, Profilo, Licenza, Log, ecc.) sono ora visibili anche agli utenti non admin: prima sparivano se mancava un permesso.
- Nel menu Licenza il conteggio utenti diventa rosso se hai superato il massimo della licenza.

## v3.6.0 — 2026-06-27

- Nuovo pulsante "Cambia chiave" nel menu Licenza: l'admin puo' incollare una nuova chiave (es. da demo a pagato) senza riavviare nulla.
- I menu di sistema restano sempre attivi a prescindere dalla licenza: solo le integrazioni di business vengono limitate.

## v3.5.1 — 2026-06-27

- Migliorata l'affidabilita' del collegamento al server licenze Emironet.

## v3.5.0 — 2026-06-27

- Nuovo menu **Licenza** con piano, scadenza, giorni rimanenti, moduli abilitati e ultima verifica. Pulsante "Verifica ora" per controllare subito lo stato.
- Avviso giallo se la licenza scade entro 30 giorni, rosso se entro 7. Schermata di blocco se la licenza e' scaduta: contattare Emironet per il rinnovo.

## v3.4.3 — 2026-06-27 (TEST FITTIZIO HAPPY PATH)

Bump di test per verificare il flusso "Aggiorna ora" end-to-end: pull dell'immagine `:latest`. Verra' rollbackato a 3.4.2 dopo il test.

## v3.4.2 — 2026-06-27

- Helper dialog custom (`appConfirm`, `appAlert`, `appPrompt`, `appToast`): tutti i prossimi prompt/confirm/alert vanno con questi al posto dei popup browser, coerenti col resto della dashboard.
- Sostituiti i 2 confirm browser introdotti nei menu Rete & Dominio (rinnovo cert) e Aggiornamento (avvia update).
- Fix: l'endpoint `POST /api/admin/update/apply` ora ritorna stringhe pulite in `detail` invece di dict (no piu' "Errore: [object Object]" nella UI).

## v3.4.1 — 2026-06-27

- Testi UI piu' brevi nei menu Rete & Dominio, Aggiornamento, onboarding licenza demo. Tagliato ~40% di stringhe descrittive ridondanti.

## v3.4.0 — 2026-06-27

- Nuovo menu **Sistema → Aggiornamento**: l'admin vede la versione installata e quella disponibile, le note di rilascio, e decide se aggiornare ora oppure aspettare. Niente push automatici da Emironet.
- Tre modalita' di aggiornamento configurabili via `EHUB_UPDATE_METHOD`:
  - `disabled` (default sicuro): istruzioni manuali via SSH
  - `docker_socket`: pull + restart via Python docker lib (richiede mount socket)
  - `host_script`: invoca uno script bash sull'host appliance
- Le release stable vengono pubblicate da Emironet sul repo pubblico [e-hub-releases](https://github.com/eliaferrarii/e-hub-releases) tramite `version.json`. La build `:latest` su GHCR continua a essere quella di sviluppo (auto-pubblicata ad ogni commit), ma i clienti vedono solo le versioni marcate stable.

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
