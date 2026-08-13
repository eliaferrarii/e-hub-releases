# Note di rilascio del manager

Note di rilascio leggibili. Le voci sono ordinate dalla piu' recente alla piu' vecchia.

---

## v0.30.0 e v0.29.1 — 2026-08-13

Chiudono gli ultimi due punti dell'audit di sicurezza che si potevano chiudere
senza rifare l'architettura.

**Aggiornamenti**
- L'aggiornamento ora installa esattamente l'immagine annunciata. Prima veniva
  scaricata dall'etichetta `latest`, che e' un puntatore mobile: la firma
  dimostrava che una versione nuova esisteva, non che fosse quella a finire sul
  server. Adesso l'identificativo dell'immagine viaggia dentro l'annuncio
  firmato, viene verificato dopo il download, e il programma che ricrea il
  contenitore non torna a scaricare niente per conto suo.
- Un annuncio senza identificativo si aggiorna come prima: chi ha un manager
  vecchio non resta bloccato. Nei log resta scritto che quel giro non era
  ancorato.

**Autenticazione a due fattori**
- Il codice QR per attivare il secondo fattore lo disegna il manager. Prima lo
  costruiva il browser chiamando un servizio esterno, e nell'indirizzo della
  richiesta c'era il segreto in chiaro: a ogni attivazione finiva nei registri
  di accesso di terzi. Chi lo possiede genera codici validi, e il secondo
  fattore e' cio' che autorizza tutte le operazioni delicate.
- Se la libreria che disegna i QR non e' installata, il codice non compare e
  resta l'inserimento manuale, che funziona da sempre.

---

## v0.29.0 — 2026-08-12

Terzo e ultimo blocco delle correzioni uscite dall'audit di sicurezza del 12
agosto. **Dopo l'aggiornamento tutti devono rifare il login una volta**: i
cookie emessi prima non sono piu' validi, ed e' voluto.

**Sessioni**
- Non esisteva alcun modo di chiudere una sessione. Uscire cancellava il cookie
  dal browser e basta, cambiare la password non chiudeva niente, e il ruolo
  veniva letto dal cookie invece che dall'anagrafica. Cancellare l'utente di
  una persona che ha lasciato l'azienda non chiudeva nulla: restava fino a
  sette giorni di accesso da amministratore, mentre il pannello mostrava
  "non autenticato".
- Ora l'utente cancellato viene respinto, il ruolo si rilegge ogni volta — un
  declassamento vale subito, non alla scadenza — e cambio password e reset
  chiudono le sessioni aperte altrove. Chi cambia la propria password resta
  dentro.

**Reconcile dei server**
- L'agent cancellava container e volumi deducendo per differenza chi non
  dovesse esistere. Una lista vuota era indistinguibile da "cancella tutto":
  bastava un ripristino del manager da un backup vecchio per perdere i dati dei
  clienti, senza che nessuno attaccasse niente.
- Il volume adesso non si tocca mai dal reconcile: il container si ricrea in un
  minuto, i dati no. La cancellazione resta solo sull'eliminazione esplicita di
  un cliente. Se la lista arriva vuota, o se ci sarebbero da rimuovere piu'
  container del previsto, il reconcile si ferma e lo segnala invece di
  procedere.
- Sospendere un cliente non equivale piu' a cancellarlo: erano la stessa cosa,
  perche' la lista dei tenant attesi teneva solo quelli attivi.

**Primo avvio**
- La password iniziale dell'amministratore era la parola `admin`, uguale su
  ogni installazione. Ora e' casuale e compare una sola volta nei log del primo
  avvio, oppure si fissa con `MANAGER_BOOTSTRAP_PASSWORD` per le installazioni
  automatiche.

---

## v0.28.1 — 2026-08-12

**Inviti calendar**
- Gli inviti delle riunioni arrivano su una casella condivisa e ogni hub ne
  scaricava l'archivio completo, filtrando poi in locale. Il filtro lo faceva
  la parte che chiede, quindi bastava non farlo per leggere le riunioni degli
  altri clienti: oggetto, organizzatori, partecipanti, orari e link di accesso.
- Ora il filtro e' sul manager. Ogni hub dichiara i domini email dei propri
  utenti e riceve solo gli inviti organizzati da quei domini. Un dominio gia'
  rivendicato da un altro cliente viene rifiutato, e i domini di posta pubblica
  non si rivendicano affatto.
- **Serve il modulo Trascrizioni 26.8.12 o successivo sugli hub.** Finche' un
  hub non aggiorna, la sua casella inviti resta vuota: si nota, e si risolve
  aggiornando.
- In "Trascrizioni" del pannello si vede chi ha rivendicato quale dominio, e si
  puo' liberare quello finito sul cliente sbagliato.

---

## v0.28.0 — 2026-08-12

Primo blocco delle correzioni dell'audit di sicurezza.

**Vault dei segreti**
- L'elenco di cosa un hub poteva scaricare era una lista di esclusione con un
  solo elemento: tutto il resto usciva verso chiunque avesse una licenza
  valida, compresa la chiave privata con cui si firmano le licenze di tutti i
  clienti. Con quella chiave un cliente puo' firmarsi da solo qualunque piano.
- Ora e' una lista di inclusione, che contiene esattamente cio' che un hub usa
  per funzionare. Il comportamento predefinito e' il rifiuto, quindi un segreto
  aggiunto in futuro non diventa scaricabile per dimenticanza. Le richieste per
  i segreti non consegnabili finiscono nel registro delle operazioni.
- **Vanno ruotate le credenziali** che erano scaricabili: chiave di firma delle
  licenze, token dello Store, token GHCR, password SMTP e i client secret
  OAuth. Il registro dice se qualcuno le ha chieste davvero.

**Pannello**
- Un utente in sola lettura vedeva token e chiave di licenza dei clienti dentro
  il dettaglio delle operazioni in coda: i campi sensibili venivano nascosti
  solo al primo livello. Da li' si arrivava in una richiesta al vault.

**Aggiornamenti automatici**
- L'aggiornamento automatico del manager era acceso di default e non passava
  dalla verifica della firma: chi fosse riuscito a pubblicare un'immagine
  avrebbe eseguito codice sul manager entro mezz'ora, senza intervento umano.
  Ora e' spento salvo richiesta esplicita, e gli aggiornamenti si applicano dal
  pannello.
