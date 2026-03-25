# 0 — Start

---

## English

### What do we have?
You have a Python web server with a `Dockerfile` already set up. Before we move to Docker Compose, let's learn how to manually build and run a Docker container.

### Tasks
1. Look at the `Dockerfile` and think about what each line does.
2. Build the Docker image:
   ```
   docker build -t workshop .
   ```
3. Run a container from the built image (with port mapping):
   ```
   docker run -p 8000:8000 workshop
   ```
4. Open your browser and go to: `http://localhost:8000/hello`. You should see `{"message": "Hello, World!"}`
5. Stop the container with `Ctrl+C`.

### Why does this matter?
Every Docker Compose operation runs these commands under the hood. Understanding the basics helps you understand what's happening behind the scenes.

---

## Slovenščina

### Kaj imamo?
Pred teboj je Python web server z že pripravljenim `Dockerfile`-om. Preden začnemo, se najprej seznani s tem, kako ročno zgradimo in zaženemo Docker container.

### Naloge
1. Preglej `Dockerfile` in razmisli, kaj vsaka vrstica naredi.
2. Zgradi Docker image:
   ```
   docker build -t workshop .
   ```
3. Zaženi container iz zgrajenega image-a (z mapiranjem portov):
   ```
   docker run -p 8000:8000 workshop
   ```
4. Odpri brskalnik in pojdi na: `http://localhost:8000/hello`, kjer bi moral/a videti `{"message": "Hello, World!"}`.
5. Ustavi container s `Ctrl+C`.

### Zakaj je to pomembno?
Vsaka Docker Compose operacija na koncu izvede prav te ukaze. Razumevanje osnov ti bo pomagalo razumeti, kaj se dogaja "pod pokrovom".
