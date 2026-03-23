# 4 — Test Container

---

## English

### What we've done so far
We have a working development setup: web server with live reload and a database. The project also has tests in `tests/test_app.py`, but we can't run them in Docker yet.

### Task
Add a test service to `docker-compose.yml` that runs tests instead of the web server. Use profiles so the test container doesn't start alongside other services.

### Sub-tasks
1. Add a new service `test` in `docker-compose.yml`.
2. Use the same `build` as the `web` service.
3. Override `CMD` to run `poetry run test` instead of the server.
4. Add `profiles: ["test"]` — this prevents the test container from starting during a normal `docker compose up`.
5. Make sure the test service has access to the database (environment variables and `depends_on`).

### Hints
- CMD is overridden in Compose with `command:`.
- Profiles mean a service only starts when you explicitly request that profile.
- The test service needs the same `DB_*` environment variables as the `web` service.

### Why does this matter?
Tests should run in an isolated container, separate from the web server. Profiles let you keep the test configuration in the same `docker-compose.yml` without running tests every time you start the app.

### Verify your solution
Run:
```
docker compose --profile test run test
```

Both tests should pass.

---

## Slovenščina

### Kaj smo naredili do zdaj?
Imamo delujoč development setup: web server z live reload-om in bazo podatkov. Projekt ima tudi teste v `tests/test_app.py`, ampak jih zaenkrat ne moremo zagnati v Docker-ju.

### Naloga
Dodaj test service v `docker-compose.yml`, ki požene teste namesto web serverja. Uporabi profile, da se test container ne zažene skupaj z ostalimi service-i.

### Pod-naloge
1. Dodaj nov service `test` v `docker-compose.yml`.
2. Uporabi isti `build` kot `web` service.
3. Prepiši `CMD` tako, da namesto serverja požene `poetry run test`.
4. Dodaj `profiles: ["test"]` — to prepreči, da bi se test container zagnal ob normalnem `docker compose up`.
5. Poskrbi, da ima test service dostop do baze (environment variables in `depends_on`).

### Namigi
- CMD se v Compose prepiše z `command:`.
- Profile pomenijo, da se service zažene samo, ko eksplicitno zahtevamo ta profil.
- Test service potrebuje iste `DB_*` environment variables kot `web` service.

### Zakaj je to pomembno?
Teste želimo poganjati v izoliranem container-ju, ločeno od web serverja. Profile omogočajo, da imamo test konfiguracijo v istem `docker-compose.yml`, brez da bi se testi pognali vsakič ko zaženemo aplikacijo.

### Preveri rešitev
Poženi:
```
docker compose --profile test run test
```

Oba testa bi morala uspeti.
