ENGLISH:
--------
 Mantis Bug Tracker speaks with computerized voice when you receive a new ticket on your different Projects

I uploaded a video where you can watch how this script works ;-P
https://www.youtube.com/watch?v=D_k34P53D4g


CATALAN:
--------
Fa molt de temps, vaig crear un script amb Bash [http://joancatala.net/categoria-offtopic/parlant-amb-mbrola-les-noves-incidencies-del-mantis-bug-tracker] que em llegia els tickets globals del sistema de ticketing que tenim al meu treball, el Mantis Bug Tracker. I amb la veu d'mbrola s'escoltava molt bé.

Ara he refet aquesta aplicació amb Python, s'anomena mantis-parla.py i em descarrega els tickets nous del Mantis Bug Tracker via RSS amb feedparser de Python. Els tickets nous vol dir els tickets que no estan assignats o que no estan resolts o que no estan tancats. Al Mantis Bug Tracker, els tickets nous es veuen de color entre roig i rosa.

 Doncs bé, mantis-parla.py descarrega els tickets nous de cada projecte que tenim configurat i s'autorefresca cada 60 segons.
I quan detecta un ticket nou que no existia 60 segons abans, parla amb la veu computeritzada del espeak.

![Captura de pantalla de mantis-parla.py ](https://github.com/joancatala/mantis-parla/blob/master/mantis-bug-tracker-voice-veu-voz-espeak-text-to-speech-openbsd.png)

Al següent video es pot veure el seu funcionament (i jo truque l'aplicació modificant els fitxers que m'ha descarregat, per tal de que "detecte fitxers nous" i parle.) Pots escoltar la veu a partir del minut 0:34 segons.

Evidentment sonaria millor amb flite o ivona, però no parla valenicà. O amb loquendo, però no em funciona de moment a OpenBSD (investigaré!).

L'objectiu de mantis-parla.py és poder estar treballant en coses sense necessitat d'obrir el Mantis Bug Tracker i que, en cas d'arribar una incidència nova, l'ordinador em parlarà per a informar-me.

Bàsicament, els requeriments que calen per fer servir aquesta versió són:

- OpenBSD/FreeBSD/NetBSD o GNU/Linux
- python 3
- sty
- feedparser
- toilet
- espeak

Podràs instal·lar fàcilment els mòduls amb:

pip3 install feedparser sty

Probablement, una de les aplicacions més frikis que he fet en ma vida XDDDD
