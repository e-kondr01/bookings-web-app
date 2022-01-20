# Bookings app
Built using FastAPI and Tortoise ORM.

Uses FastAPI Admin and FastAPI Users.

# Local deploy
```
docker-compose up --build
```

# Migrations
```
docker exec bookings_fastapi aerich migrate
docker exec bookings_fastapi aerich upgrade
```
