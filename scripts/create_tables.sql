create table users(
    login varchar(50) primary key,
    first_name text,
    last_name text,
    user_info text,
    contacts text
);

create table user_services(
    id uuid primary key,
    title varchar(50),
    description text,
    user_login text,
    cost float,
    currency text
);