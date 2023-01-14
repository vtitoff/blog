INSERT INTO users (login, first_name, last_name, user_info, contacts) VALUES
('sweetly', 'Ratliff', 'Sweet', 'дизайнер', ''),
('alstrong', 'Aline', 'Strong', 'дизайнер', ''),
('seren', 'Serena', 'Weber', 'редактор', ''),
('brady', 'Brady', 'Cline', 'менеджер', ''),
('grant', 'Marisol', 'Grant', 'учитель', '');


INSERT INTO user_services (id, title, description, cost, currency, user_login) VALUES
(gen_random_uuid(), 'логотип', '', 10, '$', 'sweetly'),
(gen_random_uuid(), 'логотип', '', 15, '$', 'alstrong'),
(gen_random_uuid(), 'написать статью', '', 20, '$', 'seren'),
(gen_random_uuid(), 'ведение проекта', '', 50, '$', 'brady'),
(gen_random_uuid(), 'занятие', '', 10, '$', 'grant')