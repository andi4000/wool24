FROM python:3.9-slim as python-base

ENV PYTHONUNBUFFERED=true
ENV PYTHONDONTWRITEBYTECODE=true
ENV PIP_DISABLE_PIP_VERSION_CHECK=true
ENV PIP_ROOT_USER_ACTION=ignore

# ------------------------------------------------------------------------------------

FROM python-base as builder
ARG POETRY_VERSION=1.4.2
WORKDIR /build
COPY poetry.lock pyproject.toml ./
RUN \
    --mount=type=cache,target=/root/.cache/pip \
    pip3 install poetry==${POETRY_VERSION} \
    && poetry export --with prod --without-hashes -o requirements.txt

# ------------------------------------------------------------------------------------

FROM python-base as prod
WORKDIR /app
COPY --from=builder /build/ /build/
RUN \
    --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=/var/cache/apt \
    apt-get update \
    && apt-get install -y --no-install-recommends \
    firefox-esr \
    && pip3 install -r /build/requirements.txt \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /build


COPY wool24 /app/wool24
ENV PYTHONPATH /app
ENTRYPOINT [ "python", "/app/wool24/main.py" ]

