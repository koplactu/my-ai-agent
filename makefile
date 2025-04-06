run-agent: colima build
	docker compose run --rm --service-ports agent

build: colima
	docker compose build

down:
	docker compose down

colima:
	colima status || colima start --arch aarch64 --memory 4
