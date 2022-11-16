build:
	make build_base && make build_main && make build_nginx

build_base:
	docker build -f Dockerfile.base -t belcanto_base .

build_main:
	docker build -t belcanto_web .

build_nginx:
	cat old_sites_archive/old_sites.tar.gz.* > old_sites_archive/old_sites.tar.gz && docker build -f Dockerfile.nginx -t belcanto_nginx .

up:
	docker-compose  -f docker-compose.yml up

down:
	docker-compose -f docker-compose.yml down

up_debug:
	COMPOSE_HTTP_TIMEOUT=500 BELCANTO_DEBUG=on docker-compose  -f docker-compose.yml up -d

down_debug:
	BELCANTO_DEBUG=on docker-compose -f docker-compose.yml down

down_dev:
	docker-compose -f docker-compose-dev.yml down

cleanup:
	./docker_cleanup.sh

up_local:
	COMPOSE_HTTP_TIMEOUT=500 docker-compose  -f docker-compose-local.yml up -d

down_local:
	docker-compose -f docker-compose-local.yml down

up_local_m1:
	COMPOSE_HTTP_TIMEOUT=500 docker-compose  -f docker-compose-local-m1.yml up -d

down_local_m1:
	COMPOSE_HTTP_TIMEOUT=500 docker-compose  -f docker-compose-local-m1.yml down
