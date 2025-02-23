FROM postgres:15
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=expenses_db
COPY init.sql /docker-entrypoint-initdb.d/
