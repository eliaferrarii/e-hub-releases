# E-HUB Release Notes

Note di rilascio leggibili. Le voci sono ordinate dalla piu' recente alla piu' vecchia.

---

## v3.17.103 — 2026-07-15

Rilascio maggiore consolidato (oltre 70 versioni beta). Alcune novita' importanti richiedono attenzione: la sezione **Utenti** e' stata rifatta e la voce di menu **Chat** e **Documenti** ora arrivano dallo Store integrazioni.

**Utenti: gestione tramite email**
- Sezione "Utenti" spostata dalla vecchia posizione dentro "Configurazione" a un tab dedicato nel gruppo "Sistema": e' piu' facile trovarla.
- L'identita' di un utente ora e' la sua **email** (non piu' lo username). Un utente puo' essere creato solo se gli si assegna un'indirizzo email valido, e la password temporanea viene inviata automaticamente a quell'indirizzo.
- Aggiunti campi **Nome** e **Cognome** con pulsanti "Modifica nome" / "Modifica email" per aggiornare i dati senza ricreare l'account.
- Pulsanti nella tabella: **Mail benvenuto** (rimanda le credenziali iniziali), **Mail reset password** (invia link per reimpostarla), **Elimina**.
- Pallino di stato online accanto a ogni utente, aggiornato in tempo reale.
- Migrazione automatica: gli utenti esistenti conservano le credenziali. La prima volta che l'admin apre il pannello, l'account admin di sistema riceve un placeholder che va aggiornato con l'email vera.

**Chat integrata tra utenti (modulo Store)**
- Nuovo modulo **Chat** installabile dallo Store, libero (nessuna licenza richiesta).
- Messaggistica 1-1 tra utenti dell'hub: sidebar con l'elenco contatti, area conversazione a destra, ricerca per nome/email.
- Widget "Follow me" opzionale: cliccando sull'icona a fianco al nome del contatto, la chat si "aggancia" in basso a destra e resta visibile su TUTTE le pagine dell'hub (dashboard, documenti, ticket, integrazioni). Cosi' non serve tornare al tab Chat per rispondere.
- Notifiche di messaggi non letti sulla voce del menu.

**Documenti come modulo Store**
- Il pannello **Lettura/Scrittura File** (caricamento e indicizzazione documenti) e' passato ad essere un modulo Store installabile invece che una sezione core sempre presente.
- Funzionalita' identiche a prima: chi lo aveva installato non si accorge di nulla. Per chi non lo usa, la voce di menu non compare piu' e non consuma spazio.

**Store integrazioni consolidato**
- Nuovi moduli disponibili nello Store: **Chat**, **Lettura/Scrittura File**, **Magazzino Emironet** (con seriali per ordine e login personale con account Zoho), **Home Assistant 2.1**, **Fortinet FortiCare**, **CDR TWT**, **WhatsApp**.
- Il catalogo si aggiorna automaticamente ogni volta che apri lo Store: nuove versioni dei moduli installati compaiono con un pulsante "Aggiorna".
- Ogni modulo dichiara con quale versione minima dell'hub e' compatibile: se il tuo hub e' troppo vecchio, l'install viene bloccato con un messaggio chiaro invece di rompere l'UI.
- Firma Ed25519 sul bundle: se qualcuno alterasse il pacchetto lungo la strada, l'install fallisce.

**Zoho: accesso per singolo operatore**
- Sezione "Il mio Desk" e "Magazzino": ogni operatore fa login con il suo account Zoho personale (OAuth) e vede solo i suoi ticket / ordini, senza usare le credenziali centrali dell'hub.
- Le configurazioni Zoho a livello di hub (per il bot AI) restano invariate.

**Rimozioni**
- **Calendario Zoho** e **Collaboration 7** non sono piu' presenti nel core dell'hub: non erano utilizzati dai clienti attivi. Rimossi per pulizia.
- La vecchia "bot key" (chiave API bot) e' stata deprecata: non veniva piu' utilizzata dall'esterno.

