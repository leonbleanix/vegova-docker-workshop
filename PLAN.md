# Docker workshop
We want to create a workshop for computer science high school students where Docker can be worked on in stages, 
going from simple to more complex.

We want to have a basic starting Dockerfile that will run a python web server.
The docker setup will be upgraded as we go.

## Stages
1. Add a docker-compose.yml file for the server.
    - Add build definition.
    - Add port mapping.
    - Cover core docker compose commands: `up`, `down`, `logs`, `ps`, `build`.

2. Add a local volume for live code changes.

3. Add a database container.
   - Environment variables for database connection.
   - Add a named volume for database persistence.
   - "depends_on" to ensure the database container is started before the web server.

4. Multi-stage builds to create a production image.
   - Need a test endpoint that will check if development dependencies are present.

5. Add a test container which runs tests instead of the web server.
   - Use profiles to run tests from docker compose without starting the web server.

6. Resource limits.
   - Add `mem_limit` and `cpus` constraints to services.
   - Use `docker stats` to observe resource usage.

