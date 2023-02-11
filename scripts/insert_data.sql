INSERT INTO users (
                   login,
                   first_name,
                   last_name,
                   user_info,
                   contacts,
                   registered,
                   last_activity,
                   country,
                   city,
                   gender,
                   rating) VALUES
('sweetly', 'Ratliff', 'Sweet', 'дизайнер', null, '2020-12-17 07:37:16', '2022-12-10 10:30:10', 'Россия', 'Москва', 'Мужской', 5),
('alstrong', 'Aline', 'Strong', 'дизайнер', null, '2020-12-17 07:37:16', '2022-12-10 10:30:10', 'Россия', 'Екатеринбург', 'Женский', 5),
('seren', 'Serena', 'Weber', 'редактор', null, '2020-12-17 07:37:16', '2022-12-10 10:30:10', 'Беларусь', 'Минск', 'Женский', 5),
('brady', 'Brady', 'Cline', 'менеджер', null, '2020-12-17 07:37:16', '2022-12-10 10:30:10', 'Россия', 'Москва', 'Мужской', 5),
('grant', 'Marisol', 'Grant', 'учитель', null, '2020-12-17 07:37:16', '2022-12-10 10:30:10', 'Россия', 'Москва', 'Мужской', 5);


INSERT INTO user_services (id, title, description, cost, currency, user_login) VALUES
(gen_random_uuid(), 'логотип', null, 10, '$', 'sweetly'),
(gen_random_uuid(), 'логотип', null, 15, '$', 'alstrong'),
(gen_random_uuid(), 'написать статью', null, 20, '$', 'seren'),
(gen_random_uuid(), 'ведение проекта', null, 50, '$', 'brady'),
(gen_random_uuid(), 'занятие', null, 10, '$', 'grant')