# 5 — Production Build

---

## English

### What we've done so far
We have a complete development setup: web server, database, live reload, and tests. But our Docker image contains everything — tests, development dependencies, Dockerfile, task files. That's not appropriate for production.

### Task
Convert the `Dockerfile` into a multi-stage build that creates a lean production image without unnecessary files.

### Sub-tasks
1. Name the current stage in the `Dockerfile` (e.g. `FROM python:3.13-slim AS dev`).
2. Add a new stage `prod` that:
   - Starts from the same base image.
   - Installs Poetry.
   - Copies **only** `pyproject.toml` and `poetry.lock`.
   - Installs **only** production dependencies (without the dev group).
   - Copies **only** the `app/` directory.
   - Uses the same `CMD` as dev.
   - Creates a non-root user and switches to it with `USER`.
3. In `docker-compose.yml`, add `target: dev` to the `web` service so development still works.

### Hints
- Multi-stage build: each `FROM` line starts a new stage.
- To skip dev dependencies with Poetry: `poetry install --without dev`
- Poetry creates a virtual environment by default — you don't need that in Docker. Look into `poetry config virtualenvs.create`.
- `target` in Compose tells Docker which stage to build.
- To create a non-root user: `RUN useradd -r appuser`, `mkdir /home/appuser` to make a home directory for it.
- `USER appuser` to make the container use the new user — this must come after all `RUN`/`COPY` commands that need root.
- Copied files need to be assigned to the created user. Example: `COPY --chown=appuser:appuser ./app /app/app`
- To build the production image: `docker build --target prod -t workshop-prod .`

### Why does this matter?
Production images should be as small as possible, containing only what's needed to run the application. Fewer files means a smaller attack surface, faster deploys, and less disk space used. Running as a non-root user limits damage if an attacker escapes the application — they won't have root access inside the container.

### Verify your solution
Build and run the production image:
```
docker build --target prod -t workshop-prod .
docker run -p 8000:8000 workshop-prod
```

Open your browser at: `http://localhost:8000/production-check`

Expected response: `{"message": "production-ready"}`

If you see `"not production-ready"` with a list of issues, read the list and fix your `prod` stage accordingly.

---

## Slovenščina

### Kaj smo naredili do zdaj?
Imamo razvojno okolje: web server, bazo, live reload in teste. Ampak naš Docker image vsebuje vse — 
teste, razvojne odvisnosti, Dockerfile, task datoteke. Za produkcijo to ni primerno.

### Naloga
Spremeni `Dockerfile` v multi-stage build, ki ustvari vitek produkcijski image brez nepotrebnih datotek.

### Pod-naloge
1. Poimenuj trenutno stopnjo v `Dockerfile` (npr. `FROM python:3.13-slim AS dev`).
2. Dodaj novo stopnjo `prod`, ki:
   - Se začne iz istega base image-a.
   - Namesti Poetry.
   - Kopira **samo** `pyproject.toml` in `poetry.lock`.
   - Namesti **samo** produkcijske odvisnosti (brez dev skupine).
   - Kopira **samo** `app/` direktorij.
   - Nastavi isti `CMD` kot dev.
   - Ustvari neprivilegiranega uporabnika in nanj preklopi z `USER`.
3. V `docker-compose.yml` dodaj `target: dev` k `web` service-u, da development še vedno deluje.

### Namigi
- Multi-stage build: vsaka `FROM` vrstica začne novo stopnjo.
- Za izpust dev odvisnosti pri Poetry: `poetry install --without dev`
- Poetry privzeto ustvari virtual environment — v Docker-ju tega ne potrebuješ. Poglej `poetry config virtualenvs.create`.
- `target` v Compose pove Docker-ju, katero stopnjo naj zgradi.
- Za ustvaritev neprivilegiranega uporabnika: `RUN useradd -r appuser`, `mkdir /home/appuser`, da mu naredimo home direktorij. 
- `USER appuser` da image začne uporabljat nepreviligiranega userja — to mora biti po vseh `RUN`/`COPY` ukazih, ki potrebujejo root.
- Kopirane datoteke se morajo dodeliti neprivilegiriranemu uporabniku. Primer: `COPY --chown=appuser:appuser ./app /app/app`
- Za gradnjo produkcijskega image-a: `docker build --target prod -t workshop-prod .`

### Zakaj je to pomembno?
Production image-i morajo biti čim manjši in vsebovati samo tisto, kar je potrebno za zagon aplikacije. Manj datotek pomeni manjšo attack surface, hitrejše deploy-e in manj porabljenega prostora. Zagon z neprivilegiranim uporabnikom omeji škodo, če napadalec pobegne iz aplikacije — v containerju ne bo imel root dostopa.

### Preveri rešitev
Zgradi in zaženi production image:
```
docker build --target prod -t workshop-prod .
docker run -p 8000:8000 workshop-prod
```

Odpri brskalnik na: `http://localhost:8000/production-check`

Če vidiš `{"message": "production-ready"}`, je naloga opravljena.

Če vidiš `"not production-ready"` z listo problemov, preberi seznam in popravi svojo `prod` stopnjo.
