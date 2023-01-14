INSERT INTO users (login, first_name, last_name, user_info, contacts) VALUES
('sweetly', 'Ratliff', 'Sweet', 'дизайнер', null),
('alstrong', 'Aline', 'Strong', 'дизайнер', null),
('seren', 'Serena', 'Weber', 'редактор', null),
('brady', 'Brady', 'Cline', 'менеджер', null),
('grant', 'Marisol', 'Grant', 'учитель', null);


INSERT INTO user_services (id, title, description, cost, currency, user_login) VALUES
(gen_random_uuid(), 'логотип', null, 10, '$', 'sweetly'),
(gen_random_uuid(), 'логотип', null, 15, '$', 'alstrong'),
(gen_random_uuid(), 'написать статью', null, 20, '$', 'seren'),
(gen_random_uuid(), 'ведение проекта', null, 50, '$', 'brady'),
(gen_random_uuid(), 'занятие', null, 10, '$', 'grant')