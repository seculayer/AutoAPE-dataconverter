# Contribute

## 의존성 설치

```console
poetry install
```

## Format & sort import

```console
poetry run isort dataconverter/ tests/
poetry run black dataconverter/ tests/
```

Bash 커맨드

```bash
poetry run isort $(git diff --name-only -- '*.py') tests && poetry run black $(git diff --name-only -- '*.py') tests
```

Fish 커맨드

```fish
poetry run isort $(git diff --name-only -- '*.py') tests; and poetry run black $(git diff --name-only -- '*.py') tests
```

## Type check

```console
poetry run mypy -- dataconverter/ tests/

# Run as mypy daemon
poetry run dmypy run -- dataconverter/ tests/
```

## Lint

```console
poetry run pylint
poetry run prospector
```


## 테스트

```console
# 테스트
poetry run pytest

# 커버리지 테스트
poetry run pytest --cov=dataconverter -p pytest_cov
```

