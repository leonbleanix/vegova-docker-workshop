# 1 — Docker Compose

---

## English

### What we've done so far
In the previous task, we manually built an image and ran a container with `docker build` and `docker run`.
This works, but you have to remember all the parameters (port mapping, image name, ...) every time.

### Task
Create a `docker-compose.yml` file that automates the build and run of our web server.

### Sub-tasks
1. Create a `docker-compose.yml` file in the project root.
2. Define a service called `web`.
3. Set `build` to use the existing `Dockerfile`.
4. Add port mapping so the server is accessible on port 8000.

### Hints
- A Docker Compose file starts with `services:`.
- To build from the current directory: `build: .`
- Port mapping format: `"external:internal"`

### Useful commands
Once you have your `docker-compose.yml`, try these commands:
- `docker compose up` — build and start the server
- `docker compose down` — stop and remove containers
- `docker compose logs` — show logs
- `docker compose ps` — show running containers
- `docker compose build` — rebuild images

### Why does this matter?
Docker Compose lets you define your entire setup in a single file.
Instead of remembering long `docker run` commands, you just run `docker compose up`.

### Verify your solution
Run `docker compose up` and open your browser at: `http://localhost:8000/hello`

Expected response: `{"message": "Hello, World!"}`

---

## Slovenščina

### Kaj smo naredili do zdaj?
V prejšnji nalogi smo ročno zgradili image in zagnali container z `docker build` in `docker run`.
To deluje, ampak si morate zapomniti vse parametre (port mapping, ime image-a, ...) vsakič znova.

### Naloga
Ustvari datoteko `docker-compose.yml`, ki bo avtomatizirala gradnjo in zagon našega web serverja.

### Pod-naloge
1. Ustvari datoteko `docker-compose.yml` v korenskem direktoriju projekta.
2. Definiraj service z imenom `web`.
3. Nastavi `build` tako, da uporabi obstoječi `Dockerfile`.
4. Dodaj port mapping, da bo server dostopen na portu 8000.

### Namigi
- Docker Compose datoteka se začne s `services:`.
- Za build iz trenutnega direktorija: `build: .`
- Port mapping format: `"zunanji:notranji"`

### Uporabni ukazi
Ko imaš `docker-compose.yml`, preizkusi te ukaze:
- `docker compose up` — zgradi in zaženi strežnik
- `docker compose down` — ustavi in odstrani container-je
- `docker compose logs` — prikaži log-e
- `docker compose ps` — prikaži aktivne container-je
- `docker compose build` — na novo zgradi image-e

### Zakaj je to pomembno?
Docker Compose ti omogoča, da celotno konfiguracijo zapišeš v eno datoteko.
Namesto da si zapomniš dolge `docker run` ukaze, samo poženeš `docker compose up`.

### Preveri rešitev
Poženi `docker compose up` in odpri brskalnik na: `http://localhost:8000/hello`

Pričakovani odgovor: `{"message": "Hello, World!"}`
