# 2 — Database Container

---

## English

### What we've done so far
We have a Docker Compose setup that builds and runs our web server. But the app has a `/db` endpoint that tries to connect to a PostgreSQL database. Right now it returns an error because no database is running.

### Task
Add a PostgreSQL container to `docker-compose.yml` and connect the web server to the database.

### Sub-tasks
1. Add a new service `db` using the `postgres:17` image.
2. Set environment variables for the `db` service:
   - `POSTGRES_USER`
   - `POSTGRES_PASSWORD`
   - `POSTGRES_DB`
3. Add environment variables to the `web` service so it can connect to the database:
   - `DB_HOST` — the name of the database service in the Docker Compose file
   - `DB_PORT` — the default PostgreSQL port
   - `DB_USER`, `DB_PASSWORD`, `DB_NAME` — same values as above
4. Add `depends_on` so the database starts before the web server.
5. Add a named volume for persistent database storage.

### Hints
- In Docker Compose, containers address each other by service name (e.g. `db`).
- The default PostgreSQL port is `5432`.
- A named volume is defined in two places: under the service and at the bottom of the file under `volumes:`.
- Volume format for the service: `volume-name:/var/lib/postgresql/data`

### Why does this matter?
Real applications need databases. Docker Compose lets you run multiple containers that communicate with each other using a single command. Named volumes ensure your data survives container restarts.

### Verify your solution
Run `docker compose up` and open your browser at: `http://localhost:8000/db`

Expected response: `{"message": "connected"}`

To verify data persistence (named volume):
1. Open `http://localhost:8000/db/persist` — each visit adds a row to the database.
2. Refresh a few times to accumulate rows.
3. Stop containers with `docker compose down` (without the `-v` flag).
4. Start again with `docker compose up`.
5. Open `http://localhost:8000/db/persist` — previous visits should still be there.

---

## Slovenščina

### Kaj smo naredili do zdaj?
Imamo Docker Compose konfiguracijo, ki zgradi in zažene naš web server.
Ampak aplikacija ima tudi `/db` endpoint, ki poskuša vzpostaviti povezavo s PostgreSQL bazo.
Zaenkrat ta endpoint vrne napako, ker baza ne teče.

### Naloga
Dodaj PostgreSQL container v `docker-compose.yml` in poveži web server z bazo.

### Pod-naloge
1. Dodaj nov service `db`, ki uporablja image `postgres:17`.
2. Nastavi environment spremenljivke za `db` service:
   - `POSTGRES_USER`
   - `POSTGRES_PASSWORD`
   - `POSTGRES_DB`
3. Dodaj environment variables za `web` service, da se bo znal povezati na bazo:
   - `DB_HOST` — ime service-a baze v Docker Compose datoteki
   - `DB_PORT` — privzeti PostgreSQL port
   - `DB_USER`, `DB_PASSWORD`, `DB_NAME` — iste vrednosti kot zgoraj
4. Dodaj `depends_on`, da se baza zažene pred web serverjem.
5. Dodaj named volume za trajno shranjevanje podatkov baze.

### Namigi
- V Docker Compose se container-ji med sabo naslovijo po imenu service-a (npr. `db`).
- Privzeti PostgreSQL port je `5432`.
- Named volume se definira na dveh mestih: pri service-u in na koncu datoteke pod `volumes:`.
- Format za volume pri service-u: `ime-volumna:/var/lib/postgresql/data`

### Zakaj je to pomembno?
Prave aplikacije potrebujejo bazo podatkov. Docker Compose omogoča, da z enim ukazom poženeš več container-jev, ki med seboj komunicirajo. Named volume zagotovi, da podatki preživijo ponovni zagon container-jev.

### Preveri rešitev
Poženi `docker compose up` in odpri brskalnik na: `http://localhost:8000/db`

Pričakovani odgovor: `{"message": "connected"}`

Za preverjanje trajnosti podatkov (named volume):
1. Odpri `http://localhost:8000/db/persist` — vsak obisk doda vrstico v bazo.
2. Osveži nekajkrat, da se nabere več vrstic.
3. Ustavi container-je z `docker compose down` (brez `-v` zastavice).
4. Ponovno zaženi z `docker compose up`.
5. Odpri `http://localhost:8000/db/persist` — prejšnji obiski bi morali biti še vedno prisotni.