**Migliorie di sicurezza e stabilita'**
- Nuovo controllo automatico per bloccare tentativi ripetuti di login errato (protezione anti-brute force).
- Aggiornamento in-app: quando clicchi "Aggiorna ora" dallo Store, l'hub mostra ora una pagina di attesa dedicata mentre il container si riavvia (non piu' schermata 502 del reverse proxy).
- Migliorata la ricerca ibrida sui documenti (miglior ranking quando piu' file trattano lo stesso argomento).

**Hotfix inclusi in questo rilascio**
- Ripristinate funzioni di SMS, Webhook e Zoho Creator che erano state rimosse per errore durante la pulizia di Calendario Zoho / Collaboration 7 (v3.17.98-102).
- Menu Utenti ora si popola correttamente anche dopo aggiornamento (v3.17.103).

---

## v3.15.31 — 2026-07-07

Micro-rilascio di manutenzione: fix critico per gli update on-prem + polish annunci.

**Update on-prem: i valori nuovi arrivano davvero**
- Prima, alcuni limiti fissati come variabili d'ambiente al primo avvio del container (es. "solo 10 file in coda contemporaneamente") non venivano piu' cambiati dagli aggiornamenti successivi: Watchtower preservava le vecchie env e le nuove versioni di codice le vedevano ignorate. Per gli hub on-prem senza SSH non c'era modo di risolvere.
- Ora quei valori sono decisi dall'immagine stessa (dal codice), non dalle env: al primo restart post-update i tenant on-prem e cloud ricevono i nuovi limiti in maniera identica. Il limite "10 file in coda" scompare (diventa 100), la barra chunk arriva a 10.000, i rate limit di ricerca/upload/webhook si allineano tutti alla configurazione aggiornata.

**Annunci amministratore**
- Il pulsante "Gestisci" degli annunci ora apre una finestra dedicata con l'elenco degli annunci pubblicati e un pulsante rosso per eliminarli. Sotto la lista c'e' il form per pubblicarne uno nuovo (titolo, testo, tipo Informazione/Avviso/Urgente) invece delle vecchie tre finestrine in sequenza.

---

## v3.15.28 — 2026-07-07

Rilascio corposo con novita' importanti (43 versioni beta consolidate).

**E-Desk (nuovo)**
- Nuova sezione "Il mio Desk": vista Kanban dei ticket Zoho Desk con drag & drop tra colonne per cambiare stato, ordinate secondo il flusso italiano (Nuovo → Assegnato → In lavorazione → In attesa del cliente → Risposto → In attesa del commerciale → Scalato al fornitore → Da pianificare → Pianificato → Attesa Generica → Chiuso).
- Vista dettaglio ticket integrata nell'hub con sidebar sinistra contenente: contatto, anagrafica CRM completa (nome, ruolo, contatti, indirizzo, azienda, settore, sito web, sede), commerciale (owner CRM), contratti attivi con badge di scadenza.
- Le immagini nelle email dei ticket ora sono visibili (proxy verso Zoho autenticato).
- Finestra di risposta al cliente in stile client mail, con "Da / A / Oggetto" precompilati automaticamente dal dipartimento.
- Nota interna in finestra dedicata, senza campi email.
- Menzioni Zoho tra operatori (`@Nome Cognome`) ora rese leggibili nei commenti.
- Notifiche in basso a destra all'arrivo di nuovi ticket o aggiornamenti sui ticket assegnati (funzionano su qualsiasi vista dell'hub).
- Aggiornamento automatico ogni 20 secondi + dopo ogni azione, senza refresh manuale.

**Annunci amministratore**
- Gli annunci pubblicati dall'admin diventano un banner persistente in cima a qualsiasi pagina, non piu' un widget della dashboard.
- Nessun utente puo' piu' chiuderli o rimuoverli.
- Se l'admin elimina un annuncio, questo sparisce entro un minuto anche a tutti gli altri utenti collegati, senza reload.

**Documenti / ricerca**
- Ricerca documenti significativamente migliorata su corpora grandi: quando piu' PDF trattano lo stesso argomento, il chatbot non "dimentica" piu' file che restano invisibili nei primi risultati.
- Nuovo matching sul nome del file: se la domanda contiene una parola presente nel titolo del PDF (es. `manuale_A5E.pdf`), i chunk di quel documento vengono spinti in alto anche quando il corpo non contiene quella parola.
- Caricamento file: puoi ora selezionare piu' documenti contemporaneamente dal dialog di scelta file (Ctrl/Shift+click), sia in caricamento veloce sia in accodamento background.
- Il limite di file accodabili in coda passa da 10 a 100.
- Contatore chunk indicizzati sopra la tabella documenti con barra di progresso verso il target consigliato (10.000, configurabile).

**Sessioni utente**
- Le sessioni di login sopravvivono al riavvio dell'hub: quando aggiorni l'hub e il servizio si riavvia, resti loggato senza doverti riautenticare (funziona anche per E-Desk e per la connessione Zoho personale).

**Sidebar riducibile**
- Nuovo bottone in alto a destra del menu per ridurlo a sole icone e guadagnare spazio orizzontale.
- La preferenza viene ricordata dal browser.

**ACL utenti**
- Il pannello "Accessi modulo" ora elenca tutte le voci del menu, comprese quelle riservate all'amministratore (marcate "SOLO ADMIN" con avviso).
- E-Desk e Feedback diventano moduli assegnabili ai singoli utenti.

---

## v3.6.31 — 2026-06-30

- Le indicazioni tecniche "Stato server" e "Ultimo aggiornamento" nel fondo della sidebar restano visibili solo agli amministratori.

## v3.6.30 — 2026-06-30

