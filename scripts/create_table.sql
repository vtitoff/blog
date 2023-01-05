create table users(
    login varchar(50) primary key,
    first_name text,
    last_name text,
    user_info text,
    services json
);