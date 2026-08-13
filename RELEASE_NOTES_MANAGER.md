# Note di rilascio del manager

Note di rilascio leggibili. Le voci sono ordinate dalla piu' recente alla piu' vecchia.

---

## v0.33.1 e v0.33.0 — 2026-08-13

- **L'aggiornamento di un'istanza rispetta il canale scelto.** Un'istanza puo'
  girare da un'etichetta diversa dal canale che segue — e' normale, ed e' come
  funziona il passaggio fra canali — e spostando l'aggiornamento sull'agente si
  era persa la logica che teneva conto della differenza. Senza, un cliente su
  stable si sarebbe ritrovato il ramo beta al primo aggiornamento.
- L'istanza dichiara il proprio canale; l'immagine da installare la decide il
  gestore da un elenco fisso, cosi' nessuno puo' farsi installare qualcosa di
  arbitrario sul server che lo ospita.

---

## v0.32.2 — 2026-08-13

- **"Ricrea" rispondeva errore 500.** I due nuovi tipi di operazione erano
  dichiarati solo dalla parte dell'agente e non da quella del gestore, che li
  rifiutava. Corretto, con un controllo automatico che d'ora in poi verifica
  che le due parti restino allineate.

---

## v0.32.1 — 2026-08-13

- Il pulsante **"Ricrea"** sulla riga di ogni cliente, che nella 0.32.0 era
  rimasto senza interfaccia: l'operazione esisteva ma non era raggiungibile.
- La ricreazione rimette in piedi l'istanza con la stessa immagine di prima,
  invece di ripartire dal canale predefinito. Cambiare etichetta al contenitore
  confonderebbe il meccanismo che gestisce il passaggio fra canali.

---

## v0.32.0 — 2026-08-13

Chiude il problema piu' grave dell'audit di sicurezza: l'isolamento fra i
clienti che stanno sullo stesso server.

**Istanze dei clienti**
- Ogni istanza riceveva il comando del motore Docker del server, per potersi
  ricreare da sola quando l'admin premeva "Aggiorna ora". E' un permesso che
  vale come amministratore dell'intera macchina: da li' si arrivava ai dati e
  alle credenziali di tutti gli altri clienti ospitati accanto, e non serviva
  forzare niente, bastava un programma scritto da un utente dell'istanza.
- Adesso l'istanza **chiede** l'aggiornamento al gestore, che lo fa applicare
  dal proprio agente. Per l'utente non cambia niente: stesso bottone, stessa
  attesa. Cambia che quel permesso non lo ha piu' nessuna istanza.
- Le istanze nuove nascono anche con limiti di memoria e processi, che prima
  non c'erano.
- **Le istanze gia' esistenti hanno ancora quel permesso**: un aggiornamento
  normale non lo toglie, perche' ricrea l'istanza cosi' com'era. Per ognuna
  c'e' "Ricrea" nel pannello, che la ricostruisce con le impostazioni di oggi
  senza toccare i dati. Va fatto una volta per cliente.

**Accesso alle appliance dal pannello**
- L'apparato del cliente non puo' piu' scrivere i cookie del pannello: poteva
  sovrascrivere la sessione dell'amministratore che lo stava guardando.
- L'accesso al pannello di un'appliance ora chiede il secondo fattore, come
  gia' faceva il terminale verso lo stesso apparato.

---

## v0.31.0 — 2026-08-13

Chiude l'ultimo problema grave dell'audit di sicurezza. Non cambia niente per
chi usa il pannello, tranne un pulsante in piu' sui server.

**Agent dei server**
- La lista che l'agent riceve non contiene piu' le chiavi di licenza dei
  clienti. Il token dell'agent e' confinato al suo server, ma con quelle chiavi
  si arrivava lontano: chi lo rubava si prendeva le licenze di tutti i clienti
  ospitati li'. All'agent non servivano — il contenitore del cliente se la fa
  dare da solo al primo avvio — ed e' cosi' che funziona adesso.
- **"Ruota token"** sulla riga di ogni server: genera un token nuovo e mostra
  il comando per riconfigurare l'agent. Prima non c'era modo di cambiarlo, e
  l'unica strada era cancellare il server e rifarlo, perdendo lo storico.
  Serve il secondo fattore, e l'agent va riconfigurato subito dopo.
- Nella tabella dei server compare l'indirizzo da cui l'agent ha chiamato
  l'ultima volta, e i tentativi di autenticazione falliti finiscono nel
  registro delle operazioni. Prima un token in mano ad altri non lasciava
  alcuna traccia.

**Attivazione dei clienti**
- Il codice di installazione ora si lega al primo hub che lo usa. Prima poteva
  essere riusato da qualsiasi macchina, quante volte si voleva, e valeva
  quanto la licenza stessa. Se un cliente va reinstallato da zero, si rigenera
  la chiave dal pannello: azzera il collegamento e permette una nuova
  attivazione.

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
