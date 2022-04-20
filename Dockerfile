# syntax=docker/dockerfile:1
FROM mambaorg/micromamba:0.22.0
# Micromamba is pure cpp conda; fast and light with easy of access to conda-forge.

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml
RUN micromamba install -y -f /tmp/environment.yml && \
    micromamba clean --all --yes

WORKDIR /bigboost
COPY . .

ARG MAMBA_DOCKERFILE_ACTIVATE=1
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]

