# Začnemo z uradno Python sliko kot osnovo za naš container.
# Start with the official Python image as a base for our container.
FROM python:3.13-slim

# Nastavimo delovni direktorij znotraj containerja. Vsi nadaljnji ukazi se izvajajo tukaj.
# Set the working directory inside the container. All following commands run from here.
WORKDIR /app

# Poetry je orodje za upravljanje Python knjižnic (podobno kot npm za JavaScript).
# Namestimo ga, da bomo lahko namestili vse potrebne knjižnice za naš projekt.
# Poetry is a tool for managing Python packages (similar to npm for JavaScript).
# We install it so we can install all the libraries our project needs.
RUN pip install poetry

# Kopiramo vse datoteke iz našega projekta v container.
# Copy all files from our project into the container.
COPY . .

# Namestimo vse knjižnice, ki jih naš projekt potrebuje (definirane v pyproject.toml).
# Install all libraries our project needs (defined in pyproject.toml).
RUN poetry install

# Zaženemo web server, ko se container zažene.
# Start the web server when the container starts.
CMD ["poetry", "run", "dev"]
