# donmir_notes_api

## What it does
A small HTTP service written in Python (standard library only, no
dependencies). It exposes three endpoints:

- `GET /` returns a welcome message
- `GET /healthz` returns `OK` with status 200 when the service is up
- `GET /notes` returns a JSON list of notes (`id` and `title`)

Any other path returns 404. The notes list is currently static.

## How to run
```bash
./scripts/run.sh
```
The server listens on the port from the `PORT` environment variable
(default 8080), for example `PORT=9000 ./scripts/run.sh`.

## How to test
```bash
./scripts/test.sh
```
The tests start the application and check that `/healthz` returns 200
and that `/notes` returns the expected JSON.

## Rollback

Argo CD deploys what is on the `main` branch, from the `k8s` folder.
To roll back, undo the commit that deployed the bad version, with a new commit:

    git log --oneline -- k8s
    git revert <commit>
    git push

Argo CD deploys the previous version within three minutes. Do not use
`kubectl rollout undo`: self-heal would put the bad version back.
