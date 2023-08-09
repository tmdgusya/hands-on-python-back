# How to start

## Set up Poetry environment

```shell
poetry install
```

```shell
docker-compuse up -d
```

## Set up docker environment

### In docker-container

```shell
mysql -uroot -ppassword
```

```shell
create database roach
```

```shell
use roach
```

```shell
CREATE TABLE user_account (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(30),
    fullname VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE address (
    id INT AUTO_INCREMENT NOT NULL,
    email_address VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (id)
);
```

## Execute fastapi

```shell
uvicorn main:app --reload
```

```shell
localhost:8000/docs
```