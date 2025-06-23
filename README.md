🃏 Blackjack LLM – Web App in Streamlit
🔗 Demo live: Gioca ora su Streamlit

🎯 Obiettivo del progetto
Questa applicazione implementa un gioco di Blackjack completo, sviluppato in Python e reso accessibile tramite Streamlit. Il sistema permette all’utente di:

Giocare contro il dealer (CPU)

Gestire un saldo iniziale

Puntare, pescare carte e fermare la mano

Visualizzare l’esito della partita e lo storico delle ultime mani

🧱 Architettura del codice
Il progetto è strutturato in modo modulare e OOP, con le seguenti classi principali:

Classe	Responsabilità
Carta	Rappresenta una carta da gioco (valore + seme)
Mazzo	Gestisce la creazione e la distribuzione delle carte
Partecipante	Superclasse per Giocatore e Dealer, gestisce la mano
Giocatore	Include saldo, puntate e contatori vittorie/sconfitte
Dealer	Erede di Partecipante, segue regole fisse del banco
Partita	Coordina le interazioni tra giocatore, dealer e mazzo

🎮 Funzionalità principali
✅ Saldo iniziale e gestione delle puntate

✅ Logica completa del Blackjack (21, sballo, pareggio, vittoria)

✅ Statistiche di vittorie, sconfitte e pareggi

✅ Interfaccia web semplice e interattiva

✅ Storico visivo delle ultime 10 mani

🧠 Tecnologie usate
Python 3.11+

Streamlit per la UI

OOP per la logica di gioco

PlantUML per la modellazione UML del progetto
