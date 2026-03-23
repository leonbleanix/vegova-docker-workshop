# 3 — Development Server

---

## English

### What we've done so far
We have a web server and database running in Docker containers. Problem: every time we change our code, we need to rebuild the image (`docker compose build`) and restart. That's slow.

### Task
Configure Docker Compose so code changes are reflected automatically without rebuilding.

### Sub-tasks
1. Add a bind mount volume to the `web` service that maps the local `app/` directory into the container.
2. Set the environment variable `FLASK_DEBUG=1` on the `web` service — this enables auto-reload on code changes.

### Hints
- Bind mount format: `./local-path:/container-path`
- Think about where the `app/` directory lives inside the container (check the `WORKDIR` in `Dockerfile`).
- `FLASK_DEBUG` is set just like any other environment variable.

### Why does this matter?
During development you don't want to wait for a rebuild on every change. Bind mounts let local changes appear instantly inside the container, and debug mode auto-restarts the server.

### Verify your solution
1. Run `docker compose up`.
2. Open `http://localhost:8000/hello` — you see `Hello, World!`.
3. Change the message in `app/main.py` (e.g. to `"Hello, Docker!"`).
4. Refresh the browser — **without rebuilding**, you should see the new message.

---

## Slovenščina

### Kaj smo naredili do zdaj?
Imamo web server in bazo podatkov, ki tečeta v Docker container-jih. Problem: vsakič ko spremenimo kodo, moramo na novo zgraditi image (`docker compose build`) in ponovno zagnati container. To je počasno.

### Naloga
Nastavi Docker Compose tako, da se spremembe kode samodejno odražajo brez ponovne gradnje.

### Pod-naloge
1. Dodaj bind mount volume za `web` service, ki preslika lokalni `app/` direktorij v container.
2. Nastavi environment variable `FLASK_DEBUG=1` za `web` service — to vklopi samodejni ponovni zagon serverja ob spremembah.

### Namigi
- Bind mount format: `./lokalna-pot:/pot-v-containerju`
- Razmisli, kje v container-ju se nahaja `app/` direktorij (poglej `WORKDIR` v `Dockerfile`).
- `FLASK_DEBUG` se nastavi enako kot ostale environment variables.

### Zakaj je to pomembno?
Med razvojem ne želiš čakati na ponovno gradnjo ob vsaki spremembi. Bind mount-i omogočajo, da se lokalne spremembe takoj odrazijo v container-ju, debug način pa samodejno požene server znova.

### Preveri rešitev
1. Poženi `docker compose up`.
2. Odpri `http://localhost:8000/hello` — vidiš `Hello, World!`.
3. Spremeni sporočilo v `app/main.py` (npr. v `"Hello, Docker!"`).
4. Osveži brskalnik — **brez ponovne gradnje** bi moralo prikazati novo sporočilo.
