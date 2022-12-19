DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS clients;                  
DROP TABLE IF EXISTS stylists;

CREATE TABLE clients (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255), 
    phone_number VARCHAR(255)
);

CREATE TABLE stylists (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255) 
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    date_time VARCHAR,
    client_id SERIAL NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    stylist_id SERIAL NOT NULL REFERENCES stylists(id) ON DELETE CASCADE
);