- Dopo un aggiornamento gli amministratori continuano a vedere l'elenco delle novita'. Gli utenti standard ricevono un avviso piu' semplice che conferma soltanto l'aggiornamento dell'hub.

## v3.6.29 — 2026-06-30

- Le voci tecniche del menu Sistema (Licenza, MCP server, Log, Data e Ora) sono ora riservate agli amministratori. Gli utenti standard hanno una sidebar piu' pulita: solo Profilo e Feedback.

## v3.6.28 — 2026-06-30

- La configurazione del backup verso un servizio cloud esterno e' stata rimossa. Il backup locale prima degli aggiornamenti resta attivo come prima.

## v3.6.27 — 2026-06-30

- Nuova voce Feedback nel menu: ogni utente puo' segnalare bug, suggerire nuove funzionalita' o lasciare un'altra nota. Il messaggio arriva direttamente al team di supporto Emironet.

## v3.6.26 — 2026-06-30

- Il blocco anti tentativi di accesso riconosce ora l'IP reale del cliente, non quello del proxy davanti all'hub. Cosi' un attacco da un singolo IP non blocca piu' tutti gli utenti legittimi.

## v3.6.25 — 2026-06-30

- Le nuove installazioni si collegano al portale Emironet sul nuovo dominio e-hub.cloud.

## v3.6.24 — 2026-06-29

- Le nuove installazioni si agganciano al portale Emironet senza configurazione manuale.

## v3.6.23 — 2026-06-28

- L'hub comunica al portale Emironet la versione installata e il numero utenti correnti ad ogni verifica licenza.

## v3.6.22 — 2026-06-28

- Menu Aggiornamento ridisegnato: versione installata -> nuova con freccia, niente piu' riquadro 'Metodo'.
- Menu Integrazioni e MCP server: ora mostrano solo le voci incluse nella licenza.
- Backup locale + ripristino: nel menu Aggiornamento puoi creare backup, scaricarli e ripristinare uno stato precedente. Backup automatico prima di ogni 'Aggiorna ora'.
- Licenza scaduta: blocco immediato se il manager conferma la scadenza; i 14 giorni di grace valgono solo se il manager e' offline.
- Canale beta opzionale: nel menu Aggiornamento puoi iscriverti al canale beta per provare le anteprime.
- Barra aggiornamento piu' fluida e affidabile (no falsi completamenti).

## v3.6.15 — 2026-06-28

- Risolto: attivando il canale beta l'hub continuava a vedere solo le versioni stable. Ora riceve correttamente le anteprime.
- La barra dell'aggiornamento avanza fluida senza salti, niente banner duplicati in alto, ricarica solo al 100%.

## v3.6.13 — 2026-06-28

- Nel menu Aggiornamento puoi attivare "Iscrivimi al canale beta" per ricevere versioni in anteprima. Disattivabile in qualsiasi momento per tornare al canale stabile.

## v3.6.12 — 2026-06-28

- L'aggiornamento automatico ora funziona anche se il pacchetto di rilascio e' privato (autenticazione via token interna, niente azione richiesta al cliente).

## v3.6.11 — 2026-06-28

- Quando esce una nuova versione di E-HUB ricevi una mail e vedi un popup in basso a destra (puoi disabilitarlo dal menu Notifiche).

## v3.6.10 — 2026-06-28

- La barra dell'aggiornamento avanza piu' velocemente e la pagina si ricarica appena il servizio e' tornato online.
- Risolto: dopo il login si vedevano tutti i menu finche' non si cambiava pagina; ora la licenza filtra subito le voci.
- Quando ricarichi la pagina (F5 o dopo un aggiornamento) resti sul menu in cui eri, non vai piu' sempre alla Dashboard.
- Risolto: per qualche secondo si intravedeva la Dashboard prima del login al primo caricamento.

## v3.6.9 — 2026-06-28

- Durante l'aggiornamento ora vedi solo la percentuale e la barra. A fine aggiornamento la pagina si ricarica subito.

## v3.6.8 — 2026-06-28

- Al termine dell'aggiornamento la barra mostra un conto alla rovescia prima di ricaricare la pagina, cosi' fai in tempo a leggere l'esito.

## v3.6.7 — 2026-06-28

- Quando clicchi "Aggiorna ora" vedi una barra di avanzamento con le fasi (scaricamento, riavvio, completato), cosi' sai sempre cosa sta succedendo.

## v3.6.6 — 2026-06-28

- Risolto: se la licenza scade domani il menu mostra 1 giorno e non 2.

## v3.6.5 — 2026-06-28

- Il bottone "Aggiorna ora" nel menu Aggiornamento ora applica davvero l'aggiornamento: scarica la nuova versione e riavvia il servizio in autonomia. La pagina si riconnette dopo qualche secondo.
- Nessun aggiornamento automatico: l'hub si aggiorna solo quando l'admin clicca il bottone.

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
